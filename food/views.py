from food.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ParseError, ValidationError
import datetime


class TableListView(APIView):
    serializer_class = TableSerializer
    queryset = Table.objects.all()

    def get(self, request, *args, **kwargs):
        tables = self.queryset.all()
        serializer = self.serializer_class(tables, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        table_id = request.data.get('id', None)

        if table_id is None:
            raise ParseError("Field is required!")

        try:
            table = self.queryset.get(id=table_id)
        except Table.DoesNotExist:
            raise Http404
        else:
            table.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RoleListView(APIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def get(self, request, *args, **kwargs):

        serializer = self.serializer_class(self.queryset.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        role_id = request.data.get('role_id', None)

        if role_id is None:
            raise ParseError("field is required")

        users_with_this_role = User.objects.filter(role_id=role_id)

        if users_with_this_role:
            raise ValidationError()

        try:
            role = self.queryset.get(id=role_id)
        except Role.DoesNotExist:
            raise Http404
        else:
            role.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class DepartmentListView(APIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get(self, request, *args, **kwargs):
        departments = self.queryset.all()
        serializer = self.serializer_class(departments, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        department_id = request.data.get('id', None)

        if department_id is None:
            raise ParseError("field is required!")

        try:
            department = self.queryset.get(id=department_id)
        except Department.DoesNotExist:
            raise Http404
        else:
            department.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)


class UserAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data

        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):

        user_id = request.data.get('user_id', None)

        try:
            user = self.queryset.get(id=user_id)
        except User.DoesNotExist:
            raise Http404
        else:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryListView(APIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, department_id=None, *args, **kwargs):
        if department_id:
            try:
                department = Department.objects.get(id=department_id)
            except Department.DoesNotExist:
                raise Http404
            else:
                meal_categories = self.queryset.filter(department=department).order_by('id')
                serializer = self.serializer_class(meal_categories, many=True)

                return Response(serializer.data)

        meal_categories = self.queryset.all()
        serializer = self.serializer_class(meal_categories, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        category_id = request.data.get('id', None)

        if category_id is None:
            raise ParseError("field is required!")

        try:
            meals_category = self.queryset.get(id=category_id)
        except Category.DoesNotExist:
            raise Http404
        else:
            meals_category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class StatusView(APIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def get(self, request, *args, **kwargs):
        statuses = self.queryset.all()
        serializer = self.serializer_class(statuses, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        status_id = request.data.get('id', None)

        if status_id is None:
            raise ParseError("field is required!")

        try:
            status_obj = self.queryset.get(id=status_id)
        except Status.DoesNotExist:
            raise Http404
        else:
            status_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class ServiceListView(APIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get(self, request, *args, **kwargs):
        percentage = self.queryset.all()

        serializer = self.serializer_class(percentage, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        percentage_id = request.data.get('id', None)

        if percentage_id is None:
            raise ParseError("field is required")

        try:
            percentage = self.queryset.get(id=percentage_id)
        except Service.DoesNotExist:
            raise Http404
        else:
            percentage.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class MealListView(APIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    def get(self, request, meals_category_id=None, *args, **kwargs):
        if meals_category_id:
            try:
                meals_category = Category.objects.get(id=meals_category_id)
            except Category.DoesNotExist:
                raise Http404
            else:
                meals = self.queryset.filter(category=meals_category)
                serializer = MealSerializer(meals, many=True)
                return Response(serializer.data)

        meals = self.queryset.all()
        serializer = self.serializer_class(meals, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        meal_id = request.data.get('id', None)

        if meal_id is None:
            raise ParseError("field is required!")

        try:
            meal = self.queryset.get(id=meal_id)
        except Meal.DoesNotExist:
            raise Http404
        else:
            meal.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class OrderView(APIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    def get(self, request, pk=None, *args, **kwargs):

        days = request.query_params.get('days', None)
        if days:
            orders = self.queryset.filter(
                date__gt=datetime.datetime.now() - datetime.timedelta(days=int(days))
            ).order_by('-date')
            serializer = self.serializer_class(orders, many=True)

            return Response(serializer.data)

        if pk:
            try:
                order = self.queryset.get(id=pk)
            except Orders.DoesNotExist:
                raise Http404
            else:
                serializer = self.serializer_class(order)
                return Response(serializer.data, status=status.HTTP_200_OK)

        orders = self.queryset.all()
        serializer = self.serializer_class(orders, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data.copy()

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(waiter=self.request.user)

    def delete(self, request, *args, **kwargs):
        order_id = request.data.get('id', None)

        if order_id is None:
            raise ParseError("field is required!")

        try:
            order = self.queryset.get(id=order_id)
        except Orders.DoesNotExist:
            raise Http404
        else:
            order.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class GetActiveOrderListView(APIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

    def get(self, request):
        orders = self.queryset.filter(isitopen=True)
        serializer = self.serializer_class(orders, many=True)

        return Response(serializer.data)


class MealsToOrderView(APIView):
    queryset = Orders.objects.all()
    serializer_class = MealsToOrderSerializer

    def get(self, request, *args, **kwargs):
        order_id = request.query_params.get('order_id', None)
        if order_id:
            try:
                order = self.queryset.get(id=order_id)
            except Orders.DoesNotExist:
                raise Http404

            serializer = self.serializer_class(order)

            return Response(serializer.data)

        else:
            raise ParseError("field is required!")

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        order_id = request.data.get('order_id', None)
        meal_id = request.data.get('meal_id', None)
        if order_id is None:
            raise ParseError("field is required!")
        if meal_id is None:
            raise ParseError("field is required!")
        try:
            order = self.queryset.get(id=order_id)
        except Orders.DoesNotExist:
            raise Http404
        try:
            meal = order.meals.get(id=meal_id)
        except Meal.DoesNotExist:
            raise Http404
        meal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CheckView(APIView):
    queryset = Check.objects.all()
    serializer_class = CheckSerializer

    def get(self, request, *args, **kwargs):
        checks = self.queryset.all()

        serializer = self.serializer_class(checks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        self._close_order(serializer.data['order_id'])

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        check_id = request.data.get('id', None)

        if check_id is None:
            raise ParseError("field is required")

        try:
            check = self.queryset.get(id=check_id)
        except Check.DoesNotExist:
            raise Http404
        else:
            check.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)