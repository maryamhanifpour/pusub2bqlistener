
Aim: Deliver a bunch of low volume messages from Pubsub to Bigquery with not much preprocessing required. Messages get accumulated in Pubsub by events randomly distributed in time and there is no need for the messages to be immediately available in Bigquery. So no need for a constantly running job and no worries about the latency.
Solution:
A subscriber script to deliver messages accumulated in pubsub to bigquery. 

publish.py: Use it to publish test data to a pubsub topic.

listener.py: Use it to to deliver messages accumalted in pubsub to a bigquery table.


![alt text](https://github.com/maryamhanifpour/pusub2bqlistener/blob/master/Listener.PNG)

Cons:
Streaming inserts to Bigquery unless Subscriber App delivers data to Cloud Storage and Cloud Storage triggers another job to batch load the data to Bigquery.
