# Tamrin1 FastAPI DevOps Pipeline

This project is a small FastAPI API that can be used to practice a basic DevOps pipeline.

## 1. Run the app locally

```powershell
venv\Scripts\activate
pip install -r requirements-dev.txt
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## 2. Run tests locally

```powershell
pytest
```

## 3. Run lint locally

```powershell
ruff check .
```

## 4. Build Docker image locally

```powershell
docker build -t tamrin1-api .
```

## 5. Run Docker container locally

```powershell
docker run --rm -p 8000:8000 tamrin1-api
```

## 6. GitHub Actions pipeline

The pipeline is defined in:

```text
.github/workflows/ci.yml
```

It runs automatically on pushes to `main` or `master`, and on pull requests.

Pipeline stages:

1. Checkout code
2. Install Python
3. Install dependencies
4. Lint with Ruff
5. Test with Pytest
6. Build Docker image

## 7. First Git commands

```powershell
git status
git add .
git commit -m "Add FastAPI CI pipeline"
```
