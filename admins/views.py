from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.

def login_admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # تم تسجيل الدخول بنجاح، يمكنك توجيه المستخدم إلى الصفحة الرئيسية أو أي صفحة أخرى
            return redirect('login_admin')
        else:
            # فشل تسجيل الدخول، يجب إظهار رسالة خطأ للمستخدم
            error_message = 'Invalid username or password'
            return render(request, 'admins/login.html', {'error_message': error_message})
    else:
        # الطلب GET، يجب التحقق من حالة تسجيل الدخول
        if request.user.is_authenticated:
            # المستخدم مسجل الدخول بالفعل، يمكن توجيهه إلى الصفحة الرئيسية أو أي صفحة أخرى
            return redirect('login_admin')
        else:
            # المستخدم لم يسجل الدخول، يتم عرض صفحة تسجيل الدخول
            return render(request, 'admins/login.html')