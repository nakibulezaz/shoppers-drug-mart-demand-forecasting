import os
from data_prep import load_and_merge, split_store_data

RAW_TRAIN = "data/raw/train.csv"
RAW_STORE = "data/raw/store.csv"

PROCESSED_DIR = "data/processed"

def main():
    # Ensure processed folder exists
    os.makedirs(PROCESSED_DIR, exist_ok=True)

    print("Loading and merging raw data...")
    df = load_and_merge(RAW_TRAIN, RAW_STORE)

    # Save cleaned merged dataset
    merged_path = f"{PROCESSED_DIR}/cleaned_merged.csv"
    df.to_csv(merged_path, index=False)
    print(f"Saved cleaned merged dataset → {merged_path}")

    # Generate train/test for Store 1
    print("Splitting Store 1 data...")
    train, test = split_store_data(df, store_id=1)

    train_path = f"{PROCESSED_DIR}/store_1_train.csv"
    test_path = f"{PROCESSED_DIR}/store_1_test.csv"

    train.to_csv(train_path, index=False)
    test.to_csv(test_path, index=False)

    print(f"Saved Store 1 train → {train_path}")
    print(f"Saved Store 1 test → {test_path}")

    print("Processing complete.")


if __name__ == "__main__":
    main()