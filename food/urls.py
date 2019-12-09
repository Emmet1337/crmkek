from django.urls import path
from django.conf.urls import url
from food import views

urlpatterns = [
    path('table/', views.TableListView.as_view()),
    path('role', views.RoleListView.as_view()),
    path('department', views.DepartmentListView.as_view()),
    path('category', views.CategoryListView.as_view()),
    path('status', views.StatusView.as_view()),
    path('service', views.ServiceListView.as_view()),
    path('meal', views.MealListView.as_view()),
]