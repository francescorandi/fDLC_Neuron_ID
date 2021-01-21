#!/usr/bin/env python

from distutils.core import setup
import git

requirements = [
    "numpy",
    "scipy",
    "torch",
    "gitpython"
]

# Get git commit info to build version number/tag
repo = git.Repo('.git')
git_hash = repo.head.object.hexsha
git_url = repo.remotes.origin.url
v = repo.git.describe(always=True)
if repo.is_dirty(): v += ".dirty"

setup(name='fdlc',
      version=v,
      description='Deep Learning Correspondence for Neuron ID',
      author='Xinwei Yu',
      author_email='xinweiy@princeton.edu',
      packages=['fdlc'],
      package_data={'fdlc': ['model/model.bin']},
      install_requires=requirements
)
