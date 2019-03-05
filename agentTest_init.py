"""Script to test AMQP Agent functionality"""
from AMQPAgent import AMQPAgent
import datetime
import subprocess
import signal
import time

def getTstr():
    """Return Time String"""
    return datetime.datetime.now().strftime('%H:%M:%S.%f')

totLimit = 11  # total number of messages to send in test
bLimit = 3     # number of msgs per batch

# Create python 3 agent
host = '127.0.0.1'
msgForm = {'PassCtrl':False, 
           'time':getTstr(), 
           'sharedValue':0.0, 
           'sender':'PY3'}
py3 = AMQPAgent('PY3', host, msgForm)

# start 2nd process
cmd = "ipy32 agentTest_ipy.py " + host + ' ' + str(totLimit) +' ' + str(bLimit)
ipyProc = subprocess.Popen(cmd)
start =time.time()
runFlag = 1
while runFlag:
    
    for messageCount in range(bLimit):
        py3.msg['sender'] = 'PY3'
        py3.msg['time'] = getTstr()
        if py3.msg['sharedValue'] >= totLimit:
            runFlag = 0
            break
        py3.msg['sharedValue'] += 1
        py3.send('toIPY',py3.msg)

    if runFlag:
        py3.msg['time'] = getTstr()
        py3.msg['PassCtrl'] = True
        py3.send('toIPY',py3.msg)

        py3.receive('toPY3', py3.callback)

print('PY3 Finished')
# close other script for sure
ipyProc.send_signal(signal.SIGTERM)
print('IPY terminated')
end =time.time()
print('Elapsed time =  %f' % (end-start))

"""
Results:
Code acts as expected, i.e. messages sent and recieved in a parallel fashion
enabeling the recieving process to take action while new messages continue 
to be received.

The inital delay between the first batch send and the begining of
parallel processing is probably due to queue intialization within 
rabbitMQ or Erlang.

Discussion:
Loop structure and message send / receive points are important to 
make the process run smoothly.

Research a way to clear queues - lingering messages can cause problems.

"""