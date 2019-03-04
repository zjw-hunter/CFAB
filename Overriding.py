#Overriding

class bird:
    
    def speak(self):
        print("tweet")

class crow(bird):
    
    def speak(self):
        print("CAW!")

b = bird()
c = crow()

b.speak()
c.speak()