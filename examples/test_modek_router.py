#!/usr/bin/env python3
"""
Test script for the ScaleDown Model Router

This script demonstrates how the model router analyzes different types of prompts
and recommends the most appropriate model for each task.
"""

import sys
import os

# Add the project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.scaledown.routing.model_router import ModelRouter, route_prompt


def print_separator(text=""):
    """Print a formatted separator."""
    if text:
        print(f"\n{'=' * 20} {text} {'=' * 20}")
    else:
        print("\n" + "=" * 60)


def test_routing_examples():
    """Test the router with various example prompts."""
    
    test_cases = [
        # Simple tasks
        {
            "name": "Simple Translation",
            "prompt": "Translate 'Hello, how are you?' to Spanish",
            "preferences": {"speed_priority": 0.8}
        },
        {
            "name": "Basic Question",
            "prompt": "What is the capital of France?",
            "preferences": {"cost_weight": 0.9}
        },
        
        # Moderate tasks
        {
            "name": "Email Writing",
            "prompt": "Write a professional email to decline a job offer politely, explaining that I've accepted another position",
            "preferences": {}
        },
        {
            "name": "Data Analysis",
            "prompt": "Analyze this sales data and identify the top 3 trends: Q1: $1.2M, Q2: $1.5M, Q3: $1.3M, Q4: $2.1M",
            "preferences": {}
        },
        
        # Complex tasks
        {
            "name": "Code Generation",
            "prompt": """Write a Python function that implements a binary search tree with the following methods:
            - insert(value)
            - delete(value)
            - find(value)
            - inorder_traversal()
            Include proper error handling and docstrings.""",
            "preferences": {"quality_priority": 0.8}
        },
        {
            "name": "System Design",
            "prompt": "Design a scalable microservices architecture for an e-commerce platform handling 1M daily users",
            "preferences": {}
        },
        
        # Advanced tasks
        {
            "name": "Research Paper Analysis",
            "prompt": """Review this research methodology and provide expert critique on the statistical approach used 
            for analyzing the correlation between social media usage and mental health outcomes in adolescents. 
            Consider sample size, confounding variables, and statistical significance.""",
            "preferences": {"quality_priority": 0.9}
        },
        {
            "name": "Creative Writing",
            "prompt": """Write the opening chapter of a science fiction novel set in 2150 where humanity has 
            colonized Mars. Include vivid descriptions of the Martian landscape, introduce the protagonist 
            (a terraforming engineer), and establish the central conflict involving a mysterious signal from Earth.""",
            "preferences": {"quality_priority": 0.8}
        },
        
        # Special requirements
        {
            "name": "Vision Task",
            "prompt": "Look at this image and describe what you see, identify any text, and explain the color scheme used",
            "preferences": {"require_vision": True}
        },
        {
            "name": "Large Context Task",
            "prompt": "Here is a 50-page legal document: [imagine 50 pages of text here]. Summarize the key points and identify any potential legal risks",
            "preferences": {"require_large_context": True}
        },
        
        # Cost-sensitive tasks
        {
            "name": "Bulk Processing",
            "prompt": "Categorize this product description into our taxonomy: 'Blue wireless headphones with noise cancellation'",
            "preferences": {"max_cost_per_1k": 0.001, "speed_priority": 0.9}
        }
    ]
    
    router = ModelRouter()
    
    for test_case in test_cases:
        print_separator(test_case["name"])
        
        print(f"Prompt: {test_case['prompt'][:100]}{'...' if len(test_case['prompt']) > 100 else ''}")
        print(f"Preferences: {test_case['preferences']}")
        
        # Get routing decision
        decision = router.analyze_prompt(test_case["prompt"], test_case["preferences"])
        
        # Print explanation
        print(router.explain_routing(decision))
        
        input("\nPress Enter to continue to next example...")


def test_complexity_scoring():
    """Test the complexity scoring on various prompts."""
    print_separator("Complexity Scoring Test")
    
    prompts = [
        "What is 2 + 2?",
        "Explain how photosynthesis works",
        "Compare and contrast TCP and UDP protocols",
        "Implement a distributed cache with consistent hashing",
        "Design a fault-tolerant system for processing 1 billion events per day with exactly-once semantics",
        "As an expert in quantum computing, explain how Shor's algorithm threatens current cryptographic systems"
    ]
    
    router = ModelRouter()
    
    print("Complexity Scores (0-10 scale):\n")
    for prompt in prompts:
        score = router._calculate_complexity_score(prompt)
        level = router._determine_complexity_level(score)
        print(f"Score: {score:.1f} ({level.value})")
        print(f"Prompt: {prompt[:80]}{'...' if len(prompt) > 80 else ''}")
        print()


def interactive_router():
    """Interactive mode for testing custom prompts."""
    print_separator("Interactive Model Router")
    
    router = ModelRouter()
    
    while True:
        print("\nEnter your prompt (or 'quit' to exit):")
        prompt = input("> ")
        
        if prompt.lower() in ['quit', 'exit', 'q']:
            break
            
        if not prompt.strip():
            continue
            
        # Get preferences
        print("\nSet preferences (press Enter for defaults):")
        
        try:
            speed = input("Speed priority (0-1) [0.5]: ").strip()
            speed_priority = float(speed) if speed else 0.5
            
            quality = input("Quality priority (0-1) [0.5]: ").strip()
            quality_priority = float(quality) if quality else 0.5
            
            max_cost = input("Max cost per 1K tokens ($) [0.01]: ").strip()
            max_cost_per_1k = float(max_cost) if max_cost else 0.01
            
            vision = input("Requires vision? (y/n) [n]: ").strip().lower()
            require_vision = vision == 'y'
            
            preferences = {
                "speed_priority": speed_priority,
                "quality_priority": quality_priority,
                "max_cost_per_1k": max_cost_per_1k,
                "require_vision": require_vision
            }
            
        except ValueError:
            print("Invalid input. Using default preferences.")
            preferences = {}
            
        # Get and display routing decision
        decision = router.analyze_prompt(prompt, preferences)
        print(router.explain_routing(decision))
        
        # Show cost comparison
        print("\nCost Comparison (per 1K tokens):")
        for model_name, profile in router.model_profiles.items():
            if model_name in [d[0] for d in decision.alternative_models] or model_name == decision.recommended_model:
                print(f"- {profile.name}: ${profile.cost_per_1k_tokens:.4f}")


def main():
    """Main function to run all tests."""
    print("=" * 60)
    print("ScaleDown Model Router Test Suite")
    print("=" * 60)
    
    while True:
        print("\nSelect test mode:")
        print("1. Run example routing tests")
        print("2. Test complexity scoring")
        print("3. Interactive router")
        print("4. Exit")
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == '1':
            test_routing_examples()
        elif choice == '2':
            test_complexity_scoring()
        elif choice == '3':
            interactive_router()
        elif choice == '4':
            print("\nExiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
