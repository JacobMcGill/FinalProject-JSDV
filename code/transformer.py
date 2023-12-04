# Need to install "pip install sentence-transformers"
import os
from sentence_transformers import SentenceTransformer, util
import pandas as pd

in_path = os.path.join("data", "Outscraper_Austin_hotel_reviews.csv")
out_dir = "artifacts"
output_path = os.path.join(out_dir, "embedded_hotel_data.csv")

def dataframe(path):
    "Reads in hotel data as a dataframe"
    hotel_df = pd.read_csv(path)
    return hotel_df
def review_embed(df):
    "Embeds reviews and adds them as a column in Dataframe"
    model_name = 'all-MiniLM-L6-v2'
    model = SentenceTransformer(model_name)
    df["review_text"] = df["review_text"].astype(str)
    review_embeddings = model.encode(df["review_text"].tolist())
    embeddings_df = pd.DataFrame(review_embeddings, columns=[f'embedding_{i+1}' for i in range(review_embeddings.shape[1])])
    df = pd.concat([df, embeddings_df], axis=1)
    return df
def print_data_csv(df):
    "Takes embedded data and associated info and prints it as a csv"
    df.to_csv(output_path, index=False)
if __name__ == "__main__":
    hotel_data = dataframe(in_path)
    embedded_reviews = review_embed(hotel_data)
    print_data_csv(embedded_reviews)