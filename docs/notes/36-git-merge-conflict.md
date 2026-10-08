# Git merge conflict

Category: Development

## Symptoms
- CONFLICT message after merge or pull
- Files contain <<<<<<< and >>>>>>> markers

## Cause
Two branches changed the same lines.

## Fix
1. Run git status to list conflicted files
2. Edit each file, keep the correct content and remove the markers
3. Run git add on the files and complete the merge with a commit
4. Pull more often to keep conflicts small
