import yaml, os

def define_env(env):
    # Load docs/settings.yml
    cfg = os.path.join(env.project_dir, 'docs', 'settings.yml')
    with open(cfg, 'r') as f:
        settings = yaml.safe_load(f)
    env.variables['site_settings'] = settings