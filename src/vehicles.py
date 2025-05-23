class Engine:
    """
    A way of classing engines into diesel or petrol.

    input:
    petrol/deisel
    can use .start() to ignite car
    """

    def __init__(self, tp):
        if tp == "petrol":
            self.type = "Petrol"

        elif tp == "diesel":
            self.type = "Diesel"

        else:
            raise Exception("Incorrect fuel source")
        
    def start(self):
        print(f"{self.type} engine starting...")


class Transmission:
    """
    Describes the transmission type and gear number
    
    input:
    manual/auto and number of gears
    """
    def __init__(self, typ, ngears = 1):
        if typ not in ("manual", "automatic"):
            raise Exception("not a valid transmission")
        
        else:
            self._type = typ
        
        self.gmax = ngears
        self._gear = 0

    def gear(self):
        return self._gear
    
    def type(self):
        return self._type

    def shift_up(self):
        if self._type != "manual":
            raise Exception("Cannot manually shift gears")
        
        if self._gear >= self.gmax:
            pass
        
        else:
            self._gear += 1
    
    def shift_down(self):
        if self._type != "manual":
            raise Exception("Cannot manually shift gears")

        if self._gear == 0:
            pass
        
        else:
            self._gear -= 1



class Car:
    """
    Describes a car.

    input:
    petrol/diesel engine
    """
    def __init__(self, engine, transmission):
        if isinstance(engine, Engine) == True and isinstance(transmission, Transmission) == True:
            self.engine = engine
            self.transmission = transmission
        else:
            raise Exception("Incorrect inputs")

    def shift_up(self):
        return self.transmission.shift_up()
    
    def shift_down(self):
        return self.transmission.shift_down()
        
    def start(self):
        if self.transmission.type() == "manual" and self.transmission.gear() != 0:
            raise Exception("It is unsafe to start the car while in gear")
        
        self.engine.start()
        print("Car started.")


aut = Transmission("automatic", ngears=3)
trn = Transmission("manual", ngears=1)
engine = Engine("petrol")
engine.start()
print(engine.start())
cart = Car(engine=engine, transmission=trn)

cart.start()
