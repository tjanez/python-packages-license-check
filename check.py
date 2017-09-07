#!/usr/bin/env python
import pkg_resources
import argparse
import sys

from pip.utils import get_installed_distributions


def main():
    parser = argparse.ArgumentParser(description="Read all installed packages from sys.path and list licenses.")
    args = parser.parse_args()

    meta_files_to_check = ['PKG-INFO', 'METADATA']

    package_data = {}

    for installed_distribution in get_installed_distributions():
        package_name = installed_distribution.project_name
        package_data[package_name] = {}
        found_license = False
        for metafile in meta_files_to_check:
            if not installed_distribution.has_metadata(metafile):
                continue
            for line in installed_distribution.get_metadata_lines(metafile):
                if 'License: ' in line:
                    (k, v) = line.split(': ', 1)
                    package_data[package_name]['license'] = v
                    found_license = True
                if 'Version: ' in line:
                    (k, v) = line.split(': ', 1)
                    package_data[package_name]['version'] = v
        if not found_license:
            package_data[project_name]['license'] = "Found no license information"

    for package in sorted(package_data.keys()):
        print('"{}" "{}" "{}"'.format(package, package_data[package]['version'], package_data[package]['license']))

if __name__ == "__main__":
    main()
