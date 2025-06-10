import random

class Room:
    def __init__(self, name):
        self.name = name
        self.temperature = 22.0  # default
        self.heater_on = False
        self.ac_on = False
        self.lights_on = False
        self.door_status = "locked"
        self.auto_temp=False

    def update(self):
        # Random fluctuation
        self.temperature += random.uniform(-0.5, 0.5)

        if(self.auto_temp):
        # turn heater on if temp < 20
            if self.temperature < 20:
                self.toggle_heater()  
                self.temperature += 0.3 
            elif self.temperature > 26:
                self.temperature -= 0.3
                self.toggle_ac()
            else:
                self.heater_on = False
                self.ac_on = False

    def toggle_lights(self):
        print('Lights have been toggled', self.lights_on)
        self.lights_on = not self.lights_on

    def lock_door(self):
        self.door_status = "locked"
        print('Door has been locked', self.door_status)


    def unlock_door(self):
        self.door_status = "unlocked"
        print('Door has been unlocked', self.door_status)


    def toggle_ac(self):
        if self.heater_on:
            self.toggle_heater()
        self.heater_on = False
        self.ac_on = not self.ac_on
        print('AC has been toggled', self.ac_on)

    def toggle_heater(self):
        if self.ac_on:
            self.toggle_ac()
        self.heater_on = not self.heater_on
        print('Heater has been toggled', self.heater_on)

    def toggle_auto_temp(self):
        self.auto_temp = not self.auto_temp