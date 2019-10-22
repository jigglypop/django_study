from django.db import models

# Create your models here.

class User(models.Model):
    username = models.TextField()


class Article(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(User,related_name='like_articles')
   
class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# User 2명, Article 2개, Comment 4개

# u1 = User.objects.create(username='Kim')
# u2 = User.objects.create(username='Lee')

# a1 = Article.objects.create(title='1글', user=u1)
# a2 = Article.objects.create(title='2글', user=u2)
# a3 = Article.objects.create(title='3글', user=u2)
# a4 = Article.objects.create(title='4글', user=u2)

# c1 = Comment.objects.create(content='1글1댓', article=a1, user=u2)
# c2 = Comment.objects.create(content='1글2댓', article=a1, user=u2)
# c3 = Comment.objects.create(content='2글1댓', article=a2, user=u1)
# c4 = Comment.objects.create(content='4글1댓', article=a4, user=u1)
# c5 = Comment.objects.create(content='3글1댓', article=a3, user=u2)
# c6 = Comment.objects.create(content='3글2댓', article=a3, user=u1)
