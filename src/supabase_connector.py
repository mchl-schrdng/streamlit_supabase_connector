import streamlit as st
from streamlit.connections import ExperimentalBaseConnection
from supabase import create_client

class SupabaseConnection(ExperimentalBaseConnection):
    def _connect(self, **kwargs):
        # Fetch secrets from st.secrets
        url = st.secrets["SUPABASE"]["URL"]
        api_key = st.secrets["SUPABASE"]["API_KEY"]
        
        return create_client(url, api_key)

    def fetch_data(self, table_name, columns="*"):
        response = self._instance.table(table_name).select(columns).execute()
        return response.data

    def insert_data(self, table_name, values):
        response = self._instance.table(table_name).insert(values).execute()
        return response.data