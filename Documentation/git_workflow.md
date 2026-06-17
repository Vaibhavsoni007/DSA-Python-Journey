# Git Workflow Guide 🚀

This file contains the Git commands used daily during my DSA journey.

---

# Daily Workflow

After completing your work:

## 1. Check Changes

```bash
git status
```

Shows:
- Modified files
- New files
- Deleted files

---

## 2. Add Changes

```bash
git add .
```

Adds all changes to the staging area.

---

## 3. Commit Changes

```bash
git commit -m "Day01 Arrays Completed"
```

Examples:

```bash
git commit -m "Completed Day01 Arrays"
git commit -m "Completed Day02 Array Operations"
git commit -m "Added Day03 Notes"
```

---

## 4. Push to GitHub

```bash
git push
```

Uploads commits to GitHub.

---

# Quick Daily Commands

```bash
git status
git add .
git commit -m "message"
git push
```

---

# Working From Another Device (Laptop)

## Clone Repository

Download the repository to your laptop.

```bash
git clone REPOSITORY_LINK
```

Example:

```bash
git clone https://github.com/username/DSA-Python-Journey.git
```

---

## Before Starting Work

Always pull the latest changes.

```bash
git pull
```

This ensures your local repository is up-to-date.

---

## After Completing Work

```bash
git add .
git commit -m "Day02 Completed"
git push
```

---

# Working Between PC and Laptop

## If Work Was Done On PC

Push changes:

```bash
git push
```

---

## Before Starting On Laptop

Pull latest changes:

```bash
git pull
```

---

## After Finishing On Laptop

```bash
git add .
git commit -m "message"
git push
```

---

## Before Returning To PC

Again:

```bash
git pull
```

---

# Important Rule ⚠️

Always remember:

```text
Pull Before Work
Push After Work
```

---

# Useful Commands

## View Commit History

```bash
git log --oneline
```

---

## Check Connected Repository

```bash
git remote -v
```

---

## Check Current Branch

```bash
git branch
```

---

## Check Repository Status

```bash
git status
```

---

# My Git Workflow

```bash
git pull
git status
git add .
git commit -m "message"
git push
```

This is the workflow I will follow throughout my DSA journey.