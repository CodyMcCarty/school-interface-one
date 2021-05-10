# person.py
import csv
import os

class Person:
    
    @classmethod
    def load_ppl_from_csv(cls, file_name):
        # my_file_name = "..\data\students.csv"
        my_path = os.path.abspath(os.path.dirname(__file__))
        my_full_path = os.path.join(my_path, file_name)

        ppl_list = []

        with open(my_full_path, 'r') as csv_file:
            ppl_data = csv.DictReader(csv_file)
            for ppl_info in ppl_data:
                ppl_list.append(cls(**ppl_info))

        return ppl_list
    
    def __init__(self, name, age, password, role):
        self.name = name 
        self.age = age         
        self.password = password
        self.role = role

    def __str__(self):
        return f"{self.name}"




    