# app/app_graphql/mutations/research_mutation.py
import strawberry
from app_graphql.types.research_type import ResearchInput
from services.db.memory_research import research_repo

@strawberry.type
class ResearchMutation:
    @strawberry.mutation
    def create_research(self, research: ResearchInput) -> bool:
        research_repo.save(research)
        print(f"Received research: {research}")
        return True
