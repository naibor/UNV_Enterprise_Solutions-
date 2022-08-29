# django imports
from audioop import reverse
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView

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

# view one project
# def read(request, project_id):
#     project = get_object_or_404(Project, pk=project_id)
#     context = {'project': project}
#     return render(request, 'app/project_detail.html', context)

class ProjectDetailView(DetailView):
    model = Project

# # update a project
class ProjectUpdateView(UpdateView):
    model = Project
    fields = '__all__'
    
    # def get_success_url(self) -> str:
    #     return reverse('app:')
    # success_url: "/"

# # delete a project

class ProjectDeleteView(DeleteView):
    model=Project

    def get_success_url(self) -> str:
        return reverse('app:index')


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
    

    def get_queryset(self):
        status = self.kwargs.get('status','')
        return Project.objects.filter(status=status).all()
    