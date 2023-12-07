import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

dir = "artifacts"
in_path = os.path.join(dir, "cleaned_hotel_data.csv")

def dataframe(path):
    """Reads in hotel data as a dataframe and removes some problematic data."""
    hotel_df = pd.read_csv(path)
    return hotel_df

def generate_bar_chart(data, output_path):
    """Generate a bar chart to show the distribution of ratings for each hotel."""
    plt.figure(figsize=(12, min(6 + 0.2 * len(data), 16)))  # Adjust the height based on the number of hotels
    sns.barplot(x='rating', y='name', data=data, ci=None, palette='viridis')
    plt.title('Average Ratings for Different Hotels')
    plt.xlabel('Average Rating')
    plt.ylabel('Hotel Name')
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def generate_pie_chart(data, output_path):
    """Generate a pie chart to illustrate the distribution of ratings."""
    plt.figure(figsize=(8, 8))
    data['rating'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, colors=['gold', 'lightcoral', 'lightskyblue'])
    plt.title('Distribution of Ratings')
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def generate_box_plot(data, output_path):
    """Generate a box plot to visualize the spread of review ratings for each hotel."""
    plt.figure(figsize=(12, min(6 + 0.2 * len(data), 16)))  # Adjust the height based on the number of hotels
    sns.boxplot(x='rating', y='name', data=data, palette='viridis')
    plt.title('Spread of Review Ratings for Each Hotel')
    plt.xlabel('Review Rating')
    plt.ylabel('Hotel Name')
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

if __name__ == "__main__":
    # Directory for saving artifacts
    artifacts_dir = "artifacts"
    os.makedirs(artifacts_dir, exist_ok=True)

    # Load data
    hotel_data = dataframe(in_path)

    # Streamlit App
    st.title('Hotel Review Visualizations')

    # Bar Chart
    st.header('Average Ratings for Different Hotels')
    st.image(generate_bar_chart(hotel_data, os.path.join(artifacts_dir, "bar_chart.png")), use_column_width=True)

    # Pie Chart
    st.header('Distribution of Ratings')
    st.image(generate_pie_chart(hotel_data, os.path.join(artifacts_dir, "pie_chart.png")), use_column_width=True)

    # Box Plot
    st.header('Spread of Review Ratings for Each Hotel')
    st.image(generate_box_plot(hotel_data, os.path.join(artifacts_dir, "box_plot.png")), use_column_width=True)
