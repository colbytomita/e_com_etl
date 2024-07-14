import pandas as pd
import json
from datetime import datetime
import s3fs
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
os.environ['KAGGLE_USERNAME'] = os.getenv('KAGGLE_USERNAME')
os.environ['KAGGLE_KEY'] = os.getenv('KAGGLE_KEY')

from kaggle.api.kaggle_api_extended import KaggleApi



# Load Kaggle API credentials
api = KaggleApi()

api.authenticate()

# Download dataset
api.dataset_download_files('thedevastator/unlock-profits-with-e-commerce-sales-data', path='data', unzip=True)

# Load data
df = pd.read_csv('data/Amazon Sale Report.csv')

print(df.head())
