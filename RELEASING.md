# Releasing

The interop library is dual licensed under **MIT OR Apache-2.0**, at the recipient's
option. Both license texts ship with the package. `VERSION` is the stable release
version and must agree with all package metadata.

Development happens in `schematic-internal`. A release is a squash snapshot copied
to the repository of the same name under `schematic-tech`. These workflows do not
copy history, create public repositories, or push release tags.

## Trigger and behavior

After copying the reviewed snapshot to the public repository, commit it, then push
a matching version tag such as `v0.1.0`. `.github/workflows/release.yml` runs CI,
builds and tests the installable artifacts, and publishes the same verified artifacts.
It only publishes from this repository's exact `schematic-tech` name. A private-repo
tag does not publish. A normal branch push only runs CI.

The publish job uses a GitHub environment named **release**. Create that environment
in the public repository before the first release. Set its deployment rules to
allow the release tags. Required reviewers are optional; omit them if tag pushes
should publish without a second manual step. Keep Actions enabled and allow the
pinned actions used in these workflows. GitHub release uploads use the automatically
provided `GITHUB_TOKEN`; no GitHub personal access token is needed.

All public GitHub releases include source `.tar.gz` and `.zip` archives, both
licenses, and `SHA256SUMS`, alongside the language-specific artifacts. Assets are
uploaded to a draft first and the draft is then published. Already published
GitHub release assets are not overwritten on retries.

## Versions and retries

Update `VERSION` and the language's package metadata together. The first prepared
version is `0.1.0`. The release validator rejects tags that do not match the package
version. Run CI on the final public squash commit before tagging it.

If publication fails partway through, correct the external configuration and rerun
the failed GitHub Actions run for the same tag. Registry uploads skip versions
already uploaded during an earlier attempt. Do not change the contents of an
already published version or move a published tag; use a new version for code fixes.

Registry publication is separate from checker support. These packages provide
markers and runtime assumptions; they do not expand Pup/backend language discovery.

## Header, CMake, vcpkg, and Conan

There are no registry credentials to configure for this release. GitHub Actions
publishes the standalone `schematic.h`, source archives, and
`schematic-supertest-vcpkg-<version>.zip` with its normal `GITHUB_TOKEN`.

The source contains an installable CMake package (`SchematicSupertest`) exposing
`schematic::supertest`. CI checks plain C, vendoring, installation, relocation,
FetchContent from the release archive, a Conan consumer, and a vcpkg consumer.

There are two vcpkg overlays:

- `ports/schematic-supertest` in the source checkout installs that checkout.
- The release overlay ZIP is standalone. Its port downloads the release source
  archive and checks a SHA512 generated from the actual archive, without any
  placeholder hash or moving-branch dependency.

Unzip the release overlay and pass its directory to `vcpkg install
schematic-supertest --overlay-ports=/path/to/overlay`. The published archive makes
this usable immediately, without acceptance into Microsoft's central registry.
A future submission to `microsoft/vcpkg` can use the generated release port and
requires an upstream review; this workflow does not open pull requests there.

The Conan 2 recipe is included in the source archives. `conan create .` builds and
tests it in a local cache. Publishing to Conan Center similarly requires a recipe
submission and upstream review. No Conan credentials or remote are assumed here.

## Download URLs

After a `v0.1.0` release, users can download:

- `https://github.com/schematic-tech/supertest-c/releases/download/v0.1.0/schematic.h`
- `https://github.com/schematic-tech/supertest-c/releases/download/v0.1.0/supertest-c-0.1.0.tar.gz`
- `https://github.com/schematic-tech/supertest-c/releases/download/v0.1.0/schematic-supertest-vcpkg-0.1.0.zip`
- `https://raw.githubusercontent.com/schematic-tech/supertest-c/v0.1.0/include/schematic.h`

The raw `main` tree is available for browsing/development downloads; use a tag or
commit for dependencies. The header contains the MIT text and an Apache-2.0 option
notice, so a copied standalone header retains its licensing information.
