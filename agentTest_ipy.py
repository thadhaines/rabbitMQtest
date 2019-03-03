"""Second script of agentTest, meant to represent a 2nd process"""

from AMQPAgent import AMQPAgent
import sys
import datetime

def main(host,limit):
    # Create ipy 32 agent
    ipy = AMQPAgent(host)
    ipy.msg = [0,'init', 'time']

    while ipy.msg < limit:
        ipy.receive('toIPY',ipy.callback)
        ipy.msg[0] += 1
        ipy.msg[1] = 'IPY - pong'
        ipy.msg[2] = datetime.datetime.now().strftime('%H:%M:%S.%f')
        ipy.send('toPY3', ipy.msg)

    print('IPY finished')

if __name__ == "__main__":
    host = sys.argv[1]
    limit = sys.argv[2]
    main(host, limit)
