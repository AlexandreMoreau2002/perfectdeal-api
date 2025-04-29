# app/services/db/memory_research.py
from typing import List, Optional
from models.research import Research

class InMemoryResearchRepository:
    def __init__(self):
        self.researches: List[Research] = []

    def save(self, research: Research) -> None:
        self.researches.append(research)

    def list_all(self) -> List[Research]:
        return self.researches

    def get_last(self) -> Optional[Research]:
        if self.researches:
            return self.researches[-1]
        return None

    def clear(self) -> None:
        self.researches.clear()

research_repo = InMemoryResearchRepository()
