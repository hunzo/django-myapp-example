from django.db import models
# Create your models here.


class EmailList(models.Model):
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.email


class EmailGroupList(models.Model):
    name = models.CharField(max_length=200)
    email_list = models.ManyToManyField(EmailList)

    def __str__(self):
        return self.name


class RecipientList(models.Model):
    name = models.CharField(max_length=20)
    content = models.TextField()
    email_list = models.ManyToManyField(EmailGroupList)

    def __str__(self):
        return self.name



    
    
