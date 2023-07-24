from streamlit.connections import ExperimentalBaseConnection
from supabase import create_client

class SupabaseConnection(ExperimentalBaseConnection):
    def __init__(self, **kwargs):
        # Initialize Supabase client using secrets
        url = st.secrets["SUPABASE"]["URL"]
        api_key = st.secrets["SUPABASE"]["API_KEY"]
        self._instance = create_client(url, api_key)

    def fetch_data(self, table_name, selected_columns="*"):
        query = self._instance.table(table_name).select(selected_columns)
        response = query.execute()
        return response.data

    def insert_data(self, table_name, data):
        response = self._instance.table(table_name).insert(data).execute()
        return response.data
