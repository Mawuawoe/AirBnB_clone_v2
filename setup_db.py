#!/usr/bin/python3
"""
This script drops and recreates the database schema.
"""

from models import storage

if __name__ == "__main__":
    storage.reload()
    print("Database schema recreated successfully.")
