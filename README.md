
A subscriber script to deliver messages accumulated in pubsub to bigquery. 

publish.py: Use it to publish test data to a pubsub topic.

listener.py: Use it to to deliver messages accumalted in pubsub to a bigquery table.


![alt text](https://github.com/maryamhanifpour/pusub2bqlistener/blob/master/Listener.PNG)

Cons:
Streaming inserts to Bigquery unless Subscriber App delivers data to Cloud Storage and Cloud Storage triggers another job to batch load the data to Bigquery.
