# Need to install "pip install sentence-transformers"
import os
from sentence_transformers import SentenceTransformer, util
import pandas as pd

in_path = os.path.join("data", "Outscraper_Austin_hotel_reviews.csv")
out_dir = "artifacts"
output_path = os.path.join(out_dir, "embedded_data")

# def embed_model():
#     "Model to embed hotel review data"
#     model_name = 'paraphrase-MiniLM-L6-v2'
#     model = SentenceTransformer(model_name)
def dataframe(path):
    "Reads in hotel data as a dataframe"
    hotel_df = pd.read_csv(path)
    return hotel_df
def review_embed(df):
    "Embeds reviews and adds them as a column in Dataframe"
    model_name = 'paraphrase-MiniLM-L6-v2'
    model = SentenceTransformer(model_name)
    review_embeddings = model.encode(df["review_text"].tolist())
    for i in range(reviews_embeddings.shape[1]):
        df[f'embedding_{i+1}'] = reviews_embeddings[:, i]
    return df
if __name__ == "__main__":
    hotel_data = dataframe(in_path)
    embedded_reviews = review_embed(hotel_data)
    print(embedded_reviews)