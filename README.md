
# Selected topic: Automating Credit Card Fraud Detection

Rationale: Credit cards are now a ubiquitous part of daily life. As such the increased use comes with it the greater possiblity of fraud. Consumers need to feel confident in their use and in the bank's ability to detect and respond to fraudulent charges quickly.


## Description of the source of data

https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud/versions/2?resource=download

"The datasets contains transactions made by credit cards in September 2013 by european cardholders.
This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions."

## Description of Data
* 6,362,620 rows and 11 columns
* Appears to have no duplicate entries
* Columns are ['step', 'type', 'amount', 'nameOrig', 'oldbalanceOrg', 'newbalanceOrig',
       'nameDest', 'oldbalanceDest', 'newbalanceDest', 'isFraud',
       'isFlaggedFraud']
* Number of entries labeled "isFraud": 8,213
* Number of entries  "isFlaggedFraud": 16
* Number of entries both labeled "isFraud" and "isFlaggedFraud": 16
 * It seems that all transactions that were flagged as fraud turned out to be fraud, however, this only accounts for .19% of fraud


## Questions to Answer
* Is there a way to detect credit card fraud based on:
  * Time of transaction
  * Amount of transaction
  * Store where the purchase was made

* Can this process be automated?

## Description of Communication Protocols
* One check-in via Slack at least once per day before the end of the day
* Weekly Meetings
 * First meeting is November 13 at 6pm

By November 13:
* At least one branch for each team member
* Each team member has at least four commits for the duration of the first segment



## Machine Learning Model (35 points)
Team members will be expected to present a provisional machine learning model that stands in for the final machine learning model and accomplishes the following:

Takes in data from the provisional database
Outputs label for input data


## Database Integration (25 points)
Team members will be expected to present a provisional database that stands in for the final database and accomplishes the following:

Sample data that mimics the expected final database structure or schema
Draft machine learning model is connected to the provisional database

## ERD
SQL Database Mockup
![ERD Final](https://user-images.githubusercontent.com/108309093/202322334-6a219149-1d01-4fc3-a3a1-79c61978a3d1.png)

## Visualization
https://benjaminhogan7.github.io/

Above is a link to where the final visualization will live. One visualization that is not included is a goal of having a real time fraud detection with user input from a site. Included are: 
* Visualization showing the number of transactions, where the color is showing the average amount of transactions
* A chart showing the number of transactions broken down by type and whether they are fraud or not
* A bar chart showing the average amount of transactions that are fraud and not fraud for the transaction types cash out and transfer
* A chart showing the ratio of the transaction amount of fraud to the beginning balance of the origin account and destination account.
* A pie chart showing the breakdown of the number of transactions of each type

The sample shown in these visualizations is based 100,000 randomly selected transactions out of the original 6 million. It seems to be closely representative of the full data set. In the full data set, only .1334% of transactions were fraud, whereas in the sample .106% are fraud.

