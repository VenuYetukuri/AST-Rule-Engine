class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type    # "operator" or "operand"
        self.left = left         # Left child node
        self.right = right       # Right child node
        self.value = value
import re

def parse_rule(rule_string):
    # Simplified parsing logic (a full implementation would need to handle nested expressions and parentheses)
    if "AND" in rule_string:
        left_part, right_part = rule_string.split("AND", 1)
        left_node = parse_rule(left_part.strip())
        right_node = parse_rule(right_part.strip())
        return Node(node_type="operator", left=left_node, right=right_node, value="AND")
    elif "OR" in rule_string:
        left_part, right_part = rule_string.split("OR", 1)
        left_node = parse_rule(left_part.strip())
        right_node = parse_rule(right_part.strip())
        return Node(node_type="operator", left=left_node, right=right_node, value="OR")
    else:
        return Node(node_type="operand", value=rule_string.strip())

# Example usage:
rule1_ast = parse_rule("((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)")

