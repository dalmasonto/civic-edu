from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from main.utils import StandardResultsSetPagination
from main.permissions import IsAuthenticatedOrPostOnly
from main.authentication import AUTH_CLASS

from rest_framework.filters import SearchFilter, OrderingFilter

from .serializers import AccountSerializer, ProfileSerializer
from .models import Profile


class AccountViewSet(viewsets.ModelViewSet):
    queryset = User.objects.prefetch_related('profile').all().order_by('id')
    serializer_class = AccountSerializer

    authentication_classes = [AUTH_CLASS]
    permission_classes = [IsAuthenticatedOrPostOnly]

    pagination_class = StandardResultsSetPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['id', 'first_name', 'last_name', 'email', 'username']
    filterset_fields = ['is_superuser', 'is_staff']
    search_fields = ['email', 'first_name', 'last_name', 'username', 'profile__phone_number']


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('id')
    serializer_class = ProfileSerializer

    authentication_classes = [AUTH_CLASS]
    permission_classes = [IsAuthenticatedOrPostOnly]

    pagination_class = StandardResultsSetPagination

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = []
    search_fields = []

