from django.urls import path
from food import views


urlpatterns = [
    path('table', views.TableListView),
    path('role', views.RoleListView),
    path('department', views.DepartmentListView),
    path('category', views.CategoryListView),
    path('status', views.StatusListView),
    path('service', views.ServiceListView),
    path('meal', views.MealListView),
]