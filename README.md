# cookiecutter

## Getting started

You'll need to [install cookiecutter][cookiecutter-install].

If you're on a Mac this is as simple as:

```sh
brew install cookiecutter
```

[cookiecutter-install]: https://cookiecutter.readthedocs.io/en/stable/installation.html

## Create a new project

Change to whereever you want to create the new project directory, then run:

```sh
cookiecutter gh:chizovation/cookiecutter
```

and follow the prompts.

## User Config

If you use Cookiecutter a lot, you’ll find it useful to have a user config
file. By default Cookiecutter tries to retrieve settings from a .cookiecutterrc
file in your home directory.

```yaml
default_context:
  # values used with chizovation's cookiecutter
  full_name: 'Devin Townsend'
  email: 'devin@example.com'
  github_owner: 'poozerOrg'
```

You can read the official documentation [here][cookiecutter-user-config].

[cookiecutter-user-config]: https://cookiecutter.readthedocs.io/en/stable/advanced/user_config.html
