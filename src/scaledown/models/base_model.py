from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List

import re
from ..guides import get_guide_for_model
from ..guides.optimizer import GuideBasedOptimizer

class BaseModel(ABC):
    """Base class for AI model integrations."""
    
    def __init__(self, model_name: str, **kwargs):
        """Initialize model with configuration.
        
        Args:
            model_name: Name/identifier of the model
            **kwargs: Additional model-specific configuration
        """
        self.model_name = model_name
        self.config = kwargs
        self.guide_optimizer = GuideBasedOptimizer(model_name)
    
    @abstractmethod
    def count_tokens(self, text: str) -> int:
        """Count the number of tokens in text for this model."""
        pass
    
    @abstractmethod
    def get_token_limit(self) -> int:
        """Get the token limit for this model."""
        pass
    
    def optimize_prompt(self, prompt: str) -> str:
        """Optimize a prompt for this specific model.
        
        Args:
            prompt: The original prompt
            
        Returns:
            The optimized prompt
        """
        # Use guide-based optimization if available
        if self.guide_optimizer.has_guide():
            result = self.guide_optimizer.optimize(prompt)
            return result["optimized"]
        
        # Generic optimization if no guide available
        # Remove common unnecessary phrases
        optimized = prompt
        optimized = re.sub(r"Please\s+", "", optimized)
        optimized = re.sub(r"Could you\s+", "", optimized)
        optimized = re.sub(r"I would like you to\s+", "", optimized)
        
        return optimized
    
    def get_optimization_details(self, prompt: str) -> Dict[str, Any]:
        """Get detailed information about the prompt optimization.
        
        Args:
            prompt: The prompt to optimize
            
        Returns:
            Dictionary with optimization details
        """
        if self.guide_optimizer.has_guide():
            result = self.guide_optimizer.optimize(prompt)
            
            # Add token information
            original_count = self.count_tokens(prompt)
            optimized_count = self.count_tokens(result["optimized"])
            saved_tokens = original_count - optimized_count
            saved_percentage = (saved_tokens / original_count * 100) if original_count > 0 else 0
            
            result.update({
                "original_tokens": original_count,
                "optimized_tokens": optimized_count,
                "saved_tokens": saved_tokens,
                "saved_percentage": saved_percentage,
                "model": self.model_name
            })
            
            return result
        
        # Basic optimization details if no guide available
        optimized = self.optimize_prompt(prompt)
        original_count = self.count_tokens(prompt)
        optimized_count = self.count_tokens(optimized)
        saved_tokens = original_count - optimized_count
        saved_percentage = (saved_tokens / original_count * 100) if original_count > 0 else 0
        
        return {
            "original": prompt,
            "optimized": optimized,
            "guide_name": None,
            "guide_source": None,
            "transformations": [],
            "tip": None,
            "original_tokens": original_count,
            "optimized_tokens": optimized_count,
            "saved_tokens": saved_tokens,
            "saved_percentage": saved_percentage,
            "model": self.model_name
        }