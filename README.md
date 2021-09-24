# Python_Geospatial_analysis
Python Streamlit Geospatial analysis 

All python based dependencies can be installed using pip and you also need xampp for running this.

1) created US_Source_states_cities.xlsx manually from below link : https://www.britannica.com/topic/list-of-cities-and-towns-in-the-United-States-2023068#ref326625
2) SignUp and took api key from : https://opencagedata.com
source link : https://amaral.northwestern.edu/blog/getting-long-lat-list-cities
3) Ran get_cord.py to generate respective state-cities latitude and longitude datasets.
4) Took all above datasets and kept in cities folder
5) cd to cities folder and Run combine_xlsx.py to generate all_US_states.xlsx
6) You need xampp running on your windows machine.
7) Run the streamlit run  Streamlit_Geospatial_app.py
