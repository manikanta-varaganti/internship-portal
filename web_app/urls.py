from django.urls import path
from . import views
urlpatterns= [
    path('userhome/',views.home,name='user-home'),
    path('',views.apphome,name='app-home'),
    path('homepage/',views.homepage,name='homepage'),
    path('application/', views.application, name='application'),
    path('applied/',views.createpost,name="applied"),
    path('export/',views.export_excel, name='export_excel')
    
    
]
