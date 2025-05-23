import os
import sys

name = sys.argv[1] if len(sys.argv) > 1 else "World"
greeting = f"Hello, {name}! 👋"
print(greeting)

# Output for GitHub Actions
with open(os.environ.get('GITHUB_OUTPUT', '/dev/null'), 'a') as f:
    f.write(f"greeting={greeting}\n")
