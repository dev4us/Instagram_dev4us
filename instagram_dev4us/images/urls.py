#from django.conf.urls import url
from django.urls import path
from . import views

"""urlpatterns = [
    url(
        regex= r'^all/$',
        view= views.ListAllImages.as_view(),
        name= 'all_images',
    )
]"""
app_name = "images"
urlpatterns = [
    path('all/', views.ListAllImages.as_view(), name='all_images'),
    path('comments/', views.ListAllComments.as_view(), name='all_images'),
    path('likes/', views.ListAllLikes.as_view(), name='all_images'),
]
