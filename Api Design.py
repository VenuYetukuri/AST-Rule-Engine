def create_rule(rule_string):
    return parse_rule(rule_string)
def combine_rules(rules):
    combined_root = None
    for rule in rules:
        rule_ast = parse_rule(rule)
        if combined_root is None:
            combined_root = rule_ast
        else:
            combined_root = Node(node_type="operator", left=combined_root, right=rule_ast, value="AND")
    return combined_root
def evaluate_rule(node, data):
    if node.type == "operand":
        # Example of basic parsing; in practice, more complex parsing of conditions is needed
        attribute, operator, value = re.split(r'([<>=]+)', node.value)
        attribute, value = attribute.strip(), value.strip()
        if operator == ">":
            return data.get(attribute) > float(value)
        elif operator == "<":
            return data.get(attribute) < float(value)
        elif operator == "=":
            return data.get(attribute) == value.strip("'")
    elif node.type == "operator":
        if node.value == "AND":
            return evaluate_rule(node.left, data) and evaluate_rule(node.right, data)
        elif node.value == "OR":
            return evaluate_rule(node.left, data) or evaluate_rule(node.right, data)
    return False


