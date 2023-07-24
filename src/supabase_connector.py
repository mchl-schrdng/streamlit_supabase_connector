# Streamlit's experimental connection interface
from streamlit.connections import ExperimentalBaseConnection

# Supabase client for database operations
from supabase import create_client

class SupabaseConnection(ExperimentalBaseConnection):
    """
    A custom connection class for Streamlit to interact with Supabase.
    This class provides methods to fetch and insert data into a Supabase database.
    """

    def __init__(self, **kwargs):
        """
        Initializes the Supabase client using credentials from Streamlit secrets.
        """
        # Retrieve Supabase credentials from Streamlit secrets
        url = st.secrets["SUPABASE"]["URL"]
        api_key = st.secrets["SUPABASE"]["API_KEY"]

        # Create a Supabase client instance
        self._instance = create_client(url, api_key)

    def fetch_data(self, table_name, selected_columns="*"):
        """
        Fetches data from a specified table in Supabase.

        Parameters:
        - table_name (str): The name of the table to fetch data from.
        - selected_columns (str, optional): Columns to select in the query. Defaults to "*".

        Returns:
        - list[dict]: List of dictionaries representing rows of data.
        """
        # Construct the query and execute it
        query = self._instance.table(table_name).select(selected_columns)
        response = query.execute()

        # Return the fetched data
        return response.data

    def insert_data(self, table_name, data):
        """
        Inserts data into a specified table in Supabase.

        Parameters:
        - table_name (str): The name of the table to insert data into.
        - data (dict): Data to be inserted.

        Returns:
        - dict: Inserted data.
        """
        # Execute the insert operation
        response = self._instance.table(table_name).insert(data).execute()

        # Return the inserted data
        return response.data