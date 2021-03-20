from celery.schedules import crontab
from celery.task import periodic_task
from .models import *

@periodic_task(run_every=(crontab(minute='*/1')), name="update_order_status", ignore_result=False)
def update_order_status():
    print('here')
    order_detail = OrderDetail.objects.get(id=1)
    print(order_detail)
    order_detail.status = 'rejected'
    order_detail.save()
    return 1