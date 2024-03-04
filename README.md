# MicroRSS

MicroRSS is a really simple RSS reader; given a file containing a list of
RSS feeds, it produces a HTML file containing links to the latest items
from all the feeds.

## Usage

Invoke the script like this:

```sh
python generate.py INFILE OUTFILE
```

`INFILE` is expected to be a file containing a list of URLs that point to RSS
or Atom feeds, with one URL per line. If the `INFILE` argument is omitted,
URLs will be read from `STDIN`.

`OUTFILE` is the output HTML file. If the `OUTFILE` argument is omitted,
the output will be sent to `STDOUT`.
