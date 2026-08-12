import kagglehub

# Download the latest version.
kagglehub.dataset_download('bricevergnou/spotify-recommendation')

# Download a specific version.
kagglehub.dataset_download('bricevergnou/spotify-recommendation/versions/1')

# Download a single file.
kagglehub.dataset_download('bricevergnou/spotify-recommendation', path='data.csv')

# Download one directory while preserving its nested structure.
kagglehub.dataset_download(
    'moltean/fruits/versions/99',
    path='fruits-360_meta/fruits-360-meta/Papers',
)

# Download a dataset, directory, or file, even if previously downloaded to cache.
kagglehub.dataset_download('bricevergnou/spotify-recommendation', force_download=True)

# Download a dataset to a custom output directory.
kagglehub.dataset_download('bricevergnou/spotify-recommendation', output_dir='./data')

# Download a single file to a custom output directory.
kagglehub.dataset_download('bricevergnou/spotify-recommendation', path='data.csv', output_dir='./data')

# Overwrite an existing output directory.
kagglehub.dataset_download('bricevergnou/spotify-recommendation', output_dir='./data', force_download=True)
