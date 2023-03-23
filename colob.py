import timeimport logging
import logging.config

logging.config.fileConfig(fname="logging.conf", disable_existing_loggers=False)
# Get the logger specified in the filelogger = logging.getLogger("sLogger")
class Carrier:
    """Shuttle cost in USD, weight in kg, year built in format:YYYY"""    
    def __init__(
        self,
        cost: float,
        year_built: int,
        weight: float,
    ) -> None:
        self._cost: float = cost        self._year_built: int = year_built        self._weight: float = weight    def get_age(self) -> int:
        timestamp = time.time()
        current_year = time.gmtime(timestamp).tm_year        age = current_year - self._year_built        return age    def get_cost(self):
        return self._cost    def get_year_built(self):
        return self._year_built    def get_weight(self):
        return self._weighttest = Carrier(cost=5, year_built=1955, weight=2000)
print(test.get_age())
class SpaceShuttle(Carrier):
    def __init__(self, cost: float, year_built: int, weight: float) -> None:
        super().__init__(cost, year_built, weight)
        self.fuel_cost = None        self.average_personel_exp = None        self.mission_cost = None        self.burn_rate_var = None    CEPAJAV_CONSTANT = 2500    """Imperial units everywhere"""    def _get_burn_rate_variable(self, orbit_height: float) -> float:
        self.burn_rate_var = self.CEPAJAV_CONSTANT / orbit_height        return self.burn_rate_var    def get_fuel_cost(self, fuel_cost: float, burn_rate: float, orbit_height: float):
        burn_rate_variable = self._get_burn_rate_variable(orbit_height)
        self.fuel_cost = fuel_cost * burn_rate * burn_rate_variable        return self.fuel_cost    def get_average_personel_expenses(
        self, base_salary: float, people_count: int    ) -> float:
        self.average_personel_exp = base_salary * people_count        return self.average_personel_exp    def calculate_mission_cost(
        self,
        fuel_cost: float,
        burn_rate: float,
        orbit_height: float,
        base_salary: float,
        people_count: int,
    ) -> float:
        total_fuel_cost = self.get_fuel_cost(fuel_cost, burn_rate, orbit_height)
        average_personel_cost = self.get_average_personel_expenses(
            base_salary, people_count        )
        self.mission_cost = total_fuel_cost + average_personel_cost        return self.mission_cost    def get_full_report(self):
        mission_data = {
            "Shuttle age": self.get_age(),
            "Shuttle cost": self.get_cost(),
            "Shuttle year built": self.get_year_built(),
            "Mission Cost": self.mission_cost,
            "Fuel cost": self.fuel_cost,
            "Burn rate variable": self.burn_rate_var,
            "Average personel expenses": self.average_personel_exp,
        }
        print(mission_data)
my_shuttle = SpaceShuttle(cost=5000, year_built=1979, weight=5000000)
print(
    my_shuttle.calculate_mission_cost(
        fuel_cost=5.5,
        burn_rate=8.7,
        orbit_height=1500,
        base_salary=25000,
        people_count=85,
    )
)
my_shuttle.get_full_report()