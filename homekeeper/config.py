import homekeeper.common
import logging
import json
import os

fopen = homekeeper.common.fopen


class Config(object):
    """Representation of the homekeeper configuration file."""

    def __init__(self):
        self.base_directory = None
        self.dotfiles_directory = os.path.join(os.getenv('HOME'), 'dotfiles')
        self.includes = []
        self.excludes = ['.git', '.gitignore', 'LICENSE', 'README.md']
        self.cleanup_symlinks = True
        self.overwrite = True
        self.override = False

    def load(self, pathname):
        with fopen(pathname, 'r') as f:
            data = json.loads(f.read())
            if 'base' in data:
                self.base_directory = data['base']
            if 'base_directory' in data:
                self.base_directory = data['base_directory']
            if 'directory' in data:
                self.dotfiles_directory = data['directory']
            if 'dotfiles_directory' in data:
                self.dotfiles_directory = data['dotfiles_directory']
            if 'cherrypicks' in data:
                self.includes = data['cherrypicks']
            if 'includes' in data:
                self.includes = data['includes']
            if 'excludes' in data:
                self.excludes = data['excludes']
            else:
                self.excludes = []
            self.override = self.base_directory is not None
            logging.info('loaded configuration from %s', pathname)

    def save(self, pathname):
        with fopen(pathname, 'w') as f:
            data = {
                'base_directory': self.base_directory,
                'dotfiles_directory': self.dotfiles_directory,
                'includes': self.includes,
                'excludes': self.excludes,
            }
            f.write(json.dumps(data, sort_keys=True, indent=4))
            logging.info('saved configuration to %s', pathname)
