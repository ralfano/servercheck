import click
import json
import sys


@click.command()
@click.option("--filename", "-f", default=None)
@click.option("--server", "-s", default=None, multiple=True)
def cli(filename: str, server: str) -> None:
    if not filename and not server:
        raise click.UsageError("Must provide a JSON file or a server")
    # Create a set to prevent duplicate server/port combinations
    servers = set()
    # If --filename or -f option is used then attempt to read
    # the file and add all values to the `servers` set.
    if filename:
        try:
            print(f"opening file {filename}")
            with open(filename) as f:
                json_servers = json.load(f)
                for s in json_servers:
                    servers.add(s)
        except Exception as e:
            print(f"Error: Unable to open or read JSON file {str(e)}")
            sys.exit(1)

    # If --server or -s option are used then add those values
    # to the set.
    if server:
        print(f"server: {server}")
        for s in server:
            servers.add(s)

    print(servers)


if __name__ == "__main__":
    cli()
