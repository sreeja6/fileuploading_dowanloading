from django.db import models

class Filedetails(models.Model):
    No = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=20)
    file = models.FileField(upload_to='my_files/')