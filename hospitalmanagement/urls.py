"""

Developed By : sumit kumar
facebook : fb.com/sumit.luv
Youtube :youtube.com/lazycoders


"""




from django.contrib import admin
from django.urls import path
from phtrs import views
from django.contrib.auth.views import LoginView,LogoutView


#-------------FOR ADMIN RELATED URLS
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),

    path('adminclick', views.adminclick_view),
    path('workerclick', views.workerclick_view),
    path('citizenclick', views.citizenclick_view),

    path('adminsignup', views.admin_signup_view),
    path('workersignup', views.worker_signup_view,name='workersignup'),
    path('citizensignup', views.citizen_signup_view),
    
    path('adminlogin', LoginView.as_view(template_name='hospital/adminlogin.html')),
    path('workerlogin', LoginView.as_view(template_name='hospital/workerlogin.html')),
    path('citizenlogin', LoginView.as_view(template_name='hospital/citizenlogin.html')),

    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='hospital/index.html'),name='logout'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),

]


#---------FOR worker RELATED URLS-------------------------------------
urlpatterns +=[
    path('worker-dashboard', views.worker_dashboard_view,name='worker-dashboard'),

]


#---------FOR citizen RELATED URLS-------------------------------------
urlpatterns +=[

    path('citizen-dashboard', views.citizen_dashboard_view,name='citizen-dashboard'),
    path('citizen-submit-hole', views.citizen_submit_hole_view, name='citizen-submit-hole')

]

#Developed By : sumit kumar
#facebook : fb.com/sumit.luv
#Youtube :youtube.com/lazycoders
