#!/usr/bin/python3
"""Generates a .tgz archive from the
contents of the web_static folder"""

from fabric.api import local
from datetime import datetime

def do_pack():
    """ Function to compress files i.e A Fabric script that
    generates a .tgz archive from the contents of the web_static """
    local("mkdir -p versions")
    result = local("tar -cvzf versions/web_static_{}.tgz web_static"
                   .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")),
                   capture=True)
    if result.failed:
        return None
    return result
