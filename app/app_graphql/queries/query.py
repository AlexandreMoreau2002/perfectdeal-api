# app/app_graphql/queries/querie.py
import strawberry
from app_graphql.queries.annonce_query import AnnonceQuery
from app_graphql.queries.research_query import ResearchQuery

@strawberry.type
class Query(AnnonceQuery, ResearchQuery):
    """Mutation racine regroupant toutes les mutations disponibles."""
    pass
