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
- **Remote (GitHub)**: Updated predict.py and README.md (teammate pushed)
- **Local (Your Computer)**: Modified utils.py and new config.py (uncommitted)

### Complete Workflow Guide

---

#### **STEP 1: Retrieve Teammate's Changes from GitHub**

Before making any changes or commits, always get the latest updates from the remote repository.

**Command:**
```bash
git pull origin main
```

**What This Does:**
1. **Fetches** the latest commits from GitHub
2. **Merges** them into your local main branch
3. Updates your local files (predict.py and README.md get teammate's changes)
4. Your uncommitted work (utils.py and config.py) remains untouched

**Alternative - Check Before Merging:**
```bash
# See what's changed on remote before pulling
git fetch origin
git log HEAD..origin/main --oneline
# Then merge when ready
git pull origin main
```

**Expected Output:**
```
remote: Counting objects: 5, done.
Unpacking objects: 100% (5/5), done.
From https://github.com/yourusername/ml-project
   abc1234..def5678  main     -> origin/main
Updating abc1234..def5678
Fast-forward
 predict.py | 10 ++++++++--
 README.md  |  5 ++++-
 2 files changed, 12 insertions(+), 3 deletions(-)
```

---

#### **STEP 2: Review Your Local Work**

Check what files you've modified locally and ensure everything looks correct.

**Command:**
```bash
git status
```

**Expected Output:**
```
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  modified:   utils.py

Untracked files:
  config.py
```

**View Your Changes:**
```bash
# See exactly what you changed in utils.py
git diff utils.py

# See all unstaged changes
git diff
```

---

#### **STEP 3: Stage Your Local Changes**

Add your modified and new files to the staging area, preparing them for commit.

**Command:**
```bash
git add utils.py config.py
```

**Alternative Options:**
```bash
# Stage all changes (modified, new, and deleted files)
git add .

# Stage only modified files (not new files)
git add -u

# Stage interactively (choose what to stage)
git add -p
```

**Verify Staging:**
```bash
git status
```

**Expected Output:**
```
On branch main
Changes to be committed:
  modified:   utils.py
  new file:   config.py
```

---

#### **STEP 4: Commit Your Local Changes**

Save your staged changes with a descriptive commit message.

**Command:**
```bash
git commit -m "Add model save/load functions and configuration file"
```

**Best Practice - Detailed Commit Message:**
```bash
git commit -m "Add model persistence and configuration

- Implement save_model() and load_model() in utils.py
- Create config.py with training parameters
- Add model path and hyperparameter settings"
```

**Expected Output:**
```
[main 9a8b7c6] Add model save/load functions and configuration file
 2 files changed, 45 insertions(+)
 create mode 100644 config.py
```

---

#### **STEP 5: Push Your Work to GitHub**

Upload your local commits to the remote repository on GitHub.

**Command:**
```bash
git push origin main
```

**What Happens:**
1. Git sends your commits to GitHub
2. Remote repository updates with your changes
3. Your commit appears in the project history
4. Teammates can now pull your changes

**Expected Output:**
```
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 856 bytes | 856.00 KiB/s, done.
Total 4 (delta 2), reused 0 (delta 0)
To https://github.com/yourusername/ml-project.git
   def5678..9a8b7c6  main -> main
```

---

### Complete Command Sequence

```bash
# Step 1: Get teammate's changes
git pull origin main

# Step 2: Check your local changes
git status
git diff utils.py

# Step 3: Stage your files
git add utils.py config.py

# Step 4: Commit with message
git commit -m "Add model save/load functions and configuration file"

# Step 5: Push to GitHub
git push origin main
```

---

### Potential Issues and Solutions

#### **Issue 1: Merge Conflict**

**When It Happens:**
You and your teammate edited the **same lines** in the **same file**.

**Error Message:**
```
Auto-merging utils.py
CONFLICT (content): Merge conflict in utils.py
Automatic merge failed; fix conflicts and then commit the result.
```

**How to Fix:**
```bash
# 1. Open the conflicted file (utils.py)
#    Look for conflict markers:
<<<<<<< HEAD
your code here
=======
teammate's code here
>>>>>>> origin/main

# 2. Manually edit to keep the correct code
#    Remove the markers (<<<<<<, =======, >>>>>>>)
#    Keep what you need from both versions

# 3. Stage the resolved file
git add utils.py

# 4. Complete the merge commit
git commit -m "Resolve merge conflict in utils.py"

# 5. Push the resolved version
git push origin main
```

**Prevention:**
- Communicate with teammates about file changes
- Pull frequently before starting work
- Work on different files when possible

---

#### **Issue 2: Local Changes Block Pull**

**When It Happens:**
Your local uncommitted changes conflict with incoming remote changes.

**Error Message:**
```
error: Your local changes to the following files would be overwritten by merge:
    utils.py
Please commit your changes or stash them before you merge.
```

**Solution 1 - Stash (Temporary Save):**
```bash
# Save your changes temporarily
git stash

# Pull remote changes
git pull origin main

# Restore your changes on top
git stash pop

# If conflicts occur after pop, resolve them
git add utils.py
git commit -m "Your message"
git push origin main
```

**Solution 2 - Commit First:**
```bash
# Commit your work first
git add utils.py config.py
git commit -m "WIP: Add model persistence"

# Then pull (may need to merge)
git pull origin main

# Push everything
git push origin main
```

**Which to Choose:**
- Use **stash** if changes are incomplete
- Use **commit** if changes are ready

---

#### **Issue 3: Push Rejected (Outdated Local)**

**When It Happens:**
Someone pushed new commits while you were working.

**Error Message:**
```
! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://github.com/yourusername/ml-project.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
```

**Solution:**
```bash
# Pull the new commits first
git pull origin main

# If no conflicts, push again
git push origin main

# If conflicts occur, resolve them:
# 1. Edit conflicted files
# 2. git add [resolved-files]
# 3. git commit -m "Merge remote changes"
# 4. git push origin main
```

**Prevention:**
Always run `git pull origin main` before `git push origin main`

---

#### **Issue 4: Accidental Changes to Wrong Files**

**When It Happens:**
You staged files you didn't mean to commit.

**Solution - Unstage Files:**
```bash
# Unstage specific file (keep changes)
git restore --staged config.py

# Unstage all files (keep changes)
git restore --staged .

# Discard unstaged changes completely (CAREFUL!)
git restore config.py
```

---

#### **Issue 5: Wrong Commit Message**

**When It Happens:**
You committed with a typo or unclear message.

**Solution - Amend Last Commit:**
```bash
# Change the last commit message
git commit --amend -m "Correct commit message"

# If already pushed, force push (use with caution)
git push --force origin main
```

**Warning:** Only amend commits that haven't been pushed, or coordinate with team first.

---

### Best Practices for Collaboration

1. **Pull First, Push Last**
   ```bash
   git pull origin main  # Always start with this
   # ... do your work ...
   git push origin main  # End with this
   ```

2. **Commit Often, Push Regularly**
   - Small commits are easier to review and merge
   - Push at least once per work session

3. **Write Clear Commit Messages**
   - Bad: "fixed stuff", "updates", "changes"
   - Good: "Add data validation to preprocessing", "Fix memory leak in training loop"

4. **Check Status Frequently**
   ```bash
   git status  # Run this often to stay aware
   ```

5. **Communicate with Team**
   - Announce when working on shared files
   - Use issues/comments on GitHub
   - Regular sync meetings

6. **Use Branches for Big Features** (Advanced)
   ```bash
   # Create feature branch
   git checkout -b feature/new-model
   
   # Work and commit on branch
   git add .
   git commit -m "Implement new model"
   
   # Push branch
   git push origin feature/new-model
   
   # Create Pull Request on GitHub for review
   ```

---

### Verification Checklist

After completing the workflow, verify:

- [ ] All teammate's changes are in your local repository
- [ ] Your changes are committed with clear message
- [ ] No uncommitted changes remain (`git status` is clean)
- [ ] Your commits are on GitHub (check website)
- [ ] No conflicts or errors occurred

**Quick Verification Commands:**
```bash
# Check if local matches remote
git status

# View recent commit history
git log --oneline -5

# Confirm remote connection
git remote -v

# See what's on GitHub vs local
git fetch origin
git log origin/main --oneline -5
```

---

### Summary: Why This Order Matters

1. **Pull first** → Get latest changes to avoid conflicts
2. **Review** → Know what you're committing
3. **Stage** → Select what to commit
4. **Commit** → Save your work locally
5. **Push** → Share your work with team

This sequence ensures smooth collaboration and minimizes conflicts!


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
