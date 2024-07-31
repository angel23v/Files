from django.db import models
import os

def upload_to(instance, filename):
    if instance.folder:
        folder_path = instance.folder.name
        return os.path.join('uploads', folder_path, filename)
    return os.path.join('uploads', instance.owner, filename)

class Folder(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subfolders')

    def __str__(self):
        return self.name

class File(models.Model):
    file_c = models.FileField(upload_to=upload_to)
    owner = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.file_c.name



