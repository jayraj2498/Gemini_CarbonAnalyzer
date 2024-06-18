# Gemini CO2 Emissions Analysis Dashboard 🚗🌍

Welcome to the **Gemini CO2 Emissions Analysis Dashboard**! This project uses the power of Google Gemini's language model to convert natural language queries into SQL queries, enabling exploration and analysis of vehicle fuel consumption and CO2 emissions data from a MySQL database.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Libraries and Tools](#libraries-and-tools)
- [Project Structure](#project-structure)
- [Showcase](#showcase)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This dashboard allows users to interact with vehicle emissions data through natural language queries. It translates these queries into SQL commands, retrieves data from a MySQL database, and displays the results interactively.

## Features
- **Natural Language Querying**: Convert English questions into SQL queries.
- **Detailed Vehicle Data**: Access information on vehicle models, fuel consumption, engine sizes, CO2 emissions, and more.
- **Interactive Data Display**: View and interact with data directly within the app.
- **Custom Analysis**: Perform complex queries and obtain tailored insights.

## Installation

### Prerequisites
- Python 3.9+
- MySQL Database
- [Streamlit](https://streamlit.io/)
- [Google Generative AI](https://cloud.google.com/genai) API Key

### Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/gemini-co2-emissions-dashboard.git
    cd gemini-co2-emissions-dashboard
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your environment variables by creating a `.env` file:
    ```env
    GOOGLE_API_KEY=your_google_genai_api_key
    host=your_mysql_host
    user=your_mysql_username
    password=your_mysql_password
    dbc=your_mysql_database_name
    ```

## Usage

### Running the App
To run the Streamlit app, use the following command:
```bash
streamlit run co2_gemini.py
