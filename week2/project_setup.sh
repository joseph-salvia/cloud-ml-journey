#!/bin/bash

echo "============================"
echo "PROJECT SETUP INITIALIZATION"
echo "============================"

mkdir -p projects/new_ml_project/data/{raw,processed,exports}
mkdir -p projects/new_ml_project/{notebooks,tests,logs,configs,backups}
mkdir -p projects/new_ml_project/src/{utils,models}

touch ~/projects/new_ml_project/README.md
touch ~/projects/new_ml_project/src/main.py
touch ~/projects/new_ml_project/src/utils/helpers.py
touch ~/projects/new_ml_project/src/models/model.py
touch ~/projects/new_ml_project/tests/test_main.py
touch ~/projects/new_ml_project/configs/dev.conf
touch ~/projects/new_ml_project/configs/prod.conf
touch ~/projects/new_ml_project/logs/app.log
touch ~/projects/new_ml_project/logs/error.log

cd ~/projects/new_ml_project/backups
cp ~/projects/new_ml_project/configs/dev.conf ~/projects/new_ml_project/backups/dev.conf.bak
cp ~/projects/new_ml_project/configs/prod.conf ~/projects/new_ml_project/backups/prod.conf.bak
cd ~

echo "# New ML project" > ~/projects/new_ml_project/README.md
echo "Created on: $(date)" >> ~/projects/new_ml_project/README.md
echo "Author: Joseph Salvia" >> ~/projects/new_ml_project/README.md

echo "Files created"
find ~/projects/new_ml_project -type f
echo "Total files:"
find ~/projects/new_ml_project -type f | wc -l

echo ""
echo "Checking for Empty files"
find ~/projects -name "*.py" -size 0 -exec echo "Warning, empty file detected {}" \;

echo "============================"
echo "	SETUP COMPLETE!"
echo "============================"

tree ~/projects
