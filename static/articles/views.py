from django.shortcuts import render,redirect,get_object_or_404
from .models import Article,Comment
from .forms import ArticleForm,CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    return render(request,'articles/index.html',{'articles':articles})

def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save()
            return redirect('articles:detail', article.pk)
    else:
        article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/create.html', context)

    
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()
    comment_form = CommentForm()
    context = {
        'article': article,
        'comments': comments,
        'comment_form': comment_form
    }
    return render(request, 'articles/detail.html', context)

def update(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST,instance=article)
        if article_form.is_valid():
            article = article_form.save()
            article_pk = article.pk
            return redirect(f'/articles/{article_pk}/detail/')
    else:
        form = ArticleForm(instance=article)
    context = {
        'form':form
    }
    return render(request,'articles/update.html',context)
    
def delete(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('/articles/')

def comment_create(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect('articles:detail',article_pk)

def comment_delete(request,article_pk,comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    article = comment.article
    comment.delete()
    article_pk = article.pk
    return redirect('articles:detail',article_pk)