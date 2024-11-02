from django.db import models
from users.models import Users


class Category(models.Model):
    cat_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.cat_name


class Bars(models.Model):
    owner_bar = models.ForeignKey(
        to=Users,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    img = models.ImageField(upload_to='bars_img')
    bar_category = models.ManyToManyField(
        to=Category,
        db_index=True
    )
    public = models.BooleanField(
        default=True,
        db_index=True
    )

    def __str__(self):
        return self.name
    
    
class ImgBar(models.Model):
    where_img = models.ForeignKey(
        to=Bars,
        on_delete=models.CASCADE
    )
    img = models.ImageField(upload_to='bars_img')
    name_img = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name_img
    
    
class BarMessages(models.Model):
    where_message = models.ForeignKey(
        to=Bars,
        on_delete=models.CASCADE
    )
    owner_message = models.ForeignKey(
        to=Users,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class FavoriteBar(models.Model):
    whose_bar = models.ForeignKey(
        to=Users,
        on_delete=models.CASCADE
    )
    bar = models.ManyToManyField(
        to=Bars,
        related_name='favorite_bar',
        blank=True,
        null=True
    )