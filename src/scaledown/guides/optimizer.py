"""
Prompt optimization using model-specific prompting guides.
"""

import re
import random
from .prompting_guides import get_guide_for_model

class GuideBasedOptimizer:
    """Optimizer that improves prompts based on model-specific guides."""
    
    def __init__(self, model_name):
        """Initialize optimizer with a specific model name.
        
        Args:
            model_name: The name of the model to optimize for
        """
        self.model_name = model_name
        self.guide = get_guide_for_model(model_name)
    
    def has_guide(self):
        """Check if a guide exists for this model."""
        return self.guide is not None
    
    def get_guide_info(self):
        """Get basic information about the guide."""
        if not self.guide:
            return None
        
        return {
            "name": self.guide["name"],
            "source": self.guide["source"],
            "url": self.guide["url"],
            "tip_count": len(self.guide["tips"])
        }
    
    def get_random_tip(self):
        """Get a random tip from the guide."""
        if not self.guide:
            return None
        
        return random.choice(self.guide["tips"])
    
    def optimize(self, prompt_text):
        """Optimize a prompt based on the guide.
        
        Args:
            prompt_text: The prompt text to optimize
            
        Returns:
            dict: The optimization result containing:
                - original: The original prompt
                - optimized: The optimized prompt
                - guide_name: The name of the guide used
                - guide_source: The source of the guide
                - transformations: List of transformations applied
                - tip: A relevant tip from the guide
        """
        if not self.guide:
            return {
                "original": prompt_text,
                "optimized": prompt_text,
                "guide_name": None,
                "guide_source": None,
                "transformations": [],
                "tip": None
            }
        
        # Apply transformations
        optimized = prompt_text
        applied_transformations = []
        
        for transform in self.guide["transformations"]:
            pattern = transform["pattern"]
            replacement = transform["replacement"]
            
            # Check if the pattern exists in the text
            if re.search(pattern, optimized):
                # Apply the transformation
                before = optimized
                optimized = re.sub(pattern, replacement, optimized)
                
                # Record the transformation if it changed something
                if before != optimized:
                    applied_transformations.append({
                        "pattern": pattern,
                        "replacement": replacement,
                        "before": before,
                        "after": optimized
                    })
        
        # Select a relevant tip
        tip = self.get_random_tip()
        
        return {
            "original": prompt_text,
            "optimized": optimized,
            "guide_name": self.guide["name"],
            "guide_source": self.guide["source"],
            "transformations": applied_transformations,
            "tip": tip
        }