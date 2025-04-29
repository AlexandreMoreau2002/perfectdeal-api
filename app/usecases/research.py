from app_graphql.types.research_type import ResearchInput

def process_research(research: ResearchInput) -> ResearchInput:
    """Manipule et nettoie une recherche avant enregistrement."""
    if research.motorization:
        research.motorization = research.motorization.upper()
    return research
