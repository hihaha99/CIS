import os, django ,json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CISnew.settings")
django.setup()
from info.models import Stores ,Dishes
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

filename = os.path.join(BASE_DIR,'CISnew','database.json')

with open(filename) as f:
    data = json.load(f)
    for store in data:
        name = store['Name']
        start_hour= str(store['Operating Hours'][0][0])+":"+str(store['Operating Hours'][0][1])+":"+str(store['Operating Hours'][0][2])
        end_hour = str(store['Operating Hours'][1][0])+":"+str(store['Operating Hours'][1][1])+":"+str(store['Operating Hours'][1][2])
        wait_time = store["Waiting Time"]
        menu = store["Food available"]
        store1 = Stores(name=name,start_hour=start_hour,end_hour=end_hour,wait_time=wait_time)
        store1.save()
        for food in menu:
            dname = food 
            details = menu[dname]
            price = details[0]
            dstart_hour = str(details[1][0])+":"+str(details[1][1])+":"+str(details[1][2])
            dend_hour = str(details[2][0])+":"+str(details[2][1])+":"+str(details[2][2])
            dish = Dishes(store=store1,dname=dname,price=price,start_hour=dstart_hour,end_hour=dend_hour)
            dish.save()