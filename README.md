# Python Cookiecutter

A cookiecutter for making new Python repositories

1. Create a repository on GitHub, clone it, but *don't* change inside. For example:

    ```shell
    $ git clone git+https://github.com/cthoyt/glorious_avocado.git
    ```

2. Install `cookiecutter` with:

    ```shell
    $ pip install cookiecutter
    ```

3. Run `cookiecutter` with:

    ```shell
    $ cookiecutter https://github.com/cthoyt/cookiecutter-python-package --output-path glorious_avocado
    ```
   
   Change `glorious_avocado` to your package name.

4. Enter the requested information, then win! Remember, package names should only have letters, numbers,
   and underscores.
