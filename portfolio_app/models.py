from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200, default="Evan's Portfolio")
    description = models.TextField(default='')
    image = models.ImageField(upload_to='project_images/', default='profile_pics.jpg')
    # Add other fields like tags, links, etc.
def get_absolute_url(self):
    return reverse('project_detail', args=[str(self.id)])


    def __str__(self):
        return self.title