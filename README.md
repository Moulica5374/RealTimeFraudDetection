# RealTimeFraudDetection
 This project implements a real-time fraud detection pipeline using AWS services. It continuously streams transaction data, detects fraudulent activity using predefined rules, and visualizes flagged transactions via a Gradio dashboard.

 Features :
 
 Real-time streaming of transaction data using Amazon Kinesis.
 
 Rule-based fraud detection using AWS Lambda.
 
 DynamoDB integration for storing detected fraudulent transactions.
 
 Interactive Gradio dashboard to view and analyze fraud cases.

 # Architecture Overview:
 
Transaction data is streamed into Amazon Kinesis.

AWS Lambda is triggered by new events in the Kinesis stream.

Lambda processes each transaction and applies fraud detection rules.

Fraudulent transactions are stored in a DynamoDB table called FraudTransactions.

A Gradio dashboard displays the fraud records in a user-friendly interface.

# Components

## Transaction Producer

 Simulates real-time transactions in JSON format.

 Sends each transaction to an Amazon Kinesis data stream.

 ## AWS Lambda Function

 Triggered automatically by new data in Kinesis.

Applies simple rules to classify a transaction as "fraud" or "safe".

If a transaction is fraudulent, it is written to the FraudTransactions DynamoDB table.

## DynamoDB Table

Named FraudTransactions.

Stores all transaction records identified as fraud by the Lambda function.

## Gradio Dashboard

A web-based dashboard created using Gradio.

Connects to DynamoDB and displays all fraud entries.

Provides filtering, searching, and data exploration features.


## Sample Transaction Format
{
  "transaction_id": "TX1001",
  "user_id": "U123",
  "amount": 12500,
  "region": "North America",
  "timestamp": "2025-06-08T12:00:00Z"
}

