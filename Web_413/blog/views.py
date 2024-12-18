from django.shortcuts import render
from blog.models import Article


def index(request):
    data = Article.objects.all()
    context = {
        "data":data,
    }
    return render(request, "list.html", context)

def detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'article_detail.html', {'article': article})
