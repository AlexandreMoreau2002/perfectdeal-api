from playwright.async_api import async_playwright
from urllib.parse import urlencode, quote_plus
from models.research import Research

async def fetch_leboncoin_page(url: str) -> str:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url, timeout=60000)
        content = await page.content()
        await browser.close()
        return content


async def scrape_from_research(research: Research) -> None:
    """Simule le scraping basé sur la recherche utilisateur."""
    print("🔎 Lancement du scraping avec la recherche suivante :")
    print(f"Marque: {research.brand}")
    print(f"Modèle: {research.model}")
    print(f"Motorisation: {research.motorization}")
    print(f"Années: {research.yearMin} - {research.yearMax}")
    print(f"Prix max: {research.priceMax}")
    print(f"Kilométrage max: {research.mileageMax}")
    print(f"Carburant: {research.fuel}")
    print(f"Transmission: {research.transmission}")
    print(f"Texte libre: {research.freeText}")

    url = build_leboncoin_url(research)
    print("---------------")
    print(f"URL générée : {url}")
    print("---------------")

    html = await fetch_leboncoin_page(url)
    print("HTML récupéré :", html)


def build_leboncoin_url(research: Research) -> str:

    base_url = "https://www.leboncoin.fr/recherche"

    mapping = {
        "priceMax": research.priceMax,
        "yearMin": research.yearMin,
        "yearMax": research.yearMax,
        "mileageMax": research.mileageMax,
        "fuel": research.fuel,
        "gearbox": research.transmission,
    }

    # Base params obligatoires
    params = {
        "category": 2, # Car
        "text": f"{research.brand} {research.model}",
    }

    # Ajouter dynamiquement les options disponibles
    for key, value in mapping.items():
        if value is not None:
            params[key] = value

    query_string = urlencode(params, quote_via=quote_plus)
    url = f"{base_url}?{query_string}"

    return url
