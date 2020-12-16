from django.db import models


#-------------------------------------------- start work ----------------------------#

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    contact = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Image(models.Model):
    img_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'media/')

    def __str__(self):
        return self.user.name