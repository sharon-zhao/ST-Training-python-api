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


class CourseDisplays(APIView):
    permission_classes = ()

    def get(self, request):
        """Index request"""
        course_displays = CourseDisplay.objects.all()
        data = CourseDisplaySerializer(course_displays, many=True).data
        return Response(data)

    serializer_class = CourseDisplaySerializer

    def post(self, request):
        """Create request"""
        print('------------------------------------')
        print(request.data)
        course_display = CourseDisplaySerializer(data=request.data['course_display'])

        if course_display.is_valid():
            m = course_display.save()
            return Response(course_display.data, status=status.HTTP_201_CREATED)
        else:
            return Response(course_display.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDisplayDetail(APIView):

    permission_classes = ()

    def get(self, request, pk):
        """Show request"""
        course_display = get_object_or_404(CourseDisplay, pk=pk)
        data = CourseDisplaySerializer(course_display).data
        # Only want to show owned applications?
        # if not request.user.id == data['owner']:
        #     raise PermissionDenied('Unauthorized, you do not own this mango')
        return Response(data)

    def delete(self, request, pk):

        """Delete request"""
        course_display = get_object_or_404(CourseDisplay, pk=pk)
        course_display.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
