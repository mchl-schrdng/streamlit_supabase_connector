from streamlit.connections import ExperimentalBaseConnection
from supabase import create_client
import streamlit as st

class SupabaseConnection(ExperimentalBaseConnection):
    @property
    def _instance(self):
        return getattr(self, "_supabase_client", None)

    @_instance.setter
    def _instance(self, value):
        self._supabase_client = value

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
