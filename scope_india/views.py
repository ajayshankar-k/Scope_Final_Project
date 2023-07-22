from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail.message import EmailMessage
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import json
import random

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')


#------------------- contact page ------------------

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        frommail = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['Message']
        obj = Contact()
        obj.name = name
        obj.email = frommail
        obj.subject = subject
        obj.message = message
        obj.save()
        tomail = 'info@scopeindia.org'
        send_mail = EmailMessage(subject,message,frommail,[tomail])
        send_mail.send()
        messages.success(request,'Mail send successfully!!!',extra_tags='contact')
        return redirect('contact')
    else:
        return render(request,'contact.html')



# --------------------- registration page ---------------------------------------------------

def registration(request):

    if request.method=='POST':
        ran = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
           'O','P','R','S','T','U','V','X','Y','Z',
           '0','1','2','3','4','5','6','7','8','9']
        rando = random.sample(ran,10)
        password_list = ''
        for i in rando:
            password_list = password_list + i

        obj = Student(request.POST,request.FILES)
        fname = request.POST['fname']
        lname = request.POST['lname']
        gender = request.POST['gender']
        dob = request.POST['dob']
        email = request.POST['email']
        phone = request.POST['phone']
        country =request.POST['country']
        state = request.POST['state']
        city = request.POST['city']
        avatar = request.FILES['avatar']
        hobby = request.POST.getlist('hobby[]')

        password_list2 = make_password(password_list)

        obj = Student()
        obj1 = User()
        
        obj.fname = fname
        obj.lname = lname
        obj.gender = gender
        obj.dob = dob
        obj.email = email
        obj.phone = phone
        obj.country = country
        obj.state = state
        obj.city = city
        obj.avatar = avatar
        obj.hobby = hobby
        obj.password = password_list
        obj1.username = email
        obj1.password = password_list2
       
        if User.objects.filter(username=email).exists():
            messages.error(request,'Email already exist!!!',extra_tags='exist')
            return redirect('register')
        else:
            obj.save()
            obj1.save()
            
            subject = 'Registration Success'
            message = f'{password_list} , is your temporary password use it reset your password'
            frommail = 'ajayshaz35@gmail.com'
            tomail = email 
            send_mail = EmailMessage(subject,message,frommail,[tomail])
            send_mail.send()
            messages.success(request,'Registration success!!!',extra_tags='signup')
            return redirect('signin')


    return render(request,'register.html')

#-------------------------------------------------- dashboard -------------------------------------------------------------

#----------- Main Dashboard available courses -----------

@login_required(login_url='signin')
def dashboard(request):
    user = request.user
    semail = user.username
    savatar = Student.objects.get(email=semail)
    student_count = Student.objects.all().count()
    course_count = Course.objects.all().count()
    search_data = Course.objects.all()
    enroll_count = Picked.objects.filter(email=semail).count()
    

    return render(request,'dashboard.html',{'student_count':student_count,'savatar':savatar,'search_data':search_data,'course_count':course_count,'enroll_count':enroll_count,})

#------- signup course logic --------

@login_required(login_url='signin')
def signedup(request):
    if request.method == 'POST':
        course_id = request.POST['course_id']
        user_id = request.POST['user_id']
        user = request.user
        semail = user.username
        course_exist = Picked.objects.filter(email=semail)
        for course in course_exist:
            if course.Course_id == course_id:
                messages.error(request,'You have already Signedup for this course!!!',extra_tags='course')
                return redirect('dashboard')
        else:
            obj3 = Picked()
            obj3.Course_id = course_id
            obj3.user_id = user_id
            obj3.email = semail
            obj3.save()
            messages.error(request,'Signup successfull!!!',extra_tags='course_success')
            return redirect('course_signup')
    else:
        return HttpResponse('failed')




#----------- Courses Signed up page -----------

@login_required(login_url='signin')
def course_signup(request):
    user = request.user
    semail = user.username
    savatar = Student.objects.get(email=semail)
    course_signed = Picked.objects.filter(email=semail)
    ids=[]
    for i in course_signed:
        ids.append(i.Course_id)
    signedup = Course.objects.filter(id__in=ids)
    for i in signedup:
        i.title
    return render(request,'course_signup.html',{'savatar':savatar,'signedup':signedup})

#----------- profile page -----------

@login_required(login_url='signin')
def profile1(request):
    user = request.user
    semail = user.username
    savatar = Student.objects.get(email=semail)
    return render(request,'profile.html',{'savatar':savatar})

#----------- profile edit page -----------

@login_required(login_url='signin')
def profile_edit(request):
    user = request.user
    semail = user.username
    savatar = Student.objects.get(email=semail)

    if request.method=='POST':
        edit_fname = request.POST['edit_fname']
        edit_lname = request.POST['edit_lname']
        edit_gender = request.POST['edit_gender']
        edit_phone = request.POST['edit_phone']
        edit_country = request.POST['edit_country']
        edit_state = request.POST['edit_state']
        edit_city = request.POST['edit_city']
        try:
            obj=Student.objects.get(email=semail)
            obj.avatar=request.FILES['edit_avatar']
            obj.save()
            Student.objects.filter(email=semail).update(fname=edit_fname,lname=edit_lname,gender=edit_gender,phone=edit_phone,country=edit_country,state=edit_state,city=edit_city)
            messages.success(request,'Profile updated successfully !!!',extra_tags='profile')
            return redirect('profile')
        except:
            Student.objects.filter(email=semail).update(fname=edit_fname,lname=edit_lname,gender=edit_gender,phone=edit_phone,country=edit_country,state=edit_state,city=edit_city)
            savatar = Student.objects.get(email=semail)
            messages.success(request,'Profile updated successfully !!!',extra_tags='profile')
            return render(request,'profile.html',{'savatar':savatar})

    else:
        return render(request,'profile_edit.html',{'savatar':savatar})
    
#----------- Search page -----------
    
@login_required(login_url='signin')
def search(request):
    user = request.user
    semail = user.username
    savatar = Student.objects.get(email=semail)
    if 'search' in request.GET:
        search = request.GET['search']
        search_data = Course.objects.filter(title__icontains=search)
        if request.method == 'POST':
            course_id = request.POST['course_id']
            user_id = request.POST['user_id']
            user = request.user
            semail = user.username
            course_exist = Picked.objects.filter(email=semail)
            for course in course_exist:
                if course.Course_id == course_id:
                    messages.error(request,'You have already Signedup for this course!!!',extra_tags='course')
                    return redirect('dashboard')
            else:
                obj3 = Picked()
                obj3.Course_id = course_id
                obj3.user_id = user_id
                obj3.email = semail
                obj3.save()
                messages.error(request,'You have already Signedup for this course!!!',extra_tags='course_success')
                return redirect('course_signup')

        return render(request,'search.html',{'savatar':savatar,'search_data':search_data})
    else:
        return redirect('dashboard')
    
#----------- Change password page -----------

@login_required(login_url='signin')
def change_pass(request):
    user = request.user
    semail = user.username
    savatar = Student.objects.get(email=semail)
    if request.method=='POST':
        pass_email = request.POST['pass_email']
        new_pass = request.POST['new_pass']
        user = request.user
        semail = user.username

        if semail==pass_email:
            User.objects.filter(username=pass_email).update(password=make_password(new_pass))
            messages.success(request,'Password updated successfully!!!',extra_tags='pass')
            logout(request)
            return redirect('signin')
        else:
            messages.error(request,'Enter email correctly!!!',extra_tags='signin')
            return render(request,'change_pass.html')
    
    return render(request,'change_pass.html',{'savatar':savatar})


# --------------------- login / logout ---------------------------------------------------
def signin(request): 
 
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            if user.check_password(password):
                if request.POST.get('chk'):
                    request.session.set_expiry(0)
                else:
                    request.session.set_expiry(259200) 
                    request.session.modified = True    
                
                login(request,user)
                return redirect ('dashboard')
            else:
                messages.error(request,'Incorrect password!!!',extra_tags='signin')
                return redirect('signin')
        else:
            messages.error(request,'Incorrect username!!!',extra_tags='signin')
            return redirect('signin') 
    else:
        return render(request,'login.html')
   
#------------------ logout --------------------

def signout(request):
    logout(request)
    return redirect('signin')

#------------------------------------------ Forget password ---------------------------------------------------------------------

def forget_pass(request):
    if request.method=='POST':
        forget_email= request.POST['forget_email']
        ran = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
           'O','P','R','S','T','U','V','X','Y','Z',
           '0','1','2','3','4','5','6','7','8','9']
        rando = random.sample(ran,10)
        password_list = ''
        for i in rando:
            password_list = password_list + i
        if User.objects.filter(username=forget_email).exists():
            Student.objects.filter(email=forget_email).update(password=password_list)
            subject = 'Your OTP'
            message = f'{password_list} , is your otp do not share your otp'
            frommail = 'ajayshaz35@gmail.com'
            tomail = forget_email
            send_mail = EmailMessage(subject,message,frommail,[tomail])
            send_mail.send()
            return redirect('otp')
        else:
            messages.error(request,'Enter correct email !!!',extra_tags='forget_pass')
            return redirect('forget_pass')


    else:
        return render(request,'forget_pass.html')
    
#----------- otp page -----------
    
def otp(request):
    if request.method=='POST':
        new_otp = request.POST['new_otp']
        new_pass = request.POST['new_pass']
        student2 = Student.objects.get(password=new_otp)
        if new_otp == student2.password:
            User.objects.filter(username=student2.email).update(password=make_password(new_pass))
            messages.success(request,'Password changed successfully !!!',extra_tags='otp')
            return redirect('signin')
        else:
            messages.error(request,'Enter correct OTP !!!',extra_tags='otp')
            return redirect('otp')
    else:
        return render(request,'otp.html')

    

# Create your views here.
