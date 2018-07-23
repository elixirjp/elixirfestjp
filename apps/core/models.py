from django.contrib.auth.models import User
from django.db import models


class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    email = models.EmailField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ex_entry'
        verbose_name = verbose_name_plural = 'スピーカー応募申込'


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ex_news'
        verbose_name = verbose_name_plural = 'お知らせ'


class Session(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    speaker = models.CharField(max_length=100)
    speaker_icon = models.ImageField(upload_to='speaker')
    twitter_link = models.URLField(blank=True)
    order = models.IntegerField(default=0)
    is_keynote = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ex_session'
        ordering = ['-is_keynote', 'order']
        verbose_name = verbose_name_plural = 'セッション内容'


class LightningTalk(models.Model):
    title = models.CharField(max_length=255)
    speaker = models.CharField(max_length=100)
    speaker_icon = models.ImageField(upload_to='lt')
    twitter_link = models.URLField(blank=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ex_lightning_talk'
        ordering = ['order']
        verbose_name = verbose_name_plural = 'ライトニングトーク'
