import smtplib
from email.utils import make_msgid
from os import popen

from MySQLdb import connect
from django.shortcuts import render, redirect
from django.urls import reverse

from django.core.files.storage import FileSystemStorage
import os
from owner.settings import BASE_DIR

from .models import addbuilderdetails,addbookingdetails,addcustomerdetails,addprojectdetails,addsitedetails,userlogin,newreg

# Create your views here.

def index(request):
    return render(request,"index.html")

def userreg(request):
    if request.method == "POST":
        s1 = request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        s5 = request.POST.get('t5')
        newreg.objects.create(name=s1, email_id=s2, password=s3, contact_no=s4, city=s5)
        userlogin.objects.create(username=s2, password=s3,utype='user')
        base_url = reverse('logcheck')
        msg = "new user created"
        return redirect(base_url, msg=msg)
    return render(request,"reg.html")

def homeabout(request):
    return render(request,"about.html")

def insertbooking(request):
    if request.method == "POST":
        s1 = request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        s5 = request.POST.get('t5')
        addbookingdetails.objects.create(customer_id=s1, project_id=s2, site_no=s3, booking_date=s4, cost=s5)
        return render(request, "bookingdetails.html")
    return render(request,"bookingdetails.html")


def insertbuilder(request):
    if request.method == "POST":
        s1 = request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        s5 = request.POST.get('t5')
        s6 = request.POST.get('t6')
        s7 = request.POST.get('t7')
        addbuilderdetails.objects.create(builder_name=s1, company_name=s2, start_date=s3, no_of_project=s4, web_site=s5, email_id=s6, contact_no=s7)
        return render(request, "builderdetails.html")
    return render(request,"builderdetails.html")


def insertcustomer(request):
    if request.method == "POST":
        s1 = request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        s5 = request.POST.get('t5')
        addcustomerdetails .objects.create(customer_id=s1, name=s2, address	=s3, city=s4, contact_no=s5)
        return render(request, "customerdeatils.html")
    return render(request,"customerdeatils.html")


def insertproject(request):
    if request.method == "POST" and request.FILES['myfile']:
        s1 = request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        s5 = request.POST.get('t5')
        s6 = request.FILES['myfile']
        s7 = request.POST.get('t7')

        fs = FileSystemStorage()
        filename = fs.save(s6.name, s6)
        uploaded_file_url = fs.url(filename)
        pat = os.path.join(BASE_DIR, '/media/' + filename)


        addprojectdetails.objects.create(project_id=s1, name=s2, location=s3, details=s4, start_date=s5, plan_image=s6, end_date=s7)
        return render(request, "pojectdetails.html")
    return render(request,"pojectdetails.html")


def insertsite(request):
    if request.method == "POST":
        s1 = request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3')
        s4 = request.POST.get('t4')
        s5 = request.POST.get('t5')
        addsitedetails.objects.create(project_id=s1, site_no=s2, size=s3, site_type=s4, estimate_cost=s5)
        return render(request,"sitedeatils.html")
    return render(request,"sitedeatils.html")

def viewbooking(request):
    userdict=addbookingdetails.objects.all()
    return render(request,"showbooking.html",{"userdict":userdict})

def viewbuilders(request):
    userdict=addbuilderdetails.objects.all()
    return render(request,"showbuilder.html",{"userdict":userdict})

def viewcustomer(request):
    userdict=newreg.objects.all()
    return render(request,"showcustomer.html",{"userdict":userdict})

def viewproject(request):
    userdict=addprojectdetails.objects.all()
    return render(request,"showproject.html",{"userdict":userdict})

def viewsite(request):
    userdict=addsitedetails.objects.all()
    return render(request,"showsite.html",{"userdict":userdict})



def logcheck(request):
    if request.method=="POST":
        username=request.POST.get('t1')
        request.session['username'] = username
        password = request.POST.get('t2')
        count=userlogin.objects.filter(username=username).count()
        if count>=1:
            udata=userlogin.objects.get(username=username)
            upass=udata.password
            utype=udata.utype
            if upass==password:
                if utype=='owner':
                    return render(request,'owner_home.html',{'msg':'login success'})
                if utype=='customer':
                    return render(request,'customer_home.html')
                else:
                   return render(request,'login.html',{'msg':'invalid password'})
        else:
            return render(request, 'login.html', {'msg': 'invalid username'})

    return render(request,'login.html')


def sendmail(request):
    if request.method == "POST":
        to = request.POST.get('t1','')
        message = request.POST.get('t2', '')
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(' jk3413157@gmail.com', ' hioo oupk lswi wcnt')
        mail.sendmail(' jk3413157@gmail.com',to,message)
        mail.close()
        return render(request, 'maildemo.html')
    return render(request, 'maildemo.html')

def changepassword(request):
    uname=request.session['username']
    if request.method == 'POST':
        currentpass = request.POST.get('t1', '')
        newpass = request.POST.get('t2', '')
        confirmpass = request.POST.get('t3', '')

        ucheck = userlogin.objects.filter(username=uname).values()
        for a in ucheck:
            u = a['username']
            p = a['password']
            if u == uname and currentpass == p:
                if newpass == confirmpass:
                    userlogin.objects.filter(username=uname).update(password=newpass)
                    base_url=reverse('logcheck')
                    msg='password has been changed successfully'
                    return redirect(base_url,msg=msg)
                else:
                    return render(request, 'changepass.html',{'msg': 'both the usename and password are incorrect'})
            else:
                return render(request, 'changepass.html',{'msg': 'invalid username'})
    return render(request, 'changepass.html')