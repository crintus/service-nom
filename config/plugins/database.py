import os
import dj_database_url

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DB', 'postgres'),
        'USER': os.environ.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'postgres'),
        'HOST': os.environ.get('POSTGRES_PORT_5432_TCP_ADDR', 'postgres'),
        'PORT': os.environ.get('POSTGRES_1_PORT_5432_TCP_PORT', 'vs')
    }
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

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# {'NAME': 'postgres', 'USER': 'postgres', 'PASSWORD': '', 'HOST': 'postgres', 'PORT': 5432, 'CONN_MAX_AGE': 500, 'ENGINE': 'django.db.backends.postgresql_psycopg2'}