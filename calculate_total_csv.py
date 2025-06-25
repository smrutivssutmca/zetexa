
import csv

input_file = 'user_input.csv'
output_file = 'user_totals.csv'

user_total = {}

try:
    with open(input_file, 'r') as csv_file:
        data = csv.reader(csv_file)
        
        for row in data:
            user_id = data["user_id"]
            amount = data["amount"]
            
            user_total[user_id] += amount
except Exception as e:
    print("Error occoured while reading the file : ", str(e))
        

try:
    with open(output_file, 'w') as csv_file:
        data = csv.writer(csv_file)
        
        data.writerow(['user_id', 'total_amount'])
        
        for user_id, amount in user_total.items():
            data.writerow([user_id, amount])
except Exception as e:
    print("Error occoured while reading the file : ", str(e))
        
    
