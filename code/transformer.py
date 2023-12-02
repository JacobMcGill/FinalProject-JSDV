# Need to install "pip install sentence-transformers"
import os
from sentence_transformers import SentenceTransformer, util
import pandas as pd

in_path = os.path.join("data", "Outscraper.csv")
out_dir = "artifacts"
output_path = os.path.join(out_dir, "embedded_data")

def embed_model():
    "Model to embed hotel review data"
    model_name = 'paraphrase-MiniLM-L6-v2'
    model = SentenceTransformer(model_name)
def dataframe(path):
    "Reads in hotel data as a dataframe"
    hotel_df = pd.read_csv(path)
    return hotel_df
def review_embed(df):
    "Embeds reviews and adds them as a column in Dataframe"
    review_embeddings = model.encode(df["snippet"].tolist())
    for i in range(reviews_embeddings.shape[1]):
        df[f'embedding_{i+1}'] = reviews_embeddings[:, i]
    return review_embeddings