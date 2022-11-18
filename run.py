# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Grocery_Galore')

def get_dailysales_data():
    """
    Request daily sales data from users
    """
    print("Please enter the sales data from the past day")
    print("Enter the daily sales data in this order: Apples, Oranges, Bananas, Avocado, Pears, Grapes, Mangos")
    print("Input should be 7 numbers, seperated by commas.")
    print("Example: 11,22,33,44,55,66,77\n")

    data_str = input("Enter your data here: ")
    print(f"The data you have provided is {data_str}")


get_dailysales_data()


