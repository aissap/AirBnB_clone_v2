#!/usr/bin/python3
""" Distributes an archive to your web servers """
from fabric.api import env, put, run
import os.path


env.user = 'ubuntu'
env.hosts = ["18.206.197.184", "54.237.37.228"]
env.key_filename = "~/.ssh/id_rsa"


def do_deploy(archive_path):
    """ Deploys the archive to web servers """
    if not os.path.exists(archive_path):
        return False

    try:
        archive_name = os.path.basename(archive_path)
        base_name = os.path.splitext(archive_name)[0]
        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{}/'.format(base_name))
        main = "/data/web_static/releases/{}".format(base_name)
        run('tar -xzf /tmp/{} -C {}/'.format(archive_name, main))
        run('rm /tmp/{}'.format(archive_name))
        run('mv {}/web_static/* {}/'.format(main, main))
        run('rm -rf /data/web_static/current')
        run('ln -s {}/ "/data/web_static/current"'.format(main))
        return True

    except Exception as e:
        print(e)
        return False
