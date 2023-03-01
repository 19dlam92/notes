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

# data types
    # VARCHAR
    # CHAR
    # INT
    # TINYINT
    # BIGINT
    # FLOAT
    # TEXT
    # DATETIME