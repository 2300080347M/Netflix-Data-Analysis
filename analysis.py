def dataset_info(df):

    print("\n========== DATASET INFORMATION ==========")

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())


def movies_vs_tvshows(df):

    print("\n========== MOVIES VS TV SHOWS ==========")

    print(df["type"].value_counts())


def top10_countries(df):

    print("\n========== TOP 10 COUNTRIES ==========")

    country = df["country"].str.split(", ").explode()

    print(country.value_counts().head(10))


def top10_genres(df):

    print("\n========== TOP 10 GENRES ==========")

    genre = df["listed_in"].str.split(", ").explode()

    print(genre.value_counts().head(10))


def rating_distribution(df):

    print("\n========== CONTENT RATINGS ==========")

    print(df["rating"].value_counts())


def release_trend(df):

    print("\n========== RELEASE TREND ==========")

    print(df["release_year"].value_counts().sort_index())


def top_directors(df):

    print("\n========== TOP DIRECTORS ==========")

    print(df["director"].value_counts().head(10))