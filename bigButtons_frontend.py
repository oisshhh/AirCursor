import streamlit as st

# App layout config
st.set_page_config(page_title="Railway Ticket Booking", layout="wide")

# Global CSS for station/passenger/confirmation buttons
st.markdown("""
    <style>
        div.stButton > button {
            height: 110px !important;
            font-size: 16px !important;
            font-weight: bold;
            margin: 6px 0;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 1
if 'zone' not in st.session_state:
    st.session_state.zone = None
if 'station' not in st.session_state:
    st.session_state.station = None
if 'passengers' not in st.session_state:
    st.session_state.passengers = 1

# Station data
stations = {
    "North": ["BIDHANNAGAR", "DUMDUM", "BIRATI", "BARASAT", "BARRACKPORE","PALTA"],
    "South": ["BUDGE BUDGE", "AKRA","MAJERHAT", "TALLYGUNGE", "PARK CIRCUS","SEALDHA"]
}

# Helper functions
def go_to_page(n):
    st.session_state.page = n

def reset_all():
    st.session_state.page = 1
    st.session_state.zone = None
    st.session_state.station = None
    st.session_state.passengers = 1

# -------------------- PAGE 1 --------------------
if st.session_state.page == 1:
    st.title("🚆 Railway Ticket Booking")
    st.markdown("### Choose a zone:")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("## 🧭 North Zone")
        if st.button("Click for North Zone", key="zone_north_btn", use_container_width=True):
            st.session_state.zone = "North"
            go_to_page(2)
            st.rerun()

    with col2:
        st.markdown("## 🧭 South Zone")
        if st.button("Click for South Zone", key="zone_south_btn", use_container_width=True):
            st.session_state.zone = "South"
            go_to_page(2)
            st.rerun()

# -------------------- PAGE 2 --------------------
elif st.session_state.page == 2:
    zone = st.session_state.zone
    st.title(f"📍 Select a Station in {zone} Zone")
    st.markdown("### Click on one of the stations:")

    station_list = stations[zone]
    cols_per_row = 3

    for i in range(0, len(station_list), cols_per_row):
        cols = st.columns(cols_per_row)
        for j in range(cols_per_row):
            if i + j < len(station_list):
                station = station_list[i + j]
                with cols[j]:
                    if st.button(f"Select {station}", use_container_width=True):
                        st.session_state.station = station
                        go_to_page(3)
                        st.rerun()

    if st.button("⬅️ Back to Zone Selection", use_container_width=True):
        go_to_page(1)
        st.rerun()

# -------------------- PAGE 3 --------------------
elif st.session_state.page == 3:
    st.title("🧍 Select Number of Passengers")

    st.markdown(f"Zone:{st.session_state.zone}   Station:{st.session_state.station}")
    rows = 2
    cols_per_row = 3

    for row in range(rows):
        cols = st.columns(cols_per_row, gap="medium")
        for col_index in range(cols_per_row):
            passenger_num = row * cols_per_row + col_index + 1
            if cols[col_index].button(str(passenger_num), key=f"passenger_{passenger_num}", use_container_width=True):
                st.session_state.passengers = passenger_num
                st.session_state.page = 4
                st.rerun()
    if st.button("⬅️ Back to Station Selection", use_container_width=True):
        go_to_page(2)
        st.rerun()

# -------------------- PAGE 4 --------------------
elif st.session_state.page == 4:
    st.title("Are you sure you want to confirm your booking?")

    st.markdown(f"**Zone:** {st.session_state.zone}")
    st.markdown(f"**Station:** {st.session_state.station}")
    st.markdown(f"**Passengers:** {st.session_state.passengers}")

    confirm_click = st.button("✅ YES - Confirm", use_container_width=True)
    cancel_click = st.button("❌ NO - Go Back to Passenger Selection", use_container_width=True)

    if confirm_click:
        st.session_state.page = 5
        st.rerun()

    if cancel_click:
        st.session_state.page = 3
        st.rerun()

# -------------------- PAGE 5 --------------------
elif st.session_state.page == 5:
    st.title("🎉 Thank You for Booking!")

    st.success(
        f"Your ticket from **{st.session_state.station}** in **{st.session_state.zone} Zone** "
        f"for **{st.session_state.passengers} passenger(s)** has been confirmed."
    )

    st.balloons()

    if st.button("🔁 Book Another Ticket", use_container_width=True):
        reset_all()
        st.rerun()
