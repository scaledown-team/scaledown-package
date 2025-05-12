import requests
import json
from typing import Dict, Any, Optional

class ScaleDownAPIClient:
    """Client for the ScaleDown API for prompt compression and carbon tracking."""
    
    BASE_URL = "https://tc9sbclr37.execute-api.us-east-1.amazonaws.com/dev"
    DEFAULT_API_KEY = ""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize API client.
        
        Args:
            api_key: ScaleDown API key (uses default if None)
        """
        self.api_key = api_key or self.DEFAULT_API_KEY
    
    def compress_prompt(self, prompt: str, model: str, rate: float = 0.5) -> Dict[str, Any]:
        """Compress prompt using ScaleDown API.
        
        Args:
            prompt: The prompt to compress
            model: Target model (e.g., "gpt-4o", "claude-3-5-sonnet")
            rate: Compression rate (0.0-1.0, with 1.0 being maximum compression)
            
        Returns:
            API response with compression details
            
        Raises:
            Exception: If the API request fails
        """
        url = f"{self.BASE_URL}/compress"
        
        headers = {
            "accept": "*/*",
            "content-type": "application/json",
            "x-api-key": self.api_key
        }
        
        payload = {
            "prompt": prompt,
            "model": model,
            "scaledown": {
                "rate": rate
            }
        }
        
        response = requests.post(url, headers=headers, json=payload)
        
        if response.status_code != 200:
            raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
        
        return response.json()
