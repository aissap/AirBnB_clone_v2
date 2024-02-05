#!/usr/bin/python3
""" Distributes an archive to your web servers """
from fabric.api import env
from fabric.api import put
from fabric.api import run
import os.path


env.user = 'ubuntu'
env.hosts = ["18.206.197.184", "54.237.37.228"]
env.key_filename = "~/id_rsa"


def do_deploy(archive_path):
    """ Deploys the archive to web servers """
    if os.path.exists(archive_path) is False:
        return False

    try:
        archive_name = os.path.basename(archive_path)
        base_name = os.path.splitext(archive_name)[0]
        put(archive_path, '/tmp/')
        sudo('mkdir -p /data/web_static/releases/{}/'.format(base_name))
        main = "/data/web_static/releases/{}".format(base_name)
        sudo('tar -xzf /tmp/{} -C {}/'.format(archive_name, main))
        sudo('rm /tmp/{}'.format(archive_name))
        sudo('mv {}/web_static/* {}/'.format(main, main))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s {}/ "/data/web_static/current"'.format(main))
        return True

    except:
        return False
