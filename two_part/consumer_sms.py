import pika
import time
import sys
import model
import connect
import json

def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='task_sms')

    def callback(ch, method, properties, body):
        data = json.loads(body.decode('utf-8'))
        subscriber = model.Subscriber.objects.get(id=data['id'])
        time.sleep(1)
        subscriber.sms_send = True
        print(f'For {subscriber.fullname} sent  sms to phone {subscriber.phone}')


    
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_sms', on_message_callback=callback, auto_ack=True)

    
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)