# rabbitMQtest - batchCase
Same as previous test, though messages are sent in batches and processed by the recieving end as they are recieved. 
Control is swapped via a message flag caught and processed in the callback functions. Process meant to more closely mimic use case scenario.


Main script == agentTest_init.py

Code to test cross instance/code language communication via Advanced Message Queueing Protocol (AMQP).

An AMQP Agent is used to simplify the sending and receiveing of messages. Messages may be native python objects because json dumps/loads is implemented on either end of a transfer.

# Result
Code acts as expected, i.e. messages sent and recieved in a parallel fashion
enabeling the recieving process to take action while new messages continue 
to be received.

The inital delay between the first batch send and the begining of
parallel processing is probably due to queue intialization within 
rabbitMQ or Erlang. Probably.

# Discussion
Loop structure and message send / receive points are important to 
make the process run smoothly.

Research should be done to find a way to clear queues as lingering messages can cause undesired results.