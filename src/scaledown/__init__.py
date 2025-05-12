from .templates import Template, TemplateManager, get_default_manager as get_default_template_manager
from .styles import Style, StyleManager, get_default_style_manager
from .api import ScaleDown
# Add the following import to enable guide-based optimization
import sys
import os
# Make sure the guides module is in the path
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

# Create a singleton instance for easy access
sd = ScaleDown()

# Export main classes
__all__ = [
    'Template', 
    'TemplateManager', 
    'Style',
    'StyleManager',
    'ScaleDown',
    'sd',
    'get_guide_for_model',
    'PROMPTING_GUIDES'
]
try:
    from .guides import get_guide_for_model, PROMPTING_GUIDES
except ImportError:
    # If the guides module doesn't exist, create placeholder functions
    def get_guide_for_model(model_name):
        return None
    PROMPTING_GUIDES = {}
