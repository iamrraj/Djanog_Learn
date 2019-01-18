from django.db import models

# For All Profile SignUp
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import datetime

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)
    image = models.ImageField(blank = True, null = True )

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Categoty(models.Model):
    Id = models.AutoField(primary_key=True)
    name  = models.CharField(max_length=200)
    pub_date = models.DateTimeField( 'Date published' )

    def __str__( self ):
        return self.name

    def __unicode__(self):
        return self.Id

    def was_published_recently( self ):
        now = timezone.now()
        return now - datetime.timedelta( days = 1 ) <= self.pub_date <= now

class Product(models.Model):
    categoty = models.ForeignKey(Categoty, on_delete=models.CASCADE)
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    image = models.ImageField(blank = True, null = True)
    acprice = models.IntegerField()
    discount = models.CharField(max_length = 20)
    disprice = models.IntegerField()
    description = models.TextField()
    offer = models.CharField(max_length = 400)
    specification = models.TextField()
    seller = models.CharField(max_length = 100)
    pub_date = models.DateTimeField( 'Date published' )
    available = models.BooleanField(default=True)
    stock = models.IntegerField(default=True)

    def __str__( self ):
        return self.name

    def __unicode__(self):
        return self.Id

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

    def was_published_recently( self ):
        now = timezone.now()
        return now - datetime.timedelta( days = 1 ) <= self.pub_date <= now



class Slide(models.Model):
    Id = models.AutoField(primary_key=True)
    image = models.ImageField(blank = True, null = True)
    pub_date = models.DateTimeField( 'Date published' )

    def __str__( self ):
        return self.image

    def __unicode__(self):
        return self.Id

    def was_published_recently( self ):
        now = timezone.now()
        return now - datetime.timedelta( days = 1 ) <= self.pub_date <= now


