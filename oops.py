# oops learning

class bulb: #bulb
    def __init__(self,watt,type): # object
        self.watt=watt  
        self.type=type

    def change_type(self,type):
        print("This is method initiation")
        self.type=type


bulb1=bulb(100,"LED")
print(bulb1.watt)
print(bulb1.type)

bulb1.change_type("Filament")
print(bulb1.type)



    


