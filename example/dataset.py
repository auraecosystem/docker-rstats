import kagglehub
from kagglehub import KaggleDatasetAdapter
# Load a Dataset with a specific version of a CSV, then remove a column
dataset = kagglehub.dataset_load(
    KaggleDatasetAdapter.HUGGING_FACE,
    "unsdsn/world-happiness/versions/1",
    "2016.csv",
)
dataset = dataset.remove_columns('Region')

# Load a Dataset with specific columns from a parquet file, then split into test/train splits
dataset = kagglehub.dataset_load(
    KaggleDatasetAdapter.HUGGING_FACE,
    "robikscube/textocr-text-extraction-from-images-dataset",
    "annot.parquet",
    pandas_kwargs={"columns": ["image_id", "bbox", "points", "area"]}
)
dataset_with_splits = dataset.train_test_split(test_size=0.8, train_size=0.2)

# Load a Dataset by executing a SQL query against a SQLite DB, then rename a column
dataset = kagglehub.dataset_load(
    KaggleDatasetAdapter.HUGGING_FACE,
    "wyattowalsh/basketball",
    "nba.sqlite",
    sql_query="SELECT person_id, player_name FROM draft_history",
)
dataset = dataset.rename_column('season', 'year')
