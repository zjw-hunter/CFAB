class bike:
    def __init__(self, color, style):
        self.color = color
        self.style = style
    def __str__(self):
        return("I'm a " + self.color + " " + self.style + " bike")
class car:
    def __init__(self, make, model, mileage):
        self.make = make
        self.model = model
        self.mileage = mileage
    
    def drive(self, miles):
        self.mileage += miles

class library:
    def __init__(self, hours, distance):
        self.hours = hours
        self.distance = distance
    
    def isOpen(self, day, time):
        if( time >= self.hours[day][0] and time <= self.hours[day][1]):
            return True
        return False

racingBike = bike('red', 'racing')
print(racingBike)

electric = car('tesla', 'x', 0)
print(electric.mileage)
electric.drive(200)
print(electric.mileage)

myLibrary = library({'monday': [10,19], 'tuesday': [10,19], 'wednesday': [10,19], 'thursday': [10,19],
'friday': [10,17], 'saturday': [10,17], 'sunday':[-1,-1]}, 5)
print(myLibrary.isOpen('sunday', 9))