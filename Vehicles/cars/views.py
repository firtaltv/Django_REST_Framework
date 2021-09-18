from rest_framework import generics
from .serializers import CarDetailSerializer, CarsListSerializer
from .models import Car
from .permissions import IsOwnerReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer


class CarsListView(generics.ListAPIView):
    serializer_class = CarsListSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAdminUser,)


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsOwnerReadOnly,)
