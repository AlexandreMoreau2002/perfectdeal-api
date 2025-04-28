# app/graphql/queries/annonce_query.py
import strawberry
from typing import List
from services.db.memory import ad_repo
from app_graphql.types.annonce_type import AnnonceType

@strawberry.type
class Query:
    @strawberry.field
    def list_ads(self) -> List[AnnonceType]:
        return ad_repo.list_all()