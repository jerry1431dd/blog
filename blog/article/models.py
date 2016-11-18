from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=128, unique=True)
    content = models.TextField()
    pubDateTime = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.title
    

    
    
class Comment(models.Model):
    article = models.ForeignKey(Article)
    content = models.CharField(max_length=128)
    pubDateTime = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.article.title + '-' + str(self.id)
    
class Book(models.Model):
    title = models.CharField(max_length=128,unique= True)
    author = models.CharField(max_length=128)
    publisher = models.CharField(max_length=128)
    pubDate = models.DateTimeField(max_length=128)
    version = models.CharField(max_length=128)
    price = models.IntegerField()
    
    def __str__(self):
        return self.title
    
    