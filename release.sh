#!/bin/sh

sudo rm -Rf ./dist

sudo docker rmi jayshihchou/lnrun -f
sudo docker build -f docker/Dockerfile -t jayshihchou/lnrun .
sudo docker create --name lnrun jayshihchou/lnrun --entrypoint /
sudo docker cp lnrun:/app/dist .
sudo docker rm -f lnrun

python -m pip install --upgrade twine
python -m twine upload ./dist/lnrun*.whl --verbose
