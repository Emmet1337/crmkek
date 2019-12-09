from rest_framework import serializers
from food.models import Table, Role, Department, User, Category, Status, Service, Meal


class TableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Table
        fields = ('name',)


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = ('name',)


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ('name',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    roleid = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all())

    class Meta:
        model = User
        fields = ('name', 'surname', 'login', 'password', 'email', 'roleid', 'dateofadd', 'phone')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    departmentid = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())

    class Meta:
        model = Category
        fields = ('name', 'departmentid')


class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = ('name',)


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ('percentage',)


class MealSerializer(serializers.HyperlinkedModelSerializer):
    categoryid = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Meal
        fields = ('name', 'categoryid', 'price', 'description')

