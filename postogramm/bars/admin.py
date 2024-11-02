from django.contrib import admin
from .models import Bars, Category, BarMessages, FavoriteBar, ImgBar

admin.site.register(Bars)
admin.site.register(BarMessages)
admin.site.register(Category)
admin.site.register(FavoriteBar)
admin.site.register(ImgBar)