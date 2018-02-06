from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('auth.User')   #Connecting each user with an authrised user
    title = models.CharField(max_length=264)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    """
    The function publish() is to grab the time at the time
    when user wants to publish the blog.
    """
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    """
    The function approve_comments helps in a way that it
    will only publish comments that have been approved
    """
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    """
    The function get_absolute_url(self) is used to send the user to 
    post details page after he has hit the publish button
    """
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)   #anyone who is posting the comment
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    """
    The function get_absolute_url(self) is used to send user to the
    post_list page after user is done commenting
    """
    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text
