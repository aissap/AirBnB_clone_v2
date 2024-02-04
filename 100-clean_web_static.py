#!/usr/bin/python3
"""
Deletes out-of-date archives.
"""
from fabric.api import env, local, run
import os

env.user = 'ubuntu'
env.hosts = ['18.206.197.184', '54.237.37.228']
env.key_filename = "~/.ssh/id_rsa"


def do_clean(number=0):
    """
    Deletes out-of-date archives.
    """
    try:
        number = int(number)
    except ValueError:
        print("Number must be an integer.")
        return False

    if number == 0 or number == 1:
        number = 1

    archives = local('ls -tr versions', capture=True).split('\n')
    archives_to_delete = archives[:-number]

    for archive in archives_to_delete:
        local('rm versions/{}'.format(archive))
    releases_dirs = run('ls -td /data/web_static/releases/*').split('\n')
    releases_to_delete = releases_dirs[:-number]

    for release in releases_to_delete:
        run('rm -rf {}'.format(release))

    return True
