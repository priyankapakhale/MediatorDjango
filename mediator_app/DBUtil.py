from django.db import connection, transaction


# Select and return list of rows having dict of column - value pairs.
def sql_select(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    ret_list = []
    i = 0
    for row in results:
        dict = {}
        field = 0
        while True:
           try:
                dict[cursor.description[field][0]] = str(results[i][field])
                field = field + 1
           except IndexError as e:
                break
        i = i + 1
        ret_list.append(dict)
    return ret_list