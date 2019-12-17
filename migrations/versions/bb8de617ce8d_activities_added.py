"""activities added

Revision ID: bb8de617ce8d
Revises: 99c391ff2809
Create Date: 2019-12-17 15:26:40.751814

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb8de617ce8d'
down_revision = '99c391ff2809'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('activity', sa.Column('business', sa.String(), nullable=False))
    op.add_column('activity', sa.Column('business_link', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('activity', 'business_link')
    op.drop_column('activity', 'business')
    # ### end Alembic commands ###
