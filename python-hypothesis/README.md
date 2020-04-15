# Examples of targeted PBT with [`hypothesis`](https://hypothesis.readthedocs.io/)

Examples of targeted property-based testing using the [`Hypothesis`](https://hypothesis.readthedocs.io/en/latest/) library:

- [`test_pathgen.py`](./test_pathgen.py): Standard example of targeted data generation.
- [`test_quicksort.py`](./test_quicksort.py): Attempt to reproduce worst-case behaviour of naive quick-sort by maximizing run-time.

## Instructions

```bash
$ pip install -r requirements.txt
$ pytest
```

More commonly, you want to run specific tests with full logging like this:

```bash
$ pytest -s test_pathgen.py -k paths_with_target --hypothesis-show-statistics
```

The `--hypothesis-show-statistics` flag comes with the Hypothesis Pytest [plugin](https://hypothesis.readthedocs.io/en/latest/details.html#the-hypothesis-pytest-plugin).
