from django.db import models


class FAQ(models.Model):
    question = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = 'Frequently Asked Questions'


PRIORITY_LEVEL = (
    ('low', 'LOW'),
    ('medium', 'MEDIUM'),
    ('high', 'HIGH'),
)


class Notification(models.Model):
    posted_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    priority_level = models.CharField(max_length=10, choices=PRIORITY_LEVEL)
    message = models.TextField()

    def __str__(self):
        return self.title



