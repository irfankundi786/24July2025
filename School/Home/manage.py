#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""


# import oracledb
# oracledb.init_oracle_client(lib_dir=r"D:\instantclient-basic-windows.x64-19.28.0.0.0dbru\instantclient_19_28")

import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Home.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
