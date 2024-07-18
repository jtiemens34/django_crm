from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer

# Create your views here.
class CustomerListCreate(generics.ListCreateAPIView):
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer
  def delete(self, request, *args, **kwargs):
    Customer.objects.all().delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
class CustomerRetreiveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer
  lookup_field = "email"
class CustomerList(APIView):
  def get(self, request, format=None):
    first_name = request.query_params.get("first_name", "")
    last_name = request.query_params.get("last_name", "")
    if first_name and last_name:
      customers = Customer.objects.filter(last_name__icontains=first_name)
      customers = Customer.objects.filter(last_name__icontains=last_name)
    else:
      customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)