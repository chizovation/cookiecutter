# CONTRIBUTING

## Keeping the CHANGELOG up to date

This project uses `changesets` to manage the changelog.

Ideally you will add changeset entries locally and push with your feature
commits.

### Preparing to manage `changesets` locally

Changesets is best managed via `yarn`

```sh
brew install yarn
```

### Adding a changeset entry

#### Locally

Simply run the following:

```sh
yarn changeset
```

then follow the prompts.

#### In a Pull Request

The [changeset bot][changeset-bot] monitors pull requests and will comment with

> :warning: No Changeset found

if there are no changeset fragments.

The same comment will contain a link:

> Click here if you're a maintainer who wants to add a changeset to this PR

which will allow you to quicky add an entry using the web-editor functionality
provided by gitlab.

### Updating the changelog

The CHANGELOG file is not updated until a special pull request is approved and merged.

When that takes place, the fragments in `.changesets/` are used to construst
the changelog entry for the latest version.

## Sign Your Commits

This project (aspires to) **reject unsigned commits**.

You can read about [setting up signed commits][setup-signed].

If you need to refresh your commits to sign them
[this might be useful][quick-change-author].

[setup-signed]: https://chisel.malik-wright.uk/blog/tech/2020-07-05-signed-git-commits/
[quick-change-author]: https://chisel.malik-wright.uk/quicklets/2021-02-07-quicklet-change-author-multiple-commits/
[changeset-bot]: https://github.com/apps/changeset-bot
