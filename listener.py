from google.cloud import pubsub_v1
from google.cloud import bigquery


project_id = ""  # replace with your project id
subscription_name = "" # replace with your subscription name

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(
    project_id, subscription_name)



client = bigquery.Client()
dataset_id = '' # replace with your dataset ID
table_id = ''  # replace with your table ID
table_ref = client.dataset(dataset_id).table(table_id)
table = client.get_table(table_ref)  # API request

def callback(message):
    try:
        dict = eval(message.data.decode())
        errors = client.insert_rows(table, dict)
        assert errors == []
        message.ack()
    except AssertionError:
        print('error inserting message with message id: ', errors)
    except Exception as e:
        print('error decoding message on {}' .format(e))

future = subscriber.subscribe(subscription_path, callback=callback)

try:
    # When timeout is unspecified, the result method waits indefinitely.
    future.result(timeout=60)
except Exception as e:
    print('Listening for messages on {} threw an Exception: {}.'.format(subscription_name, e))

