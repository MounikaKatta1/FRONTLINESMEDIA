import os
import json

os.makedirs("../data", exist_ok = True)
data_path = os.path.join("../data", "expenses.json")

def file_exists():
    if not os.path.exists(data_path):
        os.makedirs("../data", exist_ok = True)
        with open(data_path, "w") as f:
            json.dump([], f, indent=3) 
    return True
            
def load_data():
    if file_exists():
        with open(data_path, "r") as f:
            data = json.load(f)
    return data

def save_data(expenses):
    if file_exists():
        extract_data = load_data()
    extract_data.append(expenses)
    
    with open(data_path, "w") as f:
        json.dump(extract_data, f, indent=3)
    return

