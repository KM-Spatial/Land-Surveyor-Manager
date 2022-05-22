from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Project, Task


# Get current user
def who_is_logged_in(request):
    current_user = request.user
    return current_user


class ProjectCreateForm(forms.ModelForm):
    name = forms.CharField(label='Project Name', widget=forms.TextInput(attrs={
        'class': 'form-control mb-3',
        'aria-describedby': 'placeHelp'
    }))
    client_name = forms.CharField(label='Client Name', widget=forms.TextInput(attrs={
        'class': 'form-control mb-3',
        'aria-describedby': 'placeHelp'
    }))

    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date', 'status', 'client_name'] # TODO: -> add team
        # members when organizational access implemented

        widgets = {
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'type': 'textarea'
                }
            ),
            'start_date': forms.DateInput(
                attrs={
                    'class': 'form-control mb-3',
                    'placeholder': 'select date',
                    'type': 'date',
                }
            ),
            'end_date': forms.DateInput(
                attrs={
                    'class': 'form-control mb-3',
                    'placeholder': 'select date',
                    'type': 'date',
                }
            ),
            'status': forms.Select(
                attrs={
                    'class': 'form-control mb-3',
                }
            ),
            # 'team_members': forms.SelectMultiple(
            #     attrs={
            #         'class': 'form-control',
            #     }
            # )
        }


class TaskCreationForm(forms.ModelForm):
    task_name = forms.CharField(label='Task-Name', widget=forms.TextInput(attrs={
        'class': 'form-control mb-3',
        'aria-describedby': 'placeHelp'
    }))

    class Meta:
        model = Task
        fields = ['project', 'task_name', 'task_description', 'status', 'deadline', 'set_reminder']  # TODO: -> add team
        # members when organizational access implemented

        widgets = {
            'project': forms.Select(
                attrs={
                    'class': 'form-control mb-3',
                }
            ),
            'task_description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'type': 'textarea'
                }
            ),
            # 'assigned_to': forms.SelectMultiple(
            #     attrs={
            #         'class': 'form-control',
            #     }
            # ),
            'status': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'deadline': forms.DateInput(
                attrs={
                    'class': 'form-control mb-3',
                    'placeholder': 'select date',
                    'type': 'date',
                }
            ),
            'set_reminder': forms.DateInput(
                attrs={
                    'class': 'form-control mb-3',
                    'placeholder': 'select date',
                    'type': 'date',
                }
            ),
        }

    def __init__(self, user, *args, **kwargs):
        # Only show the user specific projects
        super(TaskCreationForm, self).__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.filter(created_by=user)
