from streamlit.connections import ExperimentalBaseConnection
from supabase import create_client

class SupabaseConnection(ExperimentalBaseConnection):
    def _connect(self, **kwargs):
        url = st.secrets["SUPABASE"]["URL"]
        api_key = st.secrets["SUPABASE"]["API_KEY"]
        return create_client(url, api_key)

    def fetch_data(self, table_name):
        response = self._instance.table(table_name).select("*").execute()
        return response.data

    def insert_data(self, table_name, values):
        response = self._instance.table(table_name).insert(values).execute()
        return response.data