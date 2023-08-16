import json
import os
import subprocess

GIT_COMMIT_ARGS = ["git", "commit", "--no-verify", "-m"]


def do_git_commit(message):
    subprocess.run(GIT_COMMIT_ARGS + [message])


def git_initial_commits():
    path = os.getcwd()
    dotfiles = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith("."):
                dotfiles.append(file)

    # initialize git repo
    subprocess.run(["git", "init"])

    # add the dotfiles
    for file in dotfiles:
        subprocess.run(["git", "add", file])

    # commit the dotfiles
    do_git_commit("Initial commit")

    # add everything else
    subprocess.run(["git", "add", "."])
    # commit everything else
    do_git_commit("Add project files (cookiecutter)")


def setup_precommit():
    subprocess.run(
        [
            "pre-commit",
            "install",
            "--hook-type",
            "{{cookiecutter.pre_commit_hook_type}}",
        ]
    )
    # we'll run an autoupdate to make sure we have the latest version of the
    # hooks
    subprocess.run(["pre-commit", "autoupdate"])
    # if there are any changes, we'll commit them
    if subprocess.run(["git", "status", "--porcelain"], capture_output=True).stdout:
        subprocess.run(["git", "add", ".pre-commit-config.yaml"])
        do_git_commit("Update pre-commit hooks")


def setup_changesets():
    # yarn add @changesets/cli && yarn changeset init
    subprocess.run(["yarn", "add", "@changesets/cli"])
    subprocess.run(["yarn", "changeset", "init"])

    # yarn add @svitejs/changesets-changelog-github-compact
    subprocess.run(["yarn", "add", "@svitejs/changesets-changelog-github-compact"])

    # we need to replace the "changelog" entry in .changeset/config.json
    # and replace it with:
    # "changelog": ["@svitejs/changesets-changelog-github-compact", { "repo": "{{cookiecutter.github_owner}}/{{cookiecutter.project_slug}}" }]
    # it's a json file so we read, amend, and write it back out
    with open(".changeset/config.json", "r") as f:
        config = json.load(f)
        config["changelog"] = [
            "@svitejs/changesets-changelog-github-compact",
            {"repo": "{{cookiecutter.github_owner}}/{{cookiecutter.project_slug}}"},
        ]
        # we also want "commit" to be true
        config["commit"] = True

    # write the config back out
    with open(".changeset/config.json", "w") as f:
        json.dump(config, f, indent=2)

    # create our initial changeset fragment; .changeset/my-first-change.md
    with open(".changeset/my-first-change.md", "w") as f:
        f.write(
            """---
'{{cookiecutter.project_slug}}': patch
---

Inital Commit + Changesets
"""
        )

    # git add .changeset, package.json, and yarn.lock
    subprocess.run(["git", "add", ".changeset", "package.json", "yarn.lock"])
    # commit the changes
    do_git_commit("Initialise changesets")


def git_remote_and_project():
    # set the gi remote
    subprocess.run(
        [
            "git",
            "remote",
            "add",
            "origin",
            "git@github.com:{{cookiecutter.github_owner}}/{{cookiecutter.project_slug}}.git",
        ]
    )

    # if our is Darwin, call open with a URL for a new github repo
    if os.uname().sysname == "Darwin":
        # https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository
        subprocess.run(
            [
                "open",
                "https://github.com/new?name={{cookiecutter.project_slug}}&description={{cookiecutter.project_description}}&private=false&owner=@me",
            ]
        )


def do_changesets():
    return "{{ cookiecutter.init_changesets }}" == "True"


if __name__ == "__main__":
    # abort if git isn't installed
    if subprocess.run(["git", "--version"], capture_output=True).returncode != 0:
        print("Git is not installed. Aborting.")
        exit(1)

    # if we are NOT doing changesets, we need to remove the changesets files
    if not do_changesets():
        subprocess.run(["rm", "-rf", "package.json"])

    git_initial_commits()
    git_remote_and_project()
    setup_precommit()

    # we could mess about with pre-generated files, but it's easier to just let
    # the regular process do its thing
    if do_changesets():
        setup_changesets()
