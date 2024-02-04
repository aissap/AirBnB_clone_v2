#!/usr/bin/python3
"""Fabric script to generate a .tgz archive from web_static folder."""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """ Generates a .tgz archive from web_static folder. """
    try:
        if not os.path.exists('versions'):
            local('mkdir -p versions')
        now = datetime.now()
        times = now.strftime('%Y%m%d%H%M%S')
        name = 'web_static_{}.tgz'.format(times)
        local('tar -cvzf versions/{} web_static'.format(name))

        return 'versions/{}'.format(name)
    except Exception as e:
        return None
