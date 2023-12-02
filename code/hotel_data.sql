CREATE TABLE hotel_reviews (
    id bigserial,
    name varchar(25),
    google_id varchar(25),
    place_id varchar(25),
    location_link varchar(100),
    reviews numeric,
    review_id varchar(50) constraint review_key primary key,
    review_pagination_id varchar(25),
    author_link varchar(100),
    author_title varchar(50)
    author_id varchar(50),
    author_image varchar(125),
    review_text varchar(1000),
    review_rating numeric,
    review_timestamp numeric,
    review_datetime_utc timestamp,
    review_likes numeric,
    embedding vector(384)
)
Create index on hotel_reviews using ivfflat (embedding vector_cosine_ops)