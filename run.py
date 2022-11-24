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
    while True:

        print("Please enter the sales data from the past day")
        print("Enter the daily sales data in this order: Apples, Oranges, Bananas, Avocado, Pears, Grapes, Mangos")
        print("Input should be 7 numbers, seperated by commas.")
        print("Example: 11,22,33,44,55,66,77\n")

        data_str = input("Enter your data here: ")

        dailysales_data = data_str.split(",")

        if validate_data(dailysales_data):
            print("Data is valid!")
            break
    return dailysales_data




def validate_data(values):
    """
    Raises ValueError if strings cannot be converted into integers,
    or if there arent't exactly 6 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 7:
            raise ValueError(
                f"Exactly 7 figures are needed, you have provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try agaian.\n")
        return False

    return True



def update_sales_worksheet(datasa):
    """
    Update sales worksheet
    """
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("Dailysales")
    sales_worksheet.append_row(datasa)
    print("The sales worksheet updated successfully.\n")


def get_dailywaste_data():
    """
    Request daily waste data from users
    """
    while True:

        print("Please enter the waste data from the past day")
        print("Enter the daily waste data in this order: Apples, Oranges, Bananas, Avocado, Pears, Grapes, Mangos")
        print("Input should be 7 numbers, seperated by commas.")
        print("Example: 11,22,33,44,55,66,77\n")

        data_str = input("Enter your data here: ")

        dailywaste_data = data_str.split(",")

        if validate_data(dailywaste_data):
            print("Data is valid!")
            break
    return dailywaste_data


def update_waste_worksheet(datawa):
    """
    Update waste worksheet
    """
    print("Updating waste worksheet...\n")
    waste_worksheet = SHEET.worksheet("Dailywastechart")
    waste_worksheet.append_row(datawa)
    print("The waste worksheet updated successfully.\n")

def update_stock_worksheet(newstock_data):
    """
    Update stocklevel worksheet
    """
    print("Updating stock worksheet...\n")
    stock_worksheet = SHEET.worksheet("Stocklevels")
    stock_worksheet.append_row(newstock_data)
    print("The stock worksheet updated successfully.\n")

def calculate_newstock_data(sales_row, waste_row):
    """ 
    Compare sales and waste data with the preivious stock and the retock data to calculate the new stock for each item type.

    The new stock is calculated by subtracting the daily sales and the daily waste from the previous stock and andding the daily restock level
   
    """
    print("Calculating new stock data...\n")
    stock = SHEET.worksheet("Stocklevels").get_all_values()
    stock_row = stock[-1]
    restock = SHEET.worksheet("Dailyrestock").get_all_values()
    restock_row = restock[-1]

    newstock_data = []
    for stock, sales, waste, restock in zip(stock_row, sales_row, waste_row, restock_row):
        newstock = int(stock) - (sales + waste) + int(restock)
        newstock_data.append(newstock)

    return newstock_data
    

def main():
    """
    Run all the functions of the programme.
    """
    datasa = get_dailysales_data()
    dailysales_data = [int(num) for num in datasa]
    update_sales_worksheet(dailysales_data)
    datawa = get_dailywaste_data()
    dailywaste_data = [int(num) for num in datawa]
    update_waste_worksheet(dailywaste_data)
    newstock_data = calculate_newstock_data(dailysales_data, dailywaste_data)
    print(newstock_data)
    update_stock_worksheet(newstock_data)




    





print("Welcome to Grocery Galore Data Automation.")
main()


