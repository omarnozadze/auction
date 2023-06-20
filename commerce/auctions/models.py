from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length = 64)

    def __str__(self):
        return self.name

class Bid(models.Model):
    bid = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True, related_name = "user_bid")

    def __str__(self):
        return f"Bid {self.bid}$ by {self.user}"

class Listing(models.Model):
    title = models.CharField('Title',max_length = 32)
    description = models.CharField('Description',max_length = 256)
    image_url = models.URLField('IMG',max_length = 1024)
    price = models.ForeignKey(Bid, on_delete = models.CASCADE)
    owner = models.ForeignKey(User,on_delete = models.CASCADE)
    category = models.ForeignKey(Category,null = True, blank = True, on_delete = models.CASCADE)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    
    commenter = models.ForeignKey(User, related_name = "commenter", null = True, blank = True, on_delete = models.CASCADE)
    

    def __str__(self):
        return self.commenter