# rabbitMQtest
Main script == agentTest_init.py

Code to test cross instance/code language communication via Advanced Message Queueing Protocol (AMQP).

An AMQP Agent is used to simplify the sending and receiveing of messages. Messages may be native python objects because json dumps/loads is implemented on either end of a transfer.

# Result
Code works as expected. Can accomplish over 10 ping-pong type message cycles per second.

# Bottom Line
While this may work for sending all desired data, it may be faster/easier, to use as control signal communication for SQL database access across code instances.
