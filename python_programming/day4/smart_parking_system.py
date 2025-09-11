from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, plateno, name):
        self.__plateno = plateno
        self.__name = name
    def get_plateno(self):
        return self.__plateno
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    @abstractmethod
    def display(self):
        pass
    @abstractmethod
    def calculate_parking_fee(self, hours):
        pass
class Bike(Vehicle):
    def __init__(self,plateno,name,helmet_required):
        super().__init__(plateno,name)
        self.helmet_required = helmet_required
    def display(self):
        print(f"Bike-License:{self.get_plateno()}, Owner: {self.get_name()}, Helmet Required: {self.helmet_required}")
    def calculate_parking_fee(self, h):
        return 20 * h
class Car(Vehicle):
    def __init__(self,plateno,name,seats):
        super().__init__(plateno,name)
        self.seats = seats
    def display(self):
        print(f"Car - License: {self.get_plateno()}, Owner: {self.get_name()}, Seats: {self.seats}")
    def calculate_parking_fee(self, h):
        return 50 * h
class SUV(Vehicle):
    def __init__(self, plate,name, four_wheel_drive):
        super().__init__(plate, name)
        self.four_wheel_drive = four_wheel_drive
    def display(self):
        print(f"SUV - License: {self.get_plateno()}, Owner: {self.get_name()}, 4WD: {self.four_wheel_drive}")
    def calculate_parking_fee(self, hours):
        return 70 * hours
class Truck(Vehicle):
    def __init__(self,plateno,name, max_load_capacity):
        super().__init__(plateno,name)
        self.max_load_capacity = max_load_capacity
    def display(self):
        print(f"Truck - License: {self.get_plateno()}, Owner: {self.get_name()}, Max Load: {self.max_load_capacity} tons")
    def calculate_parking_fee(self, hours):
        return 100 * hours
class ParkingSpot:
    def __init__(self, spot_id, size):
        self.spot_id = spot_id
        self.size = size
        self.__occupied = False
        self.__vehicle = None
    def get_status(self):
        return "Occupied" if self.__occupied else "Available"
    def assign_vehicle(self, vehicle):
        type_map = {
            Bike: ['S', 'M', 'L', 'XL'],
            Car: ['M', 'L', 'XL'],
            SUV: ['L', 'XL'],
            Truck: ['XL']
        }
        for v_type, sizes in type_map.items():
            if isinstance(vehicle , v_type):
                if self.size in sizes:
                    if not self.__occupied:
                        self.__vehicle = vehicle
                        self.__occupied = True
                        print(f"Vehicle {vehicle.get_plateno()} parked in spot {self.spot_id}")
                        return True
                    else:
                        print(f"Spot {self.spot_id} already occupied")
                        return False
        print(f"Vehicle type does not fit spot {self.spot_id}")
        return False
    def remove_vehicle(self):
        if self.__occupied:
            vehicle = self.__vehicle
            self.__vehicle = None
            self.__occupied = False
            print(f"Vehicle {vehicle.get_plateno()} removed from spot {self.spot_id}")
            return vehicle
        else:
            print(f"No vehicle to remove in spot {self.spot_id}")
            return None
    def show_spot(self):
        status = self.get_status()
        print(f"Spot ID: {self.spot_id}, Size: {self.size}, Status: {status}")
class ParkingLot:
    def __init__(self):
        self.spots = []
    def add_spot(self, spot):
        self.spots.append(spot)
    def show_spots(self):
        for spot in self.spots:
            spot.show_spot()
    def park_vehicle(self, vehicle):
        for spot in self.spots:
            if spot.assign_vehicle(vehicle):
                return
        print("No suitable spot available")
    def unpark_vehicle(self, vehicle, hours):
        for spot in self.spots:
            if spot._ParkingSpot__vehicle == vehicle:
                spot.remove_vehicle()
                fee = vehicle.calculate_parking_fee(hours)
                return fee
        print("Vehicle not found in parking lot")
        return 0
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
class CashPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} via Cash")
class CardPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} via Card")
class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} via UPI")
lot = ParkingLot()
lot.add_spot(ParkingSpot(1, 'S'))
lot.add_spot(ParkingSpot(2, 'M'))
lot.add_spot(ParkingSpot(3, 'L'))
lot.add_spot(ParkingSpot(4, 'XL'))
bike = Bike("BIKE123", "Alice", True)
car = Car("CAR456", "Bob", 4)
suv = SUV("SUV789", "Charlie", True)
truck = Truck("TRK101", "Dave", 10)
vehicles = [bike, car, suv, truck]
print("\n--- Display Vehicles ---")
for v in vehicles:
    v.display()
print("\n--- Parking Vehicles ---")
for v in vehicles:
    lot.park_vehicle(v)
print("\n--- Parking Spot Status ---")
lot.show_spots()
print("\n--- Unparking Vehicles and Processing Payment ---")
for v in vehicles:
    hours = int(input(f"Enter parking duration in hours for {v.get_plateno()}: "))
    fee = lot.unpark_vehicle(v, hours)
    print(f"Parking Fee: ₹{fee}")
method = input("Choose payment method (cash/card/upi): ").strip().lower()
if method == 'cash':
    payment = CashPayment()
elif method == 'card':
    payment = CardPayment()
else:
    payment = UPIPayment()
payment.process_payment(fee)
print("\n--- Final Parking Spot Status ---")
lot.show_spots()