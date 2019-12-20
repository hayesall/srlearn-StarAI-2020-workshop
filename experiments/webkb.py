# Copyright © 2019 Alexander L. Hayes

from srlearn.rdn import BoostedRDN
from srlearn import Database
from srlearn import Background

import numpy as np
import time

_run_times = 10

_train_times = []

for _ in range(_run_times):

    db = Database.from_files(
        pos="datasets/webkb/train1/train1_pos.txt",
        neg="datasets/webkb/train1/train1_neg.txt",
        facts="datasets/webkb/train1/train1_facts.txt",
    )

    bk = Background(
        modes=[
            "courseprof(-Course, +Person).",
            "courseprof(+Course, -Person).",
            "courseta(+Course, -Person).",
            "courseta(-Course, +Person).",
            "faculty(+Person).",
            "project(-Proj, +Person).",
            "project(+Proj, -Person).",
            "sameperson(-Person, +Person).",
        ],
    )

    clf = BoostedRDN(
        background=bk,
        target="faculty",
        node_size=2,
        max_tree_depth=3,
    )

    _start = time.perf_counter()

    clf.fit(db)

    _end = time.perf_counter()

    _difference = _end - _start
    print(_difference)
    _train_times.append(_difference)

print("Mean runtime for `clf.fit()` and standard deviation:")
print(np.mean(_train_times))
print(np.std(_train_times))

print("Raw numbers", _train_times)
