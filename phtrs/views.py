from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime,timedelta,date
from django.conf import settings

# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'hospital/index.html')


#for showing signup/login button for admin(by sumit)
def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'hospital/adminclick.html')


#for showing signup/login button for worker(by sumit)
def workerclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'hospital/workerclick.html')


#for showing signup/login button for citizen(by sumit)
def citizenclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'hospital/citizenclick.html')




def admin_signup_view(request):
    form=forms.AdminSigupForm()
    if request.method=='POST':
        form=forms.AdminSigupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)
            return HttpResponseRedirect('adminlogin')
    return render(request,'hospital/adminsignup.html',{'form':form})




def worker_signup_view(request):
    userForm=forms.WorkerUserForm()
    workerForm=forms.WorkerForm()
    mydict={'userForm':userForm,'workerForm':workerForm}
    if request.method=='POST':
        userForm=forms.WorkerUserForm(request.POST)
        workerForm=forms.WorkerForm(request.POST,request.FILES)
        if userForm.is_valid() and workerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            worker=workerForm.save(commit=False)
            worker.user=user
            worker.status=True
            worker=worker.save()
            my_worker_group = Group.objects.get_or_create(name='worker')
            my_worker_group[0].user_set.add(user)
        return HttpResponseRedirect('workerlogin')
    return render(request,'hospital/workersignup.html',context=mydict)


def citizen_signup_view(request):
    userForm=forms.CitizenUserForm()
    citizenForm=forms.CitizenForm()
    mydict={'userForm':userForm,'citizenForm':citizenForm}
    if request.method=='POST':
        userForm=forms.CitizenUserForm(request.POST)
        citizenForm=forms.CitizenForm(request.POST,request.FILES)
        if userForm.is_valid() and citizenForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            citizen=citizenForm.save(commit=False)
            citizen.user=user
            #citizen.assignedworkerId=request.POST.get('assignedworkerId')
            citizen.status=True
            citizen=citizen.save()
            my_citizen_group = Group.objects.get_or_create(name='citizen')
            my_citizen_group[0].user_set.add(user)
        return HttpResponseRedirect('citizenlogin')
    return render(request,'hospital/citizensignup.html',context=mydict)



#-----------for checking user is worker , citizen or admin(by sumit)
def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()
def is_worker(user):
    return user.groups.filter(name='worker').exists()
def is_citizen(user):
    return user.groups.filter(name='citizen').exists()


#---------AFTER ENTERING CREDENTIALS WE CHECK WHETHER USERNAME AND PASSWORD IS OF ADMIN,worker OR citizen
def afterlogin_view(request):
    if is_admin(request.user):
        return redirect('admin-dashboard')
    elif is_worker(request.user):
        accountapproval=models.Worker.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('worker-dashboard')

    elif is_citizen(request.user):
        accountapproval=models.Citizen.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('citizen-dashboard')









#---------------------------------------------------------------------------------
#------------------------ ADMIN RELATED VIEWS START ------------------------------
#---------------------------------------------------------------------------------
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_dashboard_view(request):
    #for both table in admin dashboard

    return render(request,'hospital/admin_dashboard.html',)


















#---------------------------------------------------------------------------------
#------------------------ ADMIN RELATED VIEWS END ------------------------------
#---------------------------------------------------------------------------------




#---------------------------------------------------------------------------------
#------------------------ worker RELATED VIEWS START ------------------------------
#---------------------------------------------------------------------------------
@login_required(login_url='workerlogin')
@user_passes_test(is_worker)
def worker_dashboard_view(request):
    #for three cards

    return render(request,'hospital/worker_dashboard.html')




#---------------------------------------------------------------------------------
#------------------------ worker RELATED VIEWS END ------------------------------
#---------------------------------------------------------------------------------



#---------------------------------------------------------------------------------
#------------------------ citizen RELATED VIEWS START ------------------------------
#---------------------------------------------------------------------------------
@login_required(login_url='citizenlogin')
@user_passes_test(is_citizen)
def citizen_dashboard_view(request):
    holes = models.Hole.objects.all()
    return render(request, 'hospital/citizen_dashboard.html', {'holse': holes})


@login_required(login_url='citizenlogin')
@user_passes_test(is_citizen)
def citizen_submit_hole_view(request):
    submit_form=forms.CitizenSubmitHoleForm()
    mydict={'submit_form':submit_form}
    if request.method=='POST':
        submit_form=forms.CitizenSubmitHoleForm(request.POST,request.FILES)
        if submit_form.is_valid():
            submit_form=submit_form.save(commit=False)
            hole=submit_form
            hole.priority=10-hole.size
            hole.save()
            # my_citizen_group = Group.objects.get_or_create(name='citizen')
            # my_citizen_group[0].user_set.add(user)
        return HttpResponseRedirect('citizen-dashboard')
    return render(request,'hospital/citizen_dashboard_cards.html',context=mydict)




#------------------------ citizen RELATED VIEWS END ------------------------------
#---------------------------------------------------------------------------------















#Developed By : sumit kumar
#facebook : fb.com/sumit.luv
#Youtube :youtube.com/lazycoders
