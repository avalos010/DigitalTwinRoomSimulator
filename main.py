import streamlit as st
import time
from models import Room
import asyncio
from streamlit_autorefresh import st_autorefresh

def create_room(name):
    if name not in st.session_state:
        st.session_state[name] = Room(name)

    room = st.session_state[name]

    st.title(f"🏠 {name} Digital Twin")

    st_autorefresh(interval=1000, key=f"{name}_refresh")

    # Device control buttons
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        if st.button(f"Toggle {name} Heater", disabled=room.auto_temp):
            room.toggle_heater()
    with col2:
        if st.button(f"Toggle {name} AC", disabled=room.auto_temp):
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
    with col5:
        if st.button(f"Toggle {name} Auto Temp"):
            room.toggle_auto_temp()

    room.update()

    # Display current status
    st.metric(f"{name} Temp", f"{room.temperature:.1f} °C")
    st.write(f"Auto Temp: {'ON' if room.auto_temp else 'OFF'}")
    st.write(f"Heater: {'ON' if room.heater_on else 'OFF' }")
    st.write(f"AC: {'ON' if room.ac_on else 'OFF'}")
    st.write(f"Light: {'ON' if room.lights_on else 'OFF'}")
    st.write(f"Door: {'UNLOCKED' if room.door_status == 'unlocked' else 'LOCKED'}")

create_room("Living Room")
create_room("Bedroom")
create_room("Kitchen")