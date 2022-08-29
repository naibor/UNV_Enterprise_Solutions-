from django.urls import path
from . import views

urlpatterns = [
    # view all projects 
    path('', views.index, name='index'),
    # view one project
    path('<int:project_id>/', views.read, name='read'),
    # create a project
    # delete a project
    # path('<int:project_id>/', views.delete, name='delete'),
    # update a project
    # path('<int:project_id>/', views.update, name='update')
]