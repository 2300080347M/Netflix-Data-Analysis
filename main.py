from utils import load_dataset

from data_cleaning import clean_data

from analysis import *

from visualization import *

from report import create_report

from database import create_database, run_queries

print("=" * 60)
print("NETFLIX DATA ANALYSIS PROJECT")
print("=" * 60)

# Load Dataset
df = load_dataset("dataset/netflix_titles.csv")

# Dataset Information
dataset_info(df)

# Cleaning
df = clean_data(df)

# Save Clean Dataset
df.to_csv("output/cleaned_netflix.csv", index=False)

print("\nCleaned Dataset Saved Successfully!")

# Analysis
movies_vs_tvshows(df)

top10_countries(df)

top10_genres(df)

rating_distribution(df)

release_trend(df)

top_directors(df)

# Visualizations
plot_movies_vs_tvshows(df)

plot_top_genres(df)

plot_top_countries(df)

plot_release_trend(df)
plot_movies_vs_tvshows(df)
plot_top_genres(df)
plot_top_countries(df)
plot_release_trend(df)
plot_rating_distribution(df)
plot_top_directors(df)
plot_top_actors(df)
plot_duration_distribution(df)
plot_content_added(df)
plot_missing_values(df)
create_report(df)

create_database(df)
run_queries()

print("\nProject Completed Successfully!")