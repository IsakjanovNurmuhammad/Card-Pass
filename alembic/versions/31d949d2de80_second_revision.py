"""Second Revision

Revision ID: 31d949d2de80
Revises: 4c88a366e9a6
Create Date: 2023-10-06 21:37:15.345946

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '31d949d2de80'
down_revision: Union[str, None] = '4c88a366e9a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('admins')
    op.drop_table('students')
    op.drop_table('staff')
    op.drop_table('teachers')
    op.drop_index('ix_check-out_id', table_name='check-out')
    op.drop_table('check-out')
    op.drop_index('ix_card-pass_id', table_name='card-pass')
    op.drop_table('card-pass')
    op.drop_index('ix_check-in_id', table_name='check-in')
    op.drop_table('check-in')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('check-in',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"check-in_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('checkin_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='check-in_pkey')
    )
    op.create_index('ix_check-in_id', 'check-in', ['id'], unique=False)
    op.create_table('card-pass',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"card-pass_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('staff', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='card-pass_pkey')
    )
    op.create_index('ix_card-pass_id', 'card-pass', ['id'], unique=False)
    op.create_table('check-out',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"check-out_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('checkout_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='check-out_pkey')
    )
    op.create_index('ix_check-out_id', 'check-out', ['id'], unique=False)
    op.create_table('teachers',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('number', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='teachers_pkey')
    )
    op.create_table('staff',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('number', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='staff_pkey')
    )
    op.create_table('students',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('number', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('paid', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='students_pkey')
    )
    op.create_table('admins',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('born', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('phone_number', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('gmail', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('country', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('region', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('is_staff', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('is_superuser', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('is_verified', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='admins_pkey')
    )
    # ### end Alembic commands ###
