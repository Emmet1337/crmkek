from food.serializers import *
from rest_framework import generics, filters


class TableListView(generics.ListAPIView):
    serializer_class = TableSerializer
    queryset = Table.objects.all()


class RoleListView(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class DepartmentListView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['departmentid__name', ]


class StatusListView(generics.ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class MealListView(generics.ListAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
