from django.contrib import admin
from django.urls import path , include
# from django.conf import settings
# from django.conf.urls.static  import static      
#from .import views,Hod_views,Staff_views,Student_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),
]