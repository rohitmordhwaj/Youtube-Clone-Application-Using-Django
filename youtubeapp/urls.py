from . import views 
from django.conf.urls import url
from django.urls import path


app_name = "youtubeapp"

urlpatterns = [
    url(r'^newvedio/', views.NewVideo.as_view(), name='new_vedio'),
    url(r'^regester/', views.Regester.as_view(), name='regester'),
    url(r'^login/', views.Login.as_view(), name='login'),
   # url(r'^video/<int:id>', views.VedioView.as_view(), name='video'),
    path('video/<int:id>', views.VedioView.as_view(), name='video'),
    path('logout/', views.LogoutView.as_view()),
    path('comment', views.CommentView.as_view()),
]

