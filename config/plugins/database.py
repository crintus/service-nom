import os
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default='postgres://postgres:@postgres:5432/postgres',
        conn_max_age=500
    )
}
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'PASSWORD': os.environ.get('POSTGRES_PASSWORD', ''),
#         'HOST': os.environ.get('POSTGRES_HOST', 'postgres'),
#         'PORT': os.environ.get('POSTGRES_PORT', 5432),
#         'OPTIONS': {
#             'connect_timeout': 25,
#         }

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(dj_database_url.config(
    default='postgres://postgres:@postgres:5432/postgres',
    conn_max_age=500
))

# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)
