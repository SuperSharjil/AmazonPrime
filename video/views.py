from django.shortcuts import render, redirect
from django.db import connection
import datetime


# Create your views here.
def index(request):
	if request.session.get('id'):
		cursor = connection.cursor()
		sql = "SELECT * FROM VIDEO JOIN TRENDING ON VIDEO.VIDEO_ID=TRENDING.VIDEO_ID;"

		cursor.execute(sql)
		result = cursor.fetchall()
		cursor.close()
		dict_result = []

		for r in result:
			video_id = r[0]
			video_title = r[1]
			description = r[2]
			rating = r[6]
			row = {'video_id': video_id, 'video_title': video_title, 'description': description, 'rating': rating}
			dict_result.append(row)

		return render(request, 'video/feed.html', {'trending': dict_result})

	else:
		return render(request, 'user/login.html', )


def VideoDetail(request, id):
	if request.session.get('id'):
		cursor = connection.cursor()
		try:
			sql = 'INSERT INTO "AMAZON"."WATCH" VALUES ( %s, %s, %s);'
			cursor.execute(sql, [request.session.get('id'), id, datetime.datetime.now()])
		except:
			sql = 'UPDATE "WATCH" SET WATCH_TIME=%s WHERE USER_ID=%s AND VIDEO_ID=%s;'
			cursor.execute(sql, [datetime.datetime.now(), request.session.get('id'), id])

		sql = "SELECT * FROM VIDEO WHERE VIDEO_ID=%s;"
		cursor.execute(sql, [id])
		result = cursor.fetchall()

		video_id = result[0][0]
		video_title = result[0][1]
		description = result[0][2]
		release_date = result[0][3]
		rating = result[0][6]
		age_restriction = result[0][7]
		watch_count = result[0][9] + 1

		sql = 'UPDATE "VIDEO" SET WATCH_COUNT=%s WHERE VIDEO_ID=%s;'
		cursor.execute(sql, [watch_count, id])
		video = {'video_id': video_id, 'video_title': video_title, 'description': description, 'release_date': release_date, 'rating': rating, 'watch_count': watch_count}
		rate = 'NULL'
		dict_result = []
		try:
			sql = 'SELECT * FROM CAST_CREW JOIN VIDEO_CAST_CREW ON CAST_CREW.CREW_ID = VIDEO_CAST_CREW.CREW_ID WHERE VIDEO_CAST_CREW.VIDEO_ID = %s;'
			cursor.execute(sql, [id])
			result = cursor.fetchall()
			for r in result:
				cast_id = r[0]
				cast_name = r[1]
				row = {'cast_id': cast_id, 'cast_name': cast_name}
				dict_result.append(row)
		except:
			pass

		try:
			sql = 'SELECT * FROM "RATING_TABLE" WHERE USER_ID=%s AND VIDEO_ID=%s;'
			cursor.execute(sql, [request.session.get('id'), id])
			result = cursor.fetchall()
			rate = result[0][2]
		except:
			pass

		cursor.close()
		rate = {'rating': rate}

		row = {'age': age_restriction}
		if request.session.get('age') < age_restriction:
			return render(request, 'video/age_restriction.html', {'age': row})
		else:
			return render(request, 'video/details.html', {'video': video, 'cast': dict_result, 'rating': rate})

	else:
		return render(request, 'user/login.html', )


def SeriesDetails(request, id):
	if request.session.get('id'):
		cursor = connection.cursor()

		sql = "SELECT * FROM SERIES WHERE SERIES_ID=%s;"
		cursor.execute(sql, [id])
		result = cursor.fetchall()

		series_id = result[0][0]
		series_title = result[0][1]
		seasons = result[0][2]
		episodes = result[0][3]
		start_date = result[0][4]
		if result[0][5] == 1:
			ongoing_status = 'YES'
		else:
			ongoing_status = 'NO'
		series = {'series_id': series_id, 'series_title': series_title, 'seasons': seasons, 'episodes': episodes, 'start_date': start_date, 'ongoing_status': ongoing_status}

		sql = "SELECT * FROM VIDEO JOIN SERIES_VIDEO ON VIDEO.VIDEO_ID=SERIES_VIDEO.VIDEO_ID WHERE SERIES_VIDEO.SERIES_ID=%s;"

		cursor.execute(sql, [id])
		result = cursor.fetchall()
		cursor.close()
		dict_result = []

		for r in result:
			video_id = r[0]
			video_title = r[1]
			description = r[2]
			rating = r[6]
			season_num = r[12]
			episode_num = r[13]
			row = {'video_id': video_id, 'video_title': video_title, 'description': description, 'rating': rating, 'season_num': season_num, 'episode_num': episode_num}
			dict_result.append(row)

		cursor.close()
		return render(request, 'video/seriesdetails.html', {'series': series, 'video': dict_result})

	else:
		return render(request, 'user/login.html', )


def Trending(request):
	if request.session.get('id'):
		cursor = connection.cursor()
		sql = "SELECT * FROM VIDEO JOIN TRENDING ON VIDEO.VIDEO_ID=TRENDING.VIDEO_ID;"

		cursor.execute(sql)
		result = cursor.fetchall()
		cursor.close()
		dict_result = []

		for r in result:
			video_id = r[0]
			video_title = r[1]
			description = r[2]
			rating = r[6]
			row = {'video_id': video_id, 'video_title': video_title, 'description': description, 'rating': rating}
			dict_result.append(row)

		return render(request, 'video/trending.html', {'trending': dict_result})

	else:
		return render(request, 'user/login.html', )


def Movies(request):
	if request.session.get('id'):
		cursor = connection.cursor()
		sql = "SELECT * FROM VIDEO WHERE VIDEO_TYPE=1;"

		cursor.execute(sql)
		result = cursor.fetchall()
		cursor.close()
		dict_result = []

		for r in result:
			video_id = r[0]
			video_title = r[1]
			description = r[2]
			rating = r[6]
			row = {'video_id': video_id, 'video_title': video_title, 'description': description, 'rating': rating}
			dict_result.append(row)

		return render(request, 'video/movies.html', {'movies': dict_result})

	else:
		return render(request, 'user/login.html', )


def Series(request):
	if request.session.get('id'):
		cursor = connection.cursor()
		sql = "SELECT * FROM SERIES"

		cursor.execute(sql)
		result = cursor.fetchall()
		cursor.close()
		dict_result = []

		for r in result:
			series_id = r[0]
			series_title = r[1]
			seasons = r[2]
			episodes = r[3]
			start_date = r[4]
			if r[5] == 1:
				ongoing_status = 'YES'
			else:
				ongoing_status = 'NO'
			row = {'series_id': series_id, 'series_title': series_title, 'seasons': seasons, 'episodes': episodes, 'start_date': start_date, 'ongoing_status': ongoing_status}
			dict_result.append(row)

		return render(request, 'video/series.html', {'series': dict_result})

	else:
		return render(request, 'user/login.html', )


def GetTitle(request):
	if request.session.get('id'):
		search = '%' + request.GET.get('title', '') + '%'
		cursor = connection.cursor()
		if request.GET.get('AdvancedSearch', ''):
			category = request.GET.get('category', '')
			country = request.GET.get('country', '')
			language = request.GET.get('language', '')
			sql = "SELECT * FROM VIDEO JOIN VIDEO_CATEGORY ON VIDEO.VIDEO_ID = VIDEO_CATEGORY.VIDEO_ID JOIN VIDEO_LANGUAGE ON VIDEO.VIDEO_ID = VIDEO_LANGUAGE.VIDEO_ID WHERE LOWER(VIDEO.VIDEO_TITLE) LIKE LOWER(%s) AND VIDEO_CATEGORY.CATEGORY_ID=%s AND VIDEO.REGION=%s AND VIDEO_LANGUAGE.LANGUAGE_ID=%s;"
			cursor.execute(sql, [search, category, country, language])
			result = cursor.fetchall()
			dict_result = []

			for r in result:
				video_id = r[0]
				video_title = r[1]
				description = r[2]
				rating = r[6]
				row = {'video_id': video_id, 'video_title': video_title, 'description': description, 'rating': rating}
				dict_result.append(row)

		else:
			sql = "SELECT * FROM VIDEO WHERE LOWER(VIDEO_TITLE) LIKE LOWER(%s)"
			cursor.execute(sql, [search])
			result = cursor.fetchall()
			dict_result = []

			for r in result:
				video_id = r[0]
				video_title = r[1]
				description = r[2]
				rating = r[6]
				row = {'video_id': video_id, 'video_title': video_title, 'description': description, 'rating': rating}
				dict_result.append(row)

		sql = "SELECT * FROM CATEGORY"
		cursor.execute(sql)
		result = cursor.fetchall()
		dict_category = []
		for r in result:
			category_id = r[0]
			category_name = r[1]
			row = {'category_id': category_id, 'category_name': category_name}
			dict_category.append(row)

		sql = "SELECT * FROM COUNTRY"
		cursor.execute(sql)
		result = cursor.fetchall()
		dict_country = []
		for r in result:
			country_id = r[0]
			country_name = r[1]
			row = {'country_id': country_id, 'country_name': country_name}
			dict_country.append(row)

		sql = "SELECT * FROM LANGUAGE"
		cursor.execute(sql)
		result = cursor.fetchall()
		dict_language = []
		for r in result:
			language_id = r[0]
			language_name = r[1]
			row = {'language_id': language_id, 'language_name': language_name}
			dict_language.append(row)

		cursor.close()
		return render(request, 'video/search.html', {'search': request.GET.get('title', ''), 'video': dict_result, 'category': dict_category, 'country': dict_country, 'language': dict_language})
	else:
		return render(request, 'user/login.html', )


def Rate(request, id):
	if request.session.get('id'):
		rate = request.GET.get('rating', '')
		cursor = connection.cursor()

		try:
			sql = 'INSERT INTO "AMAZON"."RATING_TABLE" VALUES( %s, %s, %s);'
			cursor.execute(sql, [request.session.get('id'), id, rate])
		except:
			sql = 'UPDATE "RATING_TABLE" SET RATE=%s WHERE USER_ID=%s AND VIDEO_ID=%s;'
			cursor.execute(sql, [rate, request.session.get('id'), id])

		cursor.execute("""
		BEGIN 
			VIDEO_RATING_UPDATE(:inVal);
		END;
		/""", {"inVal": id})

		cursor.close()
		response = redirect('/video/' + id.__str__())
		return response
	else:
		return render(request, 'user/login.html', )


def Cast(request, id):
	if request.session.get('id'):
		cursor = connection.cursor()

		sql = "SELECT * FROM CAST_CREW WHERE CREW_ID=%s"
		cursor.execute(sql, [id])
		cast_name = cursor.fetchall()[0][1]
		cast = {'cast_name': cast_name}

		sql = "SELECT * FROM VIDEO JOIN VIDEO_CAST_CREW ON VIDEO.VIDEO_ID=VIDEO_CAST_CREW.VIDEO_ID WHERE VIDEO_CAST_CREW.CREW_ID=%s;"
		cursor.execute(sql, [id])
		result = cursor.fetchall()
		cursor.close()
		dict_result = []

		for r in result:
			video_id = r[0]
			video_title = r[1]
			description = r[2]
			rating = r[6]
			row = {'video_id': video_id, 'video_title': video_title, 'description': description, 'rating': rating}
			dict_result.append(row)

		return render(request, 'video/cast.html', {'cast': cast, 'video': dict_result})
	else:
		return render(request, 'user/login.html', )


def MoviesFranchise(request):
	if request.session.get('id'):
		cursor = connection.cursor()
		sql = "SELECT * FROM MOVIE_FRANCHISE;"

		cursor.execute(sql)
		result = cursor.fetchall()
		cursor.close()
		dict_result = []

		for r in result:
			franchise_id = r[0]
			franchise_title = r[1]
			row = {'franchise_id': franchise_id, 'franchise_title': franchise_title}
			dict_result.append(row)

		return render(request, 'video/moviefranchise.html', {'MoviesFranchise': dict_result})

	else:
		return render(request, 'user/login.html', )


def MoviesFranchiseDetails(request, id):
	if request.session.get('id'):
		cursor = connection.cursor()
		sql = "SELECT * FROM MOVIE_FRANCHISE WHERE MOVIE_FRANCH_ID=%s;"

		cursor.execute(sql, [id])
		result = cursor.fetchall()
		franchise_id = result[0][0]
		franchise_title = result[0][1]
		franchise = {'franchise_id': franchise_id, 'franchise_title': franchise_title}

		sql = "SELECT * FROM VIDEO JOIN MOVIE_VIDEO ON VIDEO.VIDEO_ID=MOVIE_VIDEO.MOVIE_ID WHERE MOVIE_VIDEO.MOVIE_FRANCH_ID=%s;"

		cursor.execute(sql, [id])
		result = cursor.fetchall()
		cursor.close()
		dict_result = []

		for r in result:
			video_id = r[0]
			video_title = r[1]
			description = r[2]
			release_date = r[3]
			rating = r[6]
			row = {'video_id': video_id, 'video_title': video_title, 'description': description, 'release_date': release_date, 'rating': rating}
			dict_result.append(row)

		return render(request, 'video/moviefranchisedetails.html', {'franchise': franchise, 'movie': dict_result})

	else:
		return render(request, 'user/login.html', )


