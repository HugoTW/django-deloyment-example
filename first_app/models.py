from django.db import models


# SuperUserInformation
# User: hugoweng
# Email: hugo@hugo.com
# Password: test



class Topic(models.Model):

    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name


class Webpage(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class UserInfo(models.Model):

    email = models.EmailField(max_length=128 , unique=True)
    firstName = models.CharField(max_length=128)
    lastName = models.CharField(max_length=128)

    def __str__(self):
        return str(self.email)
