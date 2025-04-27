PerfectDeal API v1

⸻

🎯 Objectif

Développer une API FastAPI intelligente capable de :
	•	Scraper automatiquement les annonces automobiles ciblées sur Leboncoin.
	•	Filtrer selon des critères métier très précis (motorisation exacte, kilométrage, prix).
	•	Analyser et scorer les annonces par pertinence.
	•	Retourner un top des meilleures annonces, prêtes à être consultées.

⸻

⚙️ Fonctionnalités principales

🔎 Recherche ciblée - /search
	•	Input :
	•	Mot-clé de recherche (ex : “Audi A7 3.0 TDI 245 S-Line”)
	•	Critères de filtre :
	•	Année mini
	•	Année maxi
	•	Finition S-line
	•	Motorisation obligatoire
	•	Traitement :
	•	Scraping Leboncoin.
	•	Extraction d’informations brutes.
	•	Filtrage strict selon critères métier.
	•	Output :
	•	JSON listant toutes les annonces filtrées.

🧠 Scoring d’annonces - /score
	•	Input :
	•	JSON d’annonces (sortie de /search)
	•	Traitement :
	•	Embedding des textes.
	•	Similarité avec recherche initiale.
	•	Règles métier (kilométrage, prix, finition, etc.)
	•	Output :
	•	JSON des X meilleures annonces classées avec leurs scores.

⸻

📚 Stack technique
	•	FastAPI — Serveur d’API léger et rapide.
	•	BeautifulSoup ou Playwright — Scraping web.
	•	SentenceTransformers — Embedding de textes pour la similarité.
	•	scikit-learn — Calculs de similarité cosine.
	•	Docker — Containerisation.
	•	Poetry — Gestion des dépendances.
	•	GraphQL (évolution possible avec Strawberry).

⸻

🛠️ Installation

1. Cloner le projet

git clone <repo-url>
cd perfectdeal-api

2. Lancer l’application avec Docker

make build
make up

L’API sera disponible sur : http://127.0.0.1:8000

⸻

📜 Documentation API
	•	Swagger UI : http://127.0.0.1:8000/docs
	•	ReDoc : http://127.0.0.1:8000/redoc

⸻

🔧 Commandes utiles (Makefile)

Commande	Description
make build	Build les containers Docker
make up	Démarre l’application en Docker
make down	Stoppe les containers
make restart	Restart rapide
make shell	Ouvre un shell dans le container
make logs	Voir les logs du container

⸻

🧱 Architecture technique (prévue)

app/
├── main.py              # Entrée FastAPI
├── api/
│   ├── routes/
│   │   ├── search.py    # Endpoint /search
│   │   └── score.py     # Endpoint /score
│   └── models/
│       └── schemas.py   # Schémas Pydantic
├── services/
│   ├── scraper.py       # Scraping Leboncoin
│   ├── filter.py        # Filtrage métier
│   ├── scoring.py       # Scoring + Similarité
│   └── utils.py         # Fonctions utilitaires
├── data/
│   └── annonces_raw.json # Stockage temporaire (optionnel)
├── Dockerfile
├── pyproject.toml
└── Makefile

⸻

🧠 Scoring de base

Critère	Pondération
Correspondance moteur/modèle	Très forte (filtrage obligatoire)
Kilométrage faible pour l’année	+10%
Prix compétitif par rapport à l’année	+10%
Présence finition S-Line / RS-Line	+5%
Annonce complète (texte, photos)	+5%

⸻

📝 Notes
	•	Architecture conçue pour évoluer vers un SaaS minimal plus tard.
	•	Les pondérations de scoring seront configurables dynamiquement.

⸻

✅ Résumé

PerfectDeal API vise à transformer une recherche pénible sur Leboncoin en un classement intelligent des meilleures affaires auto, selon ton besoin précis.