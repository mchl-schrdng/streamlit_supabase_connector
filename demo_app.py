import streamlit as st
from src.supabase_connector import SupabaseConnection  # Assuming the class is in supabase_connector.py

def main():
    st.title("Streamlit App with Supabase")

    # Initialize our custom Supabase connection
    conn = st.experimental_connection("supabase_conn", type=SupabaseConnection)

    # Dropdown to select a table
    tables = ["crypto_analysis", "table2", "table3"]  # Replace with your actual table names
    selected_table = st.selectbox("Select a table:", tables)

    # Button to fetch data
    if st.button("Fetch Data"):
        data = conn.fetch_data(selected_table)
        st.write(data)

    # For demonstration: Insert sample data
    if st.button("Insert Sample Data"):
        sample_data = {"col1": "value1", "col2": "value2", "col3": "value3"}  # Adjust as per your table schema
        inserted_data = conn.insert_data(selected_table, sample_data)
        st.write("Inserted Data:", inserted_data)

if __name__ == "__main__":
    main()