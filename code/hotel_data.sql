--For SQL to set up table and index
CREATE TABLE hotel_reviews (
    id bigserial,
    name varchar(25),
    google_id varchar(25),
    place_id varchar(25),
    location_link varchar(100),
    reviews_link varchar(100)
    reviews numeric,
    review_id varchar(50) constraint review_key primary key,
    author_title varchar(50)
    author_id varchar(50),
    review_text varchar(50000),
    owner_anwer varchar(50000),
    owner_answer_timestamp timestamp,
    review_rating numeric,
    review_timestamp numeric,
    review_likes numeric,
    embedding vector(384)
)
Create index on hotel_reviews using ivfflat (embedding vector_cosine_ops) with (lists = 386)