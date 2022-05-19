from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from .models import Project, Task
from .forms import ProjectCreateForm, TaskCreationForm


# Project Based Views

class CreateProject(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'project/new_project.html'
    form_class = ProjectCreateForm
    success_message = "Project %(name) has been created successfully"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    # def form_valid(self, form):
    #     # -> Send an Email
    #     pass


class ProjectDetail(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'project/project_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['task'] = Task.objects.all()
        return context


class ProjectUpdate(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Project
    template_name = 'project/new_project.html'
    form_class = ProjectCreateForm
    success_message = "Project information updated successfully"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    # Make sure person updating is the project owner
    def test_func(self):
        project = self.get_object()
        if self.request.user == project.created_by: # -> TODO: Allow if user is in Organization
            return True
        return False


class RemoveProject(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Project
    template_name = 'project/project_delete.html'
    success_url = '/dashboard/'  # TODO: Change this URL to the Projects List URls
    success_message = "The project has been deleted successfully"

    # Make sure person deleting is the project owner
    def test_func(self):
        project = self.get_object()
        if self.request.user == project.created_by:
            return True
        return False


class ProjectList(LoginRequiredMixin, ListView):
    model = Project
    context_object_name = 'project'
    template_name = 'project/project_list.html'

    # def get_context_object_name(self, *args, **kwargs):
    #     context = super().get_context_object_name(*args, **kwargs)
    #     context['task'] = Task.objects.all()
    #     return context


# Task Manager Views
class CreateTask(LoginRequiredMixin, CreateView):
    template_name = 'project/new _task.html'
    form_class = TaskCreationForm
    success_message = "New Task Created"

    def get_form_kwargs(self):
        kwargs = super(CreateTask, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return Project.objects.filter(created_by=user)


