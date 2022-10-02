from django.urls import path
from . import views 


urlpatterns = [
    path('',views.query, name="query"),
    path('seek', views.seek, name="seek"),
    path('indeed', views.indeed, name="indeed"),
    path('trademe', views.trademe, name="trademe"),
    path('about', views.about, name="about")
    
]