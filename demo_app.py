import streamlit as st
import polars as pl
from src.supabase_connector import SupabaseConnection

def main():
    # Create two columns for the logos
    col1, col2 = st.sidebar.columns(2)
    
    # Display the logos in the respective columns
    col1.image("streamlit-logo.png", width=100)
    col2.image("supabase-logo.png", width=100)

    # Sidebar content
    st.sidebar.header("Supabase + Streamlit")

    # Initialize our custom Supabase connection
    conn = st.experimental_connection("supabase_conn", type=SupabaseConnection)

    # Dropdown to select a table in the sidebar
    tables = ["crypto_analysis", "customers"]
    selected_table = st.sidebar.selectbox("Select a table:", tables)

    # Main content area
    st.header(f"Working with table: {selected_table}")

    # If the 'customers' table is selected, show UI for inserting data
    if selected_table == "customers":
        st.subheader("Insert Data into Customers Table")
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")

        if st.button("Insert Data"):
            if first_name and last_name:
                inserted_data = conn.insert_data("customers", {"first_name": first_name, "last_name": last_name})
                st.success("Data inserted successfully!")
            else:
                st.warning("Please fill in both fields before inserting.")

    # Button to fetch data (available for all tables)
    if st.button("Fetch Data"):
        data = conn.fetch_data(selected_table)
        if data:
            df = pl.DataFrame(data)
            st.write(df)

if __name__ == "__main__":
    main()
