# macros/main.py
import yaml
import os

def define_env(env):
    """ This function is run by mkdocs-macros-plugin. """
    # Load our settings.yml
    settings_path = os.path.join(env.project_dir, 'docs', 'settings.yml')
    with open(settings_path, 'r', encoding='utf-8') as f:
        settings = yaml.safe_load(f)
    # Expose values as template variables
    env.variables['site_settings'] = settings
