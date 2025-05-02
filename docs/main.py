import yaml, os, sys

# Paths
ROOT = os.path.dirname(os.path.abspath(__file__))
MKDOCS_YML = os.path.join(ROOT, 'mkdocs.yml')
SETTINGS_YML = os.path.join(ROOT, 'docs', 'settings.yml')

# Load settings
try:
    with open(SETTINGS_YML) as f:
        settings = yaml.safe_load(f)
except Exception as e:
    print(f"Error loading settings.yml: {e}")
    sys.exit(1)

# Load mkdocs.yml
try:
    with open(MKDOCS_YML) as f:
        config = yaml.safe_load(f)
except Exception as e:
    print(f"Error loading mkdocs.yml: {e}")
    sys.exit(1)

# Override values
config['site_name'] = settings.get('site_name', config.get('site_name'))
config['site_description'] = settings.get('site_description', config.get('site_description'))
config.setdefault('theme', {})
config['theme']['logo'] = settings.get('logo', config['theme'].get('logo'))
config['theme']['favicon'] = settings.get('logo', config['theme'].get('favicon'))

# Write back
with open(MKDOCS_YML, 'w') as f:
    yaml.dump(config, f, sort_keys=False)

print("✅ main.py: mkdocs.yml updated.")