import pandas as pd
import csv
import os
import re

df1 = pd.read_csv('data/Austin_Hotel_Reviews_60_x_200.csv')
df2 = pd.read_csv('data/Outscraper_Austin_hotel_reviews_40_hotels_with_zip.csv')
merged_df = pd.concat([df1, df2])

df_columns_cut_off = merged_df.drop(['query', 'review_pagination_id','author_link', 'author_image','review_img_url','review_img_urls','review_photo_ids','owner_answer_timestamp_datetime_utc','review_link','review_datetime_utc','reviews_id','review_questions_Rooms','review_questions_Service','review_questions_Location','review_questions','review_questions_Trip type','review_questions_Travel group','review_questions_Hotel highlights','review_questions_Noteworthy details','review_questions_None','review_questions_Nearby activities','review_questions_Safety','review_questions_Walkability','review_questions_Food & drinks','review_questions_Wi-fi'],axis=1)
