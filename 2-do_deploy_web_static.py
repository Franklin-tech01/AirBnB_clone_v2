#!/usr/bin/python3
"""Deploy archive...Fabric script that generates a .tgz archive 
from the contents of the web_static folder.
Distributes an archive to a wb server"""

from fabric.operations import local, run, put, env
from os import path
from datetime import datetime


env.hosts = ['35.237.202.116', '34.73.195.113']
env.user = 'ubuntu'


def do_pack():
    """ Function to compress files i.e A Fabric script that
    generates a .tgz archive from the contents of the web_static """
    local("mkdir -p versions")
    date = datetime.datetime.now()
    date_format = date.strftime("%Y%m%d%H%M%S")
    result_archive = local("tar -cvzf versions/web_static_{}.tgz web_static"
                           .format(date_format))
    if result_archive.succeeded:
        return "versions/web_static_{}.tgz".format(date_format)
    else:
        return None


def do_deploy(archive_path):
    """ Deploy archive i.e Function to distribute an archive to a server """

    if not path.exists(archive_path):
        return False

    rex = r'^versions/(\S+).tgz'
    match = re.search(rex, archive_path)
    filename = match.group(1)
    
    # uncompress the archive
    # -x: Extract files from an archive
    # -z: Uncompress whit gzip command
    # -f: use archive file or device ARCHIVE
    # -C: Change to directory.
    res = put(archive_path, "/tmp/{}.tgz".format(filename))
    if res.failed:
        return False

    #make dir
    res = run("mkdir -p /data/web_static/releases/{}/".format(filename))
    if res.failed:
        return False

    res = run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
              .format(filename, filename))
    if res.failed:
        return False

    #delete the archive
    res = run("rm /tmp/{}.tgz".format(filename))
    if res.failed:
        return False

    #move files
    res = run("mv /data/web_static/releases/{}"
              "/web_static/* /data/web_static/releases/{}/"
              .format(filename, filename))
    if res.failed:
        return False
    res = run("rm -rf /data/web_static/releases/{}/web_static"
              .format(filename))
    if res.failed:
        return False

    #softlink to new deploy
    res = run("rm -rf /data/web_static/current")
    if res.failed:
        return False
    res = run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
              .format(filename))
    if res.failed:
        return False
    print('New version deployed!')
    return True
