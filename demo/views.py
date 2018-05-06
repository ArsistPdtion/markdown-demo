from django.shortcuts import render
from django.http import HttpResponse
from .models import Dictory,ExampleModel,DocumentDemo
from markdown_demo.settings import MEDIA_ROOT
import markdown

# Create your views here.

def index(request):
    # print('123')
    book_list = DocumentDemo.objects.all().values('name','content')
    for book in book_list:
        print('path:', '/home/administrator/mybook/mongo/' + book['name'])
        with open(r'/home/administrator/mybook/mongo/' + book['name'] ,'w') as f:
            f.write(book['content'])
    return render(request,'show_file.html')

def get_file(request):
    file = Dictory.objects.all().values('summary')
    # print(type(file[0]))
    # a = file['summary']
    print("file[0]['summary']",file[0]['summary'])
    print('file lujing',MEDIA_ROOT+file[0]['summary'])
    # with open(MEDIA_ROOT+file[0]['summary'],'r') as f:
    file_list = file[0]['summary'].split('/')
    print('file list',file_list)
    file_url = '\\' + file_list[0] + '\\' + file_list[1]
    with open(MEDIA_ROOT + file_url ) as f:
        # print(f.read())
        file_content = f.read()
        print(file_content)
    return render(request,'show_file.html',{'file':file_content})

def get_desc(request):
    dictory = Dictory()
    dictory.desc = markdown.markdown(dictory.desc,
                                     extensions = [
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                         'markdown.extensions.toc',
                                     ])
    return render(request,'show_file.html',context={'dictory':dictory})


