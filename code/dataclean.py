import pandas as pd
import csv
import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#reomve reduntant columns from csv
df1 = pd.read_csv('data/Austin_Hotel_Reviews_with_latitudelongitude_.csv')

df_columns_cut_off = df1.drop(['query', 'review_pagination_id','author_link', 'author_image','review_img_url','review_img_urls','review_photo_ids','owner_answer_timestamp_datetime_utc','review_link','review_datetime_utc','reviews_id','review_questions_Rooms','review_questions_Service','review_questions_Location','review_questions','review_questions_Trip type','review_questions_Travel group','review_questions_Hotel highlights','review_questions_Safety','review_questions_Noteworthy details','review_questions_None','review_questions_Nearby activities','review_questions_Safety','review_questions_Walkability','review_questions_Food & drinks','review_questions_Wi-fi'],axis=1)

df_columns_cut_off['Google Reivews'] = df_columns_cut_off['review_text']

#remove stopwords from 'Google Reviews'
nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def remove_stopwords(text):
    words = word_tokenize(text)
    return ' '.join([word for word in words if word.lower() not in stop_words])

df = df_columns_cut_off
df['Google Reivews'] = df['Google Reivews'].astype(str).apply(remove_stopwords)
print(df['Google Reivews'])