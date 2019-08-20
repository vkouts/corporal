import random
from django.db.models import Max
from rest_framework import mixins
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from core.api.serializers import PictureSerializer, BackColorSerializer
from core.models import Picture, BackColor


class PictureViewSet(
    mixins.ListModelMixin,
    GenericViewSet):
    queryset = Picture.objects.filter(visible=True)
    permission_classes = (permissions.AllowAny, )
    serializer_class = PictureSerializer

    @action(detail=False, methods=['GET'], serializer_class=PictureSerializer, 
        permission_classes=(permissions.AllowAny, ))
    def random(self, request, *args, **kwargs):
        max_id = self.queryset.aggregate(max_id=Max("id"))['max_id']
        while True:
            pk = random.randint(1, max_id)
            picture = self.queryset.filter(pk=pk).first()
            if picture:
                ser = self.serializer_class(picture)
                return Response(ser.data)


class BackColorViewSet(
    mixins.ListModelMixin,
    GenericViewSet):
    queryset = BackColor.objects.filter(visible=True)
    permission_classes = (permissions.AllowAny, )
    serializer_class = BackColorSerializer

    @action(detail=False, methods=['GET'], serializer_class=BackColorSerializer, 
        permission_classes=(permissions.AllowAny, ))
    def random(self, request, *args, **kwargs):
        max_id = self.queryset.aggregate(max_id=Max("id"))['max_id']
        while True:
            pk = random.randint(1, max_id)
            color = self.queryset.filter(pk=pk).first()
            if color:
                ser = self.serializer_class(color)
                return Response(ser.data)