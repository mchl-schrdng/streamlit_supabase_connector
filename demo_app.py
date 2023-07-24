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

    # Custom Query Parameters
    st.subheader("Custom Query Parameters")
    limit = st.number_input("Limit (number of rows)", min_value=1, max_value=1000, value=10)
    
    # Assuming you want to filter the 'customers' table by 'first_name' for demonstration
    if selected_table == "customers":
        filter_column = st.selectbox("Filter Column", ["first_name", "last_name"])
        filter_value = st.text_input(f"Value for {filter_column}")

    # Fetch Data Button
    if st.button("Fetch Data from Selected Table"):
        data = conn.fetch_data(selected_table, limit=limit, filter_column=filter_column, filter_value=filter_value)
        if data:
            df = pl.DataFrame(data)
            st.write(df)

if __name__ == "__main__":
    main()