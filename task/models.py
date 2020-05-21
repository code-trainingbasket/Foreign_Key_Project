from django.db import models

# Create your models here.
class Category(models.Model):
	typ = models.CharField(max_length=50)
	
	def __str__(self):
		return self.typ

class Payment(models.Model):
	price= models.IntegerField()

	def __str__(self):
		return str(self.price)


class Post(models.Model):
	name= models.CharField(max_length=50,primary_key=True)
	descr = models.TextField(max_length=100)
	category= models.ForeignKey(Category,on_delete=models.CASCADE)
	price = models.ForeignKey(Payment,on_delete=models.CASCADE)

	def __str__(self):
		return self.name