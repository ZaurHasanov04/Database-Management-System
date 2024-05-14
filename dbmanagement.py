import click
import sqlite3

DB_NAME = 'sqlite3.db'

@click.group
def cli():
    pass


@click.command()
@click.option('--query', prompt = True)
def create_table(query):
    execute_query(query)
    click.echo("Created Table Successfully!")


@click.command()
@click.option('--query', prompt = True)
def insert(query):
    execute_query(query)
    click.echo('Insert Successfully')


def execute_query(query):
    # Execute SQL query
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    cli.add_command(create_table)
    # cli.add_command(logout)
    # cli.add_command(select)
    cli.add_command(insert)
    # cli.add_command(delete)
    cli()






