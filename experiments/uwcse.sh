# Copyright 2019 Alexander L. Hayes
# MIT License

for i in $(seq 1 10); do

  START_TIME=$(date +%s)

  java -jar v1-0.jar -l -train datasets/uwcse/train1/ -trees 10 -target advisedby > out.log

  END_TIME=$(date +%s)

  echo "$(($END_TIME - $START_TIME))"
done
