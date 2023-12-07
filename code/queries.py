import os
import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer, util
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create PostgreSQL engine
DATABASE_USERNAME = os.environ["DATABASE_USERNAME"]
DATABASE_PASSWORD = os.environ["DATABASE_PASSWORD"]
DATABASE_HOST = os.environ["DATABASE_HOST"]
DATABASE_PORT = os.environ["DATABASE_PORT"]
DATABASE_DATABASE = os.environ["DATABASE_DATABASE"]

SQLALCHEMY_DATABASE_URL = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_DATABASE}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

def sql_query(question):
    """Takes a query, embeds it, and executes a SQL query to return the result as a DataFrame."""
    model_name = 'all-MiniLM-L6-v2'
    model = SentenceTransformer(model_name)
    embedded_text = model.encode(question, convert_to_numpy=True).tolist()

    query = f"""
        WITH cosine AS (
            SELECT *, '{embedded_text}'::vector(384) <=> embedding AS cosine
            FROM hotel_reviews
        )
        SELECT name, rating, zip_code, cosine FROM cosine , location_link
        WHERE cosine < 0.3
        ORDER BY cosine ASC
        LIMIT 3
    """

    result_df = pd.read_sql_query(text(query), engine)
    return result_df

def main():
    st.title("Hotel Reviews Similarity Search")

    # Input SQL query from the user
    query = st.text_area("Enter your SQL query:")

    if st.button("Run Query"):
        if query:
            # Execute the SQL query and display the result
            result = sql_query(query)
            st.table(result)
        else:
            st.warning("Please enter an SQL query.")

if __name__ == "__main__":
    main()