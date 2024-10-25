CREATE TABLE rules (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rule_name TEXT NOT NULL,
    rule_string TEXT NOT NULL
);

CREATE TABLE rule_metadata (
    rule_id INTEGER,
    attribute TEXT,
    value_type TEXT,
    FOREIGN KEY(rule_id) REFERENCES rules(id)
);
