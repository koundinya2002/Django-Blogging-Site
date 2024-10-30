from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="blog_posts")

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author) + ' | ' + str(self.author.id)

    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s | %s | %s" % (self.post, self.author, self.body)


class Reply(models.Model):
    comment = models.ForeignKey(Comment, related_name="responses", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s | %s | %s" % (self.comment, self.author, self.body)