from django.urls import path
from . import views

urlpatterns = [
  path("customers/", views.CustomerListCreate.as_view(), name='customer-view-create'),
  path('customers/<str:email>', views.CustomerRetreiveUpdateDestroy.as_view(), name='customer-retrieve-update-destroy')
]