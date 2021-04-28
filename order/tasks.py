from celery.schedules import crontab
from celery.task import periodic_task
from celery.utils.log import get_task_logger
from .models import *
from django.db.models import Q
from datetime import datetime
logger = get_task_logger(__name__)


@periodic_task(run_every=(crontab(minute='*/1')), name="update_order_status", ignore_result=False)
def update_order_status():
    current_datetime = datetime.now()
    order_detail = OrderDetail.objects.filter(Q(order_delivery_datetime__lte=current_datetime))
    order_detail.update(status='rejected')
    logger.info(order_detail)
    return 1