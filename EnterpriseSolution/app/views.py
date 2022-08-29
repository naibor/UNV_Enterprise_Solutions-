from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Project
#  index page view all projects(get)
def index(request):
    project_list = Project.objects.all()
    # template = loader.get_template('app/index.html')
    context = {'project_list': project_list}
    return render(request, 'app/index.html', context)

# view one project
def read(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'app/detail.html', {'project': project})
    

# create a project (post)
# def create(request):
#     return HttpResponse("CREATE A PROJECTS GO HERE!!!")
#     pass
# # update a project
# def update(request, project_id):
#     return HttpResponse(" UPDATE A PROJECTS GO HERE!!!")
#     pass
# # delete a project
# def delete(request, project_id):
#     return HttpResponse("DELETE A PROJECTS GO HERE!!!")
#     pass