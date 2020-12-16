from django.contrib import admin

# Register your models here.
<<<<<<< HEAD

from .models import Article, Comment

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title','content','created_at','updated_at')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','content','article_id')

admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment,CommentAdmin)
=======
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at')
admin.site.register(Article, ArticleAdmin)

>>>>>>> django_crud/master
