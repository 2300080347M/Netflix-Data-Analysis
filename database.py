import sqlite3
import pandas as pd


def create_database(df):

    conn = sqlite3.connect("output/netflix.db")

    df.to_sql(
        "netflix",
        conn,
        if_exists="replace",
        index=False
    )

    print("\n✅ SQLite Database Created Successfully!")

    conn.close()


def run_queries():

    conn = sqlite3.connect("output/netflix.db")

    cursor = conn.cursor()

    print("\n" + "="*60)
    print("SQL ANALYSIS")
    print("="*60)

    # Total Movies
    cursor.execute("""
    SELECT COUNT(*)
    FROM netflix
    WHERE type='Movie'
    """)

    print("\nTotal Movies:", cursor.fetchone()[0])

    # Total TV Shows
    cursor.execute("""
    SELECT COUNT(*)
    FROM netflix
    WHERE type='TV Show'
    """)

    print("Total TV Shows:", cursor.fetchone()[0])

    # Top 10 Countries
    cursor.execute("""
    SELECT country,
           COUNT(*) AS Total
    FROM netflix
    GROUP BY country
    ORDER BY Total DESC
    LIMIT 10
    """)

    print("\nTop Countries")

    for row in cursor.fetchall():
        print(row)

    # Ratings
    cursor.execute("""
    SELECT rating,
           COUNT(*)
    FROM netflix
    GROUP BY rating
    ORDER BY COUNT(*) DESC
    """)

    print("\nRatings")

    for row in cursor.fetchall():
        print(row)

    conn.close()