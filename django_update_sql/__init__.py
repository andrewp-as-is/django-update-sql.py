from django.db import connection, models


def update_sql(queryset, **kwargs):
    query = queryset.query.chain(models.sql.UpdateQuery)
    query.add_update_values(kwargs)
    compiler = query.get_compiler(queryset.db)
    sql, params = compiler.as_sql()
    cursor = connection.cursor()
    return cursor.mogrify(sql, params).decode('utf8')
