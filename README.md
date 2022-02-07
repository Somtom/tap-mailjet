# tap-mailjet

`tap-mailjet` is a Singer tap for mailjet.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

## Installation

- [ ] `Developer TODO:` Update the below as needed to correctly describe the install procedure. For instance, if you do not have a PyPi repo, or if you want users to directly install from your git repo, you can modify this step as appropriate.

```bash
pipx install tap-mailjet
```

## Configuration

### Accepted Config Options

```json
{
  "api_key": "your api key",
  "api_secret": "your api secret",
  "start_date": "2022-02-07T12:00:00"
}

```

- `date_start`: Starting timestamp for replications. Used in case the stream supports timestamp filtering
- `api_key`: Your Mailjet API key - can be found in [your account settings](https://app.mailjet.com/account/api_keys)
- `api_secret`: Your Mailjet API secret - can be found in [your account settings](https://app.mailjet.com/account/api_keys)


A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-mailjet --about
```

### Source Authentication and Authorization

The authentication and authorization works by using your Mailjet API keys.
The `api_key` and `api_secret` can be found in [your account settings](https://app.mailjet.com/account/api_keys)
and need to be entered in your `config.json` (see section above)

## Usage

You can easily run `tap-mailjet` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-mailjet --version
tap-mailjet --help
tap-mailjet --config CONFIG --discover > ./catalog.json
```

## Developer Resources

- [ ] `Developer TODO:` As a first step, scan the entire project for the text "`TODO:`" and complete any recommended steps, deleting the "TODO" references once completed.

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tap_mailjet/tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-mailjet` CLI interface directly using `poetry run`:

```bash
poetry run tap-mailjet --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any _"TODO"_ items listed in
the file.

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-mailjet
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-mailjet --version
# OR run a test `elt` pipeline:
meltano elt tap-mailjet target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to 
develop your own taps and targets.
