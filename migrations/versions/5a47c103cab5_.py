"""empty message

Revision ID: 5a47c103cab5
Revises: 10c126fb4bae
Create Date: 2016-05-15 11:39:42.205415

"""

# revision identifiers, used by Alembic.
revision = '5a47c103cab5'
down_revision = '10c126fb4bae'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_animes_timestamp', table_name='animes')
    op.drop_index('ix_articles_timestamp', table_name='articles')
    op.drop_index('ix_courses_timestamp', table_name='courses')
    op.drop_index('ix_movies_timestamp', table_name='movies')
    op.drop_index('ix_photos_timestamp', table_name='photos')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_photos_timestamp', 'photos', ['timestamp'], unique=False)
    op.create_index('ix_movies_timestamp', 'movies', ['timestamp'], unique=False)
    op.create_index('ix_courses_timestamp', 'courses', ['timestamp'], unique=False)
    op.create_index('ix_articles_timestamp', 'articles', ['timestamp'], unique=False)
    op.create_index('ix_animes_timestamp', 'animes', ['timestamp'], unique=False)
    ### end Alembic commands ###
