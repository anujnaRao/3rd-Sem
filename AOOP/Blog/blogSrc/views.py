from django.shortcuts import render, redirect
from blogSrc.models import Blog
from blogSrc.forms import createBlog
from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse


# Create your views here.

class Index(TemplateView):
    template_name = 'index.html'


def upload(request):
    upload = createBlog()
    if request.method == 'POST':
        upload = createBlog(request.POST)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'insert.html', {'upload_form': upload})


def display(request):
    shelf = Blog.objects.all()
    return render(request, 'display.html', {'shelf': shelf})
