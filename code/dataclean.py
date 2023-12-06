import pandas as pd
import csv
import os


in_path = os.path.join("data", "Austin_Hotel_Reviews_with_latitudelongitude_.csv")
out_dir = "artifacts"
output_path = os.path.join(out_dir, "cleaned_hotel_data.csv")

def clean_data(in_path, output_path):
    """reomve reduntant columns from csv"""
    df1 = pd.read_csv(in_path)

    df_columns_cut_off = df1.drop(['query', 'review_pagination_id','author_link', 'author_image','review_img_url','review_img_urls','review_photo_ids','owner_answer_timestamp_datetime_utc','review_link','review_datetime_utc','reviews_id','review_questions_Rooms','review_questions_Service','review_questions_Location','review_questions','review_questions_Trip type','review_questions_Travel group','review_questions_Hotel highlights','review_questions_Safety','review_questions_Noteworthy details','review_questions_None','review_questions_Nearby activities','review_questions_Safety','review_questions_Walkability','review_questions_Food & drinks','review_questions_Wi-fi'],axis=1)

    df_columns_cut_off['Google Reviews'] = df_columns_cut_off['review_text']

    df = df_columns_cut_off
    df.to_csv(output_path, index=False, mode ="w")
if __name__ == "__main__":
    clean_data(in_path, output_path)