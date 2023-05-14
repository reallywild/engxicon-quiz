from django.db import models


class Dictionary(models.Model):
    sentence = models.CharField(max_length=300)

class ProgDictionary(models.Model):
    sentence = models.CharField(max_length=300)

class TVDictionary(models.Model):
    sentence = models.CharField(max_length=300)

class BookDictionary(models.Model):
    sentence = models.CharField(max_length=300)

# class UserMistakes(models.Model):
#     # need user
#     sentence = models.ForeignKey(Dictionary, max_length=100, on_delete=models.CASCADE)    
#     word = models.CharField(max_length=25)