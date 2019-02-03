from django.db import models

# Create your models here.



class BlogAbiturient(models.Model):
    name = models.TextField()
    area = models.ForeignKey('BlogArea', on_delete=models.DO_NOTHING)
    city = models.ForeignKey('BlogCity', on_delete=models.DO_NOTHING)
    country = models.ForeignKey('BlogCountr', on_delete=models.DO_NOTHING)
    region = models.ForeignKey('BlogRegion', on_delete=models.DO_NOTHING)


class BlogApplication(models.Model):
    enlisted = models.BooleanField()
    abiturient = models.OneToOneField('BlogAbiturient', on_delete=models.DO_NOTHING, unique=True)
    special = models.ForeignKey('BlogSpecial', on_delete=models.DO_NOTHING)


class BlogArea(models.Model):
    name = models.TextField()


class BlogCity(models.Model):
    name = models.TextField()


class BlogCountr(models.Model):
    name = models.TextField()


class BlogFacully(models.Model):
    name = models.TextField()


class BlogRegion(models.Model):
    name = models.TextField()


class BlogSpecial(models.Model):
    name = models.TextField()
    fac = models.ForeignKey('BlogFacully', on_delete=models.DO_NOTHING)
