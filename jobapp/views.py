from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic

from .forms import *
from .models import *


# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        a = loginform(request.POST)
        if a.is_valid():
            em = a.cleaned_data['email']
            ps = a.cleaned_data['password']
            b = regismodel.objects.all()
            for i in b:
                cmp = i.cmp_name
                id = i.id
                if i.email == em and i.password == ps:
                    return render(request, 'profile.html', {'cmp': cmp, 'id': id})
            else:
                return HttpResponse('login faild')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        a = regisform(request.POST)
        if a.is_valid():
            cmp = a.cleaned_data['cmp_name']
            add = a.cleaned_data['address']
            em = a.cleaned_data['email']
            ph = a.cleaned_data['phone']
            ps = a.cleaned_data['password']
            cp = a.cleaned_data['cpassword']
            if ps == cp:
                b = regismodel(cmp_name=cmp, address=add, email=em, phone=ph, password=ps)
                b.save()
                return redirect(login)
            else:
                return HttpResponse('incorrect password...')
        else:
            return HttpResponse('registraction faild..')
    else:
        return render(request, 'register.html')


# def navbar(request):
#     return render(request,'navbar.html')
#
# def footer(request):
#     return render(request,'footer.html')

def profile(request):
    return render(request, 'profile.html')


def jobview(request, id):
    a = regismodel.objects.get(id=id)
    cm = a.cmp_name
    em = a.email
    if request.method == 'POST':
        a = jobform(request.POST)
        if a.is_valid():
            cmp_name = a.cleaned_data['cmp_name']
            email = a.cleaned_data['cmp_email']
            title = a.cleaned_data['title']
            type = a.cleaned_data['jobtype']
            wrktype = a.cleaned_data['wrktype']
            required = a.cleaned_data['exp_required']
            qualification = a.cleaned_data['qualification']
            b = jobmodels(cmp_name=cmp_name, cmp_email=email, title=title, jobtype=type, wrktype=wrktype,
                          exp_required=required, qualification=qualification)
            b.save()
            return HttpResponse('upload success')

        else:
            return HttpResponse('registraction faild..')
    else:
        return render(request, 'addjob.html', {'cm': cm, 'em': em})


def jobdisplay(request):
    a = jobmodels.objects.all()
    return render(request, 'jobdisplay.html', {'a': a})


def delete(request, id):
    a = jobmodels.objects.get(id=id)
    a.delete()
    return redirect(jobdisplay)


def edit(request, id):
    a = jobmodels.objects.get(id=id)
    if request.method == 'POST':
        a.cmp_name = request.POST.get('cmp_name')
        a.cmp_email = request.POST.get('cmp_email')
        a.title = request.POST.get('title')
        a.jobtype = request.POST.get('jobtype')
        a.wrktype = request.POST.get('wrktype')
        a.exp_required = request.POST.get('exp_required')
        a.qualification = request.POST.get('qualification')
        a.save()
        return redirect(jobdisplay)
    else:
        return render(request, 'edit.html', {'a': a})

# Function based programe

class usereg(generic.CreateView):
    form_class = user
    template_name = 'user.html'
    success_url = reverse_lazy('userlog')


class userlog(generic.View):
    form_class = log
    template_name = 'userlogin.html'

    def get(self, request):
        a = log
        return render(request, 'userlogin.html')

    def post(self, request):
        if request.method == 'POST':
            a = log(request.POST)
            if a.is_valid():
                em = a.cleaned_data['email']
                ps = a.cleaned_data['password']
                b = User.objects.all()
                for i in b:
                    if i.email == em and i.password == ps:
                        return HttpResponse('login success')
                else:
                    return HttpResponse('login failed')

# function based programm

#
# def uregister(request):
#     if request.method=='POST':
#            un=request.POST.get("username")
#            fn=request.POST.get("first_name")
#            ln=request.POST.get("last_name")
#            em=request.POST.get("email")
#            ps=request.POST.get("password")
#            cps=request.POST.get("cpassword")
#            if ps==cps:
#                 b = User(username=un, first_name=fn, last_name=ln, email=em, password=ps)
#                 b.save()
#                 return redirect(ulogin)
#            else:
#                return HttpResponse("Registration Failed!")
#     else:
#         return render(request,'user.html')
#
#
# def ulogin(request):
#     if request.method == 'POST':
#         a = ulogform(request.POST)
#         if a.is_valid():
#             em = a.cleaned_data['email']
#             ps = a.cleaned_data['password']
#             b = User.objects.all()
#             for i in b:
#                 # cmp = i.companyname
#                 # id = i.id
#                 if i.email == em and i.password == ps:
#                     return HttpResponse("Login Success")
#                     # return render(request, 'profile.html',{'cmp':cmp, 'id':id})
#             else:
#                 return HttpResponse("Login failed")
#     else:
#         return render(request, 'userlogin.html')