from sentence_transformers import SentenceTransformer, util
import pandas as pd
from engine import engine
from sqlalchemy import text

# def sql_query(text):
#     """Takes query, embeds it, and has a sql query that returns the top 5 hotels in similarity"""
#     model_name = 'all-MiniLM-L6-v2'
#     model = SentenceTransformer(model_name)
#     embedded_text = model.encode(text)
#     query = f"""with cosine as (
# 	    select *,
# 	    ST_Distance(embedding, 'POINT({embedded_text})') ::vector(384)
#             <=> embedding as cosine
# 	        from hotel_reviews)
#         select name from cosine 
#         where cosine <0.4
#         order by cosine asc limit 10"""
#     result_df = pd.read_sql_query(text(sql_query), engine)
#     return result_df

def sql_query(question):
    """Takes query, embeds it, and has a SQL query that returns the top 10 hotels in similarity"""
    model_name = 'all-MiniLM-L6-v2'
    model = SentenceTransformer(model_name)
    embedded_text = model.encode(question, convert_to_numpy=True).tolist()
    
    # Convert the PyTorch tensor to a list of float values
    # embedding_values = embedded_text.numpy().tolist()
    
    # Create a comma-separated string of the embedded values
    # embedding_string = ','.join(map(str, embedded_text))

    query = f"""
        with cosine as (
        select *, '{embedded_text}'::vector(384)
        <=> embedding as cosine
        from hotel_reviews)
        select name, cosine from cosine 
        where cosine <0.4
        order by cosine asc limit 10
    """

    result_df = pd.read_sql_query(text(query), engine)
    return result_df

if __name__ == "__main__":
    print(sql_query("hotel with clean beds"))