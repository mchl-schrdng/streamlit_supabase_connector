import streamlit as st
from src.supabase_connector import SupabaseConnection

def main():
    st.title("Streamlit App with Supabase")

    # Initialize our custom Supabase connection
    conn = st.experimental_connection("supabase_conn", type=SupabaseConnection)

    # Dropdown to select a table
    tables = ["crypto_analysis", "table2", "table3"]
    selected_table = st.selectbox("Select a table:", tables)

    # Multi-select for columns
    all_columns = ["col1", "col2", "col3"]
    selected_columns = st.multiselect("Select columns:", all_columns, default=all_columns)

    # Button to fetch data
    if st.button("Fetch Data"):
        data = conn.fetch_data(selected_table, columns=','.join(selected_columns))
        st.write(data)

    # Insert data (for demonstration purposes)
    if st.button("Insert Sample Data"):
        sample_data = {"col1": "value1", "col2": "value2", "col3": "value3"}
        inserted_data = conn.insert_data(selected_table, sample_data)
        st.write("Inserted Data:", inserted_data)

if __name__ == "__main__":
    main()
