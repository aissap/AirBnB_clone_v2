#!/usr/bin/python3
""" Full deployment script """
from fabric.api import env, run
from datetime import datetime
from os.path import exists
from fabric.operations import local, put

env.user = 'ubuntu'
env.hosts = ['18.206.197.184', '54.237.37.228']
env.key_filename = "~/.ssh/id_rsa"


def do_pack():
    """ Packs the contents of web_static directory """
    try:
        dt = datetime.now()
        archive_name = 'versions/web_static_{}.tgz'.format(
            dt.strftime("%Y%m%d%H%M%S"))
        local('mkdir -p versions')
        local('tar -cvzf {} web_static'.format(archive_name))
        return archive_name
    except:
        return None


def do_deploy(archive_path):
    """ Deploys the archive to web servers """
    if not exists(archive_path):
        return False

    try:
        archive_name = archive_path.split("/")[-1]
        base_name = archive_name.split(".")[0]
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


def deploy():
    """ Full deployment script """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
