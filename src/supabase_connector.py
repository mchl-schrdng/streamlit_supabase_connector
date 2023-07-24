from streamlit.connections import ExperimentalBaseConnection
from supabase import create_client

class SupabaseConnection(ExperimentalBaseConnection):
    def _connect(self, **kwargs):
        url = kwargs.get('url', self._secrets['SUPABASE_URL'])
        api_key = kwargs.get('api_key', self._secrets['SUPABASE_API_KEY'])
        return create_client(url, api_key)

    def fetch_data(self, table_name, columns="*"):
        response = self._instance.table(table_name).select(columns).execute()
        return response.data

    def insert_data(self, table_name, values):
        response = self._instance.table(table_name).insert(values).execute()
        return response.data