# Second project in my 200 python project series
#  USER-FRIENDLY ONLINE ELECTRONIC SHOP USING OBJECT ORIENTED PROGRAMMING
import pandas as pd
import numpy as np


class Items():
    def __init__(self, brand, model, condition):
        self.brand = brand
        self.model = model
        self.condition = condition

    def brands(self):
        print("The following brands are available")
        data = {
            'BRAND': ['Vitron', 'Ampex', 'Sony', 'Sayona'],
            'QUANTITY': [2, 4, 2, 5]
        }
        brands = np.DataFrame(data)
        print(brands)

    def models(self):
        print("The following models are available")
        data = {
            'MODEL': ['2010', '2013', '2020', '2022'],
            'QUANTITY': [3, 10, 4, 9]
        }
        models = np.DataFrame(data)
        print(models)

    def condition_of_electronic(self):
        print("Enter 1 for new item and 2 for used item")
        customer_want = input("New item or Used item?")
        if customer_want == 1:
            data = {
                'BRAND': [],
                'CONDITION': []
            }

            conditions_1 = np.DataFrame(data)
            print(conditions_1)
# customer_need = Items()
customer_details = []
print('WELCOME TO TOPHER ELECTRONICS')
name_of_customer = input('What is your name?  ')
customer_id_no = int(input('Enter your Id Number:  '))
customer_phone = int(input('Enter your phone number:  '))
customer_details.append(name_of_customer)
customer_details.append(customer_id_no)
customer_details.append(customer_phone)
customer_data = {
    'Name': [customer_details[0]],
    'ID NUMBER': [customer_details[1]],
    'PHONE NUMBER': [customer_details[2]]

}
customer_data1 = pd.DataFrame(customer_data)
print('These are your personal details')
print(customer_data1)
decision = int(input('Confirm your details: Enter 1 if they are correct or 2 if they are wrong'))
if decision == 1:
   print('choose the your preferred model, brand and condition of your electronic')
else:
    print('Kindly re-enter your information correctly')
    name_of_customer = input('What is your name?  ')
    customer_id_no = int(input('Enter your Id Number:  '))
    customer_phone = int(input('Enter your phone number:  '))
    customer_details.append(name_of_customer)
    customer_details.append(customer_id_no)
    customer_details.append(customer_phone)
    customer_data = {
        'Name': [customer_details[0]],
        'ID NUMBER': [customer_details[1]],
        'PHONE NUMBER': [customer_details[2]]

    }
    # print the brands, models and condition of the electronics

