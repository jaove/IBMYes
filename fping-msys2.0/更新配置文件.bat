@echo off
git pull

python gethost-V2Ray.py

git add .
git commit -m "Daily Update !"
git push

rem python txt2url.py
rem cd ..\..\v2rayN-Core
rem python check_v2ray.py
@pause