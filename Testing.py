def test_rule_engine():
    # Create rules and AST representations
    rule1 = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
    rule2 = "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"
    
    # Test create_rule function
    rule1_ast = create_rule(rule1)
    rule2_ast = create_rule(rule2)
    
    # Combine rules and test combined AST
    combined_rule_ast = combine_rules([rule1, rule2])
    
    # Define test data
    data1 = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
    data2 = {"age": 22, "department": "Marketing", "salary": 30000, "experience": 6}
    
    # Test evaluate_rule function
    assert evaluate_rule(rule1_ast, data1) == True
    assert evaluate_rule(rule1_ast, data2) == False
    assert evaluate_rule(combined_rule_ast, data1) == True
    assert evaluate_rule(combined_rule_ast, data2) == True
