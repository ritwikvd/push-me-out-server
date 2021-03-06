from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.notifier.models import NotificationType
from apps.notifier.serializers import SubscriberSerializer, NotificationTypeSerializer
from apps.notifier.services.notification_state_manager_service import NotificationStateManagerService


class SubscribersView(CreateAPIView):
    serializer_class = SubscriberSerializer


class TriggerNotification(APIView):
    def post(self, request, *args):
        state_manager = NotificationStateManagerService(data=request.data).insert()

        return Response(data={'state_manager_id': state_manager.id}, status=status.HTTP_200_OK)


class NotificationTypesView(ListAPIView):
    queryset = NotificationType.objects.all()
    serializer_class = NotificationTypeSerializer