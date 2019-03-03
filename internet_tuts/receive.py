import pika

#NOTE: for ironpython not to err - use 127.0.0.1 instead of localhost 
#Seems to connect to the same as localhost anyway
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    print('Stopping consumtion')
    ch.stop_consuming()
    global msg
    msg = body

channel.basic_consume(callback, queue='hello', no_ack=True)
msg = None
print(msg)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
print(msg)