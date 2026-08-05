import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input(label="Place: ")
days = st.slider(
                 label="Forecast Days",
                 min_value=1,
                 max_value=5,
                 help="Select the number of forecasted days."
                )
option = st.selectbox(
                      label="Select data to view",
                      options=("Temperature", "Conditions")
                     )
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(
                             x=dates,
                             y=temperatures,
                             labels={"x": "Date", "y": "Temperature (C)"}
                            )
            st.plotly_chart(figure)

        if option == "Conditions":
            images = {
                      "Clear": "images/clear.png",
                      "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png",
                      "Snow": "images/snow.png"
                     }
            conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_path = [images[condition] for condition in conditions]

            st.image(image_path, width=115)
            
    except KeyError:
        st.write("That place does not exist.")