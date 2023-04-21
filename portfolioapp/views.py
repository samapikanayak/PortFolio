from rest_framework.views import APIView
from . import serializers
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework import status, permissions
from rest_framework.response import Response
from django.db import transaction
from .models import User
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.viewsets import ModelViewSet
from geopy.geocoders import Nominatim
import folium
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password

class CustomTokenObtainPairView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.LoginSerializer()
    def post(self,request):
        login_response = {}
        http_status = None
        user = User.objects.filter(username=request.data['username']).first()
        # breakpoint()
        if user:
            serializer_data = self.serializer_class.validate(attrs=request.data)
            login_response = serializer_data
            http_status = status.HTTP_200_OK
        else:
            login_response['message'] = "Invalid Username or Password"
            http_status = status.HTTP_401_UNAUTHORIZED
        return Response(login_response, status=http_status)

class UserRegisterViewSet(CreateAPIView, GenericAPIView):
    ''' Register User '''
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    @transaction.atomic
    def create(self, request):
        ''' Register User '''
        response = {}
        http_status = None

        serializer = serializers.SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = request.data
        User.objects.create_user(**data)
        # serializer.save()
        response["message"] = "User Created Successfully"
        response["data"] = serializer.data
        http_status = status.HTTP_201_CREATED
        return Response(
            response,
            status=http_status
        )
       
class UserDetailGetOrUpdate(ModelViewSet):
    serializer_class = serializers.SignUpSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    lookup_field="id"
    def get_queryset(self):
        current_user = self.request.user
        if not current_user.is_superuser:
            queryset = self.queryset.filter(id=current_user.id)
        else:
            queryset = self.queryset
        # return Response({"status": "success", "count": queryset.count(),"data": queryset},status=status.HTTP_200_OK)
        return queryset

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        cur_user = self.request.user
        if not cur_user.is_superuser:
            user = self.queryset.filter(id=cur_user.id).first()
        else:
            user = self.get_object()
        user.delete()
        return Response({"status": "success", "msg": "user deleted", "data": None},status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        cur_user = self.request.user
        if not cur_user.is_superuser:
            user = self.queryset.filter(id=cur_user.id).first()
        else:
            user = self.get_object()
        serialized_data = self.serializer_class(data=request.data, instance=user)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        response = {"status": "success","message": "user updated","data": serialized_data.data}
        return Response(response, status=status.HTTP_200_OK)

class GetGeographyLocation(APIView):
    def get(self, request):
        geolocator = Nominatim(user_agent="portfolioapp")
        user = User.objects.all()
        lat_long_list = []
        try:
            for i in user:
                location = geolocator.geocode(i.home_address)
                lat, long = location.latitude, location.longitude
                lat_long_list.append((lat, long))
            map_center = lat_long_list[0]
            maps = folium.Map(location=map_center, zoom_start=2)
            for location in lat_long_list:
                marker = folium.Marker(location=location)
                marker.add_to(maps)
            maps.show_in_browser()
            return HttpResponse(maps, content_type='image/png')
        except Exception as e:
            raise ValueError("Not found")



