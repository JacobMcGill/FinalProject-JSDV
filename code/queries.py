from sentence_transformers import SentenceTransformer, util
import pandas as pd
from engine import engine
from sqlalchemy import text


def sql_query(question):
    """Takes query, embeds it, and has a SQL query that returns the top 10 hotels in similarity and returns the result as a dataframe"""
    model_name = 'all-MiniLM-L6-v2'
    model = SentenceTransformer(model_name)
    embedded_text = model.encode(question, convert_to_numpy=True).tolist()
    

    query = f"""
        with cosine as (
        select *, '{embedded_text}'::vector(384)
        <=> embedding as cosine
        from hotel_reviews)
        select name, cosine from cosine 
        where cosine <0.3
        order by cosine asc limit 3
    """

    result_df = pd.read_sql_query(text(query), engine)
    
    return result_df

if __name__ == "__main__":
    print(sql_query("hotel with clean beds"))