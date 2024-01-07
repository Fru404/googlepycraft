import yaml

# Read YAML data from a file
with open('dossier.yaml', 'r') as yaml_file:
    loaded_data = yaml.safe_load(yaml_file)

# Access the information for "Charlie"
charlie_info = loaded_data['ref']

# Print the information for "Charlie"
print(charlie_info)