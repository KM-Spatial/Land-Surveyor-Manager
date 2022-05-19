import random
import string

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse

status = (
    ('queued', 'Queued'),
    ('in_progress', 'In-Progress'),
    ('canceled', 'Cancelled'),
    ('complete', 'Complete'),
)


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    slug = models.SlugField(editable=False)
    status = models.CharField(max_length=20, choices=status, default='inline')
    client_name = models.CharField(max_length=100)
    team_members = models.ManyToManyField(User, related_name='team_members', null=True, blank=True)
    # Metadata
    add_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # generate random string
        length_of_string = 12
        value = "".join(
            random.choice(string.ascii_letters) for _ in range(length_of_string)
        )

        self.slug = slugify(value)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})


reminder_mode = (
    ('email', 'email'),
)


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=200)
    task_description = models.TextField()
    status = models.CharField(max_length=20, choices=status, default='queued')
    assigned_to = models.ManyToManyField(User, related_name='assigned_to', null=True, blank=True)
    deadline = models.DateTimeField()
    set_reminder = models.DateTimeField()
    reminder_mode = models.CharField(max_length=20, choices=reminder_mode, default='email')

    # Metadata
    add_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['project', 'task_name']

    def __str__(self):
        return self.task_name

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.project.slug})
