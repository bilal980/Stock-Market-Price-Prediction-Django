from django.db import models
from acounts.models import CustomUser
from django.utils.timezone import now


# post model for storing in database
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    content = models.TextField()
    time = models.DateTimeField(auto_now=True, blank=True)
    postImage = models.ImageField(upload_to='static/tmp/')
    slug=models.SlugField(max_length=30)
    def __str__(self):
        return self.title + " by "+self.author

# comments model for storing in database
class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField(max_length=400)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    time = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.sno)
