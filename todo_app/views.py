from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . models import Todo, TodoMirror

# Create your views here.
def post_form(request):
    return render(request, 'todo_app/post/new_post.html')

def post_detail(request, pk):
    post = get_object_or_404(Todo, id=pk)
    return render(request, 'todo_app/post/detail.html', {'post': post})

def todo_list(request):
    object_list = Todo.objects.all()

    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request, 'todo_app/post/list.html', {'page': page, 'posts': posts})

def new_post(request):
    if request.method == 'POST':
        return render(request, 'todo_app/post/detail.html', {'post': post})

    else:
        return render(request, 'todo_app/post/new_post.html')
