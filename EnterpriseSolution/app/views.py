# django imports
from audioop import reverse
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

# rest framework
from rest_framework.generics import ListAPIView

# local imports
from .serializer import ProjectImplementationSerializer, ProjectSerializer
from .models import Project,ProjectImplementation

#  index page view all projects(get)
def index(request):
    if request.method == "POST":
        project_list = Project.objects.all()[:int(request.POST.get("show_records"))]
        context = {'project_list': project_list}
        return render(request, 'app/index.html', context)
    else:
        project_list = Project.objects.all()[:10]
        context = {'project_list': project_list}
        return render(request, 'app/index.html', context)

# create a project
class ProjectCreateView(CreateView):
    model = Project
    fields = '__all__'

# view a single project
class ProjectDetailView(DetailView):
    model = Project
    fields = '__all__'

# update a project
class ProjectUpdateView(UpdateView):
    model = Project
    fields = '__all__'
    
    def get_success_url(self) -> str:
        success_url = reverse_lazy('project:index')
        return success_url

# delete a project
class ProjectDeleteView(DeleteView):
    model=Project

    def get_success_url(self) -> str:
        success_url = reverse_lazy('project:index')
        return success_url

# API 
# get all projects
class ProjectViewAll(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = "pk"

# get projects based on a country
class CountryProjectViewAll(ListAPIView):
    queryset = ProjectImplementation.objects.all()
    serializer_class = ProjectImplementationSerializer

    def get_queryset(self):
        country = self.kwargs.get('country',None)
        if country:
            return ProjectImplementation.objects.filter(country_id__country=country).all()
        return ProjectImplementation.objects.all()

    

# get projects based on the status
class ProjectStatusViewAll(ListAPIView):
    quesyset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = "pk"
    

    def get_queryset(self):
        status = self.kwargs.get('status',None)
        if status:
            return Project.objects.filter(status=status).all()
        return Project.objects.all()

    