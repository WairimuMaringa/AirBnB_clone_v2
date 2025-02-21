#!/usr/bin/python3
"""
Fabric script that generates an archive from the contents
of web static folder
"""
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """ Generate tgs compress. """
    try:
        if not os.path.exists("versions"):
            local('mkdir versions')
        t = datetime.now()
        f = "%Y%m%d%H%M%S"
        archive_path = 'versions/web_static_{}.tgz'.format(t.strftime(f))
        local('tar -cvzf {} web_static'.format(archive_path))
        return archive_path
    except BaseException:
        return None
