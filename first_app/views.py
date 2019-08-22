from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord, UserInfo
# Create your views here.

# def index(request):
#     return HttpResponse("Hello World!")

def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records' : webpage_list}
    my_dict = {'insert_hugo': "heellooo this is hugo from viewl.py"}
    return render(request, 'first_app/index.html', context = date_dict)

def help(request):
    my_dict = {'insert_help': 'please help hugo to get scuess'}
    return render(request, 'first_app/help.html', context = my_dict)

def jump(request):
    my_info = {'jump_info': 'how high can you jump'}
    return render(request, 'first_app/jump.html', context = my_info)

def user(request):
    # user_info = {'user_info': 'tempurate user info'}
    user_list = UserInfo.objects.order_by('firstName')
    user_dict = {'user_info' :user_list}

    return render(request, 'first_app/user.html', context = user_dict)


# def index(request):
#     my_dict = {'insert_me':"Hello I am from views.py!"}
#     return render(request,'first_app/index.html',context=my_dict)
