import streamlit as st
import time
from models import Room

room = Room("Living Room")

st.title("🏠 Smart Home Digital Twin")
placeholder = st.empty()

lock_button = st.button("Lock Door", key="lock")
heater_button = st.button("Toggle Heater", key="heater")
ac_button = st.button("Toggle AC", key="ac")
lights_button = st.button("Toggle Lights", key="lights")

while True: 
    room.update()
    with placeholder.container():
        st.metric("Room Temp", f"{room.temperature:.1f} °C")
        st.text(f"Heater is {'ON' if room.heater_on else 'OFF'}")
        st.text(f"AC is {'ON' if room.ac_on else 'OFF'}")
        st.text(f"Light is {'ON' if room.lights_on else 'OFF'}")
        st.text(f"Door is {'LOCKED' if room.door_status == 'locked' else 'UNLOCKED'}")

        if lock_button:
            room.lock_door()
        if heater_button:
            room.toggle_heater()
        if ac_button:
            room.toggle_ac()
        if lights_button:
            room.toggle_lights()

    time.sleep(1)