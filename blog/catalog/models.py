from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
# Create your models here.



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)



class CustomUser(AbstractUser):
    email = models.EmailField("email address", unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return self.email


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE, null=False, related_name='user_posts')
    context = models.CharField(max_length=20000)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])


class Comment(models.Model):
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE, null=False, related_name='user_comments')
    context = models.CharField(max_length=2000)
    date = models.DateField(default=timezone.now)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=False)
    def __str__(self):
        return self.context

    def get_absolute_url(self):
        return reverse('comment-detail', args=[str(self.id)])




class LikePost(models.Model):
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE, null=False, related_name='user_post_likes')
    date = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} liked {self.post}'



class LikeComment(models.Model):
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE, null=False, related_name='user_comment_likes')
    date = models.DateTimeField(default=timezone.now)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} liked {self.comment}'
