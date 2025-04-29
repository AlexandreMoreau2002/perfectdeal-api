# app/app_graphql/mutations/research_mutation.py
import strawberry
from models.research import Research
from usecases.research import process_research
from app_graphql.types.research_type import ResearchInput
from repositories.research_repository import research_repo

@strawberry.type
class ResearchMutation:
    @strawberry.mutation
    def create_research(self, research: ResearchInput) -> bool:
        # Convertit l'input GraphQL en modèle Python
        research_obj = Research(**research.__dict__)
        
        # Utilise le usecase pour appliquer le traitement (ex: motorisation en majuscules)
        processed_research = process_research(research_obj)

        # Sauvegarde la recherche modifiée
        research_repo.save(processed_research)
        
        print(f"Research saved: {processed_research}")
        return True
