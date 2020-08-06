from rest_framework import viewsets

from .serializers import StudentSerializer
from student.models import Student


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('name')
    serializer_class =StudentSerializer