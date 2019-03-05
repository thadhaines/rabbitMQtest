"""Second script of agentTest, meant to represent a 2nd process"""

from AMQPAgent import AMQPAgent
import sys
import datetime

def getTstr():
    """Return Time String"""
    return datetime.datetime.now().strftime('%H:%M:%S.%f')


def main(host,totLimit, bLimit):
    # Create ipy 32 agent
    msgForm = {'PassCtrl':False, 
           'time':getTstr(), 
           'sharedValue':0.0, 
           'sender':'IPY'}
    ipy = AMQPAgent('IPY', host, msgForm)

    runFlag = 1
    while runFlag:

        ipy.receive('toIPY',ipy.callback)

        for messageCount in range(bLimit):
            ipy.msg['sender'] = 'IPY'
            ipy.msg['time'] = getTstr()
            if ipy.msg['sharedValue'] >= totLimit:
                runFlag = 0
                break

            ipy.msg['sharedValue'] += 1
            ipy.send('toPY3',ipy.msg)

        ipy.msg['time'] = getTstr()
        ipy.msg['PassCtrl'] = True
        ipy.send('toPY3',ipy.msg)

    print('IPY finished')
    
if __name__ == "__main__":
    host = sys.argv[1]
    totLimit = int(sys.argv[2])
    bLimit = int(sys.argv[3])
    main(host, totLimit, bLimit)
