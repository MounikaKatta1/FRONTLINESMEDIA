import os
import json

os.makedirs("data", exist_ok = True)
data_path = os.path.join("data", "Expenses.json")

def load():
    os.makedirs("data", exist_ok = True)
    data_path = os.path.join("data", "Expenses.json")

while(True):
    print("""
          1. Add An Expense
          2. View All Expenses
          3. See Total Spending
          4. See Spending By Category
          5. Save Expenses To A File
          6. Load Existing Expenses When Program Starts
          7. Click To Close 
          """)
    opt = int(input("Enter The Option: "))
    if opt > 6 or opt<1:
        break
    match opt:
        case 1:
            Today = input("Enter Current Date: ")
            Expenditure = float(input("Enter Amount: "))
            Category = input("Enter Category: ")
            Description = input("Enter A Brief: ")
            data = {
                "today" : Today,
                "expenditure" : Expenditure,
                "category" : Category,
                "desc" : Description
            } 
            if os.path.exists(data_path):
                with open(data_path, "r") as f:
                    try :
                        extract_data = json.load(f)
                    except:
                        extract_data = []
            else:
                extract_data = []
                
            extract_data.append(data) 
            
            with open(data_path, "w") as f:
                json.dump(extract_data, f , indent=4)
        case 2:
            if os.path.exists(data_path):
                with open(data_path, "r") as f:
                    try:
                        extract_data = json.load(f)
                    except:
                        extract_data = []
                print("Expenses: ")
                for i in extract_data:
                    print("------------------------------------")
                    print(f'Category: {i['category']}')  
                    print(f'Expenditure: {i['expenditure']}') 
                    print(f'Description: {i['desc']}')
                    print(f'Date: {i['today']}') 
            else:
                print("No Data Found")     
        case 3:
            if os.path.exists(data_path):
                with open(data_path, "r") as f:
                    try:
                        extract_data = json.load(f)
                    except:
                        extract_data = []
                total_exp = 0
                for i in extract_data:
                    total_exp += i['expenditure']
                print("Total Expenditure: ", total_exp)
            else:
                print("No Data Found") 
        case 4:
            if os.path.exists(data_path):
                with open(data_path, "r") as f:
                    try:
                        extract_data = json.load(f)
                    except:
                        extract_data = []
                while(True):
                    ctgry = input("Enter Category(If You Want To Continue Enter Category Else Enter 'No' For List): ")
                    if ctgry.lower() == "no":
                        break
                    total_exp = 0
                    for i in extract_data:
                        if ctgry.lower() == i['category'].lower():
                            total_exp += i['expenditure']
                    print("Total Expenditure:", total_exp)
            else:
                print("No Data Found") 
        case 5:
            if os.path.exists(data_path):
                with open(data_path, "r") as f:
                    try:
                        extract_data = json.load(f)
                    except:
                        extract_data = []
                with open(data_path, 'w') as f:
                    json.dump(extract_data, f, indent = 3)
                print("Saved Successfully...")
            else:
                print("Data Not Found")
        case 6:
            if os.path.exists(data_path):
                with open(data_path, "r") as f:
                    try:
                        extract_data = json.load(f)
                    except:
                        extract_data = []
                print("Loaded Expenses File: ", extract_data)
            else:
                load()
                with open(data_path, 'w') as f:
                    json.dump([], f, indent = 3)

        