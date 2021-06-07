from order.models import *
from delivery_app.models import *
from products.models import *
from django.db.models import Avg, Q, F, Count
from fcm_django.models import FCMDevice



def send_pending_order_notification():
    order_details = OrderDetail.objects.filter(status='pending').values('delivery_person').annotate(pending_order_count=Count('delivery_person'))
    # print(order_details)
    for order in order_details:
        delivery_obj = DeliveryPerson.objects.get(id=order['delivery_person'])
        user_id = delivery_obj.user.id
        print("dp", user_id)
        if order['pending_order_count'] > 0:
            try:
                device = FCMDevice.objects.filter(user=user_id, active=True)
                print(device)
                device.send_message(title="Reminder: Pending Orders", body=f"You have {order['pending_order_count']} pending orders.")
            
            except Exception as e:
                print(e)

            
def send_inprogress_order_notification():
    order_details = OrderDetail.objects.filter(status='in_progress').values('delivery_person').annotate(in_progress_order_count=Count('delivery_person'))
    # print(order_details)
    for order in order_details:
        delivery_obj = DeliveryPerson.objects.get(id=order['delivery_person'])
        user_id = delivery_obj.user.id
        print("dp", user_id)
        if order['in_progress_order_count'] > 0:
            try:
                device = FCMDevice.objects.filter(user=user_id, active=True)
                print(device)
                device.send_message(title="Reminder: In Progress Orders", body=f"You have {order['in_progress_order_count']} in progress orders.")
            
            except Exception as e:
                print(e)
    

