# ScaleDown

![ScaleDown Logo](https://img.shields.io/badge/ScaleDown-AI%20Prompt%20Optimization-blue?style=for-the-badge)

[![PyPI version](https://img.shields.io/badge/pypi-v0.1.0-blue.svg)](https://pypi.org/project/scaledown/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Documentation](https://img.shields.io/badge/docs-latest-brightgreen.svg)](https://scaledown.ai/docs)

**ScaleDown** is a powerful Python library for optimizing prompts for large language models. It helps reduce token usage while preserving semantic meaning, saving costs and improving response quality when working with AI models like Claude, GPT, and Llama.

## ✨ Features

- 🧠 **Model-Specific Optimization**: Automatically tune prompts based on official best practices for Claude, GPT, Llama, and other LLMs
- 📊 **Token Savings**: Reduce token usage by up to 80% while maintaining prompt effectiveness
- 🧩 **Template Management**: Create, store, and reuse optimized prompt templates
- 🎨 **Style Customization**: Apply different response styles like "detailed," "concise," or "chain of thought"
- 👨‍💼 **Expert Mode**: Create domain and role-specific prompts automatically
- 🔧 **Extensible API**: Easy integration with existing AI workflows
- 🖥️ **Command-Line Interface**: Convenient CLI for prompt optimization
- 💰 Tokens Tracking: See exactly how many tokens you're saving
- 🌱 Carbon Tracking: Measure your environmental impact reduction
- ⚡ Performance Metrics: Track latency improvements


## 📋 Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Detailed Usage](#detailed-usage)
  - [Template Management](#template-management)
  - [Style Customization](#style-customization)
  - [Expert Mode](#expert-mode)
  - [Model-Specific Optimization](#model-specific-optimization)
- [CLI Usage](#cli-usage)
- [Contributing](#contributing)
- [License](#license)

## 🔧 Installation

```bash
pip install scaledown
```

For development:

```bash
git clone https://github.com/carbonscaledown/scaledown.git
cd scaledown
pip install -e .
```

## 🚀 Quick Start

```python
from scaledown import sd

# Select a template
sd.select_template("writing-1")  # Blog Post Intro

# Fill in template values
sd.set_values({"topic": "AI prompt optimization"})

# Select a style (optional)
sd.select_style("concise")

# Select a target model
sd.select_model("gpt-4")

# Generate and optimize the prompt
result = sd.optimize()

print(f"Original: {result['original']}")
print(f"Optimized: {result['optimized']}")
print(f"Tokens saved: {result['saved_tokens']} ({result['saved_percentage']:.1f}%)")
```

## 📚 Detailed Usage

### Template Management

ScaleDown includes a variety of built-in templates for common AI tasks:

```python
# List available templates
templates = sd.load("templates")
for template in templates:
    print(f"{template['id']}: {template['title']}")

# Select a template
sd.select_template("technical-1")  # Code Commenter

# Fill in template values
sd.set_values({"code": "def hello_world():\n    print('Hello, world!')"})

# Get the rendered prompt
prompt = sd.get_prompt()
```

### Style Customization

Apply different response styles to guide the AI:

```python
# List available styles
styles = sd.load("styles")
for style in styles:
    print(f"{style['id']}: {style['name']} - {style['description']}")

# Select a style
sd.select_style("chain_of_thought")

# Get the styled prompt
styled_prompt = sd.get_prompt()
```

### Expert Mode

Create domain and role-specific prompts:

```python
# List available domains and roles
domains = sd.load("expert_domains")
roles = sd.load("expert_roles")

# Create an expert style
sd.create_expert_style("Technology", "Consultant", expertise_level=85)

# Get the expert prompt
expert_prompt = sd.get_prompt()
```

### Model-Specific Optimization

Optimize prompts for specific AI models based on official best practices:

```python
# Select a model
sd.select_model("claude-3-opus")

# Get optimization details
result = sd.optimize()

print(f"Guide: {result['guide_name']} from {result['guide_source']}")
print(f"Original tokens: {result['original_tokens']}")
print(f"Optimized tokens: {result['optimized_tokens']}")
print(f"Tokens saved: {result['saved_tokens']} ({result['saved_percentage']:.1f}%)")

# Get a random tip from the guide
guide_info = sd.get_model_guide_info()
if guide_info:
    print(f"Contains {guide_info['tip_count']} optimization tips")
```

## 🖥️ CLI Usage

ScaleDown includes a command-line interface for easy optimization:

```bash
# List available templates
scaledown list templates

# Render a template with values
scaledown render technical-1 --values '{"code": "print(\"Hello world\")"}'

# Optimize a prompt
scaledown optimize technical-1 --style chain_of_thought --model gpt-4
```

For interactive usage:

```bash
python -m tests.interactive
```

### Carbon-Tracked API Compression

Use the ScaleDown API for enhanced compression with carbon tracking:

```python
# Select a model
sd.select_model("gpt-4o")

# Compress via API with carbon tracking
result = sd.compress_via_api(rate=0.5)  # 0.5 = medium compression

print(f"Original: {result['full_response']}")
print(f"Compressed: {result['compressed_response']}")
print(f"Token reduction: {result['comparison']['tokens']} ({result['comparison']['savings']}%)")
print(f"Cost savings: ${result['comparison']['cost']/100000:.5f}")
print(f"Carbon saved: {result['comparison']['carbon_saved']} gCO2e")
print(f"Time saved: {result['comparison']['time_saved']} ms")

## 🛠️ Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure your code passes the existing tests or add new tests for your feature.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- [Anthropic](https://www.anthropic.com/) for Claude prompting best practices
- [OpenAI](https://openai.com/) for GPT prompting guidelines
- [Meta AI](https://ai.meta.com/) for Llama prompting documentation

---

<p align="center">
  Made with ❤️ by <a href="https://extension.scaledown.ai">ScaleDown</a>
</p>