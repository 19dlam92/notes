# ==========================================================
# PARSING
# ==========================================================

'''

filing through and organizing data to be properly displayed


when parsing through data IF there are overlapping fields specify by . . . . 

# ==========================================================
# PARSING - GET ONE - LEFT JOIN
# ==========================================================

. . . . class method / function / query

    tables = []
    table_ids = []

    for data in results:
        if data['id'] not in table_ids:
            table_ids.append(data['id'])
            tables.append(cls(data))

        other_table_data = {
            'id' : data['other_table.id']
            'jibber' : data['jibber']
            'jabber' : data['jabber']
            'created_at' : data['other_table.created_at']
            'updated_at' : data['other_table.updated_at']
            'user_id' : data['user_id']
                foreign key
        }

        one_table.other_table.append(other_table.Other_Table(other_table_data))
        tables.append(one_table)

    return tables



    









'''

