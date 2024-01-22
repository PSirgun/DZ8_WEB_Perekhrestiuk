from model import Subscriber
from faker import Faker
import connect

fake = Faker(locale='uk_UA')

def add_subscriber():

    fake_sub = Subscriber(
        fullname=fake.name(),
        email=fake.email(),
        phone = fake.phone_number()
    )
    fake_sub.save()
    return fake_sub.id

def work_completed(id):
    subscriber = Subscriber.objects.get(id=id)
    subscriber.completed_work = True
    subscriber.save()
    


if __name__ == '__main__':
    add_subscriber()
    work_completed('65ae7668f424bae429fed11b')


