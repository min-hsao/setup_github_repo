#!/usr/bin/env python3
import os
import subprocess
import sys
import re
from getpass import getpass

def run_command(command, error_message="An error occurred", exit_on_error=True):
    try:
        result = subprocess.run(command, shell=False, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error: {error_message}")
        print(f"Details: {e.stderr}")
        if exit_on_error:
            sys.exit(1)
        return None

def create_gitignore():
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg
.env
.venv
venv/
ENV/

# IDEs
.idea/
.vscode/
*.swp
*.swo

# macOS
.DS_Store
.AppleDouble
.LSOverride
"""
    with open('.gitignore', 'w') as f:
        f.write(gitignore_content)

def create_readme(project_name, description):
    readme_content = f"""# {project_name}

{description}

## Setup
1. Clone the repository
2. Install dependencies (if any)
3. Run the project

## Usage
Describe how to use your project here.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
"""
    with open('README.md', 'w') as f:
        f.write(readme_content)

def main():
    print("GitHub Repository Setup Script")
    print("-" * 30)

    # Get user input
    github_username = input("Enter your GitHub username: ").strip()
    repo_name = input("Enter repository name: ").strip()
    description = input("Enter project description (press Enter to skip): ").strip()
    is_private = input("Make repository private? (y/n): ").lower().strip() == 'y'
    current_dir = input("Is this the directory you want to initialize? (y/n): ").lower().strip()
    
    # Validate repository name
    if not re.match(r"^[a-zA-Z0-9_-]+$", repo_name):
        print("Error: Repository name can only contain letters, numbers, '-', and '_'.")
        sys.exit(1)

    # Change directory if needed
    if current_dir != 'y':
        project_path = input("Enter the full path to your project directory: ").strip()
        if not os.path.exists(project_path):
            print(f"Error: Directory '{project_path}' does not exist.")
            sys.exit(1)
        os.chdir(project_path)

    # Initialize git if not already initialized
    if not os.path.exists('.git'):
        run_command(['git', 'init'], "Failed to initialize git repository")

    # Create .gitignore and README.md
    create_gitignore()
    create_readme(repo_name, description)

    # Add all files
    run_command(['git', 'add', '.'], "Failed to add files to git")

    # Check for staged changes
    check_changes = run_command(['git', 'status', '--porcelain'], "Failed to check changes", exit_on_error=False)
    if not check_changes.strip():
        print("No changes to commit.")
        sys.exit(0)

    # Initial commit
    run_command(['git', 'commit', '-m', 'Initial commit'], "Failed to create initial commit")

    # Check for existing GitHub CLI authentication
    auth_check = run_command(['gh', 'auth', 'status'], error_message="", exit_on_error=False)
    if "Logged in to github.com" not in auth_check:
        print("\nPlease authenticate with GitHub CLI...")
        run_command(['gh', 'auth', 'login', '-w'], "Failed to authenticate with GitHub")

    # Check for existing remote
    check_remote = run_command(['git', 'remote', 'show', 'origin'], exit_on_error=False)
    if "origin" in check_remote:
        overwrite = input("Remote 'origin' exists. Overwrite? (y/n): ").lower() == 'y'
        if not overwrite:
            print("Aborting.")
            sys.exit(1)

    # Create GitHub repository using GitHub CLI
    visibility = '--private' if is_private else '--public'
    create_repo_command = ['gh', 'repo', 'create', repo_name, visibility, '--source=.', '--remote=origin', '--push']
    run_command(create_repo_command, "Failed to create GitHub repository")

    print("\nSuccess! Your repository has been created and code pushed to GitHub.")
    print(f"Repository URL: https://github.com/{github_username}/{repo_name}")

if __name__ == "__main__":
    main()