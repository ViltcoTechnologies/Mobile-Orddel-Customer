from django.db import models
import sqlite3
import pandas as pd
from products.models import *


df = pd.read_excel('Product List.xlsx')
slno = list(df['Sr.No.'])
item_name = list(df['Item Name'])
category = list(df['Category'])
unit = list(df['UNIT'])
for i in range(len(slno)):
    cat_id = 1
    if category[i] == 'Vegetable':
        cat_id = 3
    elif category[i] == 'Fruit':
        cat_id = 4
    elif category == 'Msc.':
        cat_id = 5

    category_obj = Category.objects.get(id=cat_id)
    Product.objects.create(category=category_obj, name=item_name[i], unit=unit[i])

