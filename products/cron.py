from order.models import *
from products.models import *
from django.db.models import Avg, Q, F


def update_avg_price_job():
    product_prices = OrderDetail.objects.filter(Q(status='purchased') | Q(status='delivered')).values(product=F('order_products__product')).annotate(avg_price=Avg('order_products__unit_sale_price'))
    for product_record in product_prices:
        Product.objects.filter(id=product_record['product']).update(avg_price=product_record['avg_price'])

    print('cronjob running')