PerfectDeal API v1

⸻

🎯 Objectif

Développer une API FastAPI + GraphQL intelligente capable de :
	•	Scraper automatiquement les annonces automobiles ciblées sur Leboncoin.
	•	Filtrer selon des critères métier précis (motorisation exacte, kilométrage, prix).
	•	Analyser et scorer les annonces par pertinence.
	•	Retourner un top intelligent des meilleures annonces, prêt à être consulté.

⸻

⚙️ Fonctionnalités principales

🔎 Recherche ciblée et Scoring intelligent — /graphql
	•	Mutation GraphQL :
	•	Scraper Leboncoin en temps réel selon ta recherche.
	•	Filtrer automatiquement selon :
	•	Année mini / maxi
	•	Kilométrage maximum
	•	Motorisation obligatoire
	•	Finition (ex: S-Line obligatoire)
	•	Mutation GraphQL :
	•	Appliquer un scoring intelligent sur les annonces filtrées :
	•	Embedding (PhraseTransformer)
	•	Calcul de similarité
	•	Règles métier sur kilométrage, prix, finition
	•	Résultat :
	•	Retourner directement un JSON GraphQL avec les meilleures annonces triées.

⸻

📚 Stack technique
	•	FastAPI — Serveur API ultra-léger.
	•	Strawberry GraphQL — API en GraphQL moderne.
	•	BeautifulSoup ou Playwright — Scraping web.
	•	SentenceTransformers — Embedding de texte pour similarité intelligente.
	•	scikit-learn — Calculs de similarité cosine.
	•	Docker — Containerisation.
	•	Poetry — Gestion des dépendances.

⸻

🛠️ Installation
	1.	Cloner le projet :

git clone <repo-url>
cd perfectdeal-api

	2.	Lancer l’application avec Docker :

make build
make up

	3.	Accéder à l’API :

	•	GraphQL Playground : http://127.0.0.1:8000/graphql

⸻

📜 Documentation API
	•	Interface GraphQL (interactive) : http://127.0.0.1:8000/graphql

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

🧱 Architecture technique (évolutive)

app/
├── main.py               # Entrée FastAPI
├── api/
│   ├── exposers/
│   │   ├── resolvers/    # Mutations / Queries GraphQL
│   │   └── schemas/      # Schémas GraphQL
├── domains/
│   └── annonce.py        # Modèle interne d'annonce
├── services/
│   ├── scraper.py        # Scraping Leboncoin
│   ├── filter.py         # Filtrage métier
│   ├── scoring.py        # Scoring + Similarité
│   └── utils.py          # Fonctions utilitaires
├── data/
│   └── annonces.json     # Données brutes temporaires (optionnel)
├── Dockerfile
├── pyproject.toml
└── Makefile



⸻

🧠 Scoring de base

Critère	Pondération
Correspondance moteur/modèle	Très forte
Kilométrage faible pour l’année	+10%
Prix compétitif	+10%
Présence finition S-Line / RS	+5%
Annonce complète (texte/photos)	+5%



⸻

📝 Notes
	•	Architecture prête pour une évolution vers un SaaS léger.
	•	Les pondérations de scoring pourront être configurables dynamiquement.