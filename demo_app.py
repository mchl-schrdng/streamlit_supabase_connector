import streamlit as st
import polars as pl
from src.supabase_connector import SupabaseConnection

def main():
    st.title("Streamlit App with Supabase")

    # Initialize our custom Supabase connection
    conn = st.experimental_connection("supabase_conn", type=SupabaseConnection)

    # Dropdown to select a table
    tables = ["crypto_analysis", "customers"]
    selected_table = st.selectbox("Select a table:", tables)

    # Multi-select for columns
    if selected_table == "crypto_analysis":
        available_columns = ["column1", "column2", "column3"]  # Replace with actual column names
    elif selected_table == "customers":
        available_columns = ["first_name", "last_name"]
    selected_columns = st.multiselect("Select columns:", available_columns, default=available_columns)

    # Convert selected columns to a comma-separated string
    columns_str = ",".join(selected_columns)

    # Fetch Data Button
    if st.button("Fetch Data from Selected Table"):
        data = conn.fetch_data(selected_table, selected_columns=columns_str)
        if data:
            df = pl.DataFrame(data)
            st.write(df)

if __name__ == "__main__":
    main()