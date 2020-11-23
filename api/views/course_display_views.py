from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.course_display import CourseDisplay
from ..serializers import CourseDisplaySerializer

# Create your views here.
class CourseDisplays(generics.ListCreateAPIView):
    permission_classes = ()
    def get(self, request):
        """Index request"""
        coursedisplays = CourseDisplay.objects.all()
        data = CourseDisplaySerializer(coursedisplays, many=True).data
        return Response(data)

    serializer_class = CourseDisplaySerializer
    def post(self, request):
        """Create request"""
        # Serialize/create application
        coursedisplay = CourseDisplaySerializer(data=request.data['coursedisplay'])
        if coursedisplay.is_valid():
            m = coursedisplay.save()
            return Response(coursedisplay.data, status=status.HTTP_201_CREATED)
        else:
            return Response(coursedisplay.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDisplayDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=()
    def get(self, request, pk):
        """Show request"""
        coursedisplay = get_object_or_404(CourseDisplay, pk=pk)
        data = CourseDisplaySerializer(coursedisplay).data
        # Only want to show owned applications?
        # if not request.user.id == data['owner']:
        #     raise PermissionDenied('Unauthorized, you do not own this mango')
        return Response(data)

