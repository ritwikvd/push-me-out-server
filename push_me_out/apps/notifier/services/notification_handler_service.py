import json

from apps.notifier.exceptions.push_event_exception import PushEventException
from apps.notifier.models import Subscriber
from apps.notifier.services.notification_service import NotificationService


class NotificationHandlerService:
    def __init__(self, subscriber_id, notification_type):
        self.subscriber_id = subscriber_id
        self.notification_type = notification_type

    def handle(self):
        info = []
        for subscriber in self.__get_subscribers():
            try:
                NotificationService(subscriber).trigger_push_event(json.dumps(self.notification_type.options))
            except PushEventException as ex:
                info.append(
                    {'subscriber_id': subscriber.id, 'error': str(ex)}
                )

        return info

    def __get_subscribers(self):
        subscribers = Subscriber.objects.all()
        if self.subscriber_id is not None:
            subscribers = subscribers.filter(pk=self.subscriber_id)

        return subscribers