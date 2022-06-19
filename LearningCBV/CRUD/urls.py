from django.urls import path
from .views import *
urlpatterns = [
    path('',HomePage.as_view(), name="home"),
    path('template-view',TemplateRender.as_view(), name="template_view"),
    path('detail-view/<int:pk>/', BlogDetailView.as_view(), name='detail_view'),
    path('modify-blog/',ModifyBlog.as_view(),name='modify_blog'),
    path('add-blog',AddBlog.as_view(),name='add_blog'),
    path('update-blog/<int:pk>',UpdateBlog.as_view(),name='update_blog'),
    path('delete-blog/<int:pk>',DeleteBlog.as_view(),name='delete_blog'),
   ]