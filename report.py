from datetime import datetime


def create_report(df):

    movies = len(df[df["type"] == "Movie"])
    tvshows = len(df[df["type"] == "TV Show"])

    countries = df["country"].nunique()
    directors = df["director"].nunique()

    genres = df["listed_in"].str.split(", ").explode().nunique()

    ratings = df["rating"].mode()[0]

    release_min = df["release_year"].min()
    release_max = df["release_year"].max()

    with open("output/analysis_report.txt", "w", encoding="utf-8") as f:

        f.write("=" * 60 + "\n")
        f.write("NETFLIX DATA ANALYSIS REPORT\n")
        f.write("=" * 60 + "\n\n")

        f.write(f"Generated On : {datetime.now()}\n\n")

        f.write(f"Total Titles      : {len(df)}\n")
        f.write(f"Movies            : {movies}\n")
        f.write(f"TV Shows          : {tvshows}\n")
        f.write(f"Countries         : {countries}\n")
        f.write(f"Directors         : {directors}\n")
        f.write(f"Genres            : {genres}\n")
        f.write(f"Most Common Rating: {ratings}\n")
        f.write(f"Release Years     : {release_min} - {release_max}\n\n")

        f.write("=" * 60 + "\n")
        f.write("BUSINESS INSIGHTS\n")
        f.write("=" * 60 + "\n\n")

        f.write("• Movies dominate Netflix's catalog.\n")
        f.write("• United States contributes the most content.\n")
        f.write("• International Movies is the most popular genre.\n")
        f.write("• TV-MA is the most common content rating.\n")
        f.write("• Netflix content increased rapidly after 2015.\n")