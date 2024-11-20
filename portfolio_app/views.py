from django.shortcuts import render, get_object_or_404
from .models import Project
from . import urls


def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio_app/home.html', {'projects': projects})



def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    # ... your code to handle the project detail view ...
    return render(request, 'portfolio_app/project_detail.html', {'project': project})

# In your Project model:
def get_absolute_url(self):
    return reverse('project_detail', args=[str(self.id)])  # This should work correctly..


import os  # Import the os module
from django.conf import settings
from bakery.views import BuildableListView
from .models import Project

class ProjectListView(BuildableListView):
    model = Project
    template_name = 'portfolio_app/project_list.html'

    def build_queryset(self):
        """
        This is an example of a build_queryset method.
        """
        # Convert PosixPath objects to strings
        build_dir = str(settings.BUILD_DIR)
        build_path = str(self.build_path)

        # Now use the string values in path.join()
        target_path = os.path.join(build_dir, build_path)

        # ... rest of your build_queryset method ...

from bakery.views import BuildableDetailView  # Make sure this is imported
from .models import Project

class ProjectDetailView(BuildableDetailView):  # This should be defined in your views.py
    model = Project
    template_name = 'portfolio_app/project_detail.html'