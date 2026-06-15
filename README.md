# EthiElection

Full-stack pipeline for ingesting, classifying, and displaying Ethiopian political Facebook posts.

## Architecture

```
Python (scraper) → MySQL ← Laravel (API) ← React (UI)
```

- **Python** writes directly to MySQL (no Laravel involvement)
- **Laravel** reads from the same MySQL database and serves JSON API
- **React** only talks to the Laravel API

## Quick Start

### 1. MySQL

Start MySQL and create the database :


### 2. Laravel API (run migrations first)

```bash
cd backend
cp .env.example .env
php artisan key:generate   
php artisan migrate
php artisan serve
```

API: `GET http://127.0.0.1:8000/api/posts?classification=information|incident&page=1`

### 3. Python ingestion

```bash
cd python
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   
python runner.py
```


Re-running `python runner.py` skips duplicates via `source_url` UNIQUE constraint.

### 4. React frontend

```bash
cd frontend
npm install
cp .env.example .env
npm run dev
```

Open http://localhost:5173

## Environment Variables

| Service  | Variable            | Default                        |
|----------|---------------------|--------------------------------|
| Python   | `DB_HOST`           | localhost                      |
| Python   | `DB_NAME`           | election_db                    |
| Laravel  | `DB_DATABASE`       | election_db                    |
| Frontend | `VITE_API_URL`      | http://127.0.0.1:8000/api      |

## Classification

Posts are classified via keyword matching (Amharic + English):

- **information** — announcements, campaigns, election updates
- **incident** — violence, protests, clashes, emergencies

Incident keywords take priority when both match.
# ethi-election-monitor
