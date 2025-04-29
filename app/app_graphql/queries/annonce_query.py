# app/graphql/queries/annonce_query.py
import strawberry
from typing import List
from repositories.ad_repository import ad_repo
from app_graphql.types.annonce_type import AnnonceType

@strawberry.type
class AnnonceQuery:
    @strawberry.field
    def list_ads(self) -> List[AnnonceType]:
        return ad_repo.list_all()