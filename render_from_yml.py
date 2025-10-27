from jinja2 import Environment, FileSystemLoader
import yaml
import os
import glob

# Load Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))

# Load common variables
with open('vars/common.yml') as f:
    common_vars = yaml.safe_load(f)

# Get all host files
host_files = glob.glob('vars/*.yml')
host_files.remove('vars/common.yml')  # Remove common vars file from list

# Process each host
for host_file in host_files:
    # Extract hostname from filename (removes 'vars/' and '.yml')
    host = os.path.basename(host_file)[:-4]
    
    # Load host-specific variables
    with open(host_file) as f:
        host_vars = yaml.safe_load(f)
    
    # Combine variables
    template_vars = {**common_vars, **host_vars}
    
    # Render template
    template = env.get_template('config_from_yml.j2')
    rendered_config = template.render(template_vars)
    
    # Save rendered config
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    with open(f'{output_dir}/{host}.conf', 'w') as f:
        f.write(rendered_config)
    
    print(f"Configuration for {host} rendered to {output_dir}/{host}.conf")
