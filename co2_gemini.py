from dotenv import load_dotenv
load_dotenv()  # Load environment variables

import streamlit as st
import os
import pymysql as sql
import pandas as pd

import google.generativeai as genai

# Configure GenAI Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to Load Google Gemini Model and Provide Queries as Response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Load environment variables from .env file
load_dotenv()

# MySQL database credentials
host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv('dbc')

# Function to Retrieve Query from MySQL Database
def read_mysql_query(query):
    try:
        # Connect to MySQL database
        conn = sql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        
        # Execute SQL query
        df = pd.read_sql_query(query, conn)
        
        # Close connection
        conn.close()
        
        return df
    
    except Exception as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

# Streamlit App
# st.set_page_config(page_title="Gemini App to Co2_Emission Query MySQL", page_icon="🔍")   
# Set page configuration
st.set_page_config(
    page_title="Gemini CO2 Emissions Analysis", 
    page_icon="🌍", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# st.title("Gemini App to Query Co2_Emission MySQL Database 🚗🌍")      
# Page title and subtitle
st.title("Gemini CO2 Emissions Analysis Dashboard 🚗🌍")
st.markdown("""
Welcome to the **Gemini CO2 Emissions Dashboard**! Use natural language to query vehicle fuel consumption and CO2 emissions data from a MySQL database.

### Features:
- **Natural Language Queries**: Convert plain English questions into SQL queries.
- **Comprehensive Data**: Access detailed vehicle data.
- **Interactive Display**: View and interact with data.

### How to Use:
1. Enter your query below.
2. Click "Ask me" to generate and execute the SQL query.
3. View the results in the table.

Get started now!
""")




prompt = [
    """
You are an expert in converting English questions to SQL queries. The SQL database has a table named `fuelconsumption_modified` and contains the following columns:
1. YEAR (INT): The year of the vehicle model.
2. MAKE (VARCHAR): The manufacturer company of the vehicle.
3. ENGINE_SIZE (FLOAT): The size of the engine in liters.
4. CYLINDERS (FLOAT): The number of cylinders in the engine.
5. FUEL (VARCHAR): The type of fuel used by the vehicle.
6. FUEL_CONSUMPTION (FLOAT): The fuel consumption rate of the vehicle.
7. HWY_L_PER_100KM (FLOAT): The highway fuel consumption rate in liters per 100 kilometers.
8. COMB_L_PER_100KM (FLOAT): The combined fuel consumption rate in liters per 100 kilometers.
9. COMB_MPG (FLOAT): The combined fuel consumption rate in miles per gallon.
10. CO2_EMISSIONS (FLOAT): The carbon dioxide emissions of the vehicle.
11. BROAD_VEHICLE_CLASS (VARCHAR): The broad classification of the vehicle type.
12. TRANSMISSION_GROUP (VARCHAR): The type of transmission used in the vehicle.

Here are some examples of how to convert English questions to SQL queries:

Example 1:
Question: How many vehicles are there in the table?
SQL Query: SELECT COUNT(*) FROM fuelconsumption_modified;

Example 2:
Question: What are the makes and engine sizes of vehicles with an engine size greater than 3.5 liters?
SQL Query: SELECT MAKE, ENGINE_SIZE FROM fuelconsumption_modified WHERE ENGINE_SIZE > 3.5;

Example 3:
Question: Show the details of vehicles with a combined fuel consumption rate (COMB_L_PER_100KM) between 5 and 8 liters per 100 kilometers.
SQL Query: SELECT * FROM fuelconsumption_modified WHERE COMB_L_PER_100KM BETWEEN 5 AND 8;

Example 4:
Question: List the vehicle makes, engine sizes, and CO2 emissions for vehicles with a highway fuel consumption rate (HWY_L_PER_100KM) less than 6 liters per 100 kilometers.
SQL Query: SELECT MAKE, ENGINE_SIZE, CO2_EMISSIONS FROM fuelconsumption_modified WHERE HWY_L_PER_100KM < 6;

Example 5:
Question: Retrieve the years, makes, and transmission groups of vehicles that use diesel fuel.
SQL Query: SELECT YEAR, MAKE, TRANSMISSION_GROUP FROM fuelconsumption_modified WHERE FUEL = 'Diesel';

Please convert the following question into an SQL query. Make sure the SQL query does not contain any backticks or the word "sql" in the output.
"""
]

question = st.text_input("Enter your fuel consumption query:", key="input")
submit = st.button("Ask me")

if submit:
    response = get_gemini_response(question, prompt)
    
    # Clean the response to remove any unwanted characters or words
    sql_query = response.strip().replace("```sql", "").replace("```", "").strip()
    
    print("*" * 60)
    print("Generated SQL Query:")
    print(sql_query)
    print("*" * 60)
    
    # Fetch data from MySQL database based on the generated SQL query
    df = read_mysql_query(sql_query)
    
    if df is not None:
        st.subheader("Query Result:")
        st.dataframe(df)  # Display dataframe in Streamlit app
        
        # Print dataframe info to terminal
        print("Dataframe Info from MySQL:")
        print(df.head())  # Print the first few rows
        print(df.info())  # Print the dataframe info
    else:
        st.warning("No results found for the given query.")
