# PerfectDeal API — *Projet cloturé* 🚧

> **Pourquoi ?** Le but initial était de scrapper Leboncoin (LBC) et de classer intelligemment les annonces auto selon des critères personnels.  
> Après de multiples tests j'ai constaté qu’il est **à la fois techniquement instable** (anti‑bots agressifs, mises à jour fréquentes du site, absence d’API publique fiable) **et juridiquement risqué** (non‑respect potentiel des CGU et de la législation sur le droit des bases de données) de récupérer et ré‑exploiter les données de LBC à grande échelle.

---

## 📝 Ce que le projet m’a apporté

| 🚀 Compétence | 🎯 Mise en pratique |
|--------------|--------------------|
| **FastAPI**  | Création de ma **première** API REST/GraphQL solide. |
| **Docker**   | Environnement de dev entièrement containerisé (_Dockerfile_, `docker‑compose.yml`, `Makefile`). |
| **GraphQL**  | Mise en place de Strawberry‑GraphQL & d’un endpoint `/graphql` interactif. |
| **Architecture hexagonale légère** | Séparation **services / domaines** pour préparer la scalabilité. |

* découvrir FastAPI + GraphQL,
* comprendre comment dockeriser un micro‑service Python

---

## PerfectDeal API v1 (design initial)
*(Conservé à titre informatif)*

### 🎯 Objectif

Développer une API FastAPI + GraphQL intelligente capable de :

* Scraper automatiquement les annonces automobiles ciblées sur Leboncoin.  
* Filtrer selon des critères métier précis (motorisation exacte, kilométrage, prix).  
* Analyser et scorer les annonces par pertinence.  
* Retourner un top intelligent des meilleures annonces.

### ⚙️ Fonctionnalités principales

#### 🔎 Recherche ciblée & Scoring intelligent — `/graphql`

* **Mutation GraphQL** : lance le scraping temps réel selon ta recherche.  
* **Filtrage automatique** : année mini/maxi, kilométrage max, motorisation, finition (ex. S‑Line).  
* **Scoring** : embeddings (‌SentenceTransformers) + similarité cosine + règles métier.  
* **Résultat** : JSON trié par pertinence.

### 📚 Stack technique
* FastAPI • Strawberry‑GraphQL • BeautifulSoup/Playwright • SentenceTransformers  
* scikit‑learn • Docker • Poetry

### 🛠️ Installation rapide

```bash
git clone <repo-url>
cd perfectdeal-api
make build   # build Docker images
make up      # lance l'API sur http://127.0.0.1:8000
