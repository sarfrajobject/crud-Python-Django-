from django.contrib import admin

# Register your models here.
from.models import blog_posts

class blog_postsAdmin(admin.ModelAdmin):
    list_display = ('title','tag','author')
admin.site.register(blog_posts,blog_postsAdmin)