from django.db import models
from django.utils import timezone

#model imports
from django.contrib.auth.models import User as UserDjango
from wingmap.models import WingmanLocation




#this is a complimentry model for the User.
# we utilse django's inbuilt 'User' model.
# this model will have a one to one relationship with each users
# providing added flexibility
# class Wingmate(models.Model):
# 	user = models.OneToOneField(UserDjan);
# 	test_field = models.CharField(max_length=30, default=""); #this should have a refrence to the location DB
#
# 	def __str__(self):
# 		return self.user.username


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

	def __str__(self):
		return self.title


# User details
#class User1(models.Model):
#	user_name = models.CharField(max_length=100)
#	bio = models.TextField(max_length=500, blank=True)	imagePath = models.CharField(max_length=200)

#	def __str__(self):
#		return self.user_name + self.bio + self.imagePath


#this is a complimentry model for the User.
	# we utilse django's inbuilt 'User' model.
	# this model will have a one to one relationship with each users
	# providing added flexibility
class WingmanUser(models.Model):
	user = models.OneToOneField(UserDjango);
	bio = models.TextField(max_length=500, blank=True)
	imagePath = models.CharField(max_length=200,default='myapp/images/profileImages/Barney.jpg')
	averageRating = models.IntegerField(default=0)
	isPremium = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username

	def username(self):
		return self.user.username

class WingmanReview(models.Model):
	# review_id = models.AutoField(primary_key=True)
	reviewee = models.ForeignKey(WingmanUser, related_name='%(class)s_reviewee');
	reviewer = models.ForeignKey(WingmanUser, related_name='%(class)s_reviewer');
	rating = models.IntegerField()

	def __str__(self):
		return self.reviewee.user.username + ' reviwed by ' + self.reviewer.user.username

	class Meta:
		unique_together = ('reviewee', 'reviewer')
