from django.urls import path

from . import views

urlpatterns =[
    path ("",views.forums,name="forums"),
    path ("forums/<int:pk>",views.posts,name="forums_posts"),
    path ("posts/<int:pk>",views.post,name="forums_post"),
    path ("comments/<int:pk>",views.replies,name="forums_replies"),
]