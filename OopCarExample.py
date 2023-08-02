class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.engine_started = False

    def start_engine(self):
        if not self.engine_started:
            self.engine_started = True
            print("Engine started.")
        else:
            print("Engine is already running.")

    def stop_engine(self):
        if self.engine_started:
            self.engine_started = False
            print("Engine stopped.")
        else:
            print("Engine is already stopped.")


# Creating instances of Car class
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Accord", 2023)

# Starting and stopping the engine for car1
car1.start_engine()
car1.start_engine()  # This should print "Engine is already running."
car1.stop_engine()

# Starting and stopping the engine for car2
car2.start_engine()
car2.stop_engine()
car2.stop_engine()  # This should print "Engine is already stopped."