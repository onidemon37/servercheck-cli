import click
import json
import sys

from servercheck.http import ping_servers


@click.command()
@click.option("--filename", "-f", default=None)
@click.option("--server", "-s", default=None, multiple=True)
def cli(filename, server):
    if not filename and not server:
        raise click.UsageError("Must provide a JSON file or servers")

    # create a set to prevent duplicate server /port combinations
    servers = set()

    # If --filename or -f option is used then attempt to read
    # the file and add all values to the `servers` set.
    if filename:
        try:
            with open(filename) as f:
                json_servers = json.load(f)
                for s in json_servers:
                    servers.add(s)
        except:
            print("Error: Unable to open or read JSON file")
            sys.exit(1)

    # If --server or -s options are used then add those values
    if server:
        for s in server:
            servers.add(s)

    # Make requests and collect results
    results = ping_servers(servers)

    print("Successful Connections")
    print("----------------------")
    for server in results["success"]:
        print(server)

    print("\n Failed Connections")
    print("----------------------")
    for server in results["failure"]:
        print(server)
