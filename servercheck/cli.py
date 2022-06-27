from re import X
import click


@click.command()
@click.option("--filename", "-f", default=None)
@click.option("--server", "-s", default=None, multiple=True)
def cli(filename, server):
    if not filename and not server:
        raise click.UsageError("Must provide a JSON file or servers")


if __name__ == "__main__":
    cli()
