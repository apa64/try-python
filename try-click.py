#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Command line args with Click.

See:
- https://click.palletsprojects.com/

Usage:
    python3 try-cli.py --help
    python3 try-cli.py --count 3 Nimi
"""

import click

@click.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def main(count, name):
    for x in range(count):
        click.echo('Hello %s!' % name)
    print(f"Done.")


if __name__ == "__main__":
    main()
