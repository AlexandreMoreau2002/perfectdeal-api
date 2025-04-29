# app/app_graphql/queries/research_query.py
import strawberry
from app_graphql.types.research_type import ResearchType
from services.db.memory_research import research_repo

@strawberry.type
class ResearchQuery:
    @strawberry.field
    def list_researches(self) -> list[ResearchType]:
        return research_repo.list_all()
