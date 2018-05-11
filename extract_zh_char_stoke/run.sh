
path=./Data
nohup python -u extract_zh_char_stoke.py --input ${path}/giga_small.txt --output ${path}/giga_stoke > log_extract_stoke 2>&1 &
tail -f log_extract_stoke
