from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
from APIViewapp.models import Employee
from APIViewapp.serializer import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
#ListCreateView
class EmployeeListCreateAPIView(ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
#RetrieveUpdateAPIView
class EmployeeRetriveUpdateAPIView(RetrieveUpdateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
#RetrieveDestroyAPIView
class EmployeeRetriveDestroyAPIView(RetrieveDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
#RetrieveUpdateDestroyAPIView
class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    
#APIView
class EmployeeAPIView(APIView):
    def get(self,request):
        qs=Employee.objects.all()
        serializer=EmployeeSerializer(qs,many=True)
        return Response(serializer.data)
#ListAPIView
class EmployeeListAPIView(ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
#CreateAPIView
class EmployeeCreateAPIView(CreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
#RetrieveAPIView
class EmployeeRetriveAPIView(RetrieveAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
#UpdateAPIView
class EmployeeUpdateAPIView(UpdateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
#DestroyAPIView
class EmployeeDestroyAPIView(DestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field='id' #for changing pk as 'id' in urls.py we need to use lookup_field
