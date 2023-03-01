# Pyntax

This is a project used to demo the next generation slack platform in python.

It is an application that allows users to send test and receive an AI suggestion
on how to improve the text.

## Setup

Before getting started, make sure you have a development workspace where you
have permissions to install apps. If you don’t have one set up, go ahead and
[create one](https://slack.com/create). Also, please note that the workspace
requires any of [the Slack paid plans](https://slack.com/pricing).

### Install the Slack CLI

To use this sample, you first need to install and configure the Slack CLI.
Step-by-step instructions can be found in our
[Quickstart Guide](https://api.slack.com/future/quickstart).

### Python

This project requires python version **3.7.9** in order to execute properly,
ensure that this is your installed version with `python --version`

### Clone the Sample App

```zsh
# Clone this project onto your machine
git clone https://github.com/WilliamBergamin/pyntax.git

# Change into this project directory
cd pyntax

# Setup your python virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install the dependencies
bash setup.sh
```

In `site-packages/errant/__init__.py` update line 11 -> 16 with the bellow

```python
supported = {"en": "en_core_web_sm"}
if lang not in supported:
    raise Exception("%s is an unsupported or unknown language" % lang)

# Load spacy
nlp = nlp or spacy.load(supported[lang], disable=["ner"])
```

#### Linting

```zsh
# Run flake8 from root directory for linting
flake8 *.py && flake8 listeners/

# Run black from root directory for code formatting
black .
```

## Project Structure

### `manifest.json`

`manifest.json` is a configuration for Slack apps. With a manifest, you can
create an app with a pre-defined configuration, or adjust the configuration of
an existing app. This is also were you can define your functions and workflows
for Slack.

### `/triggers`

All trigger configuration files live in here - for this example,
`time_off_request.json` is the trigger config for a trigger that starts the Time
Off Request workflow initialized in `manifest.json`.

### `app.py`

`app.py` is the entry point for the application and is the file you'll run to
start the server. This project aims to keep this file as thin as possible,
primarily using it as a way to route inbound requests.

### `/functions`

Functions are reusable building blocks of automation that accept inputs, perform
calculations, and provide outputs. Functions can be used independently or as
steps in workflows.

### `slack.json`

Used by the CLI to interact with the project's SDK dependencies. It contains
script hooks that are executed by the CLI and implemented by the SDK.
