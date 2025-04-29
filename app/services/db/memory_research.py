# app/services/db/memory_research.py
from typing import List, Optional
from app_graphql.types.research_type import ResearchInput

class InMemoryResearchRepository:
    def __init__(self):
        self.researches: List[ResearchInput] = []

    def save(self, research: ResearchInput) -> None:
        """Sauvegarder une recherche."""
        self.researches.append(research)

    def list_all(self) -> List[ResearchInput]:
        """Lister toutes les recherches."""
        return self.researches

    def get_last(self) -> Optional[ResearchInput]:
        """Récupérer la dernière recherche effectuée."""
        if self.researches:
            return self.researches[-1]
        return None

    def clear(self) -> None:
        """Effacer toutes les recherches."""
        self.researches.clear()

research_repo = InMemoryResearchRepository()
