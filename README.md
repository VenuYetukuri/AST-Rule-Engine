# Rule Engine with Abstract Syntax Tree (AST)

## Overview

This project implements a 3-tier rule engine that determines user eligibility based on attributes such as age, department, income, and experience. The system uses an Abstract Syntax Tree (AST) to represent conditional rules, allowing for dynamic rule creation, combination, and evaluation.

### Features

- Dynamic rule creation and modification.
- Combination of multiple rules with AND/OR logic.
- Evaluation of rules against user data.
- Flexible rule representation using AST.
- Supports operators like `AND`, `OR`, and condition checks (`>`, `<`, `=`).
- Sample rules for eligibility determination based on user attributes.

## Project Structure

- **Node Class:** Represents the AST structure for a rule.
- **Rule Parsing:** Parses a string-based rule into an AST.
- **Rule Combination:** Combines multiple ASTs into a single rule.
- **Rule Evaluation:** Evaluates a rule against user data (age, department, salary, experience, etc.).

## Requirements

- Python 3.x
- `re` module (comes with Python standard library)

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git
    cd YOUR_REPO_NAME
    ```

2. Ensure Python is installed (Python 3.x). You can check your version by running:

    ```bash
    python --version
    ```

3. Install any dependencies (if applicable). For now, this project only requires Python standard library modules.

## Usage

### 1. Create and Evaluate Rules

To create a rule, call the `create_rule` function with a string representation of the rule. Example:

```python
rule1 = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
rule_ast = create_rule(rule1)
