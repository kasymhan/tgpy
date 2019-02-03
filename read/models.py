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
    abiturient = models.OneToOneField('BlogAbiturient', on_delete=models.DO_NOTHING)
    special = models.ForeignKey('BlogSpecial', on_delete=models.DO_NOTHING)



    def __str__(self):
        return self.name


class BlogArea(models.Model):
    name = models.TextField()
    out= models.IntegerField()


    def __str__(self):
        return self.name


class BlogCity(models.Model):
    name = models.TextField()
    out= models.IntegerField()


    def __str__(self):
        return self.name


class BlogCountr(models.Model):
    name = models.TextField()
    out= models.IntegerField()


    def __str__(self):
        return self.name


class BlogFacully(models.Model):
    name = models.TextField()
    out = models.IntegerField()


    def __str__(self):
        return self.name

class BlogRegion(models.Model):
    name = models.TextField()
    out = models.IntegerField()

    def __str__(self):
        return self.name


class BlogSpecial(models.Model):
    name = models.TextField()
    fac = models.ForeignKey('BlogFacully', on_delete=models.DO_NOTHING)
    out = models.IntegerField()


    def __str__(self):
        return self.name
