"""empty message

Revision ID: 2a6a02a06e03
Revises: 2e467629a577
Create Date: 2016-05-16 21:57:11.667261

"""

# revision identifiers, used by Alembic.
revision = '2a6a02a06e03'
down_revision = '2e467629a577'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notice',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=164), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_notice_timestamp'), 'notice', ['timestamp'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_notice_timestamp'), table_name='notice')
    op.drop_table('notice')
    ### end Alembic commands ###
