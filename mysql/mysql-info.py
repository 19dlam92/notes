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
            # default/expression - UPDATE NOW()
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
        # created_at
        # updated_at
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
        # updated_at - UPDATED NOW()
    # etc . . . . 