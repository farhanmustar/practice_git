# Training Outline

## Training Topics
* git branch
* git tags

* git config

* git graph (git log)
* git status
* git diff
* git stash

* git reset
* git checkout
* git rebase
* git mergetool

* git mv
* git rm
* git add
* git commit

* git remote
* git push
* git pull
* git ssh auth using pageant

* other git tools (e.g: git-gui(gitk), lazygit)

* vim :GV command (gv.vim)
* vim :Ggrep
* vim :G command (fugitive)
* vim :G command from vim (co remote)
* vim :Gedit
* vim :Gvdiffsplit
* vim rebase
* vim :3 way merge (dv)
* vim :Gblame

<!-- INTRODUCTION -->
# Git terminal command
## git branch and tag
* Branch is the main feature of git.
* Tag can be put on any commmit.
* All commit must be a part of a branch/tag.
* Any commit that is not accessible via branch or tag will be deleted.
  * commit cannot exist on its own.
* By default we have main or master branch.
* Can create branch which branchout from master or other branch. Can also create floating branch wich does not based on any branch.
* Here how to create, delete, list branch and tag.
  * git branch
  * git tag

## git config file
* show how to config (.gitconfig)
* show .gitignore

## git log graph
* Can visual using git log.
  * `git log --oneline --graph --all`
  * `git graph`   -- for those using Patrick's dotfiles.

## git mv rm add reset commit
* git rm will remove file from tracking branch and auto stage it for commit.
* git mv will move file or rename file and auto stage it.
  * this help git to recognize that the file is moved instead of two saperate operation.(delete old and add new file)
  * this way all the changes will display properly.
* git add will stage the file for commit.
* git commit to save the changes and put into the branch tree.
  * `git commit -m <commit msg>`

## git checkout reset rebase merge
* Git checkout allow us to switch to other branch or become headless if not co to branch(HEAD not pointing to any branch and thus cannot commit).
  * HEAD is your working location.
  * checkout to branch will auto HEAD point to that branch.
  * checkout to other thing such as commit or tags, the HEAD will not point to any branch or we called it headless.
    * When HEAD not pointing to any branch, you cannot commit message. but you can create new branch and commit after that.
* Git reset allow us to move our HEAD with its pointed branch to new location.
  * can have --hard --soft, hard will clear all and not inluded any changes, soft will maintain current state.
* Git rebase will bring all the branch from it base branch to new location.
  * It will clone commit and make duplicate on new base.
  * git rebase --abort  or --continue if have issue and resolved
* Git rebase --onto for selecting what to rebase.
* Git rebase interactive to rearrange commit and squash reword.
* git merge will take changes from one branch and merge with current tracking branch and add new commit.
  * git merge --abort or --continue if have issue and resolved
  * git mergetool to solve conflict.

## git remote pull push ssh
* git support push to upstream/remote git.
  * it can be hosted in github gitlab or even on other pc.
  * for example can push or pull from one AGV to another.
* show example how to list remote. add new remote set new url to remote.
* show example how to push. how to pull.
* show how to setup git ssh auth using pageant
  * how to create key. add key to pageant shortcut.
  * how to get public key. setup on gitlab/github. (github push ssh only)
  * how to setup putty and check remote connected to ssh agent.

<!-- CONTENT -->
# Git Workflow in Vim
## Vundle config
* .vimrc (vundle to inclue).
  * fugive
  * gv

  * gitgutter -> optional (I not use) to display changes in side column

## GV command
* Open graph
* Open changeset
* checkout using dot to run command
* r for refresh
* GV again to refresh and to open in same tab.

## G command to manage commit
* Stage changes
  * partial stage
* unstage changes
  * edit line for changes only
* delete changes (-x)
* commit using cc

## :G command line push pull 
* Gpush
* Gpull
* checkout
* reset
* rebase
* new branch

## vim :Gvdiffsplit
* Compare with previous commit

## vim :Gedit
* Edit file from diff branch
* Edit using explorer mode to list all in file.

## vim Gvdiffsplit
* edit compare in vertical split

<!-- CLOSING -->
## merge demo
* demo on merge and solve conflict if any.

## rebase demo
* solve conflict

## rebase interactive demo
* squash, rearrange, fixup

## Ggrep command
* find anything within the git repository.
* Grep find with options
* Ggrep shortcut

## git blame
* identify last commit
