#!/usr/bin/env python3
"""
Interactive terminal UI for ScaleDown
"""

import scaledown as sd
import os
import sys

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title="ScaleDown Interactive"):
    """Print a header with the given title."""
    clear_screen()
    print("=" * 80)
    print(f"{title.center(80)}")
    print("=" * 80)
    print()

def menu_select(prompt, options):
    """Display a menu and return the selected option."""
    print(prompt)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    
    while True:
        try:
            choice = int(input("\nEnter your choice (or 0 to go back): "))
            if choice == 0:
                return None
            if 1 <= choice <= len(options):
                return choice - 1
            print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a number.")

def select_template():
    """Select a template."""
    templates = sd.sd.load("templates")
    template_options = [f"{t['id']}: {t['title']}" for t in templates]
    
    print_header("Select a Template")
    choice = menu_select("Select a template:", template_options)
    
    if choice is not None:
        template_id = templates[choice]['id']
        sd.sd.select_template(template_id)
        return True
    return False

def fill_template_values():
    """Fill in values for the current template."""
    if sd.sd.current_template is None:
        print("No template selected.")
        input("Press Enter to continue...")
        return False
    
    print_header(f"Fill Template: {sd.sd.current_template.title}")
    print(f"Template: {sd.sd.current_template.template_text}")
    print()
    
    values = {}
    for placeholder in sd.sd.current_template.placeholders:
        values[placeholder] = input(f"Enter value for [{placeholder}]: ")
    
    sd.sd.set_values(values)
    return True

def select_style():
    """Select a style."""
    styles = sd.sd.load("styles")
    style_options = [f"{s['id']}: {s['name']} - {s['description']}" for s in styles]
    
    print_header("Select a Style")
    choice = menu_select("Select a style:", style_options)
    
    if choice is not None:
        style_id = styles[choice]['id']
        sd.sd.select_style(style_id)
        return True
    return False

def create_expert_style():
    """Create an expert style."""
    domains = sd.sd.load("expert_domains")
    roles = sd.sd.load("expert_roles")
    
    print_header("Create Expert Style")
    
    # Select domain
    domain_options = [d['name'] for d in domains]
    domain_idx = menu_select("Select a domain:", domain_options)
    if domain_idx is None:
        return False
    
    # Select role
    role_options = [r['name'] for r in roles]
    role_idx = menu_select("Select a role:", role_options)
    if role_idx is None:
        return False
    
    # Get expertise level
    print("\nEnter expertise level (1-100):")
    try:
        level = int(input("Level: "))
        if level < 1 or level > 100:
            print("Level must be between 1 and 100.")
            input("Press Enter to continue...")
            return False
    except ValueError:
        print("Please enter a number.")
        input("Press Enter to continue...")
        return False
    
    # Create the style
    domain = domains[domain_idx]['name']
    role = roles[role_idx]['name']
    sd.sd.create_expert_style(domain, role, level)
    
    print(f"\nCreated expert style: {domain} {role} (Level: {level})")
    input("Press Enter to continue...")
    return True

def view_prompt():
    """View the current prompt."""
    print_header("Current Prompt")
    
    try:
        prompt = sd.sd.get_prompt()
        print(prompt)
    except ValueError as e:
        print(f"Error: {str(e)}")
    
    input("\nPress Enter to continue...")

def mock_optimize_prompt():
    """Mock-optimize the current prompt."""
    print_header("Mock Optimization")
    
    if not sd.sd.current_model:
        print("No model selected. Please select a model first.")
        input("\nPress Enter to continue...")
        return
    
    try:
        prompt = sd.sd.get_prompt()
        print("Original prompt:")
        print(prompt)
        
        result = sd.sd.optimize()
        
        print("\nOptimized prompt:")
        print(result["optimized"])
        
        print(f"\nOriginal tokens: {result['original_tokens']}")
        print(f"Optimized tokens: {result['optimized_tokens']}")
        print(f"Tokens saved: {result['saved_tokens']} ({result['saved_percentage']:.1f}%)")
        
        # Show guide information if available
        if result.get("guide_name"):
            print("\n" + "=" * 40)
            print(f"Guide: {result['guide_name']} (from {result['guide_source']})")
            print("=" * 40)
            
            if result.get("transformations"):
                print("\nTransformations applied:")
                for i, t in enumerate(result["transformations"]):
                    print(f"  {i+1}. Pattern: {t['pattern']}")
            
            if result.get("tip"):
                tip = result["tip"]
                print(f"\nTip: {tip['title']}")
                print(f"  {tip['description']}")
                print("  Example:")
                print(f"    Before: {tip['example']['before']}")
                print(f"    After:  {tip['example']['after']}")
        
    except ValueError as e:
        print(f"Error: {str(e)}")
    
    input("\nPress Enter to continue...")

def api_compress_prompt():
    """Compress prompt via ScaleDown API with carbon tracking."""
    print_header("API Compression & Carbon Tracking")
    
    if not hasattr(sd.sd, 'current_model') or not sd.sd.current_model:
        print("No model selected. Please select a model first.")
        input("\nPress Enter to continue...")
        return
    
    try:
        prompt = sd.sd.get_prompt()
        print("Original prompt:")
        print(prompt)
        
        # Get compression rate
        print("\nEnter compression rate (0.0-1.0, higher = more compression):")
        try:
            rate = float(input("Rate: "))
            if rate < 0.0 or rate > 1.0:
                print("Rate must be between 0.0 and 1.0.")
                rate = 0.5
                print(f"Using default rate: {rate}")
        except ValueError:
            rate = 0.5
            print(f"Invalid input. Using default rate: {rate}")
        
        # Get result from API
        result = sd.sd.compress_via_api(rate=rate)
        
        print("\nCompressed prompt:")
        print(result["compressed_response"])
        
        print("\nPerformance metrics:")
        print(f"Original tokens: {result['full_usage']['tokens']}")
        print(f"Original cost: ${result['full_usage']['cost']:.5f}")
        print(f"Compressed tokens: {result['compressed_usage']['tokens']}")
        print(f"Compressed cost: ${result['compressed_usage']['cost']:.5f}")
        
        print("\nSavings:")
        print(f"Token reduction: {result['comparison']['tokens']} ({result['comparison']['savings']}%)")
        print(f"Cost savings: ${result['comparison']['cost']/100000:.5f}")
        print(f"Carbon saved: {result['comparison']['carbon_saved']} gCO2e")
        print(f"Time saved: {result['comparison']['time_saved']} ms")
        
    except Exception as e:
        print(f"Error: {str(e)}")
    
    input("\nPress Enter to continue...")
    
def main_menu():
    """Display the main menu."""
    while True:
        print_header()
        
        # Show current state
        if sd.sd.current_template:
            print(f"Template: {sd.sd.current_template.title}")
        else:
            print("Template: None")
        
        if sd.sd.current_style:
            print(f"Style: {sd.sd.current_style.name}")
        else:
            print("Style: None")
        
        if hasattr(sd.sd, 'current_model') and sd.sd.current_model:
            print(f"Model: {sd.sd.current_model}")
        else:
            print("Model: None")
        
        print("\nOptions:")
        print("1. Select Template")
        print("2. Fill Template Values")
        print("3. Select Style")
        print("4. Create Expert Style")
        print("5. Select Model")
        print("6. View Prompt")
        print("7. Mock-Optimize Prompt")
        print("8. API Compress & Carbon Track")  # New option
        print("9. Exit")
        
        try:
            choice = int(input("\nEnter your choice: "))
            
            if choice == 1:
                select_template()
            elif choice == 2:
                fill_template_values()
            elif choice == 3:
                select_style()
            elif choice == 4:
                create_expert_style()
            elif choice == 5:
                select_model()
            elif choice == 6:
                view_prompt()
            elif choice == 7:
                mock_optimize_prompt()
            elif choice == 8:
                api_compress_prompt()  # New function
            elif choice == 9:
                print("\nGoodbye!")
                sys.exit(0)
            else:
                print("Invalid choice. Please try again.")
                input("Press Enter to continue...")
        except ValueError:
            print("Please enter a number.")
            input("Press Enter to continue...")
if __name__ == "__main__":
    main_menu()