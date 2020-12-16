<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import ArticleForm

from .models import Article,Comment

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-id')
=======
from django.shortcuts import render
from .models import Article

# Create your views here.

def index(request):
    articles = Article.objects.all()
>>>>>>> django_crud/master
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

<<<<<<< HEAD
# def new(request):
#     return render(request, 'articles/new.html')

def create(request):
    # 저장 로직
    if request.method == 'POST':
    # POST 요청 -> 검증 및 저장
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        article_form = ArticleForm(request.POST)
        # 검증
        if article_form.is_valid():
        # 검증에 성공하면 저장하고
            # title = article_form.cleaned_data.get('title')
            # content = article_form.cleaned_data.get('content')
            # article = Article(title=title, content=content)
            article = article_form.save()
            # redirect
            return redirect('articles:detail', article.pk)
        # else:
            # 다시 폼으로 돌아가는 과정을 중복되어서 제거했음. 
    else:
    # GET 요청 -> Form
        article_form = ArticleForm()
    # GET -> 비어있는 Form context
    # POST -> 검증 실패시 에러메세지와 입력겂 다시 context
    context = {
        'article_form':article_form
    }
    return render(request, 'articles/new.html',context)


def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comments':comments,
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    # if request.method == 'POST':
    article.delete()
    # messages.add_message(request,messages.INFO, '댓글이 삭제되었습니다.')
    
    return redirect('articles:index')
    # else:
    #     return redirect('articles:detail', article.pk)

# def edit(request, article_pk):
#     article = Article.objects.get(pk=article_pk)
#     context = {
#         'article': article
#     }
#     return render(request, 'articles/edit.html', context)

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST,instance=article)
        if article_form.is_vaild():   
            article_form.save()
            return redirect('articles:detail', article.pk)
    else:
        article_form = ArticleForm(initial=article)
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/edit.html', context)

# def comment_create(request, article_pk):
#     article = Article.objects.get(pk=article_pk) # 안가져와도 됨
#     content = request.POST.get('content')
#     comment = Comment(article=article, content=content)
#     comment.save()
#     return redirect('article:detail',article.pk)

# def comment_create(request,article_pk):
#     article = Article.objects.get(pk=article_pk)
#     comment = Comment()
#     comment.content = request.POST.get('comment_content')
#     comment.article = article
#     # comment.article_id = article_pk
#     comment.save()
#     return redirect('articles:detail',article.pk)

def comment_create(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    comment = Comment()
    comment.content = request.POST.get('comment_content')
    comment.article = article
    comment.save()
    return redirect('articles:detail', article.pk)

def comment_delete(request,comment_pk,article_pk):
    messages.error(request, '댓글이 삭제되었습니다.')
    comment = Comment.objects.get(pk=comment_pk)
    article = Article.objects.get(pk=article_pk)
    comment.delete()
    return redirect('articles:detail', article.pk)
=======

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # 저장 로직
    title = request.GET.get('title')
    contet = request.GET.get('content')
    article = Article(title=title, content=content)
    article.save()
    context = {
        'article':article
    }
    return render(request, 'articles/create.html',conext)
>>>>>>> django_crud/master
