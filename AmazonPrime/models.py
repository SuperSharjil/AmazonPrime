# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CastCrew(models.Model):
    crew = models.OneToOneField('Video', models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cast_crew'


class Category(models.Model):
    category_id = models.FloatField(primary_key=True)
    category_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'category'


class Country(models.Model):
    country_id = models.FloatField(primary_key=True)
    name = models.CharField(max_length=255)
    flag = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'country'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Movie(models.Model):
    duration = models.DateTimeField()
    starring = models.BigIntegerField()
    director = models.BigIntegerField()
    movie_series = models.ForeignKey('MovieSeries', models.DO_NOTHING, db_column='movie_series', blank=True, null=True)
    movie = models.OneToOneField('Video', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'movie'


class MovieSeries(models.Model):
    movie_series_id = models.FloatField(primary_key=True)
    series_id = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'movie_series'


class Payment(models.Model):
    transaction_id = models.FloatField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING)
    transaction_date = models.DateField()
    amount = models.BigIntegerField()
    subscription_over_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'payment'


class Series(models.Model):
    seasons = models.BigIntegerField()
    episodes = models.BigIntegerField()
    episode_duration = models.CharField(max_length=255)
    starring = models.ForeignKey(CastCrew, models.DO_NOTHING, db_column='starring')
    director = models.BigIntegerField()
    start_date = models.DateField()
    ongoing_status = models.BigIntegerField()
    series = models.OneToOneField('Video', models.DO_NOTHING, primary_key=True)
    series_title = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'series'


class User(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    credit_card = models.BigIntegerField()
    date_of_birth = models.DateField()
    age = models.BigIntegerField()
    country = models.ForeignKey(Country, models.DO_NOTHING, db_column='country', blank=True, null=True)
    preference = models.ForeignKey(Category, models.DO_NOTHING, db_column='preference', blank=True, null=True)
    history = models.ForeignKey('Video', models.DO_NOTHING, db_column='history', blank=True, null=True)
    favourites = models.BigIntegerField(blank=True, null=True)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user'


class Video(models.Model):
    video_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    release_date = models.DateField()
    preview = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='category')
    rating = models.FloatField()
    age_restriction = models.BigIntegerField()
    region = models.ForeignKey(Country, models.DO_NOTHING, db_column='region')
    language = models.CharField(max_length=255)
    closed_caption = models.BigIntegerField(blank=True, null=True)
    external_link = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'video'

    def __str__(self):
        return self.title