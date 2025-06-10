import streamlit as st
import time
from models import Room
import asyncio
from streamlit_autorefresh import st_autorefresh

# Initialize session state for the room
if "room" not in st.session_state:
    st.session_state.room = Room("Living Room")
room = st.session_state.room

st.title("🏠 Smart Home Digital Twin")

st_autorefresh(interval=1000, key="data_refresh")

# Device control buttons
if st.button("Toggle Heater"):
    room.toggle_heater()
if st.button("Toggle AC"):
    room.toggle_ac()
if st.button("Toggle Lights"):
    room.toggle_lights()
if st.button("Lock/Unlock Door"):
    if room.door_status == "locked":
        room.unlock_door()
    else:
        room.lock_door()

room.update()

# Display current status
st.metric("Room Temp", f"{room.temperature:.1f} °C")
st.write(f"Heater: {'ON' if room.heater_on else 'OFF'}")
st.write(f"AC: {'ON' if room.ac_on else 'OFF'}")
st.write(f"Light: {'ON' if room.lights_on else 'OFF'}")
st.write(f"Door: {'UNLOCKED' if room.door_status == 'unlocked' else 'LOCKED'}")