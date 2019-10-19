if [ ! -d "./log" ]; then
  mkdir log
fi
cd ../translate
# nohup python ./__main__.py ../config/transfer.yaml --train >> log/train_transfer.log 2>&1 &
python ./__main__.py ../config/transfer.yaml --train