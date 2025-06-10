import streamlit as st
import time
from models import Room
import asyncio
from streamlit_autorefresh import st_autorefresh

def add_room(name):
    if name not in st.session_state:
        st.session_state.room = Room(name)
        
    room = st.session_state.room

    st.title(f"🏠 {name} Home Digital Twin")
    st_autorefresh(interval=1000, key=f"{name}_data_refresh")

    # Device control buttons
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button(f"Toggle {name} Heater"):
            room.toggle_heater()
    with col2:
        if st.button(f"Toggle {name} AC"):
            room.toggle_ac()
    with col3:
        if st.button(f"Toggle {name} Lights"):
            room.toggle_lights()
    with col4:
        if st.button(f"Lock/Unlock {name} Door"):
            if room.door_status == "locked":
                room.unlock_door()
            else:
                room.lock_door()

    room.update()

    # Display current status
    st.metric(f"{name} Temp", f"{room.temperature:.1f} °C")
    st.write(f"Heater: {'ON' if room.heater_on else 'OFF'}")
    st.write(f"Auto Temp: {'ON' if room.auto_temp else 'OFF'}")
    st.write(f"AC: {'ON' if room.ac_on else 'OFF'}")
    st.write(f"Light: {'ON' if room.lights_on else 'OFF'}")
    st.write(f"Door: {'UNLOCKED' if room.door_status == 'unlocked' else 'LOCKED'}")


living_room = add_room("Living Room")
bedroom = add_room("Bedroom")
bathroom = add_room("Bathroom")