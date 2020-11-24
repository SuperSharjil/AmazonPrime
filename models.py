# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CastCrew(models.Model):
    crew_id = models.FloatField(primary_key=True)
    crew_title = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cast_crew'


class Category(models.Model):
    category_id = models.FloatField(primary_key=True)
    category_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


class Country(models.Model):
    country_id = models.FloatField(primary_key=True)
    country_name = models.CharField(max_length=100)
    country_flag = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class Favourites(models.Model):
    user = models.OneToOneField('User', models.DO_NOTHING, primary_key=True)
    video = models.ForeignKey('Video', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'favourites'
        unique_together = (('user', 'video'),)


class Language(models.Model):
    language_id = models.FloatField(primary_key=True)
    language_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'language'


class MovieFranchise(models.Model):
    movie_franch_id = models.FloatField(primary_key=True)
    movie_franch_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie_franchise'


class MovieVideo(models.Model):
    movie = models.OneToOneField('Video', models.DO_NOTHING, primary_key=True)
    movie_franch = models.ForeignKey(MovieFranchise, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'movie_video'
        unique_together = (('movie', 'movie_franch'),)


class Payment(models.Model):
    transaction_id = models.FloatField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING)
    transaction_date = models.DateField()
    amount = models.FloatField()
    subscription_over_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'payment'


class RatingTable(models.Model):
    user = models.OneToOneField('User', models.DO_NOTHING, primary_key=True)
    video = models.ForeignKey('Video', models.DO_NOTHING)
    rate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rating_table'
        unique_together = (('user', 'video'),)


class Series(models.Model):
    series_id = models.FloatField(primary_key=True)
    series_title = models.CharField(max_length=255)
    seasons = models.FloatField()
    episodes = models.FloatField()
    start_date = models.DateField()
    ongoing_status = models.FloatField()

    class Meta:
        managed = False
        db_table = 'series'


class SeriesVideo(models.Model):
    series = models.OneToOneField(Series, models.DO_NOTHING, primary_key=True)
    video = models.ForeignKey('Video', models.DO_NOTHING)
    season_num = models.FloatField()
    episode_num = models.FloatField()

    class Meta:
        managed = False
        db_table = 'series_video'
        unique_together = (('series', 'video'),)


class Trending(models.Model):
    trending_id = models.FloatField(primary_key=True)
    video = models.ForeignKey('Video', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'trending'


class User(models.Model):
    user_id = models.FloatField(primary_key=True)
    user_name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    credit_card_id = models.FloatField()
    date_of_birth = models.DateField()
    age = models.FloatField()
    country = models.ForeignKey(Country, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user'


class Video(models.Model):
    video_id = models.FloatField(primary_key=True)
    video_title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    release_date = models.DateField()
    duration = models.FloatField()
    video_type = models.FloatField()
    rating = models.FloatField(blank=True, null=True)
    restriction = models.FloatField(blank=True, null=True)
    region = models.ForeignKey(Country, models.DO_NOTHING, db_column='region', blank=True, null=True)
    watch_count = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'video'


class VideoCastCrew(models.Model):
    video = models.OneToOneField(Video, models.DO_NOTHING, primary_key=True)
    crew = models.ForeignKey(CastCrew, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'video_cast_crew'
        unique_together = (('video', 'crew'),)


class VideoCategory(models.Model):
    video = models.OneToOneField(Video, models.DO_NOTHING, primary_key=True)
    category = models.ForeignKey(Category, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'video_category'
        unique_together = (('video', 'category'),)


class VideoLanguage(models.Model):
    video = models.OneToOneField(Video, models.DO_NOTHING, primary_key=True)
    language = models.ForeignKey(Language, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'video_language'
        unique_together = (('video', 'language'),)


class Watch(models.Model):
    user = models.OneToOneField(User, models.DO_NOTHING, primary_key=True)
    video = models.ForeignKey(Video, models.DO_NOTHING)
    watch_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'watch'
        unique_together = (('user', 'video'),)
