#!/usr/bin/python3
"""
A script that packs and deploy web_static to server
"""

from datetime import datetime
from fabric.api import env, local, run, put, hide
import os


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    The archive will be named with the
    urrent timestamp to ensure unique filenames.
    Returns:
        None if there is an error during the archiving process.
    """
    try:
        # Get the current date and time in the format YYYYMMDDHHMMSS
        date_time = datetime.now().strftime("%Y%m%d%H%M%S")
        # Suppress dispaly of the command executing
        with hide('running'):
            # Print the action being performed
            local("echo 'Packing web_static to versions/web_static_{}.tgz'"
                  .format(date_time))
            # Ensure the versions directory exists
            local("mkdir -p versions/")
        # Create a .tgz archive of the web_static directory
        local("tar -cvzf versions/web_static_{}.tgz web_static"
              .format(date_time))
        return "versions/web_static_{}.tgz".format(date_time)

    except Exception as e:
        # Return None if there is an error during the process
        return None


# Define the remote servers
env.hosts = ['54.160.125.157', '52.207.208.124']

# Define the Fabric user and key filename via command-line options (-u and -i)
# Note: These are placeholders and will be replaced by the command-line options


def do_deploy(archive_path):
    """
    Deploys the .tgz archive to the remote servers.

    Args:
        archive_path: The path to the .tgz archive.

    Returns:
        True if successful, False otherwise.
    """

    if not os.path.exists(archive_path):
        return False

    try:
        # uplaod zip file to /tmp/
        put(archive_path, '/tmp/')

        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        remote_release_path = "/data/web_static/releases/{}".format(no_ext)

        # Create the release directory
        run("sudo mkdir -p {}".format(remote_release_path))

        # Uncompress the archive to the release directory
        run("sudo tar -xzf /tmp/{} -C {}"
            .format(file_name, remote_release_path))

        # Remove the archive from the /tmp/ directory
        run("sudo rm /tmp/{}".format(file_name))

        # Move the contents of the web_static directory
        # to the release directory
        # extracting create a subdirectory
        run("sudo mv {}/web_static/* {}"
            .format(remote_release_path, remote_release_path))

        # Remove the now empty web_static directory
        run("sudo rm -rf {}/web_static".format(remote_release_path))

        # Delete the current symlink
        run("sudo rm -rf /data/web_static/current")

        # Create a new symlink to the release directory
        run("sudo ln -s {} /data/web_static/current"
            .format(remote_release_path))

        print("New version deployed!")
        return True
    except Exception as e:
        return False


def deploy():
    """
    Packs and deploys the static web content to the remote servers.

    Returns:
        True if successful, False otherwise.
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
