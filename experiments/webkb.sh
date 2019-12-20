# Copyright 2019 Alexander L. Hayes

for i in $(seq 1 10); do

  START_TIME=$(date +%s)

  java -jar v1-0.jar -l -train datasets/webkb/train1/ -trees 10 -target faculty > out.log

  END_TIME=$(date +%s)

  echo "$(($END_TIME - $START_TIME))"
done
