from django.shortcuts import render, redirect
from django.db import connection
import datetime
import hashlib


# Create your views here.
def index(request):
    return render(request, 'base.html', )


def UserDetail(request):
    if request.session.get('id'):
        user_id = request.session.get('id')
        cursor = connection.cursor()
        sql = 'SELECT * FROM "USER" WHERE USER_ID=%s'
        cursor.execute(sql, [user_id])
        result = cursor.fetchall()

        user_name = result[0][1]
        email = result[0][2]
        date_of_birth = result[0][5]
        country = result[0][7]
        row = {'user_id': user_id, 'user_name': user_name, 'email': email, 'date_of_birth': date_of_birth,
               'country': country}

        sql = 'SELECT * FROM "PAYMENT" WHERE USER_ID=%s ORDER BY TRANSACTION_ID DESC;'
        cursor.execute(sql, [request.session.get('id')])
        result = cursor.fetchall()
        sub_over_date = result[0][4]
        sub = {'sub_over_date': sub_over_date}

        cursor.close()
        return render(request, 'user/details.html', {'user': row, 'sub': sub})

    else:
        return render(request, 'user/login.html', )


def UserLogin(request):
    try:
        del request.session['id']
    except KeyError:
        pass
    return render(request, 'user/login.html', )


def AfterLogin(request):
    email = request.GET.get('email', '')
    password = hashlib.sha256(request.GET.get('password', '').encode()).hexdigest()

    cursor = connection.cursor()
    try:
        sql = 'SELECT * FROM "USER" WHERE EMAIL=%s AND PASSWORD=%s;'
        cursor.execute(sql, [email, password])
        result = cursor.fetchall()
        user_id = result[0][0]

        request.session['id'] = user_id
        request.session['age'] = result[0][6]

        cursor.execute("""
            BEGIN 
                USER_AGE_UPDATE(:inVal);
            END;
            /""", {"inVal": user_id})

    except:
        pass

    cursor.close()
    response = redirect('/user/')
    return response


def Logout(request):
    try:
        del request.session['id']
    except KeyError:
        pass
    response = redirect('/user/')
    return response


def Signup(request):
    try:
        del request.session['id']
    except KeyError:
        pass
    cursor = connection.cursor()
    sql = "SELECT * FROM COUNTRY"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    dict_result = []

    for r in result:
        country_id = r[0]
        country_name = r[1]
        row = {'country_id': country_id, 'country_name': country_name}
        dict_result.append(row)

    return render(request, 'user/signup.html', {'country': dict_result})


def AfterSignup(request):
    name = request.GET.get('name', '')
    email = request.GET.get('email', '')
    password = request.GET.get('password', '')
    re_password = request.GET.get('re_password', '')
    credit = request.GET.get('credit', '')
    date_of_birth = request.GET.get('date_of_birth', '')
    country = request.GET.get('country', '')

    cursor = connection.cursor()
    sql = 'SELECT USER_ID FROM "USER" WHERE EMAIL=%s'
    cursor.execute(sql, [email])
    result = cursor.fetchall()
    r = 0
    try:
        r = result[0][0]
    except:
        pass

    if password == re_password and r == 0:
        sql = 'SELECT MAX(USER_ID) FROM "USER"'
        cursor.execute(sql)
        result = cursor.fetchall()
        max_id = result[0][0] + 1
        age = 0
        password = hashlib.sha256(password.encode()).hexdigest()
        sql = 'INSERT INTO "AMAZON"."USER" VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)'
        cursor.execute(sql, [max_id, name, email, password, credit, date_of_birth, age, country])

        cursor.execute("""
        BEGIN 
            USER_AGE_UPDATE(:inVal);
        END;
        /""", {"inVal": max_id})

        request.session['id'] = max_id
        sql = 'SELECT * FROM "USER" WHERE USER_ID=%s;'
        cursor.execute(sql, [max_id])
        result = cursor.fetchall()
        request.session['age'] = result[0][6]

        sql = 'SELECT MAX(TRANSACTION_ID) FROM "PAYMENT"'
        cursor.execute(sql)
        result = cursor.fetchall()
        max_id = result[0][0] + 1

        amount = 10
        sub_over_date = datetime.date.today() + datetime.timedelta(30)
        sql = 'INSERT INTO "AMAZON"."PAYMENT" VALUES ( %s, %s, %s, %s, %s);'
        cursor.execute(sql, [max_id, request.session.get('id'), datetime.date.today(), amount, sub_over_date])
        cursor.close()

        response = redirect('/user/')
        return response

    else:
        cursor.close()
        response = redirect('/user/signup/')
        return response


def ChangePassword(request):
    if request.session.get('id'):
        return render(request, 'user/changepassword.html', )
    else:
        return render(request, 'user/login.html', )


def ChangingPassword(request):
    if request.session.get('id'):
        password = request.GET.get('password', '')
        re_password = request.GET.get('re-password', '')
        if password == re_password:
            password = hashlib.sha256(password.encode()).hexdigest()

            cursor = connection.cursor()
            sql = 'UPDATE "USER" SET PASSWORD=%s WHERE USER_ID=%s;'
            cursor.execute(sql, [password, request.session.get('id')])

            response = redirect('/user/')
            return response

        else:
            return render(request, 'user/changepassword.html', )


    else:
        return render(request, 'user/login.html', )


def History(request):
    if request.session.get('id'):
        cursor = connection.cursor()

        sql = "SELECT * FROM WATCH JOIN VIDEO ON WATCH.VIDEO_ID=VIDEO.VIDEO_ID WHERE WATCH.USER_ID=%s ORDER BY WATCH.WATCH_TIME DESC;"
        cursor.execute(sql, [request.session.get('id')])
        result = cursor.fetchall()
        cursor.close()
        dict_result = []

        for r in result:
            video_id = r[3]
            video_title = r[4]
            description = r[5]
            rating = r[9]
            watch_time = r[2]
            row = {'video_id': video_id, 'video_title': video_title, 'description': description, 'rating': rating, 'watch_time': watch_time}
            dict_result.append(row)

        return render(request, 'user/history.html', {'history': dict_result})

    else:
        return render(request, 'user/login.html', )


def Payment(request):
    if request.session.get('id'):
        return render(request, 'user/payment.html', )

    else:
        return render(request, 'user/login.html', )


def AfterPayment(request, id):
    if request.session.get('id'):
        amount = 4 + id * 2
        cursor = connection.cursor()
        sql = 'SELECT MAX(TRANSACTION_ID) FROM "PAYMENT"'
        cursor.execute(sql)
        result = cursor.fetchall()
        max_id = result[0][0] + 1
        today = datetime.date.today()

        sql = 'SELECT * FROM "PAYMENT" WHERE USER_ID=%s ORDER BY TRANSACTION_ID DESC;'
        cursor.execute(sql, [request.session.get('id')])
        result = cursor.fetchall()

        sub_over_date = result[0][4]

        sub_over_date += datetime.timedelta(30)
        sql = 'INSERT INTO "AMAZON"."PAYMENT" VALUES ( %s, %s, %s, %s, %s);'
        cursor.execute(sql, [max_id, request.session.get('id'), today, amount, sub_over_date])
        cursor.close()
        response = redirect('/user/')
        return response

    else:
        return render(request, 'user/login.html', )