from django.shortcuts import render
from twitter_notification.models import Notification


def notification_view(request):
    notification_ids = []
    notifications = Notification.objects.filter(
        reciever=request.user.id).filter(is_seen=False)

    if notifications.count() > 0:
        for notification in notifications:
            notification_ids.append(notification.id)
            notification.is_seen = True
            notification.save()
        notifications_to_render = []
        for note_id in notification_ids:
            notifications_to_render.append(
                Notification.objects.get(id=note_id))

        return render(request, 'notification.html', {'notifications_to_render': notifications_to_render})

    return render(request, 'notification.html', {'notifications': ['no notifications']})
