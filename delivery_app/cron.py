from .models import DeliveryPersonPackageLog, DeliveryPerson
from datetime import datetime 

def set_invoices_expiry():
    print('hereee')
    try:
        delivery_person_pckg = DeliveryPersonPackageLog.objects.filter(date_expiry__lte=datetime.now())
        delivery_persons = delivery_person_pckg.values_list('delivery_person', flat=True)
        delivery_persons = DeliveryPerson.objects.filter(id__in=delivery_persons)
        delivery_persons.update(used_invoices=0, pacakge=None)
        delivery_person_pckg.update(status='inactive')
    except Exception as e:
        print(e)
    print('cronjob set invoice running...')