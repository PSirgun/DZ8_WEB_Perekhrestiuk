import pika
import json
import pika.spec
import fake_subscriber

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange="part_two", exchange_type='direct')

channel.queue_declare(queue="task_email")
channel.queue_bind(exchange="part_two", queue="task_email")  

channel.queue_declare(queue="task_sms")
channel.queue_bind(exchange="part_two", queue="task_sms")  


def main(num_subscribers=5):
    for _ in range(5):
        add_subs = {'id' : str(fake_subscriber.add_subscriber())}
        channel.basic_publish(exchange='part_two', 
                              routing_key='task_email', 
                              body=json.dumps(add_subs).encode('utf-8'), 
                              properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE)
        )
        channel.basic_publish(exchange='part_two', 
                              routing_key='task_sms', 
                              body=json.dumps(add_subs).encode('utf-8'), 
                              properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE)
        )
        print ('%r' % add_subs) #не знав про таку можливість
    connection.close()

if __name__ == '__main__':
    main()






    
