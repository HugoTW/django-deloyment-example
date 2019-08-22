import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','firstProject.settings')


import django
django.setup()

## FAKE Populate Script
import random

from first_app.models import AccessRecord, Topic, Webpage, UserInfo
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name= random.choice(topics))[0]
    t.save()
    return t

def populate (N=5):
    for entry in range(N):
        #get Topic for Entry
        top = add_topic()

        #Create Fake Data
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpg= Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        #Creaet a fake access Record
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date= fake_date)[0]

def pupulateUser (N=5):
    for entry in range(N):

        fake_firstName = fakegen.first_name()
        fake_lastName = fakegen.last_name()
        fake_email = fakegen.email()
        userinfo = UserInfo.objects.get_or_create(firstName=fake_firstName, lastName= fake_lastName, email = fake_email)[0]


if __name__ == '__main__':
    print ('populating script!')
    # populate(20)
    pupulateUser(20)
    print("populating completed")
