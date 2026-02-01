# Setup GitHub Repo

A Python CLI tool that automates the process of initializing a Git repository, creating essential files, and pushing to GitHub in one command.

## Features

- 🚀 Initialize Git repository
- 📝 Auto-generate `.gitignore` (Python-focused)
- 📖 Create README.md template
- 🔐 GitHub CLI authentication
- ☁️ Create and push to GitHub repository

## Requirements

- Python 3.6+
- Git
- [GitHub CLI](https://cli.github.com/) (`gh`)

## Installation

```bash
# Install GitHub CLI (macOS)
brew install gh

# No Python dependencies required
python sgr.py
```

## Usage

```bash
python sgr.py
```

The script will interactively prompt for:

1. **GitHub username**: Your GitHub account name
2. **Repository name**: Name for the new repo
3. **Description**: Project description (optional)
4. **Visibility**: Public or private repository
5. **Directory**: Current directory or specify path

## What It Does

1. ✅ Initializes Git if not already initialized
2. ✅ Creates a Python-focused `.gitignore`
3. ✅ Generates a README.md with your project details
4. ✅ Stages and commits all files
5. ✅ Authenticates with GitHub (if needed)
6. ✅ Creates the remote repository
7. ✅ Pushes your code to GitHub

## Example

```bash
$ python sgr.py
GitHub Repository Setup Script
------------------------------
Enter your GitHub username: johndoe
Enter repository name: my-awesome-project
Enter project description: A cool Python tool
Make repository private? (y/n): n
Is this the directory you want to initialize? (y/n): y

Success! Your repository has been created and code pushed to GitHub.
Repository URL: https://github.com/johndoe/my-awesome-project
```

## License

MIT License - see [LICENSE](LICENSE) for details.
