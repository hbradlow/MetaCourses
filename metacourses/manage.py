#!/usr/bin/env python
import os
import sys

from os.path import abspath, dirname, join

from metacourses.apps import *
from django.conf import settings

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "metacourses.settings")
    sys.path.insert(0, join(settings.PROJECT_ROOT, "apps"))
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
