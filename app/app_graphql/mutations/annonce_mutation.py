# app/graphql/mutations/annonce_mutation.py
import strawberry
from models.annonce import Annonce
from services.db.memory import ad_repo
from app_graphql.types.annonce_type import AnnonceInput

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_ad(self, ad: AnnonceInput) -> bool:
        ad_pydantic = Annonce(**ad.__dict__)
        ad_repo.save(ad_pydantic)
        return True