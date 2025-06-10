import random

class Room:
    def __init__(self, name):
        self.name = name
        self.temperature = 22.0  # default
        self.heater_on = False
        self.ac_on = False
        self.lights_on = False
        self.door_status = "locked"

    def update(self):
        # Random fluctuation
        self.temperature += random.uniform(-0.5, 0.5)

        # Simple behavior: turn heater on if temp < 20
        if self.temperature < 20:
            self.heater_on = True
            self.temperature += 0.3  # heater effect
        elif self.temperature > 26:
            self.ac_on = True #AC effect
        else:
            self.heater_on = False
            self.ac_on = False

    def toggle_lights(self):
        #turn on if off and off if on
        self.lights_on = not self.lights_on

    def lock_door(self):
        self.door_status = "locked"

    def unlock_door(self):
        self.door_status = "unlocked"

    def toggle_ac(self):
        self.heater_on = False
        self.ac_on = not self.ac_on
    def toggle_heater(self):
        self.ac_on = False
        self.heater_on = not self.heater_on