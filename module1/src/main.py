from tracker import add_expense, view_expenses, total_spending, show_category_data
from tabulate import tabulate

while(True):
    print("""
          1. Add An Expense
          2. View All Expenses
          3. See Total Spending
          4. See Spending By Category
          5. Click To Close 
          """)
    opt = int(input("Enter The Option: "))
    if opt > 4 or opt<1:
        break
    match opt:
        case 1:
            resp = add_expense()
            print(resp) 
            
        case 2:
            resp = view_expenses()
            if resp:
                print(tabulate(resp, headers="keys"))
            else:
                print("No Data Yet")
                
        case 3:
            resp = total_spending()
            print(resp) 
        
        case 4:
            resp = show_category_data()
            if resp:
                print(tabulate(resp.items(), headers=['Category', 'Total'], tablefmt="grid"))
            else:
                print("No Data Yet")
            
