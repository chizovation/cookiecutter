# RELEASE PROCESS

_View a visualisation of the general process [here][changeset-flow-overview]_

## Introduction

Using `changesets` means a departure from the traditional release flow of:

- feature branch
- pull request
- merge to `main`
- release created / deployed

The process now is:

- feature branch
  - including one or more files created with `yarn changeset`
- pull request
- merge to `main`

:warning: a release is no longer created at this point

:warning: a deployment is no longer triggered at this point

## Many Feature Branches

You can create and merge as many feature branches as you desire.

Through the magic of the [changesets Github action][changesets-github-action]
feature branches that are merged to `main` will create (or update) a pull
request that controls the fate of the changelog. When this special PR is
approved and merged the fragments in `.changesets/` are combined into a new
versioned entry in the CHANGELOG file.

## This Is Not A Deployment

Merging the PR will only update the changelog. Some additional work is
performed in the [Changeset Release action][changeset-release-action] to ensure
newly created tags are pushed back to the main repo.

## Github Release

When a new tag is created in the project, the
[Github Release action][github-release-action] will perform the necessary
steps to create a
[Github release][github-release]. This is NOT the same as a project deployment.

## Updating Version References In Documentation

When a new tag is created in the project, the
[Update Doc Version action][update-doc-version-action] will perform the
necessary steps to update version mentions in _specified files_ to match the
latest release version.

This is performed with the aid of `bumpversion`.

## Project Deployment

This project **does not** perform any production deployments.

<!-- markdown link bits -->

[changeset-flow-overview]: https://github.com/chizovation/changesets-changelog-info/blob/main/docs/changeset-flow-overview.md
[changeset-release-action]: .github/workflows/changeset-release.yml
[changesets-github-action]: https://github.com/changesets/action#readme
[github-release-action]: .github/workflows/github-release.yml
[github-release]: https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases
[update-doc-version-action]: .github/workflows/update-doc-version.yml
