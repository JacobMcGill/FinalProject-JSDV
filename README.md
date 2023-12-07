# FinalProject-JSDV
Overview: The aim of this project is to collect reviews for hotels in the Austin area, then conduct an analysis of these reviews. This analysis included comparing hotels in Austin by reviews (including the review scores, number of reviews for hotels, and distribution of review scores) and using the python package “sentence-transformers” to embed written reviews as vectors. Embedding these vectors allowed us to develop a vector search function capable of identifying hotels where specific keywords (i.e. “fitness center” or “laundry service”) are frequently mentioned in reviews.

We collected hotel data using Google Map API and then Outscraper.
 
1. Google Map API (googlemap.py)
 
·  	Using the Google Cloud Platform, we generated valid Googe Maps API and retained the API key.
·  	Wrote the mapapi.py file to generate a list of hotel Place IDs using a location search URL.
·  	The resulting list consisted of 60 hotels, due to a limit Google Maps API places on the number of results that can be returned.
·  	Created a CSV with the list of hotels and their corresponding Place ID and zip codes.
 
2. Outscraper
 
·  	Using the list of Place IDs generated by mapapi.py to generate an Outscraper query to scrape 200 Google reviews per hotel.
·  	About 45 minutes of processing later, Outscraper generated an XLSX file with columns consisting of hotel name, number of reviews, rating, review text, etc. We uploaded the file as a csv to   github as Austin_Hotel_reviews_with_LatitudeLongitude_.

![Outscraper](https://github.com/JacobMcGill/FinalProject-JSDV/assets/143020777/04069a51-b29f-4e34-a74c-ce53185a94f0)

3. Data Cleaning Process

Using pandas to remove redundant columns from the original csv file. We cut 26 columns from 47 columns, so 21 columns were left. Columns that were cut off included “review_pagination_id,” “author_image,” and “review_img_url” etc. This was accomplished with dataclean.py and produced the csv “cleaned_hotel_data.csv” in the artifacts folder

4. Data embedding

After the hotel data had been cleaned we used the python package sentence_transformer to embed the column “hotel_reviews”. This package can embed written sentences based on their meaning and store these embeddings as vectors. We used the model “all-MiniLM-L6-v2” to embed the reviews as vectors and store the resulting vectors as the column “embedding”. The results were stored as the csv’s “embedded_hotel_data.csv”, which contained headers and “sql_embedded_hotel_data.csv”, which did not contain headers (Note: Due to the size of these files, were not able to upload them to github).  We uploaded “sql_embedded_hotel_data.csv” to Cloud GCP and set up the PostgreSQL database “hotels” as the table “hotel_reviews”. The schema for the table is saved as hotel_data.sql in github, which can be ran as a script in SQL prior to uploading the data to PostgreSQL.  

5. Similarity search

After we had uploaded the embedded hotel review data to PostgreSQL, we enabled the extension “vector” in our database to allow us to use vector search.  We then indexed the embedding vectors to ensure a more efficient search. We used ivvflat indexing to index the vectors. After the data had been indexed, we used vector search based off of the cosine similarity of an embedded query and embedded in the hotel. The cosine similarity calculated the difference between the vector embedding of the query (such as “Hotel with clean sheets”) and the vectors of the embedded reviews, returning the hotel with the least difference between the 2 vectors. We limited the cosine similarity to 0.3 between the query and the results(with the similarities being between 0 and 2, 0 being the most similar and 2 being the least similar), so the similarity search in SQL would only pull at most 3 hotels that had a cosine similarity of 0.3 to the written query. This was due to the fact that cosine similarities above 0.3 are generally not effective. The vector search was enabled by the function queries.py, which was used in our Streamlit app return results from these queries.

6. Limitations and extensions of our work:

Due to how the Google Maps API and Outscraper works, we were only limited to 60 hotels in our analysis and up to only 200 reviews per hotel, so this does not provide a comprehensive search of hotels in the Austin area. Also, since reviews were left by individuals who may have had strong opinions about the hotel (either positive or negative), the vector search may not capture all the services provided by the hotel. An extension to our work here could include reviews from other sites (such as Yelp or Travels.com) or data provided by the hotels themselves (such as advertised services).

7. Results

We ran the data in SQL to get these results (the SQL queries that produced these results can be found in sql_queries.sql in the code folder of our repository).


Five best-reviewed hotels in Austin

![SQL_Best](https://github.com/JacobMcGill/FinalProject-JSDV/assets/143020777/0e69a868-ab1b-4eed-8c07-5abf0f29d6ac)

Five worst-reviewed hotels in Austin

![SQL_Worst_reviews](https://github.com/JacobMcGill/FinalProject-JSDV/assets/143020777/09cb9745-adde-45af-ab84-3dbdf5e17637)

Five hotels that have the least reviews in Austin

![SQL_least](https://github.com/JacobMcGill/FinalProject-JSDV/assets/143020777/6e0d3880-3452-41de-9c88-2ba2a7874d2d)

Five zip codes that have the most hotel review counts

![SQL_zip_most](https://github.com/JacobMcGill/FinalProject-JSDV/assets/143020777/2d31a821-fceb-4cb5-be44-ce95e1cf7288)

Five zip codes that have the least hotel review counts

![SQL_zip_least](https://github.com/JacobMcGill/FinalProject-JSDV/assets/143020777/52108b48-2cd0-406a-afa1-e117f11854a1)

8. Data Visualization
We used Tableau to make some visualizations, initially we made an interactive dashboard which was planned to pair up with streamlit but however we might require some more time as streamlit interface with Tableau is different.

![hotel_map](https://github.com/JacobMcGill/FinalProject-JSDV/assets/143020777/3c7c74d1-160e-4cb1-bb23-e7d61f195f29)

As we can see the 60 hotels we have included we observed that almost 25 hotels are very much closer to the I-35 highway. Further all the hotels which are located almost close to the I-35 track a average rating ranging from (4 - 4.4).

![max_likes](https://github.com/JacobMcGill/FinalProject-JSDV/assets/143020777/94c3ba1f-c2d4-4577-8df9-3c4b542a26b6)

This bar chart shows the Top 10 Hotels who have received maximum likes on the reviews that have been posted on Google. The average rating of Sleep Inn & Suites is 4.3. It is believed that even review likes are also a good attribute to consider which hotels are the best. 

![review_discrepancy](https://github.com/JacobMcGill/FinalProject-JSDV/assets/143020777/1f45b85c-dcc3-4c3e-ae88-424cdd7ff1ee)

Here, we plotted the Top 10 hotels which have received the highest number of ‘1’ rating. We were surprised to find out that when we plotted the rating score of ‘5’ on the same graph we had some great outliers like - Hilton Austin, Embassy Suites and Holiday Inn Austin-Town Lake.

Since these hotels are very famous they in general have a high number of reviews and a smaller review score is overpowered easily by a high count of review score. 

![rating_distr](https://github.com/JacobMcGill/FinalProject-JSDV/assets/143020777/a471fa75-aabd-4a3b-aa7e-37b19a39b3dd)

We also wanted to see the range of our rating values we calculated from the 60 hotels. The range is pretty much on the higher end where we have more people submitting positive responses. 

9. Streamlit Application
   
For our vector search engine we wanted to show our results using Streamlit Application.We installed the streamlit library and once we had connected the Postgresql database, we made a SQL query function takes an SQL query as input, embeds it using a pre-trained Sentence Transformer model, and executes a SQL query against a PostgreSQL database to find similar hotel reviews.

Using streamlit commands we have created a simple web page with a title and a text area for users to input SQL queries.If the user clicks the "Run Query" button, it calls the sql_query function and displays the result in a table. Also we can obtain this particular code by running streamlit run code/queries.py

![similarity_search](https://github.com/JacobMcGill/FinalProject-JSDV/assets/143020777/32aa684b-4848-4c06-9ba1-8b4cfda5e9fb)

