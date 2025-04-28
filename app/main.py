from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app_graphql.schema import schema

app = FastAPI(title="PerfectDeal API", version="1.0")

graphql_app = GraphQLRouter(schema)

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

app.include_router(graphql_app, prefix="/graphql")



# # app/models/annonce.py
# from pydantic import BaseModel
# from typing import Optional, List, Dict
# from fastapi import FastAPI
# from strawberry.fastapi import GraphQLRouter
# import strawberry

# # ---- Model Python ----
# class Annonce(BaseModel):
#     title: str
#     price: int
#     year: int
#     mileage: int
#     url: str
#     motorization: Optional[str]
#     finish: Optional[str] = None
#     description: Optional[str] = None
#     score: Optional[float] = None

# # ---- Système en mémoire ----
# class InMemoryAdRepository:
#     def __init__(self):
#         self.ads: List[Annonce] = []

#     def save(self, ad: Annonce) -> None:
#         self.ads.append(ad)

#     def list_all(self) -> List[Annonce]:
#         return self.ads

#     def clear(self) -> None:
#         self.ads.clear()

# # ---- Instance globale ----
# ad_repo = InMemoryAdRepository()

# # ---- GraphQL ----

# @strawberry.type
# class AnnonceType:
#     title: str
#     price: int
#     year: int
#     mileage: int
#     url: str
#     motorization: Optional[str]
#     finish: Optional[str] = None
#     description: Optional[str] = None
#     score: Optional[float] = None

# @strawberry.input
# class AnnonceInput:
#     title: str
#     price: int
#     year: int
#     mileage: int
#     url: str
#     motorization: Optional[str]
#     finish: Optional[str] = None
#     description: Optional[str] = None

# @strawberry.type
# class Query:
#     @strawberry.field
#     def hello(self) -> str:
#         return "Hello World, from GraphQL"
    
#     @strawberry.field
#     def list_ads(self) -> List[AnnonceType]:
#         return ad_repo.list_all()

# @strawberry.type
# class Mutation:
#     @strawberry.mutation
#     def create_ad(self, ad: AnnonceInput) -> bool:
#         ad_pydantic = Annonce(**ad.__dict__)
#         ad_repo.save(ad_pydantic)
#         return True

# schema = strawberry.Schema(query=Query, mutation=Mutation)
# graphql_app = GraphQLRouter(schema)

# # ---- FastAPI app ----
# app = FastAPI(title="PerfectDeal API", version="1.0")

# @app.get("/")
# async def read_root():
#     return {"message": "Hello World"}

# app.include_router(graphql_app, prefix="/graphql")