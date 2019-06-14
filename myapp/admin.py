from django.contrib import admin


from .models import WingmanUser, Post, WingmanReview



# Register your models here.
admin.site.register(Post)
admin.site.register(WingmanUser)
admin.site.register(WingmanReview)
