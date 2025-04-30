# Dockerfile situé dans /app

# Étape 1 : Base image Debian
FROM python:3.12-slim

# Étape 2 : Env vars
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.7.1

# Étape 3 : Dépendances système nécessaires pour Playwright (Chromium)
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    libglib2.0-0 \
    libnss3 \
    libgdk-pixbuf2.0-0 \
    libgtk-3-0 \
    libx11-xcb1 \
    libxcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libpangocairo-1.0-0 \
    libpango-1.0-0 \
    libcairo2 \
    fonts-liberation \
    libgbm1 \
    libxext6 \
    libxfixes3 \
    libxrender1 \
    libdrm2 \
    libxshmfence1 \
    libjpeg62-turbo \
    libwebp-dev \
    && rm -rf /var/lib/apt/lists/*

# Étape 4 : Installer Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Étape 5 : Créer le dossier de travail
WORKDIR /app

# Étape 6 : Copier les fichiers poetry
COPY pyproject.toml poetry.lock* ./

# Étape 7 : Installer les dépendances
RUN poetry install --no-root

# Étape 8 : Copier tout le code
COPY . .

EXPOSE 8000

# Étape 9 : Commande de lancement
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
