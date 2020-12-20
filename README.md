<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/django-update-sql.svg?maxAge=3600)](https://pypi.org/project/django-update-sql/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/django-update-sql.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/django-update-sql.py/actions)

### Installation
```bash
$ [sudo] pip install django-update-sql
```

#### Examples
```python
from django_update_sql import update_sql

qs = Table.objects.filter(pk=42)
kwargs = dict(key='value', updated_at=datetime.now())
update_sql(qs, **kwargs) 
```

```sql
UPDATE "table" SET "key" = 'value',"updated_at" = '2020-01-23T00:49:39'::timestamp WHERE "id" = 42
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
