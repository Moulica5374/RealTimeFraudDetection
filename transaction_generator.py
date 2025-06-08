import json
import time
import random
import boto3
from datetime import datetime

# Initialize Kinesis client
kinesis = boto3.client("kinesis", region_name="us-east-1")  # Change region if needed

def generate_transaction():
    # 20 percent chance to simulate a fraud
    if random.random() < 0.2:
        amount = round(random.uniform(6000.0, 10000.0), 2)
        country = random.choice(["RU", "NG", "CN"])
    else:
        amount = round(random.uniform(10.0, 5000.0), 2)
        country = "US"

    txn = {
        "transaction_id": f"txn_{int(time.time())}",
        "user_id": f"user_{random.randint(1000, 9999)}",
        "amount": amount,
        "country": country,
        "location": random.choice(["New York", "San Francisco", "Chicago", "Miami", "Dallas"]),
        "timestamp": datetime.utcnow().isoformat()
    }
    return txn

if __name__ == "__main__":
    while True:
        txn = generate_transaction()
        print("Sending", txn)

        response = kinesis.put_record(
            StreamName="TransactionStream",
            Data=json.dumps(txn),
            PartitionKey=txn["user_id"]
        )

        print("Sent with SequenceNumber", response["SequenceNumber"])
        time.sleep(1)

