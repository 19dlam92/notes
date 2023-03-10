# ==========================================================
# CREATE
# ==========================================================

'''
INSERT INTO table
(column), (column), (column), (column)
VALUES
%(column)s, %(column)s, %(column)s, %(column)s;
'''


# ==========================================================
# GET ALL
# ==========================================================

'''
SELECT * FROM table;
'''


# ==========================================================
# GET ONE
# ==========================================================

'''
SELECT * FROM table
WHERE id = %(id)s;
'''


# ==========================================================
# JOIN
# ==========================================================

'''
SELECT * FROM table
JOIN other_table
ON table.id = other_table.foreign_key
'''

# REGULAR JOINS are useful when all tables in each column has a set of data
# EX: if we want to display ONLY owners who have pets use JOIN


# ==========================================================
# LEFT JOIN
# ==========================================================

'''
SELECT * FROM table
LEFT JOIN other_table
ON table.id = other_table.foreign_key
'''

# LEFT JOINS will include all data even if data isn't filled out in a column
# EX: if we want to display ALL owners who MAY / MAY NOT pets use LEFT JOIN


# ==========================================================
# UPDATE
# ==========================================================

'''
UPDATE table SET

WHERE

'''


# ==========================================================
# DELETE
# ==========================================================

'''
DELETE FROM table
WHERE id = %(id)s;
'''


