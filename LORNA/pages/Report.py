import streamlit as st

st.title('REPORT INCIDENT.')

# Text input
name = st.text_input("Enter your name:")

Report_date_time =st.date_input("Enter the date")

# Number input
county = st.selectbox("Enter your County:", [
        "Baringo",
        "Bomet", 
        "Bungoma",
        "Busia",
        "Elgeyo Marakwet",
        "Embu",
        "Garissa",
        "Homa Bay",
        "Isiolo",
        "Kajiado",
        "Kakamega",
        "Kericho",
        "Kiambu",
        "Kilifi",
        "Kirinyaga",
        "Kisii",
        "Kisumu",
        "Kitui",
        "Kwale",
        "Laikipia",
        "Lamu",
        "Machakos",
        "Makueni",
        "Mandera",
        "Marsabit",
        "Meru",
        "Migori",
        "Mombasa",
        "Murang'a",
        "Nairobi",
        "Nakuru",
        "Nandi",
        "Narok",
        "Nyamira",
        "Nyandarua",
        "Nyeri",
        "Samburu",
        "Siaya",
        "Taita Taveta",
        "Tana River",
        "Tharaka Nithi",
        "Trans Nzoia",
        "Turkana",
        "Uasin Gishu"
        "Vihiga",
        "Wajir",
        "",
])


region = st.selectbox("Enter your region:", [
    'Coast',
    'Central',
    'Lower Eastern',
    'North Eastern',
    'North Rift',
    'South Rift',
    'Upper Eastern',
    'West Kenya',
    'Nairobi',
] )

Address_location = st.text_input("Enter your Location:")

# Dropdown menu
gender = st.selectbox("Select your gender:", ["Male", "Female", "Other"])

# Checkbox

Type_of_attack = st.selectbox("Select the type of cyber crime attack:", [
    "Financial Fraud (Mpesa online banking)", 
    "Botnets (attacker has access to a device and its connection)", 
    "Phishing (fraudulent messages)", 
    "Malware (malicious software)", 
    "Spams (unwanted unsolicited digital communication sent out in bulk)"
])


# Submit button
if st.button("Submit"):
    # Display the form data
    st.write(f"Your name is {name}.")
    st.write(f"Reporting time at {Report_date_time}.")
    st.write(f"You are from {county}.")
    st.write(f"You are from {region}.")
    st.write(f"Your at {Address_location}.")
    st.write(f"Your gender is {gender}.")
    st.write(f"Your crime attack report is {Type_of_attack}.")
    
