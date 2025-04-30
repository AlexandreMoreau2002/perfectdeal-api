import os
import httpx
import random
from dotenv import load_dotenv
from models.research import Research
from urllib.parse import urlencode, quote_plus

load_dotenv()

SCRAPERAPI_KEY = os.getenv("SCRAPERAPI_KEY")

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
]


async def fetch_leboncoin_page(url: str) -> str:
    if not SCRAPERAPI_KEY:
        raise RuntimeError("Tu dois définir SCRAPERAPI_KEY dans ton .env")

    proxy_url = f"http://api.scraperapi.com?api_key={SCRAPERAPI_KEY}&url={url}"
    print(f"🔄 Requête via ScraperAPI : {proxy_url}")

    try:
        async with httpx.AsyncClient(
            headers={
                "User-Agent": random.choice(USER_AGENTS),
                "Accept": "text/html,application/xhtml+xml",
            },
            timeout=httpx.Timeout(60.0)
        ) as client:
            resp = await client.get(proxy_url)
            resp.raise_for_status()
            return resp.text
    except httpx.RequestError as e:
        print("❌ Erreur réseau ScraperAPI :", str(e))
        return None


async def scrape_from_research(research: Research) -> None:
    print("🔎 Lancement du scraping avec la recherche suivante :")
    # url = build_leboncoin_url(research)
    url = build_test_url()
    html = await fetch_leboncoin_page(url)
    if html:
        print("HTML récupéré :", html[:1500])
    else:
        print("❌ Aucune donnée reçue.")


def build_leboncoin_url(research: Research) -> str:
    # base_url = "https://www.leboncoin.fr/recherche"

    # params = {
    #     "category": 2,
    #     "text": f"{research.brand} {research.model}",
    #     "sort": "time",
    #     "order": "desc",
    #     "locations": "Grenoble_38000__45.19397_5.73206_4752_50000"
    # }

    # mapping = {
    #     "price": research.priceMax,
    #     "regdate": f"{research.yearMin}-{research.yearMax}" if research.yearMin and research.yearMax else None,
    #     "mileage": research.mileageMax,
    #     "fuel": research.fuel,
    #     "gearbox": research.transmission,
    # }

    # for key, value in mapping.items():
    #     if value:
    #         params[key] = value

    # query = urlencode(params, quote_via=quote_plus)
    url = "https://www.leboncoin.fr/recherche?category=2&text=audi+a7&regdate=2010-2016&fuel=2&u_car_brand=AUDI&u_car_model=AUDI_A7&vehicle_damage=undamaged&owner_type=all&sort=time&order=desc&kst=k&pi=14f8ecf1-9830-428d-82ee-420377d1f932"
    return url
    # return f"{base_url}?{query}"

def build_test_url():
    url = "https://my-website-bfcab.web.app/fr/"
    return url
