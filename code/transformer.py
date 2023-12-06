# Need to install "pip install sentence-transformers"
import os
from sentence_transformers import SentenceTransformer, util
import pandas as pd

dir = "artifacts"
in_path = os.path.join(dir, "cleaned_hotel_data.csv")
output_path_header = os.path.join(dir, "embedded_hotel_data.csv")
output_path_no_header = os.path.join(dir, "sql_embedded_hotel_data.csv")

def dataframe(path):
    "Reads in hotel data as a dataframe and removes some problematic data"
    hotel_df = pd.read_csv(path)
    hotel_df = hotel_df.drop([8081])
    return hotel_df
def review_embed(df):
    "Embeds reviews and adds them as a column in Dataframe"
    model_name = 'all-MiniLM-L6-v2'
    model = SentenceTransformer(model_name)
    df["review_text"] = df["review_text"].astype(str)
    review_embeddings = model.encode(df["review_text"].tolist())
    df['embeddings'] = review_embeddings.tolist()
    # embeddings_df = pd.DataFrame(review_embeddings, columns=[f'embedding_{i+1}' for i in range(review_embeddings.shape[1])])
    # df = pd.concat([df, embeddings_df], axis=1)
    return df
def print_data_csv_header(df):
    "Takes embedded data and associated info and prints it as a csv with a header"
    df.to_csv(output_path_header, index=True, mode = "w")
def print_data_csv_no_header(df):
    "Takes embedded data and associated info and prints it as a csv with no header"
    df.to_csv(output_path_no_header, index=True, header=False, mode = "w")
if __name__ == "__main__":
    hotel_data = dataframe(in_path)
    embedded_reviews = review_embed(hotel_data)
    print_data_csv_header(embedded_reviews)
    print_data_csv_no_header(embedded_reviews)