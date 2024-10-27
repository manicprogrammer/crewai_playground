import os
import json
from crewai_tools import BaseTool
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()


class TavilyBasicSearch(BaseTool):
    """Custom tool for the Tavily project that returns a general search"""

    name: str = 'Tavily Basic Search Tool'
    description: str = 'Custom tool for the Tavily project that performs a general search'

    def _run(self, query: str, limit: int) -> str:
        """Run the tool"""

        tavily_client = TavilyClient(api_key=os.getenv('TAVILY_API_KEY'))
        response = tavily_client.search(query=query, topic='general', limit=limit)

        # Parse the JSON response and extract the 'results' property
        results = response.get('results', [])
        
        results_json = json.dumps(results)

        return results_json
    