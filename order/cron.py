from order.models import *
from products.models import *
from django.db.models import Avg, Q, F


def send_pending_order_notification():
    order_details = OrderDetail.objects.filter(status='pending').annotate(delivery_person=F('delivery_person'))
    print(order_details)
    # user_id = delivery_obj.user.id
    # print("dp", user_id)
    # try:
    #     device = FCMDevice.objects.filter(user=user_id, active=True)
    #     print(device)
    #     device.send_message(title="New Order", body="You have received an order.")
    #
    # except:
    #     return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Unable to send notification'})