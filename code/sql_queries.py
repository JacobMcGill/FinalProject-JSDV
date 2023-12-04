# Question 1
# What are the 5 best-reviewed hotels in Austin?

query_1 = """
SELECT "name", AVG(rating) as average_rating
FROM hotel_reviews hr
GROUP BY "name"
ORDER BY average_rating DESC
LIMIT 5;
    """

# Question 2
# What are the 5 worst-reviewed hotels in Austin?
query_2 = """
SELECT "name", AVG(rating) as average_rating
FROM hotel_reviews
GROUP BY "name"
ORDER BY average_rating ASC
LIMIT 5;
    """

# Question 3
# What are the 5 least-reviewed hotels in Austin?
query_3 = """
SELECT "name", COUNT(*) as review_count
FROM hotel_reviews
GROUP BY "name"
ORDER BY review_count asc
LIMIT 5;
    """

# Question 4
# What are the top 5 zip code have the most hotel reviews?

query_4 = """
SELECT zip_code, COUNT(*) as hotel_count
FROM hotel_reviews hr 
GROUP BY zip_code
ORDER BY hotel_count DESC
LIMIT 5;
    """

# Question 5
# What are the top 5 zip code have the most hotel reviews?

query_5 = """
SELECT zip_code, COUNT(*) as hotel_count
FROM hotel_reviews hr 
GROUP BY zip_code
ORDER BY hotel_count ASC
LIMIT 5;
    """