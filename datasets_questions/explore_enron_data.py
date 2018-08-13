#!/usr/bin/python3

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset_unix.pkl", "rb"))
## Playing with dataset
"""
print(enron_data.keys())
dict_keys(['METTS MARK', 'BAXTER JOHN C', 'ELLIOTT STEVEN', 'CORDES WILLIAM R', 'HANNON KEVIN P',
'MORDAUNT KRISTINA M', 'MEYER ROCKFORD G', 'MCMAHON JEFFREY', 'HAEDICKE MARK E', 'PIPER GREGORY F',
'HUMPHREY GENE E', 'NOLES JAMES L', 'BLACHMAN JEREMY M',.........])

print(enron_data['BAXTER JOHN C'].keys())
dict_keys(['salary', 'to_messages', 'deferral_payments', 'total_payments', 'loan_advances', 'bonus', 'email_address', 
'restricted_stock_deferred', 'deferred_income', 'total_stock_value', 'expenses', 'from_poi_to_this_person', 'exercised_stock_options', 
'from_messages', 'other', 'from_this_person_to_poi', 'poi', 'long_term_incentive', 'shared_receipt_with_poi', 'restricted_stock', 
'director_fees'])


print(enron_data['BAXTER JOHN C'].values())
dict_values([267102, 'NaN', 1295738, 5634343, 'NaN', 1200000, 
'NaN', 'NaN', -1386055, 10623258, 11200, 'NaN', 6680544, 'NaN', 2660303, 'NaN', False, 1586055, 'NaN', 3942714, 'NaN'])


"""
print("Number of people ->", len(enron_data))
l = sum(len(i) for i in enron_data.values())
print("Number of features for a single subject ",l//len(enron_data))
n = 0
for i in enron_data.keys():
	if enron_data[i]["poi"] == 1:
		n = n+1

print("Number of poi's in the dataset is ",n)
print("Total stock value owned by James Prentice is ",enron_data["PRENTICE JAMES"]['total_stock_value'])
print("Total number of email to poi's by Wesley Collwell is ",enron_data["COLWELL WESLEY"]['from_this_person_to_poi'])
print("Total stock options exercised by Jeffrey K Skilling is ",enron_data["SKILLING JEFFREY K"]['exercised_stock_options'])

total_money_skilling,total_money_lay,total_money_fastow = enron_data["SKILLING JEFFREY K"]['total_payments'],enron_data["LAY KENNETH L"]['total_payments'],enron_data["FASTOW ANDREW S"]['total_payments']
print("Total money taken by Jeffrey K Skilling is ",total_money_skilling)
print("Total money taken by Kenneth Lay is ",total_money_lay)
print("Total money taken by Andrew Fastow is ",total_money_fastow)


num_quantifiable_salary = 0
for i in enron_data.keys():
	if type(enron_data[i]["salary"]) == type(1):
		num_quantifiable_salary = num_quantifiable_salary+1

print("Number of quantifiable salaries in the dataset are ",num_quantifiable_salary)

num_known_email = 0
for i in enron_data.keys():
	if enron_data[i]["email_address"] != 'NaN':
		num_known_email = num_known_email+1

print("Number of known email addresses in the dataset are ",num_known_email)

num_of_Nan_in_total_payments = 0
for i in enron_data.keys():
	if type(enron_data[i]["total_payments"]) == type("NaN"):
		num_of_Nan_in_total_payments = num_of_Nan_in_total_payments+1

print("Number of NaN in total_payments are ",num_of_Nan_in_total_payments)
print("And their contribution in the dataset is ",round((num_of_Nan_in_total_payments/len(enron_data.keys()))*100,3),"%")

num_of_poi_with_NaN_total_payments = 0
for i in enron_data.keys():
	if (type(enron_data[i]["total_payments"]) == type("NaN")) and (enron_data[i]["poi"] == True):
		num_of_poi_with_NaN_total_payments = num_of_poi_with_NaN_total_payments+1

print("Number of POIs with total payments as NaN are ",num_of_poi_with_NaN_total_payments)		