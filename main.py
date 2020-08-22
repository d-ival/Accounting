from Application import salary
from db import people
from datetime import datetime

def run():
    #utcnow = datetime.utcnow()
    #print(utcnow)
    
    print(datetime.today())
    employees = people.get_employees()
    salary.calculate_salary()

if __name__ == '__main__':
    run()