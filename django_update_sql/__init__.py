from django.db.models import sql


def update_sql(queryset, **kwargs):
    query = queryset.query.chain(sql.UpdateQuery)
    query.add_update_values(kwargs)
    compiler = query.get_compiler(queryset.db)
    sql, params = compiler.as_sql()
    return sql % params
