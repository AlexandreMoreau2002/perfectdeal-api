from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app_graphql.schema import schema

app = FastAPI(title="PerfectDeal API", version="1.0")

graphql_app = GraphQLRouter(schema)

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

app.include_router(graphql_app, prefix="/graphql")