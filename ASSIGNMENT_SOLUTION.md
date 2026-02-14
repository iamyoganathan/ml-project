# Git and GitHub Assignment Solution
**ML Project Version Control**

---

## Stage 1: Basic Setup (Foundation)

### Commands to Run (from home directory):

```bash
mkdir ml-project
cd ml-project
git init
touch train.py predict.py utils.py README.md
git status
```

### What Each Command Does:
- `mkdir ml-project` → Creates new directory
- `cd ml-project` → Navigates into directory
- `git init` → Initializes Git repository
- `touch` → Creates the 4 empty files
- `git status` → Shows untracked files

---

## Stage 2: Version Control Workflow (Application)

### Commands to Commit and Push:

```bash
# 1. Stage only train.py and utils.py
git add train.py utils.py

# 2. Commit with message
git commit -m "Add training script and utilities"

# 3. Create repository on GitHub (via website)
#    → Go to github.com → New repository → Name: ml-project

# 4. Link local repo to GitHub
git remote add origin https://github.com/yourusername/ml-project.git

# 5. Rename branch to main
git branch -M main

# 6. Push to GitHub
git push -u origin main
```

### What Each Command Does:
- `git add train.py utils.py` → Stages only these 2 files
- `git commit -m "message"` → Saves staged files to repository
- `git remote add origin [url]` → Links local repo to GitHub
- `git branch -M main` → Renames branch to "main"
- `git push -u origin main` → Uploads commits to GitHub

---

## Stage 3: Collaborative Workflow (Synthesis)

### Scenario:
- Remote has: Updated predict.py and README.md (teammate pushed)
- Local has: Modified utils.py and new config.py (uncommitted)

### Commands to Sync and Push:

```bash
# 1. Get teammate's changes from GitHub
git pull origin main

# 2. Stage your local changes
git add utils.py config.py

# 3. Commit your changes
git commit -m "Add model save/load functions and configuration file"

# 4. Push to GitHub
git push origin main
```

### What Each Command Does:
- `git pull origin main` → Downloads and merges remote changes
- `git add utils.py config.py` → Stages your local files
- `git commit -m "message"` → Commits your changes
- `git push origin main` → Uploads your commits to GitHub

### Handling Common Issues:

**Merge Conflict:**
```bash
# 1. Open conflicted file and manually resolve
# 2. Remove conflict markers (<<<<<<, =======, >>>>>>>)
# 3. Stage resolved file
git add [filename]
# 4. Complete merge
git commit -m "Resolve merge conflict"
# 5. Push
git push origin main
```

**If Pull is Blocked by Local Changes:**
```bash
# Option 1: Stash changes temporarily
git stash
git pull origin main
git stash pop

# Option 2: Commit first, then pull
git add .
git commit -m "Your message"
git pull origin main
```

**Push Rejected (Remote has new commits):**
```bash
git pull origin main  # Pull first
git push origin main  # Then push
```

---

## Best Practices

1. **Always pull before starting work**: `git pull origin main`
2. **Commit often with clear messages**: Small, focused commits
3. **Push regularly**: Don't keep changes local for days
4. **Check status frequently**: `git status`
5. **Use .gitignore**: Exclude unnecessary files

---

## Quick Command Reference

```bash
# Setup
git init                    # Initialize repository
git remote add origin [url] # Add remote repository

# Basic Workflow
git status                  # Check status
git add [file]              # Stage file
git commit -m "message"     # Commit changes
git push origin main        # Push to GitHub
git pull origin main        # Pull from GitHub

# Information
git log --oneline           # View commit history
git remote -v               # View remote repositories
git diff                    # View changes

# Undo
git restore [file]          # Discard local changes
git stash                   # Save changes temporarily
```

---

## Project Files

✅ **train.py** - Model training script  
✅ **predict.py** - Prediction script  
✅ **utils.py** - Helper functions  
✅ **config.py** - Configuration parameters  
✅ **README.md** - Project documentation

---

## Repository Link
**https://github.com/iamyoganathan/ml-project**

---

**Assignment Complete** ✓ All three stages implemented successfully.
