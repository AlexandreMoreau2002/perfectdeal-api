# app/graphql/schema.py
import strawberry
from app_graphql.queries.annonce_query import Query
from app_graphql.mutations.annonce_mutation import Mutation



schema = strawberry.Schema(query=Query, mutation=Mutation)