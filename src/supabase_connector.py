from streamlit.connections import ExperimentalBaseConnection
from supabase import create_client

class SupabaseConnection(ExperimentalBaseConnection):
    def __init__(self, **kwargs):
        url = st.secrets["SUPABASE"]["URL"]
        api_key = st.secrets["SUPABASE"]["API_KEY"]
        self._instance = create_client(url, api_key)

    def fetch_data(self, table_name, limit=10, filter_column=None, filter_value=None):
        query = self._instance.table(table_name).select("*").limit(limit)
        
        if filter_column and filter_value:
            query = query.filter(filter_column, "eq", filter_value)
        
        response = query.execute()
        return response.data

    def insert_data(self, table_name, data):
        response = self._instance.table(table_name).insert(data).execute()
        return response.data