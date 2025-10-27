# Rendering configurations with jinja2

This repo is example how to render configs from tepmplate using jinja2 template engine.
There are two ways how to load variables:
- yaml files
- xls table

## How to use this example

```
git clone https://github.com/sbezo/cisco_templates_2025.git
cd cisco_templates_2025
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```
and now render config based on template and variables:
**variables from yaml files:**
```
python3 render_from_yml.py
```

**variables from xls table:**
```
python3 render_from_xls.py
```


