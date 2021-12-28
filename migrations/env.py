import os
import sys

sys.path.append(os.getcwd())

from dotenv import dotenv_values
from logging.config import fileConfig
from os import listdir
from pymfdata.rdb.repository import Base
from pymfdata.rdb.migration import process_revision_directives

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

from common.modules.label.infrastructure.entity import LabelEntity
from common.modules.memo.infrastructure.entity import MemoEntity

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.
    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.
    Calls to context.execute() here emit the given string to the
    script output.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.
    In this scenario we need to create an Engine
    and associate a connection with the context.
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    schema = config.get_section_option(config.config_ini_section, "migration.schema")

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata,
            include_schemas=True,
            process_revision_directives=process_revision_directives,
            version_table_schema=schema
        )

        connection.execute('CREATE SCHEMA IF NOT EXISTS {0}'.format(schema))

        with context.begin_transaction():
            context.run_migrations()


env_prefix = 'common/resources/.env.'
for pfx in [f.replace('.env.', '') for f in listdir('common/resources')]:
    env = dotenv_values(env_prefix + pfx)
    config.set_section_option(pfx, 'sqlalchemy.url', '{}://{}:{}@{}:{}/{}'.format(
        env['MIGRATION_DB_ENGINE'], env['MIGRATION_DB_USER'], env['MIGRATION_DB_PASSWORD'],
        env['MIGRATION_DB_HOST'], env['MIGRATION_DB_PORT'], env['MIGRATION_DB_NAME']))
    config.set_section_option(pfx, 'migration.schema', env['MIGRATION_SCHEMA'])


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
