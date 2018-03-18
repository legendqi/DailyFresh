import string

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import *
from hashlib import sha1
# Create your views here.


def register(request):
    return render(request, 'df_user/register.html')


def register_handle(request):
    # 接受用户输入
    post = request.POST
    user_name = post.get('user_name')
    pwd = post.get('pwd')
    cpwd = post.get('cpwd')
    email = post.get('email')
    # 判断两次密码是否一致
    if pwd != cpwd:
        # 重定向到这个地址
        return redirect('/user/register/')
    else:
        # 密码加密
        s1 = sha1()
        s1.update(pwd.encode('utf-8'))
        # s1.update(pwd)
        store_pwd = s1.hexdigest()
        # 创建对象，把信息储存到数据库中
        userinfo = UserInfo()
        userinfo.email = email
        userinfo.username = user_name
        userinfo.password = store_pwd
        userinfo.save()
        # 注册成功转到登录页面
        return redirect('/user/login/')


def login(request):
    uname = request.COOKIES.get('uname', '')
    context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 1, 'uname': uname,}
    return render(request, 'df_user/login.html', context)


def register_exist(request):
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count': count})


def user_login_handle(request):
    post = request.POST
    username = post.get('username')
    pwd = post.get('pwd')
    jizhu = post.get('jizhu', 0)
    # 根据用户名查询对象
    users = UserInfo.objects.filter(username=username)#[]
    if len(users) == 1:
        s1 = sha1()
        s1.update(pwd.encode('utf-8'))
        if s1.hexdigest() == users[0].password:
            red = HttpResponseRedirect('/user/user_center_info/')
            # 记住用户名
            if jizhu!=0:
                red.set_cookie('username', username)
            else:
                red.set_cookie('username', '', max_age=-1)
            request.session['user_id'] = users[0].id
            request.session['user_name'] = username
            return red
        else:
            context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 1, 'uname': username, 'upwd': pwd}
            return render(request, 'df_user/login.html', context)
    else:
        context = {'title': '用户登录', 'error_name': 1, 'error_pwd': 0, 'uname': username, 'upwd': pwd}
        return render(request, 'df_user/login.html', context)


def user_center_info(request):
    user_email = UserInfo.objects.get(id=request.session['user_id']).email
    context = {'title': '用户中心', 'user_email': user_email,
               'user_name': request.session['user_name']}
    return render(request, 'df_user/user_center_info.html', context)