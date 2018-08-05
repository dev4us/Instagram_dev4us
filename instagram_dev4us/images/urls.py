#from django.conf.urls import url
from django.urls import path
from . import views

app_name = "images"
urlpatterns = [
    path('', views.Feed.as_view(), name='Feed'),
    path('<int:image_id>/like/', views.LikeImage.as_view(), name='like_image'),
    path('<int:image_id>/unlike/', views.UnLikeImage.as_view(), name='unlike_image'),
    path('<int:image_id>/comments/', views.CommentOnImage.as_view(), name='comment_image'),
    path('<int:image_id>/comments/<int:comment_id>/', views.ModerateComments.as_view(), name='moderate_comment'),
    path('comments/<int:comment_id>/', views.Comment.as_view(), name='comment'),
    path('search/', views.Search.as_view(), name='search'),
]
