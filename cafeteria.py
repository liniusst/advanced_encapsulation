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

reservation_db = ['Linas', 'Toma']

class Main:
    def __init__(self, visitor_name: str) -> None:
        self.visitor_name = visitor_name
    
    def get_visitor_name(self):
        return self.visitor_name
    
    def get_seats(self, seats: int):
        return seats
    
    def greetings(self):
        pass

    
class Reservation(Main):
    def check_reservation(self):
        name = input("Enter name: ")
        if name in reservation_db:
            print('yra')
        else:
            print('nera')


test = Reservation()
test.get_visitor_name(name='Linas')
test.check_reservation()