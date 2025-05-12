#!/usr/bin/env python3
"""
Test the model-specific prompting guides
"""

import sys
import os
# Add the root directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scaledown.guides.optimizer import GuideBasedOptimizer

def test_guide(model_name, prompt):
    """Test guide optimization for a specific model and prompt."""
    print(f"Testing optimization for model: {model_name}")
    print("-" * 50)
    
    # Create optimizer
    optimizer = GuideBasedOptimizer(model_name)
    
    if not optimizer.has_guide():
        print(f"No guide found for model: {model_name}")
        return
    
    # Get guide info
    guide_info = optimizer.get_guide_info()
    print(f"Guide: {guide_info['name']} (from {guide_info['source']})")
    print(f"URL: {guide_info['url']}")
    print(f"Contains {guide_info['tip_count']} tips")
    
    # Optimize prompt
    result = optimizer.optimize(prompt)
    
    print("\nOriginal prompt:")
    print(prompt)
    
    print("\nOptimized prompt:")
    print(result["optimized"])
    
    if result["transformations"]:
        print("\nTransformations applied:")
        for i, t in enumerate(result["transformations"]):
            print(f"  {i+1}. Pattern: {t['pattern']}")
    else:
        print("\nNo transformations applied.")
    
    if result["tip"]:
        tip = result["tip"]
        print(f"\nTip: {tip['title']}")
        print(f"  {tip['description']}")
        print("  Example:")
        print(f"    Before: {tip['example']['before']}")
        print(f"    After:  {tip['example']['after']}")

def test_all_guides():
    """Test optimization with all available guides."""
    test_prompts = [
        "Could you please help me write a summary of this article about climate change?",
        "I would like you to analyze this data and tell me what patterns you see.",
        "Please kindly explain how quantum computing works if you don't mind.",
        "If it's not too much trouble, could you write a short story about a robot learning to feel emotions?"
    ]
    
    models = [
        "gpt-4",
        "claude-3-opus",
        "llama-3-70b"
    ]
    
    for model in models:
        print("\n" + "=" * 60)
        print(f"MODEL: {model}")
        print("=" * 60)
        
        # Test with the first prompt
        test_guide(model, test_prompts[0])

if __name__ == "__main__":
    test_all_guides()