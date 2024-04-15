"""update Student table

Revision ID: 114cc742a6c8
Revises: 9994f807420e
Create Date: 2024-03-27 17:19:29.979261

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '114cc742a6c8'
down_revision = '9994f807420e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.alter_column('date_of_birth',
               existing_type=sa.DATE(),
               nullable=True)
        batch_op.alter_column('father_name',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
        batch_op.alter_column('mother_name',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
        batch_op.alter_column('address',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
        batch_op.alter_column('mobile',
               existing_type=mysql.VARCHAR(length=15),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.alter_column('mobile',
               existing_type=mysql.VARCHAR(length=15),
               nullable=False)
        batch_op.alter_column('address',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
        batch_op.alter_column('mother_name',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
        batch_op.alter_column('father_name',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
        batch_op.alter_column('date_of_birth',
               existing_type=sa.DATE(),
               nullable=False)

    # ### end Alembic commands ###
