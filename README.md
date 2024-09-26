# ai-experts-scanner
## Overview

This project is a Python-based tool that analyzes key people in a given company. It extracts and structures information about executives and founders, providing valuable insights for investment decisions.

## Features

- Searches for key executives and founders of a specified company
- Extracts structured data including names, roles, backgrounds, and importance
- Performs targeted searches for detailed background and importance information on each key person
- Utilizes LangChain for structured data extraction and Perplexity AI for web searches

## Usage
```bash
python -m venv venv
```
```bash
source venv/bin/activate # On Windows, Use `venv\Scripts\activate`
```
```bash
pip install -e ".[dev]"
```
```python
from ai_experts_scanner.scanner import analyze_company_key_people

# Example usage
company_name = "anthropic"
result = analyze_company_key_people(company_name)
print(f"Analysis for {company_name}:")
print(f"Number of key people identified: {len(result.key_people)}")
for person in result.key_people:
    print(f"\nName: {person.name}")
    print(f"Role: {person.role}")
    print(f"Background: {person.background}")
    print(f"Importance: {person.importance}")
```
