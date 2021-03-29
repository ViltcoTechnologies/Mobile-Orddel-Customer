import random
from django.db import models
import sqlite3
import pandas as pd
from products.models import *


df = pd.read_excel('Product List.xlsx')
slno = list(df['Sr.No.'])
item_name = list(df['Item Name'])
category = list(df['Category'])
unit = list(df['UNIT'])


def random_number_generator(a, b):
    n = round(random.uniform(a, b), 2)
    # n = random.randint(a, b)
    return n


for i in range(len(slno)):
    cat_id = 1
    vat = 0
    if category[i] == 'Vegetable':
        cat_id = 3
    elif category[i] == 'Fruit':
        cat_id = 4
    elif category == 'Msc.':
        cat_id = 5
        vat = 0.20

    avg_price = random_number_generator(50, 150)
    category_obj = Category.objects.get(id=cat_id)
    Product.objects.create(id=slno[i], vat=vat, category=category_obj, name=item_name[i], unit=unit[i], avg_price=avg_price)

