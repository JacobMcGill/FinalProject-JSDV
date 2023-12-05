import requests
import time
import pandas as pd

def process_results(url):
    response = requests.get(url)
    data = response.json()
    
    hotel_info = []
    
    if "results" in data:
        for result in data["results"]:
            place_id = result["place_id"]
            hotel_name = result["name"]
            latitude = result["geometry"]["location"]["lat"]
            longitude = result["geometry"]["location"]["lng"]

            zip_code = get_zip_code_from_coordinates(latitude, longitude)

            hotel_info.append({
                "Place ID": place_id,
                "Hotel Name": hotel_name,
                "Zip Code": zip_code
            })

            print(f"Hotel Name: {hotel_name}, Place ID: {place_id}, Zip Code: {zip_code}")

    next_page_token = data.get("next_page_token")
    
    return next_page_token, hotel_info

def get_zip_code_from_coordinates(latitude, longitude):
    # Use a geocoding service to obtain location information
    response = requests.get(f"https://nominatim.openstreetmap.org/reverse?format=json&lat={latitude}&lon={longitude}")
    data = response.json()

    # Extract the ZIP code
    address = data.get("address", {})
    zip_code = address.get("postcode", "")

    return zip_code

api_key = "AIzaSyBnrinMF5lYfCBYOVLhBBt6urAOTKLmuTk"

url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=30.2500,-97.7500&radius=100000&type=lodging&keyword=hotel&key={api_key}"
hotel_info = []

while url:
    time.sleep(2)  # Wait a bit before making the next request

    next_page_token, batch_hotel_info = process_results(url)

    # Add the results to the overall list
    hotel_info.extend(batch_hotel_info)

    if not next_page_token:
        break

    # Update the URL for the next iteration
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?key={api_key}&pagetoken={next_page_token}"

# Convert to DataFrame
df = pd.DataFrame(hotel_info)

# Save to CSV file
df.to_csv("hotel_info_with_zipcode.csv", index=False)

print("Total number of hotels:", len(hotel_info))
