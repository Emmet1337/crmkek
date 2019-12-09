from rest_framework import serializers
from food.models import Table, Role, Department, User, Category, Status, Service, Meal, Orders, OrderContent, Check


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


class OrderContentSerializer(serializers.HyperlinkedModelSerializer):
    meal_id = serializers.PrimaryKeyRelatedField(queryset=Meal.objects.all(), source='meal.id',)
    name = serializers.CharField(source='meal.name', read_only=True)
    price = serializers.CharField(source='meal.price', read_only=True)
    total = serializers.FloatField(source='get_cost', read_only=True)

    class Meta:
        model = OrderContent
        fields = ('meal_id', 'name', 'price', 'count', 'total')


class OrderSerializer(serializers.ModelSerializer):
    waiter_id = serializers.IntegerField(
        source='waiter.id',
        read_only=True
    )
    isitopen = serializers.BooleanField(
        read_only=True,
        default=True
    )
    table_id = serializers.PrimaryKeyRelatedField(
        queryset=Table.objects.all(),
        source='table.id',
    )
    table_name = serializers.CharField(
        source='table.name',
        read_only=True
    )
    meals = OrderContentSerializer(many=True, required=False)

    class Meta:
        model = Orders
        fields = ('id', 'waiter_id', 'date', 'isitopen', 'table_id', 'table_name', 'meals')

    def create(self, validated_data):
        order = Orders.objects.create(
            waiter=validated_data['waiter'],
            table=validated_data['table']['id'],
        )
        if 'meals' in validated_data:
            for meal in validated_data['meals']:
                OrderContent.objects.create(
                    order=order,
                    meal=meal['meal']['id'],
                    count=meal['count']
                ).save()
        order.save()

        return order


class MealsToOrderSerializer(serializers.HyperlinkedModelSerializer):
    order_id = serializers.IntegerField(source='id')
    meals = OrderContentSerializer(many=True)

    class Meta:
        model = Orders
        fields = ('order_id', 'meals')


class CheckSerializer(serializers.ModelSerializer):
    order_id = serializers.PrimaryKeyRelatedField(queryset=Orders.objects.all(), source='order_id')
    servicefee = serializers.FloatField(source='percentage', read_only=True)
    total_sum = serializers.FloatField(source='total_sum', read_only=True)

    class Meta:
        model = Check
        fields = ('id', 'order_id', 'date', 'servicefee', 'total_sum', 'order')