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

    # If the 'customers' table is selected, show UI for inserting data
    if selected_table == "customers":
        st.subheader("Insert Data into Customers Table")
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")

        if st.button("Insert Data"):
            if first_name and last_name:
                # Insert data into the 'customers' table
                inserted_data = conn.insert_data("customers", {"first_name": first_name, "last_name": last_name})
                st.success("Data inserted successfully!")
            else:
                st.warning("Please fill in both fields before inserting.")

    # Button to fetch data (available for all tables)
    if st.button("Fetch Data from Selected Table"):
        data = conn.fetch_data(selected_table)
        if data:
            df = pl.DataFrame(data)
            st.write(df)

if __name__ == "__main__":
    main()