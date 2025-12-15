# Fix for pyresparser deployment issue
# Add this to setup.sh or as a separate init script

import os
import sys

# Create config.cfg for pyresparser if it doesn't exist
pyresparser_path = None
for path in sys.path:
    potential_path = os.path.join(path, 'pyresparser')
    if os.path.exists(potential_path):
        pyresparser_path = potential_path
        break

if pyresparser_path:
    config_path = os.path.join(pyresparser_path, 'config.cfg')
    if not os.path.exists(config_path):
        # Create a minimal config file
        with open(config_path, 'w') as f:
            f.write("""[nlp]
lang = "en"
""")
        print(f"Created config.cfg at {config_path}")
