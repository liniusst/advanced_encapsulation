import random

reservations_db = ['Linas Stonkus']
visitors = {
    'full_name': None,
    'seats': None
}

tables = {'seats': {

}
}

class PersonsData:
    def __init__(self) -> None:
        self.visitor_name = None
        self.reservation_status = None

    def greetings(self):
        print("Hello Sir! What is your full name?")
        self.visitor_name = input("Enter your full name: ")
        return self.visitor_name

    def get_assign_status(self):
        if self.visitor_name in reservations_db:
            print(f"Hi, {self.visitor_name}, thank you for reservation before.")
            self.reservation_status = True
        else:
            print(f"Nice to see you here {self.visitor_name}")
            visitors['full_name'] = self.visitor_name
            self.reservation_status = False
        return self.reservation_status

    def tables_status(self):
        table_number =  random.randint(1,10)
        if self.reservation_status:
            print(f"Your reservated table number is: {table_number}")
        else:
            print("How many sits you need?")
            visitors['seats'] = input("Seats: ")
            
    def check_table_status(self):
        pass
            

visit = PersonsData()
visit.greetings()
visit.get_assign_status()
visit.tables_status()
print(visitors)