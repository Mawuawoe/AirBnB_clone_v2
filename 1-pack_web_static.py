#!/usr/bin/env python3
"""
A script that archives the contents of web_static folder
"""
from datetime import datetime
from fabric.api import local, hide


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

    except Exception as e:
        # Return None if there is an error during the process
        return None
