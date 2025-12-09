# transform
clone git repo  git@github.com:ilijapet/transform.git
uv venv .venv
source .venv/bin/active
uv sync
uv run uvicorn main:app --host localhost --port 8000 --reload
got to browser swager http://localhost:8000/docs#