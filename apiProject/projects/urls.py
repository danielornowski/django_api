from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('projects/', views.getProjects, name='projects'),
    path('project/create/', views.createProject, name='create-project'),
    path('project/<str:pk>/update/', views.updateProject, name='update-project'),
    path('project/<str:pk>/delete/', views.deleteProject, name='delete-project'),
    path('project/<str:pk>/', views.getProject, name='project'),
    path('project/<str:pk>/comment', views.createComment, name='createComment'),
    path('project/<str:pk>/comments', views.getComments, name='getComments')
]
