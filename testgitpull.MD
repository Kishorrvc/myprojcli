didnt work
git config --global branch.autoSetupMerge always
Test `git pull`

worked (or may be combination of autoSetupMerge & --set-upstream-to)
git branch --set-upstream-to=origin/featureX featureX
Test `git pull`

conclusion:
No matter autoSetupMerge value, this works with solely --set-upstream-to
