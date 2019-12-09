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
    roleid = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='user')
    dateofadd = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)


class Category(models.Model):
    name = models.CharField(max_length=100)
    departmentid = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department')


class Status(models.Model):
    name = models.CharField(max_length=100)


class Service(models.Model):
    percentage = models.IntegerField(default=0)


class Meal(models.Model):
    name = models.CharField(max_length=100)
    categoryid = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    price = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


class Orders(models.Model):
    waiterid = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='waiter')
    tableid = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='table')
    isitopen = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    mealid = models.ForeignKey(Meal, on_delete=models.CASCADE, null=True, related_name='meal')
    tablesname = models.CharField(max_length=100, )


class OrderContent(models.Model):
    order = models.ForeignKey(Orders, related_name='order', on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)


class Check(models.Model):
    order = models.ForeignKey(Orders, unique=True, on_delete=models.CASCADE)
    percentage = models.ForeignKey(Service, on_delete=None)
    date = models.DateTimeField(auto_now_add=True)
