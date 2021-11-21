@echo off
title cleaner

cd ..
python -Bc "import pathlib; import shutil; [shutil.rmtree(p) for p in pathlib.Path('.').rglob('.pytest_cache')]"
exit