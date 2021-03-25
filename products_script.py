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
        cat_id = 2
    elif category[i] == 'Fruit':
        cat_id = 1
    elif category[i] == 'Msc.':
        cat_id = 22

    category_obj = Category.objects.get(id=cat_id)
    if unit[i] == 'Bag':
        unit_choice = 'bag'
    elif unit[i] == 'Box':
        unit_choice = 'box'
    Product.objects.create(id=slno[i], category=category_obj, name=item_name[i], unit=unit_choice)

