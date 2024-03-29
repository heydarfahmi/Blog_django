from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from django.utils import timezone


# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(is_published=True)


class Post(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=50, null=False, default="No subject, this is post number {} ".format(0))
    slug = models.SlugField(max_length=300, unique_for_date='created')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=False)
    published = PublishedManager()
    tags = TaggableManager()

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_view', args=[self.created.year,
                                                 self.created.strftime('%m'),
                                                 self.created.strftime('%d'),
                                                 self.slug])
        #
        # def re_post(self, User):
        #     self.id = None
        #     self.author=User
        #     self.title = "Repost {} from {}".format(self.title, self.author)
        #     self.save()


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'commented by {}'.format(self.name)
