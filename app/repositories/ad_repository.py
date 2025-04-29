from typing import List, Dict

class InMemoryAdRepository:
    def __init__(self):
        self.ads: List[Dict] = []

    def save(self, ad: Dict) -> None:
        """Sauvegarder une annonce."""
        self.ads.append(ad)

    def list_all(self) -> List[Dict]:
        """Récupérer toutes les annonces."""
        return self.ads

    def clear(self) -> None:
        """Vider toutes les annonces."""
        self.ads.clear()

ad_repo = InMemoryAdRepository()