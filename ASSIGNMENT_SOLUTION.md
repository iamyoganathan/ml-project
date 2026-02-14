# Git and GitHub Version Control Assignment
**Python Machine Learning Project**

---

## Stage 1: Basic Setup (Foundation)

### Objective
Set up a new Python machine learning project with Git version control from scratch.

### Commands Sequence (Starting from Home Directory)

```bash
# 1. Create a new directory called ml-project
mkdir ml-project

# 2. Navigate into that directory
cd ml-project

# 3. Initialize a Git repository
git init

# 4. Create all four required files (empty files)
touch train.py predict.py utils.py README.md

# 5. Check the status of your Git repository
git status
```

### Expected Output Explanation

After running these commands, you should see:

1. **mkdir ml-project** - Creates a new directory named "ml-project"
2. **cd ml-project** - Changes your current working directory to ml-project
3. **git init** - Initializes an empty Git repository, creates a hidden .git folder
   - Output: `Initialized empty Git repository in /path/to/ml-project/.git/`
4. **touch commands** - Creates four empty files
5. **git status** - Shows:
   - Current branch: master (or main)
   - Untracked files: train.py, predict.py, utils.py, README.md
   - Message indicating no commits yet

**Key Concept**: At this point, Git is aware of the files but they are "untracked" - not yet part of version control.

---

## Stage 2: Version Control Workflow (Application)

### Scenario
You've added code to train.py and utils.py and want to commit and push these specific files to GitHub.

### Git Commands with Explanations

#### Command 1: Stage Specific Files
```bash
git add train.py utils.py
```
**What it does**: Stages only train.py and utils.py for commit. This adds these files to the "staging area" (also called the index). The staging area is where you prepare files before committing them. Note that predict.py and README.md are NOT staged.

**Why it's important**: Git allows selective staging, so you can commit related changes together while leaving unfinished work uncommitted.

---

#### Command 2: Commit with Message
```bash
git commit -m "Add training script and utilities"
```
**What it does**: Creates a commit (snapshot) of the staged files with a descriptive message. This saves the current state of train.py and utils.py to the repository history.

**Best Practice**: Use clear, descriptive commit messages in present tense (e.g., "Add feature" not "Added feature").

**Output**: Shows commit hash, files changed, and insertions/deletions count.

---

#### Command 3: Create GitHub Repository
**Note**: This is done on GitHub website, not terminal

1. Go to github.com and log in
2. Click the "+" icon in top right corner
3. Select "New repository"
4. Repository name: `ml-project`
5. Choose "Public" or "Private"
6. Do NOT initialize with README, .gitignore, or license (since you already have local code)
7. Click "Create repository"

**Result**: GitHub provides a repository URL: `https://github.com/yourusername/ml-project.git`

---

#### Command 4: Link Local Repository to GitHub
```bash
git remote add origin https://github.com/yourusername/ml-project.git
```
**What it does**: Adds a remote repository named "origin" pointing to your GitHub repository URL. "origin" is the conventional name for the primary remote repository.

**Verification**: Run `git remote -v` to see configured remotes:
```
origin  https://github.com/yourusername/ml-project.git (fetch)
origin  https://github.com/yourusername/ml-project.git (push)
```

---

#### Command 5: Rename Branch to Main (if needed)
```bash
git branch -M main
```
**What it does**: Renames the current branch to "main". Older Git versions use "master" as default, but GitHub now uses "main" as the default branch name.

**Note**: The `-M` flag forces the rename even if a branch named "main" already exists.

---

#### Command 6: Push to GitHub
```bash
git push -u origin main
```
**What it does**: 
- Uploads your local commits to the GitHub repository
- The `-u` flag (short for `--set-upstream`) sets up tracking between your local "main" branch and the remote "main" branch
- After using `-u` once, you can simply use `git push` in the future

**What happens**:
1. Git compresses your commits
2. Sends them to GitHub
3. Updates the remote repository
4. Sets up branch tracking

**Output**: Shows statistics about objects written, branch tracking information.

---

### Complete Workflow Summary
```bash
# 1. Stage specific files
git add train.py utils.py

# 2. Commit with message
git commit -m "Add training script and utilities"

# 3. Create repository on GitHub (via website)

# 4. Add remote repository
git remote add origin https://github.com/yourusername/ml-project.git

# 5. Ensure branch is named 'main'
git branch -M main

# 6. Push to GitHub
git push -u origin main
```

---

## Stage 3: Mini-Project - Collaborative Workflow (Synthesis)

### Scenario Details

**Remote Repository (GitHub) Status:**
- Teammate pushed updates to: `predict.py` and `README.md`
- These changes are on GitHub but not in your local repository

**Local Repository Status:**
- You modified: `utils.py` (uncommitted)
- You created: `config.py` (new file, uncommitted)
- These changes are local only

### Collaborative Workflow Guide

#### Step 1: Fetch and Review Remote Changes
```bash
git fetch origin
```
**What it does**: Downloads commits, files, and refs from the remote repository but DOESN'T merge them into your local branch.

**Purpose**: Allows you to see what changes exist on the remote before integrating them.

**Check what changed**:
```bash
git log HEAD..origin/main --oneline
```
This shows commits that exist on remote but not locally.

**Why this order**: Always fetch first to see what's changed before merging. This is especially important in professional environments.

---

#### Step 2: Pull Remote Changes
```bash
git pull origin main
```
**What it does**: Fetches AND merges remote changes into your current branch. Equivalent to running `git fetch` followed by `git merge`.

**What happens**:
1. Downloads teammate's changes (updated predict.py and README.md)
2. Merges them into your local main branch
3. Your local files now include teammate's updates

**Important**: Your uncommitted changes (utils.py modifications and config.py) remain untouched because Git doesn't merge uncommitted work.

**Alternative approach using rebase** (for cleaner history):
```bash
git pull --rebase origin main
```
This places your local commits on top of the remote commits, creating a linear history.

---

#### Step 3: Review Your Local Changes
```bash
git status
```
**Output shows**:
- Modified: utils.py (your local changes)
- Untracked: config.py (your new file)
- Both predict.py and README.md now have teammate's updates

**View your changes**:
```bash
git diff utils.py
```
Shows line-by-line differences in utils.py.

---

#### Step 4: Stage Your Changes
```bash
git add utils.py config.py
```
**What it does**: Stages both your modified utils.py and new config.py file for commit.

**Alternative - Stage all changes**:
```bash
git add .
```
Stages all modified and new files in the current directory and subdirectories.

**Verify staging**:
```bash
git status
```
Should show both files under "Changes to be committed".

---

#### Step 5: Commit Your Changes
```bash
git commit -m "Add model save/load functions and configuration file"
```
**Best Practice for commit messages**:
- Use imperative mood ("Add feature" not "Added feature")
- Be specific about what changed
- Keep first line under 50 characters
- Add detailed description if needed (leave blank line after first line)

**Better commit message example**:
```bash
git commit -m "Add model persistence and configuration

- Add save_model() and load_model() functions to utils.py
- Create config.py with model and training parameters
- Prepare for integration with training pipeline"
```

---

#### Step 6: Push Your Changes to GitHub
```bash
git push origin main
```
**What it does**: Uploads your new commit to GitHub.

**What happens on GitHub**:
1. Your commit is added to the main branch
2. GitHub timeline now shows: [Teammate's commits] → [Your commits]
3. Both sets of changes coexist in harmony

**No `-u` flag needed**: Since we already set up tracking in Stage 2, we can use the simpler `git push` command.

**Verify success**:
- Check GitHub website to see your changes
- Use `git log --oneline --graph --all` locally to see commit history

---

### Complete Collaborative Workflow
```bash
# Step 1: Fetch remote changes to review
git fetch origin

# Step 2: Pull (fetch + merge) teammate's changes
git pull origin main

# Step 3: Review your local modifications
git status
git diff utils.py

# Step 4: Stage your local changes
git add utils.py config.py

# Step 5: Commit your changes
git commit -m "Add model save/load functions and configuration file"

# Step 6: Push to GitHub
git push origin main
```

---

### Potential Issues and Solutions

#### Issue 1: Merge Conflicts
**When it occurs**: When you and your teammate modified the SAME lines in the SAME file.

**Symptoms**:
```
Auto-merging utils.py
CONFLICT (content): Merge conflict in utils.py
Automatic merge failed; fix conflicts and then commit the result.
```

**Solution**:
```bash
# 1. Open the conflicted file (utils.py)
# Git marks conflicts with:
<<<<<<< HEAD
your changes
=======
teammate's changes
>>>>>>> origin/main

# 2. Manually edit the file to resolve conflicts
# Remove conflict markers and keep desired code

# 3. Stage the resolved file
git add utils.py

# 4. Complete the merge
git commit -m "Resolve merge conflict in utils.py"

# 5. Push the resolved changes
git push origin main
```

---

#### Issue 2: Uncommitted Changes Block Pull
**When it occurs**: If your local changes conflict with incoming changes, Git won't let you pull.

**Error message**:
```
error: Your local changes to the following files would be overwritten by merge:
    utils.py
Please commit your changes or stash them before you merge.
```

**Solution Option 1 - Stash changes**:
```bash
# Temporarily save your changes
git stash

# Pull remote changes
git pull origin main

# Reapply your changes
git stash pop

# If conflicts occur, resolve them, then:
git add .
git commit -m "Your commit message"
git push origin main
```

**Solution Option 2 - Commit first**:
```bash
# Commit your changes first
git add utils.py config.py
git commit -m "WIP: Add model persistence functions"

# Then pull with merge
git pull origin main

# Resolve any conflicts if they occur
# Then push
git push origin main
```

---

#### Issue 3: Push Rejected (Remote Has New Commits)
**When it occurs**: Someone pushed to GitHub after you last pulled.

**Error message**:
```
! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://github.com/yourusername/ml-project.git'
hint: Updates were rejected because the remote contains work that you do not have locally.
```

**Solution**:
```bash
# Pull first to get latest changes
git pull origin main

# Resolve any conflicts if needed

# Then push again
git push origin main
```

**Prevention**: Always pull before starting work and before pushing.

---

#### Issue 4: Accidentally Committed to Wrong Branch
**Solution**:
```bash
# Reset the commit but keep changes
git reset HEAD~1

# Create and switch to correct branch
git checkout -b feature-branch

# Commit on the correct branch
git add .
git commit -m "Your message"
```

---

### Best Practices for Collaborative Development

#### 1. Communication
- Inform teammates before working on the same files
- Use GitHub Issues or project management tools
- Regular team syncs to discuss ongoing work

#### 2. Workflow Habits
- **Pull frequently**: Start each work session with `git pull`
- **Commit often**: Small, focused commits are easier to manage
- **Push regularly**: Don't keep large changes local for days
- **Test before pushing**: Ensure code works before pushing

#### 3. Branch Strategy (Recommended for larger projects)
```bash
# Create feature branch for new work
git checkout -b feature/model-optimization

# Work on your feature
# ... make changes ...

# Commit changes
git add .
git commit -m "Optimize model training performance"

# Push feature branch
git push origin feature/model-optimization

# Create Pull Request on GitHub for team review
# After approval, merge to main
```

#### 4. Commit Message Guidelines
- First line: Brief summary (50 chars max)
- Blank line
- Detailed description if needed
- Reference issue numbers: "Fix #123: Resolve training bug"

#### 5. .gitignore File
Create a `.gitignore` file to exclude:
```
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/

# Data files
*.csv
*.h5
*.pkl

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db
```

#### 6. Code Review Process
- Use Pull Requests for all major changes
- Review teammate's code before merging
- Use GitHub's review features (comments, suggestions)
- Require at least one approval before merging

---

### Verification Commands

```bash
# Check current status
git status

# View commit history with graph
git log --oneline --graph --decorate --all

# View remote repositories
git remote -v

# Check which branch you're on
git branch

# View differences before staging
git diff

# View differences of staged files
git diff --staged

# View file change history
git log --follow -- utils.py

# Check remote branch status
git remote show origin
```

---

## Summary

### Key Concepts Learned

1. **Version Control Basics**: Initializing repositories, tracking files, committing changes
2. **Remote Collaboration**: Connecting to GitHub, pushing and pulling changes
3. **Collaborative Workflow**: Managing local and remote changes, resolving conflicts
4. **Best Practices**: Commit messages, branch management, and team communication

### Command Reference Quick Sheet

```bash
# Setup
git init                          # Initialize repository
git remote add origin [url]       # Add remote repository
git clone [url]                   # Clone existing repository

# Basic Workflow
git status                        # Check repository status
git add [file]                    # Stage specific file
git add .                         # Stage all changes
git commit -m "message"           # Commit staged changes
git push origin [branch]          # Push to remote
git pull origin [branch]          # Pull from remote

# Branching
git branch                        # List branches
git branch [name]                 # Create branch
git checkout [name]               # Switch branch
git checkout -b [name]            # Create and switch branch
git merge [branch]                # Merge branch into current

# Collaboration
git fetch origin                  # Download remote changes
git pull origin main              # Fetch and merge
git push origin main              # Upload commits

# Information
git log                           # View commit history
git log --oneline                 # Compact history
git diff                          # View unstaged changes
git remote -v                     # View remotes

# Undo
git restore [file]                # Discard local changes
git reset HEAD~1                  # Undo last commit (keep changes)
git stash                         # Temporarily save changes
git stash pop                     # Restore stashed changes
```

---

## Project Files Created

1. **train.py** - Machine learning model training script with data loading and training functions
2. **predict.py** - Prediction script for making inferences with trained models
3. **utils.py** - Utility functions including data processing, model persistence, and evaluation
4. **README.md** - Project documentation
5. **config.py** - Configuration parameters for model and training settings

All files are properly tracked in Git version control and ready for collaborative development.

---

**Assignment Completed**: All three stages have been successfully implemented with practical demonstrations and comprehensive explanations of Git and GitHub version control workflows.
