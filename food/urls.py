from django.urls import path
from django.conf.urls import url
from food import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('table/', views.TableListView.as_view()),
    path('role', views.RoleListView.as_view()),
    path('department', views.DepartmentListView.as_view()),
    path('category', views.CategoryListView.as_view()),
    path('category/<int:departmentid>', views.CategoryListView.as_view()),
    path('status', views.StatusView.as_view()),
    path('service', views.ServiceListView.as_view()),
    path('meal', views.MealListView.as_view()),
    path('meal/<int:category_id>/', views.MealListView.as_view()),
    path('check', views.CheckView.as_view()),
    path('meals_to_order', views.MealsToOrderView.as_view()),
    path('order', views.OrderView.as_view()),
    path('active_orders/', views.GetActiveOrderListView.as_view()),
]