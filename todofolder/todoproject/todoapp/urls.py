from django.urls import path, include

from todoapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/',views.TaskListView.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.TaskDetail.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.TaskUpdate.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.TaskDelete.as_view(),name='cbvdelete'),
]
