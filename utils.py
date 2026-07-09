import pandas as pd


def load_dataset(path):
    """
    Load Netflix dataset.
    """
    try:
        df = pd.read_csv(path)
        print("✅ Dataset Loaded Successfully!")
        return df
    except Exception as e:
        print("❌ Error:", e)
        exit()