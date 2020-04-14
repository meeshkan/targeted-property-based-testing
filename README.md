# Introduction to targeted property-based testing

See the slides at [https://meeshkan.github.io/targeted-property-based-testing/](https://meeshkan.github.io/targeted-property-based-testing/).

## [`elixir-propcheck`](./elixir-propcheck)

Examples of property-based testing including targeted property-based testing written in [Elixir](https://elixir-lang.org/) with [PropCheck](https://github.com/alfert/propcheck).

The project was initialized using [`mix`](https://elixir-lang.org/getting-started/mix-otp/introduction-to-mix.html):

```bash
$ mix new elixir-propcheck --app pbt
```

`mix` comes with [Elixir](https://elixir-lang.org/install.html).

## [`python-hypothesis`](./python-hypothesis)

Examples of targeted property-based testing using the [`Hypothesis`](https://hypothesis.readthedocs.io/en/latest/) library:

- [`python-hypothesis/test_targeted_pbt.py`](./python-hypothesis/test_targeted_pbt.py): Examples for learning targeted PBT in Hypothesis

## [`erlang-targeted-pbt`](./erlang-targeted-pbt)

Examples of targeted property-based testing in [Erlang](https://www.erlang.org/). Project initialized with [rebar3](https://www.rebar3.org/):

```bash
$ rebar3 new lib erlang-targeted-pbt
```
