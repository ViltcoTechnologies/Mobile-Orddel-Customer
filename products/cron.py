from order.models import *
from products.models import *
from django.db.models import Avg, Q, F


def update_avg_price_job():
    product_prices = OrderDetail.objects.filter(Q(status='purchased') | Q(status='delivered')).values(product=F('order_products__product'), client=F('order_box__client')).annotate(avg_price=Avg('order_products__unit_sale_price'))
    for product_record in product_prices:
        print(product_record)
        # Product.objects.filter(id=product_record['product']).update(avg_price=product_record['avg_price'])
        try:
            client = Client.objects.get(id=product_record['client'])
            product = Product.objects.get(id=product_record['product'])
            avg_price_obj = AveragePrice.objects.update_or_create(client=client, product=product, avg_price=product_record['avg_price'])
            avg_price_obj.save()
        except:
            pass

    print('cronjob running')