# Problem

You are given two arrays 
`a`<sub>1</sub>, `a`<sub>2</sub>, ..., `a`<sub>n</sub> and `b`<sub>1</sub>, `b`<sub>2</sub>, ..., `b`<sub>n</sub>.
In each step, you can set `a`<sub>i</sub> = `b`<sub>i</sub> if `a`<sub>i</sub> ≥ `b`<sub>i</sub>.
Determine the minimum number of steps that are required to make all `a`'s equal.

## Input format

- First line: `n`
- Second line: `a`<sub>1</sub>, `a`<sub>2</sub>, ..., `a`<sub>n</sub>
- Third line: `b`<sub>1</sub>, `b`<sub>2</sub>, ..., `b`<sub>n</sub>

## Output format

Print the minimum number of steps that are required to make all 
a
's equal. If it is not possible, then print -1.

## Constraints

1 ≤ `n`, `a`<sub>i</sub>, `b`<sub>i</sub> ≤ 5000

| Sample input | Sample output |
|---|---|
| 2 | -1 |
| 5 6 | |
| 4 3 | |

| Sample input | Sample output |
|---|---|
| 5 | 8 |
| 5 7 10 5 15 | |
| 4 3 | |

**Solution**[number_of_steps.py]
