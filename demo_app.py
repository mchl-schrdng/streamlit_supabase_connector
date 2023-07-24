# Streamlit for web app interface
import streamlit as st

# Polars for data manipulation and display
import polars as pl

# Custom Supabase connection class
from src.supabase_connector import SupabaseConnection

def main():
    """
    Main function to run the Streamlit app. It provides an interface to select a table,
    choose specific columns, and fetch data from the selected table in Supabase.
    """
    
    # Set the title of the app
    st.title("Streamlit App with Supabase")

    # Initialize the custom Supabase connection
    conn = st.experimental_connection("supabase_conn", type=SupabaseConnection)

    # Dropdown menu to select a table from the available options
    tables = ["crypto_analysis", "customers"]
    selected_table = st.selectbox("Select a table:", tables)

    # Determine available columns based on the selected table
    if selected_table == "crypto_analysis":
        available_columns = ["column1", "column2", "column3"]  # Replace with actual column names
    elif selected_table == "customers":
        available_columns = ["first_name", "last_name"]

    # Multi-select widget for users to choose specific columns
    selected_columns = st.multiselect("Select columns:", available_columns, default=available_columns)

    # Convert the list of selected columns into a comma-separated string
    columns_str = ",".join(selected_columns)

    # Button to fetch and display data from the selected table and columns
    if st.button("Fetch Data from Selected Table"):
        data = conn.fetch_data(selected_table, selected_columns=columns_str)
        if data:
            df = pl.DataFrame(data)
            st.write(df)

# Run the main function when the script is executed
if __name__ == "__main__":
    main()