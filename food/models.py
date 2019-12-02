from django.db import models


class Table(models.Model):
    name = models.CharField(max_length=100)


class Role(models.Model):
    name = models.CharField(max_length=100)


class Department(models.Model):
    name = models.CharField(max_length=100)


class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    roleid = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='User')
    dateofadd = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)


class Category(models.Model):
    name = models.CharField(max_length=100)
    departmentid = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='Department')


class Status(models.Model):
    name = models.CharField(max_length=100)


class Service(models.Model):
    percentage = models.IntegerField(default=0)


class Meal(models.Model):
    name = models.CharField(max_length=100)
    categoryid = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Category')
    price = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
