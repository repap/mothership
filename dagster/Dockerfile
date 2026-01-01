# Wir nutzen ein schlankes Python Image
FROM python:3.13-slim

# Umgebungsvariablen setzen
ENV DAGSTER_HOME=/opt/dagster/dagster_home
ENV PYTHONUNBUFFERED=1

# System-Abhängigkeiten für Postgres (psycopg2) installieren
RUN apt-get update && apt-get install -y \
    libpq-dev \
    curl \
    gcc \
    git \
    && rm -rf /var/lib/apt/lists/*

# Arbeitsverzeichnis erstellen
WORKDIR /opt/dagster/app

# Zuerst nur requirements kopieren (Caching-Vorteil bei Docker Builds)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Jetzt den Rest des Codes kopieren
COPY . .

# Verzeichnis für Dagster Home und Config erstellen
RUN mkdir -p $DAGSTER_HOME

# WICHTIG: Die dagster.yaml muss im DAGSTER_HOME liegen
RUN cp dagster.yaml $DAGSTER_HOME/dagster.yaml
RUN cp workspace.yaml $DAGSTER_HOME/workspace.yaml

# Ports werden zur Laufzeit via docker-compose geöffnet