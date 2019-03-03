"""Script to test AMQP Agent functionality"""
from AMQPAgent import AMQPAgent
import datetime
import subprocess
import signal

limit = 30     # number of ping-pongs to perform

# Create python 3 agent
host = '127.0.0.1'
py3 = AMQPAgent(host, [0,'init','time'])

# start 2nd process
cmd = "ipy32 agentTest_ipy.py " + host + ' ' + str(limit)
ipyProc = subprocess.Popen(cmd)

while py3.msg[0] < limit:
    py3.msg[0] += 1
    py3.msg[1] = 'PY3 - Ping'
    py3.msg[2] = datetime.datetime.now().strftime('%H:%M:%S.%f')
    py3.send('toIPY',py3.msg)
    py3.receive('toPY3', py3.callback)

print('PY3 Finished')
# close other script for sure
ipyProc.send_signal(signal.SIGTERM)

"""
Results:
Cross instance communication works - can perform 10-12 ping-pongs per second.

Discussion:
While this could be used for workaround, it may not work, or be as fast,
as a database option for sending large amounts of data. Although the msg
creation could be altered to send more data, it may not be worth the effort.

AMQP could be used to alert processes of database availability and a SQL
database could be used for the main data sharing point.

Since a wait is already programmed into the agent receive function it may 
make this AMQP/SQL option semi-straight forward.
"""