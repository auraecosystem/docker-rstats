uv venv .venv
source .venv/bin/activate
uv pip install harbor
echo ".venv/" > .gitignore
harbor init --dataset ileo/sample-dataset
harbor init --task ileo/example-task -o tasks
