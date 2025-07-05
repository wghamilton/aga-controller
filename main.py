import streamlit as st
from datetime import datetime, timedelta
import pytz

def main():
    st.title("Timer for Target Date and Time")

    # Set timezone to Europe/London
    tz = pytz.timezone('Europe/London')

    # User inputs
    target_date = st.date_input("Select target date")
    target_time = st.time_input("Select target time")

    # Combine date and time and localize
    target_dt = datetime.combine(target_date, target_time)
    target_dt = tz.localize(target_dt)

    # Current time
    now = datetime.now(tz)

    # Calculate time delta
    delta = target_dt - now
    days = delta.days
    hours = delta.seconds // 3600

    # Calculate 6-hour offset
    offset_dt = target_dt - timedelta(hours=6)
    delta_offset = offset_dt - now
    days_offset = delta_offset.days
    hours_offset = delta_offset.seconds // 3600

    # Display results
    if delta.total_seconds() >= 0:
        st.success(f"Time until target: {days} days and {hours} hours.")
    else:
        st.error("The target date/time is in the past.")

    if delta_offset.total_seconds() >= 0:
        st.info(f"Time until 6-hour offset: {days_offset} days and {hours_offset} hours.")
    else:
        st.warning("The 6-hour offset time is in the past.")

if __name__ == "__main__":
    main()
