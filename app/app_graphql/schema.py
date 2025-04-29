# app/graphql/schema.py
import strawberry
from app_graphql.queries.query import Query
from app_graphql.mutations.mutation import Mutation

schema = strawberry.Schema(query=Query, mutation=Mutation)