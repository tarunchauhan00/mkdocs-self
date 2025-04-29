import yaml
import sys

# 1) Load settings (site_name, description, logo)
with open('docs/settings.yml', 'r', encoding='utf-8') as f:
    settings = yaml.safe_load(f)

# 2) Load existing mkdocs.yml
with open('mkdocs.yml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

# 3) Override with settings
config['site_name'] = settings.get('site_name', config.get('site_name'))
config['site_description'] = settings.get('site_description', config.get('site_description'))
if 'theme' not in config:
    config['theme'] = {}
config['theme']['logo'] = settings.get('logo', config['theme'].get('logo'))

# 4) Write mkdocs.yml back out
with open('mkdocs.yml', 'w', encoding='utf-8') as f:
    yaml.dump(config, f)

print("✅ main.py: mkdocs.yml updated with settings.yml values.")
