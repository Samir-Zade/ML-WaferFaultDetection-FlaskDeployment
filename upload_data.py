from pymongo.mongo_client import MongoClient
import json
import pandas as pd

#uri - uniform resource indentifier
uri = "mongodb+srv://samirzadeofficial:Samirzadeofficial@waferfaultdetection.xjzrw1s.mongodb.net/?retryWrites=true&w=majority&appName=WaferFaultDetection"

# Create a new client and connect to the server
client = MongoClient(uri)


#create datbase name and collection name
DATABASE_NAME = "WaferDetection"
COLLECTION_NAME = "WaferFaultDetection"

#read the data as dataframe
df = pd.read_csv(r"D:\Codes\Wafer-Fault-Detection\notebook\Data\Wafers-Dataset.csv")

df = df.drop("Unnamed: 0", axis = 1)
df.head()

#convert the data into json
json_record = list(json.loads(df.T.to_json()).values())

#now dump the data into database
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)