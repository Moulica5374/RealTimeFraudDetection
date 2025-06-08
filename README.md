# RealTimeFraudDetection
 This project implements a real-time fraud detection pipeline using AWS services. It continuously streams transaction data, detects fraudulent activity using predefined rules, and visualizes flagged transactions via a Gradio dashboard.

 Features :
 
 Real-time streaming of transaction data using Amazon Kinesis.
 
 Rule-based fraud detection using AWS Lambda.
 
 DynamoDB integration for storing detected fraudulent transactions.
 
 Interactive Gradio dashboard to view and analyze fraud cases.

 # Architecture Overview:

 [Transaction Generator] → [Amazon Kinesis Stream]
                                 ↓
                        [AWS Lambda Function]
                           |       
      [Fraud Detected] |       | [Safe Transaction]
                           ↓
               [DynamoDB FraudTransactions Table]
                                 ↓
                      [Gradio Fraud Dashboard]

 
