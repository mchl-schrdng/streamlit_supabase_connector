from streamlit.connections import ExperimentalBaseConnection
from supabase import create_client

class SupabaseConnection(ExperimentalBaseConnection):
    def _connect(self, **kwargs):
        # Initialize the Supabase client using secrets.
        url = st.secrets["SUPABASE"]["URL"]
        api_key = st.secrets["SUPABASE"]["API_KEY"]
        self._instance = create_client(url, api_key)

    def fetch_data(self, table_name):
        # Fetch all data from the specified table in Supabase.
        response = self._instance.table(table_name).select("*").execute()
        return response.data

    def insert_data(self, table_name, values):
        # Insert data into the specified table in Supabase.
        response = self._instance.table(table_name).insert(values).execute()
        return response.data
