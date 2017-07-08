"""coverage

Revision ID: e2ce8e26135a
Revises: 361695ca454c
Create Date: 2017-07-04 14:04:00.171859

"""
import zeus
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'e2ce8e26135a'
down_revision = '361695ca454c'
branch_labels = ()
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('filecoverage',
                    sa.Column('id', zeus.db.types.guid.GUID(), nullable=False),
                    sa.Column('job_id', zeus.db.types.guid.GUID(), nullable=False),
                    sa.Column('filename', sa.String(length=256), nullable=False),
                    sa.Column('data', sa.Text(), nullable=True),
                    sa.Column('date_created', sa.DateTime(), nullable=True),
                    sa.Column('lines_covered', sa.Integer(), nullable=True),
                    sa.Column('lines_uncovered', sa.Integer(), nullable=True),
                    sa.Column('diff_lines_covered', sa.Integer(), nullable=True),
                    sa.Column('diff_lines_uncovered', sa.Integer(), nullable=True),
                    sa.Column('repository_id', zeus.db.types.guid.GUID(), nullable=False),
                    sa.ForeignKeyConstraint(['job_id'], ['job.id'], ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(
                        ['repository_id'], ['repository.id'], ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id', 'filename'),
                    sa.UniqueConstraint('job_id', 'filename', name='unq_job_filname'))
    op.create_index(
        op.f('ix_filecoverage_repository_id'), 'filecoverage', ['repository_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_filecoverage_repository_id'), table_name='filecoverage')
    op.drop_table('filecoverage')
    # ### end Alembic commands ###
