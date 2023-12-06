--For SQL to set up table and index
--Sets up hotel_review table. Runn this as a SQL script before uploading data
CREATE TABLE hotel_reviews (
    id numeric constraint id_key primary key,
    name varchar(5000),
    google_id varchar(2500),
    place_id varchar(2500),
    location_link varchar(10000),
    reviews_link varchar(10000),
    reviews numeric,
    rating numeric,
    review_id varchar(5000),
    author_title varchar(5000),
    author_id varchar(5000),
    review_text varchar(50000),
    owner_anwer varchar(50000),
    owner_answer_timestamp numeric,
    review_rating numeric,
    review_timestamp numeric,
    review_likes numeric,
    reviews_per_score_1 numeric,
    reviews_per_score_2 numeric,
    reviews_per_score_3 numeric,
    reviews_per_score_4 numeric,
    reviews_per_score_5 numeric,
    zip_code var_char(7),
    Latitude varchar,
    Longitude varchar,
    Googe_Reviews varchar (50000),
    embedding vector(384)
)
--Creates ivvflat index for data. Run this in SQL after uploading data
Create index hotelembedding_idx on hotel_reviews using ivfflat (embedding vector_cosine_ops) with (lists = 386)
--Create ivvflat probes after index to assist with recall. This number is the square root of the lists rounded down.
set ivvflat.probes = 19

