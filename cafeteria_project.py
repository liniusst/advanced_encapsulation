# reservation:
# check if table reserved ( ask for name)
# if not assign a table ( let choose from single, double or family tables )
# implement a function that shows how many free tables and reserved tables there are( tell size of free tables)
# make a function that shows Name/Surname/Time Reserved after reserved table id is given if user want to see# ordering:
# make a function that lets customer choose anything he wishes from menus
# Give customer options to change the order before payment( delete, add,update amount )
# after ordering is finished show full cost of the order and approx waiting time# add an option to add tips(% from full cost)
# payment:
# implement payment
# Log the receipt using loggin

from typing import List

class Main:
    def greetings(self):
        print("Hello, nice to see you here.")
    
    def get_visitor_name(self):
        self.visitor_name = input("Whats your name: ")
        return self.visitor_name
    
    def get_reservations(self, reservations: List[str]):
        self.reservations = reservations
        return self.reservations
    
    def get_seats(self):
        self.seats = input("Enter seats: ")
        return self.seats
    
class Tables(Main):
    def __init__(self, table_type: str, table_id: int, table_seats: int, reserved_by: str, reserved_time: str) -> None:
        self.table_type = table_type
        self.table_id = table_id
        self.table_seats = table_seats
        self.reserved_by = reserved_by
        self.reserved_time = reserved_time

class Reservation(Tables):
    def __init__(self) -> None:
        self._reservation_status = None
        self._tables = [
            Tables("Single", 1, 2, 'Linas Stonkus', '19:20'),
            Tables("Single", 2, 2, None),
            Tables("Double", 3, 4, 'Toma', '20:00'),
            Tables("Double", 4, 4, None),
            Tables("Family", 5, 6, None),
            Tables("Family", 6, 6, None)
        ]
        self._reservations = []

    def get_reservation_status(self):
        if self.visitor_name in self.reservations:
            self._reservation_status = True
        else:
            self._reservation_status = False
        return self._reservation_status
    
    def assign_table(self):
        if self.get_reservation_status() == False:
            self.reserved_by = self.visitor_name
            self.table_seats = self.get_seats()
            self._reservations.append(self.visitor_name)
            print(self._reservations)
        else:
            print('turi rezerva')

    def get_free_tables(self):
        pass

    def get_table_status(self):
        if self.reserved_by != None:
            return f"Table {self.table_id} [{self.table_type} - {self.table_seats} ppl] - reserved by {self.reserved_by}"
        else:
            return f"Table {self.table_id} [{self.table_type} - {self.table_seats} ppl] - free"


reservation_db = ['Linas', 'Toma']


visit = Reservation()
visit.greetings()
visit.get_visitor_name()
visit.get_reservations(reservation_db)
visit.assign_table()
visit.get_free_tables()


# visit.status()
# visit.get_table_status()


