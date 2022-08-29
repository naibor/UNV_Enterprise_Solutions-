from django.urls import path
from .views import ProjectDetailView, ProjectUpdateView, ProjectDeleteView,index, ProjectViewAll, CountryProjectViewAll, ProjectStatusViewAll
app_name ="app"

urlpatterns = [
    # create a project
    # view all projects 
    path('', index, name='index'),
    # view one project
    path('<pk>/', ProjectDetailView.as_view(), name='read'),
    # delete a project
    path('<pk>/delete', ProjectDeleteView.as_view(), name='delete'),
    # update a project
    path('<pk>/edit', ProjectUpdateView.as_view(), name='update'),

    # api urls
    path('api/projects/all', ProjectViewAll.as_view(), name='api-projects-all' ),
    path('api/projects/country/<str:country>', CountryProjectViewAll.as_view(), name='api-projects-country-all' ),
    path('api/projects/status/<str:status> ', ProjectStatusViewAll.as_view(), name='api-projects-status-all' )
 
]