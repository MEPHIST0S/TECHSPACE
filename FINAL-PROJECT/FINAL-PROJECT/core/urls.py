from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegisterView, UserProfileView, 
    DepartmentListCreateView, DepartmentRetrieveUpdateDestroyView,
    PositionListCreateView, PositionRetrieveUpdateDestroyView,
    EmployeeListCreateView, EmployeeRetrieveUpdateDestroyView
)

urlpatterns = [
    # AUTH
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserProfileView.as_view(), name='profile'),

    # DEPARTMENT
    path('departments/', DepartmentListCreateView.as_view(), name='department-list-create'),
    path('departments/<int:pk>/', DepartmentRetrieveUpdateDestroyView.as_view(), name='department-detail'),

    # POSITION
    path('positions/', PositionListCreateView.as_view(), name='position-list-create'),
    path('positions/<int:pk>/', PositionRetrieveUpdateDestroyView.as_view(), name='position-detail'),

    # EMPLOYEE
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='employee-detail'),
]