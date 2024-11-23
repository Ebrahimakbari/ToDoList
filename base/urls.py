from django.urls import path
from . import views


urlpatterns =[
    path('login/',views.LoginClass.as_view(),name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('delete/',views.delete_view,name='delete'),
    path('register/',views.RegisterClass.as_view(),name='register'),
    path('',views.TaskList.as_view(),name='tasks'),
    path('create-task/',views.TaskCreate.as_view(),name='create_task'),
    path('update-task/<int:pk>',views.TaskUpdate.as_view(),name='update_task'),
    path('delete-task/<int:pk>',views.TaskDelete.as_view(),name='delete_task'),
]