from datetime import date
from storage import save_data, load_data

def add_expense():
    Today = str(date.today())
    try:
        Expenditure = float(input("Enter Amount: "))
        
        if Expenditure < 0:
            Expenditure = float(input("Enter Amount Greater Than 0: "))
    except:
        return "Error: Value Must Be A Number."
        
    Category = input("Enter Category: ").strip()
    if not Category:
        return "Error: Enter Category Value."
    
    Description = input("Enter A Brief: ").strip()
    if not Description:
        return "Error: Enter Description Value."
    
    data = {
        "today" : Today,
        "expenditure" : Expenditure,
        "category" : Category,
        "desc" : Description
    } 
            
    save_data(data)
    return "Added Successfully..."

def view_expenses():
    extract_data = load_data()
    data = {}
    if extract_data:
        return extract_data
    return []

def total_spending():
    extract_data = load_data()
    if extract_data:
        total_exp = 0
        for i in extract_data:
            total_exp += i['expenditure']
        return f'Total Expenditure: {total_exp}'
    return "No Data Found"

def show_category_data():
    extract_data = load_data()
    data = {}
    if extract_data:
        for i in extract_data:
            if i['category'] in data:
                data[i['category']] += i['expenditure']
            else:
                data[i['category']] = i['expenditure']
        return data
    return [] 