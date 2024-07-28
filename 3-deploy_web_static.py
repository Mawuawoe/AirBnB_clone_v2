#!/usr/bin/python3
"""
A sript to pack & deploy
"""
from datetime import datetime
from fabric.api import env, local, put, run, task
from os.path import exists

# Define the remote servers
env.hosts = ['52.55.249.213', '54.157.32.137']

@task
def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.

    Returns:
        The path to the created archive, or None if there was an error.
    """
    try:
        date_time = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(date_time)

        print('Packing web_static to {}'.format(archive_path))
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except Exception as e:
        print(e)
        return None

@task
def do_deploy(archive_path):
    """
    Deploys the .tgz archive to the remote servers.

    Args:
        archive_path: The path to the .tgz archive.

    Returns:
        True if successful, False otherwise.
    """
    if not exists(archive_path):
        print("Archive path doesn't exist")
        return False

    try:
        # Extract file name and directory name from the archive path
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        remote_tmp_path = "/tmp/{}".format(file_name)
        remote_release_path = "/data/web_static/releases/{}".format(no_ext)

        # Upload the archive to the /tmp/ directory on the remote server
        put(archive_path, remote_tmp_path)

        # Create the release directory
        run("mkdir -p {}".format(remote_release_path))

        # Uncompress the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_tmp_path, remote_release_path))

        # Remove the archive from the /tmp/ directory
        run("rm {}".format(remote_tmp_path))

        # Move the contents of the web_static directory to the release directory
        run("mv {}/web_static/* {}".format(remote_release_path, remote_release_path))

        # Remove the now empty web_static directory
        run("rm -rf {}/web_static".format(remote_release_path))

        # Delete the current symlink
        run("rm -rf /data/web_static/current")

        # Create a new symlink to the release directory
        run("ln -s {} /data/web_static/current".format(remote_release_path))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False

@task
def deploy():
    """
    Packs and deploys the static web content to the remote servers.

    Returns:
        True if successful, False otherwise.
    """
    archive_path = do_pack()
    if archive_path is None:
        print("Packing failed")
        return False
    return do_deploy(archive_path)
