# Note: Only run this when you are developing at your local.
# This script will create an initial user name and password for you to access Web UI at local.
import os
import sys
package_search_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(package_search_dir)

import airflow
from getpass import getpass

from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser


def main(argv):
    if len(argv) != 3:
        print "Usage: python init_credentials.py <user_name> <user_email>"
        print "       The script will then prompt you to set password."
    else:
        pa, pb = "", None
        while pa != pb:
            pa = getpass("Password: ")
            pb = getpass("Confirm Password: ")
            if pa == pb:
                break
            else:
                print "Passwords do not match! Please try again"
        user = PasswordUser(models.User())
        user.username = argv[1]
        user.email = argv[2]
        user.password = pa
        session = settings.Session()
        session.add(user)
        session.commit()
        session.close()

if __name__ == '__main__':
    main(sys.argv)