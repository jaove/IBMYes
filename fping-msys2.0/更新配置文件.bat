@echo off
git pull

python gethost-V2Ray.py

git add .
git commit -m "Daily Update !"
git push

@pause