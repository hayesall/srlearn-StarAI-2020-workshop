# Experiments Subsection

This directory includes the scripts used to reproduce "Table 1."

All scripts are made available under the terms of the `MIT License`. A copy of
the license is contained in this directory.

## Setup

The results presented in this workshop were based on the
[`srlearn==0.5.0`](https://pypi.org/project/srlearn/0.5.0/) release.

```bash
pip install srlearn==0.5.0
```

## Producing the results from Table 1

> ⚠️ Results were produced in macOS High Sierra with the following specs,
> small differences are likely to occur on.
> - **Processor** 3.4 GHz Intel Core i5
> - **Memory** 16 GB 2400 MHz DDR4
> - **Graphics** Radeon Pro 570 4096 MB

### Column 1: `srlearn` (Python/Java)

Mean and standard deviation are calculated automatically.

```bash
$ python webkb.py
$ python imdb.py
$ python uwcse.py
```

### Column 2: `BoostSRL` (Java/Shell)

Mean and standard deviation are **not** calculated automatically.
They might be calculated from an interactive Python shell with `numpy`.

```bash
$ bash webkb.sh
$ bash imdb.sh
$ bash uwcse.sh
```

## Datasets

Copies of the datasets are included in the
[`datasets/`](https://github.com/hayesall/srlearn-StarAI-2020-workshop/tree/master/experiments/datasets/)
directory for completeness. All modes and parameters are held constant, the
method for running (`srlearn` or `BoostSRL`) are varied.

## Limitations

The general way that time is calculated for the `BoostSRL` numbers use Unix
epoch time from the [`BSD DATE(1)`](https://man.openbsd.org/date) command.

```bash
START_TIME=$(date +%s)
END_TIME=$(date +%s)
echo "$(($END_TIME - $START_TIME))"
```

Whereas the `srlearn` version is calculated with the
[`time.perf_counter()`](https://docs.python.org/3/library/time.html#time.perf_counter)
function in the
[`time`](https://docs.python.org/3/library/time.html)
library, leading to this general form:

```python
_start = time.perf_counter()
_end = time.perf_counter()
print(_end - _start)
```

Each method has specific overheads that makes results imperfect for direct
comparison.
