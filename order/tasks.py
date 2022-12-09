from celery.schedules import crontab
from celery.task import periodic_task
from celery.utils.log import get_task_logger
from .models import *
from django.db.models import Q
from datetime import datetime
import pytz
logger = get_task_logger(__name__)


@periodic_task(run_every=(crontab(minute='*/1')), name="update_order_status", ignore_result=False)
def update_order_status():
    timezone = pytz.timezone("Asia/Karachi")
    current_datetime = datetime.now(tz=timezone)
    order_detail = OrderDetail.objects.filter(Q(order_delivery_datetime__lte=current_datetime), Q(status='pending'))
    logger.info(order_detail)

    if order_detail:
        for order in order_detail:
            logger.info(order)
            try:
                user_id = order.order_box.client.user.id
                try:
                    device = FCMDevice.objects.filter(user=user_id, active=True)
                    device.send_message(title="Order Rejected", body="Your order has been expired.")

                except:
                    pass


            except Exception as e:
                print(e.args)
                pass
                    

            
        order_detail.update(status='rejected')
    return 1