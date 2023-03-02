# ==========================================================
# MYSQL
# ==========================================================

# CONVENTIONS

# table naming
    # plural
    # lowercase
    # snake_casing

# table contents
    # column naming
        # singular
        # id - unique per 'user'
        # created_at - DATETIME
            # default/expression - NOW()
        # updated_at - DATETIME
            # default/expression - NOW() ON UPDATE NOW()
    # general 'checkboxes'
        # PK - primary key
        # NN - not null
        # AI - auto increment
    # AVOID key words for column naming

# PK - primary key
    # should ALWAYS be id
    # any given table only has ONE PRIMARY KEY

# foreign key
    # singular_table_name_id
    # EX: there is ONE owner that has MANY addresses

# one to many
    # table connection
        # 1:n
        # selecting the MANY table then ONE table
        # modify FOREIGN KEY to singular
    # flat - registers as ONE
    # fork - registers as MANY

# many to many
    # create a 'center' table 
        # with contents of . . . .
        # id
        # created_at - NOW()
        # updated_at - NOW() ON UPDATE NOW()
        # primary key(s)
    # naming
        # table_other_table
        # plural

# data types
    # VARCHAR
        # passwords - set to VARCHAR(255)
        # due to encryption creating a massive set of characters
    # CHAR
        # VARCHAR with tiny limit
        # states / airports
    # TEXT
        # basically VARCHAR with no limit
    # INT
        # expecting values up to 9_999_999_999
        # BIGINT goes further
        # unsigned
            # positive numbers
        # signed
            # positive and negative numbers
    # TINYINT
        # can potentially achieve booleans
        # 0 - False
        # 1 - True
    # DATETIME
        # created_at - NOW()
        # updated_at - NOW() ON UPDATE NOW()
    # etc . . . . 

# delete type cascade
    # if user is deleted 'posts' are also deleted
    # if cascade is not set 'posts' float in internet limbo


# ==========================================================
# QUERIES / SYNTAX
# ==========================================================

# basic CRUD queries

'''
SELECT * FROM table
WHERE condition(s)
'''

'''
SELECT * FROM table
JOIN other_table
ON table.id = foreign_key
WHERE condition(s)
'''

'''
INSERT INTO table (column)
VALUE $(column)s
'''

'''
UPDATE table SET
column = value
WHERE condition(s)
'''

'''
DELETE FROM table
WHERE condition(s)
'''

# ORDER BY column ASC
# ORDER BY column DESC
# WHERE id > . . . .
# WHERE id < . . . .
# WHERE id = . . . . OR id = . . . .
