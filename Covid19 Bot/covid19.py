import requests
from win10toast import ToastNotifier
import json
import time

def update():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data = r.json()
    text = f'Confirm : {data["cases"]} \n Deaths: {data["deaths"]} \n Cures: {data["recovered"]}'

    while(True):
        toast = ToastNotifier()
        toast.show_toast("Covid-19 Updates",text,duration=20)
        time.sleep(60)

update()
