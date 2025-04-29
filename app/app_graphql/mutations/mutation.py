# app/app_graphql/mutations/mutation.py
import strawberry
from app_graphql.mutations.annonce_mutation import AnnonceMutation
from app_graphql.mutations.research_mutation import ResearchMutation

@strawberry.type
class Mutation(AnnonceMutation, ResearchMutation):
    """Mutation racine regroupant toutes les mutations disponibles."""
    pass
