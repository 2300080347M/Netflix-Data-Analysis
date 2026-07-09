import pandas as pd

def clean_data(df):

    print("\nCleaning Dataset...")

    # Remove duplicates
    duplicates = df.duplicated().sum()
    print(f"Duplicate Rows: {duplicates}")

    df.drop_duplicates(inplace=True)

    # Fill Missing Values
    df["director"] = df["director"].fillna("Unknown")
    df["cast"] = df["cast"].fillna("Unknown")
    df["country"] = df["country"].fillna("Unknown")
    df["rating"] = df["rating"].fillna("Unknown")
    df["date_added"] = df["date_added"].fillna("Unknown")

    # ------------------------------------------
    # Remove leading/trailing spaces
    # ------------------------------------------
    text_columns = ["director", "cast", "country", "rating", "date_added"]

    for col in text_columns:
        df[col] = df[col].astype(str).str.strip()

    # ------------------------------------------
    # Fix invalid ratings
    # ------------------------------------------
    valid_ratings = [
        "TV-MA", "TV-14", "TV-PG", "R", "PG-13",
        "TV-Y7", "TV-Y", "PG", "TV-G", "NR",
        "G", "TV-Y7-FV", "NC-17", "UR", "Unknown"
    ]

    df.loc[~df["rating"].isin(valid_ratings), "rating"] = "Unknown"

    # ------------------------------------------
    # Keep only valid content types
    # ------------------------------------------
    valid_types = ["Movie", "TV Show"]

    df = df[df["type"].isin(valid_types)]

    # ------------------------------------------
    # Fix release_year
    # ------------------------------------------
    df["release_year"] = pd.to_numeric(
        df["release_year"],
        errors="coerce"
    )

    df = df.dropna(subset=["release_year"])

    df["release_year"] = df["release_year"].astype(int)

    print("✅ Cleaning Completed")

    return df