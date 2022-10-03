rm -rf ./destination
mkdir ./destination/
. $1
python3 keystoner.py
python3 glancenator.py
python3 neytronator_1.py