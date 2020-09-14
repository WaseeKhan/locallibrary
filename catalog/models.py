from django.db import models

# Create your models here.
from django.urls import reverse


class MyModelName(models.Model):
        my_field_name = models.CharField(max_length=20, help_text='Enter Field documentation')

        class Meta:
            ordering = ['-my_field_name']

        def get_absolute_url(self):
            return reverse('model-detail-view', args = [str(self.id)])

        def __str__(self):
            return self.my_field_name
