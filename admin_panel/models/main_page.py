from django.db import models


class BackImg(models.Model):
    img = models.ImageField(upload_to='photos/%Y/%m/%d/', max_length=100, unique=True, null=True)
    link = models.URLField(default='')
    title = models.CharField(max_length=50,default='')

    class Meta:
        db_table = 'back_img'


class BottomCarousel(models.Model):
    img = models.ImageField(upload_to='photos/%Y/%m/%d/', max_length=100, unique=True, null=True)

    class Meta:
        db_table = 'bottom_carousel'


class TopCarousel(models.Model):
    img = models.ImageField(upload_to='photos/%Y/%m/%d/', max_length=100, unique=True, null=True)
    link = models.URLField(default='')

    class Meta:
        db_table = 'top_carousel'
