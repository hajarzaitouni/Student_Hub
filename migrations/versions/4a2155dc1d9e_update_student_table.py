"""update student table

Revision ID: 4a2155dc1d9e
Revises: b13a186d4afe
Create Date: 2024-04-04 13:53:04.750842

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4a2155dc1d9e'
down_revision = 'b13a186d4afe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.alter_column('academic_year',
               existing_type=mysql.VARCHAR(length=120),
               type_=sa.Integer(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.alter_column('academic_year',
               existing_type=sa.Integer(),
               type_=mysql.VARCHAR(length=120),
               existing_nullable=False)

    # ### end Alembic commands ###
