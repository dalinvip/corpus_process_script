nohup python -u convert_tag.py --input ./Data/srl/srl.test.conll --output ./Data/srl_bmeso/srl.test.conll.bmeso --tag bmeso > log 2>&1 &
tail -f log

