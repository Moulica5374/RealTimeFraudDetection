import base64
import json
import boto3
from decimal import Decimal

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('FraudTransactions')

def lambda_handler(event, context):
    for record in event['Records']:
        try:
            # Decode and parse the transaction
            raw_data = base64.b64decode(record['kinesis']['data']).decode('utf-8')
            txn = json.loads(raw_data)

            print("Received transaction", txn)

            # Extract transaction fields
            txn_id = txn.get("transaction_id", "")
            user_id = txn.get("user_id", "")
            amount = Decimal(str(txn.get("amount", 0)))
            country = txn.get("country", "US")
            location = txn.get("location", "")
            timestamp = txn.get("timestamp", "")

            # Rule-based fraud logic
            is_high_risk_country = country in ["RU", "NG", "CN"]
            is_large_amount = amount > 5000

            if is_high_risk_country and is_large_amount:
                print("FRAUD DETECTED - User:", user_id, "Amount:", amount, "Country:", country, "Location:", location)

                # Save to DynamoDB with error handling
                try:
                    table.put_item(Item={
                        "transaction_id": txn_id,
                        "user_id": user_id,
                        "amount": amount,
                        "country": country,
                        "location": location,
                        "timestamp": timestamp
                    })
                    print("Saved to DynamoDB:", txn_id)
                except Exception as db_error:
                    print("Failed to save to DynamoDB:", db_error)

            else:
                print("Safe Transaction - User:", user_id, "Amount:", amount, "Country:", country, "Location:", location)

        except Exception as e:
            print("Error processing record:", e)

    return {"statusCode": 200, "body": "Processed"}
