Installation
============
The most recent release can be installed from
`PyPI <https://pypi.org/project/{{cookiecutter.package_name}}>`_ with:

.. code-block:: shell

    $ pip install {{cookiecutter.package_name}}

The most recent code and data can be installed directly from GitHub with:

.. code-block:: shell

    $ pip install git+https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.github_repository_name}}.git

To install in development mode, use the following:

.. code-block:: shell

    $ git clone git+https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.github_repository_name}}.git
    $ cd {{cookiecutter.github_repository_name}}
    $ pip install -e .
