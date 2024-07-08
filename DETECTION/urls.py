from django.urls import path 
from . import views



urlpatterns = [
     path('',views.index,name='index'),


     path('index',views.index,name='index'),
      path('upload', views.upload, name='upload'),

        #  path('', views.index, name='index'),
    # path('predict/', views.upload, name='predict'),
    #  path('signup',views.signup,name='signup'),


    #  path('login',views.login, name='login'),


    #  path("home",views.home,name='home'),


    #  path('logout',views.logout ,name='logout'),


    #  path('search',views.search ,name='search'),
     

     path('upload_imz',views.upload_imz ,name='upload_imz'),
     

    #  path('Account',views.Account ,name='Account'),


    #  path('recomend',views.recomend,name='recomend')
    
   
  
   
    
]