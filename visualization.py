import pandas as pd
import matplotlib.pyplot as plt


# 1. Movies vs TV Shows
def plot_movies_vs_tvshows(df):

    data = df["type"].value_counts()

    plt.figure(figsize=(6,5))

    plt.bar(data.index, data.values)

    plt.title("Movies vs TV Shows")
    plt.xlabel("Type")
    plt.ylabel("Count")

    for i, value in enumerate(data.values):
        plt.text(i, value+50, str(value), ha="center")

    plt.savefig("images/movies_vs_tvshows.png", dpi=300)

    plt.show()
    plt.close()


# 2. Top Genres
def plot_top_genres(df):

    genre = df["listed_in"].str.split(", ").explode()

    top = genre.value_counts().head(10)

    plt.figure(figsize=(10,6))

    plt.barh(top.index, top.values)

    plt.title("Top 10 Genres")
    plt.xlabel("Titles")

    plt.tight_layout()

    plt.savefig("images/top_genres.png", dpi=300)

    plt.show()
    plt.close()


# 3. Top Countries
def plot_top_countries(df):

    country = df["country"].str.split(", ").explode()

    top = country.value_counts().head(10)

    plt.figure(figsize=(10,6))

    plt.barh(top.index, top.values)

    plt.title("Top 10 Countries")
    plt.xlabel("Titles")

    plt.tight_layout()

    plt.savefig("images/top_countries.png", dpi=300)

    plt.show()
    plt.close()


# 4. Release Trend
def plot_release_trend(df):

    release = df["release_year"].value_counts().sort_index()

    plt.figure(figsize=(12,6))

    plt.plot(release.index,
             release.values,
             marker="o")

    plt.title("Netflix Release Trend")

    plt.xlabel("Release Year")
    plt.ylabel("Titles")

    plt.grid(True)

    plt.savefig("images/release_trend.png", dpi=300)

    plt.show()
    plt.close()


# 5. Rating Distribution
def plot_rating_distribution(df):

    rating = df["rating"].value_counts().head(10)

    plt.figure(figsize=(8,8))

    plt.pie(
        rating.values,
        labels=rating.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Content Rating Distribution")

    plt.savefig("images/rating_distribution.png", dpi=300)

    plt.show()
    plt.close()


# 6. Top Directors
def plot_top_directors(df):

    directors = df[df["director"] != "Unknown"]["director"].value_counts().head(10)

    plt.figure(figsize=(10,6))

    plt.barh(directors.index, directors.values)

    plt.title("Top 10 Directors")
    plt.xlabel("Titles")

    plt.tight_layout()

    plt.savefig("images/top_directors.png", dpi=300)

    plt.show()
    plt.close()


# 7. Top Actors
def plot_top_actors(df):

    actors = df["cast"].str.split(", ").explode()

    actors = actors[actors != "Unknown"]

    top = actors.value_counts().head(10)

    plt.figure(figsize=(10,6))

    plt.barh(top.index, top.values)

    plt.title("Top 10 Actors")

    plt.xlabel("Titles")

    plt.tight_layout()

    plt.savefig("images/top_actors.png", dpi=300)

    plt.show()
    plt.close()


# 8. Movie Duration Distribution
def plot_duration_distribution(df):

    movies = df[df["type"] == "Movie"].copy()

    movies["duration"] = movies["duration"].str.replace(" min", "", regex=False)

    movies = movies[movies["duration"].str.isnumeric()]

    movies["duration"] = movies["duration"].astype(int)

    plt.figure(figsize=(10,6))

    plt.hist(movies["duration"], bins=30)

    plt.title("Movie Duration Distribution")

    plt.xlabel("Duration (Minutes)")
    plt.ylabel("Movies")

    plt.savefig("images/duration_distribution.png", dpi=300)

    plt.show()
    plt.close()


# 9. Content Added Per Year
def plot_content_added(df):

    temp = df.copy()

    # Remove missing values
    temp = temp.dropna(subset=["date_added"])

    # Remove leading/trailing spaces
    temp["date_added"] = temp["date_added"].str.strip()

    # Convert to datetime
    temp["date_added"] = pd.to_datetime(
        temp["date_added"],
        format="mixed",
        errors="coerce"
    )

    # Remove invalid dates
    temp = temp.dropna(subset=["date_added"])

    yearly = temp["date_added"].dt.year.value_counts().sort_index()

    plt.figure(figsize=(12,6))

    plt.plot(yearly.index,
             yearly.values,
             marker="o")

    plt.title("Content Added to Netflix Per Year")
    plt.xlabel("Year")
    plt.ylabel("Titles")
    plt.grid(True)

    plt.savefig("images/content_added.png", dpi=300)

    plt.show()
    plt.close()
# 10. Missing Values
def plot_missing_values(df):

    missing = df.isnull().sum()

    plt.figure(figsize=(10,5))

    plt.bar(missing.index, missing.values)

    plt.xticks(rotation=45)

    plt.title("Missing Values")

    plt.tight_layout()

    plt.savefig("images/missing_values.png", dpi=300)

    plt.show()
    plt.close()