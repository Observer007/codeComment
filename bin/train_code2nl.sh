if [ ! -d "./log" ]; then
  mkdir log
fi
cd ../translate
nohup python ./__main__.py ../config/code2nl.yaml --train &
#python ./__main__.py ../config/code2nl.yaml --train