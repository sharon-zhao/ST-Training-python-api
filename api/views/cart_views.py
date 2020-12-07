from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.carts import Cart
from ..serializers import ApplicationSerializer, UserSerializer

# Create your views here.


class Applications(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):

        """Index request"""
        # applications = Application.objects.all()
        applications = Application.objects.filter(owner=request.user.id)
        data = ApplicationSerializer(applications, many=True).data
        return Response(data)

    serializer_class = ApplicationSerializer

    def post(self, request):
        print(request.user)
        """Create request"""
        # Add user to request object
        request.data['application']['owner'] = request.user.id
        # Serialize/create application
        application = ApplicationSerializer(data=request.data['application'])
        if application.is_valid():
            m = application.save()
            return Response(application.data, status=status.HTTP_201_CREATED)
        else:
            return Response(application.errors, status=status.HTTP_400_BAD_REQUEST)


class ApplicationDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)

    def get(self, request, pk):
        """Show request"""
        application = get_object_or_404(Application, pk=pk)
        data = ApplicationSerializer(application).data
        # Only want to show owned applications?
        # if not request.user.id == data['owner']:
        #     raise PermissionDenied('Unauthorized, you do not own this mango')
        return Response(data)

    def delete(self, request, pk):
        """Delete request"""
        application = get_object_or_404(Application, pk=pk)

        data = ApplicationSerializer(application).data
        print(application.owner)
        if not request.user == application.owner:
            raise PermissionDenied('Unauthorized, you do not own this application')
        application.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        print('========================')
        print(request.data)
        if request.data['appl'].get('owner', False):
            del request.data['appl']['owner']

        # Locate Application
        application = get_object_or_404(Application, pk=pk)
        # Check if user is  the same
        if not request.user == application.owner:
            raise PermissionDenied('Unauthorized, you do not own this application')

        # Add owner to data object now that we know this user owns the resource
        request.data['appl']['owner'] = request.user.id
        # Validate updates with serializer
        ms = ApplicationSerializer(application, data=request.data['appl'], partial=True)
        if ms.is_valid():
            ms.save()
            print(ms)
            return Response(ms.data)
        return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)
