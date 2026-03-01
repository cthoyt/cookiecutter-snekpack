pinact:
  pinact run --update
  cd \{\{cookiecutter.package_name\}\} && pinact run --update

format:
    npx prettier --prose-wrap always --check "**/*.md" --write
    npx prettier --prose-wrap always --check "**/*.yaml" --write
    npx prettier --prose-wrap always --check "**/*.yml" --write
