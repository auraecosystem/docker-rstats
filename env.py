import kagglehub

# Download the latest version.
kagglehub.model_download('google/bert/tensorFlow2/answer-equivalence-bem')

# Download a specific version.
kagglehub.model_download('google/bert/tensorFlow2/answer-equivalence-bem/1')

# Download a single file.
kagglehub.model_download('google/bert/tensorFlow2/answer-equivalence-bem', path='variables/variables.index')

# Download a model or file, even if previously downloaded to cache.
kagglehub.model_download('google/bert/tensorFlow2/answer-equivalence-bem', force_download=True)

# Download to a custom local directory.
kagglehub.model_download('google/bert/tensorFlow2/answer-equivalence-bem', output_dir='./models')

# Overwrite an existing output directory.
kagglehub.model_download('google/bert/tensorFlow2/answer-equivalence-bem', output_dir='./models', force_download=True)
