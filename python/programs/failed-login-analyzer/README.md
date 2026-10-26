# Failed Login Analyzer

A simple Python script that reads an SSH authentication log and finds failed login attempts.

## What it does
- Counts all failed login attempts
- Finds the IP address with the most failed attempts
- Flags IP addresses that reach a configurable number of failed attempts

## How to run
Put `analyzer.py` and `sample-auth.log` in the same folder, then run:

```
python analyzer.py
```

The alert threshold is set by the `THRESHOLD` constant at the top of `analyzer.py`.

## Example output
```
Most failed attempts: 203.0.113.50 (7 times)
Total failed logins: 13
Suspicious IPs (3+ failed attempts):
203.0.113.50 (7 times)
192.0.2.77 (3 times)
```

## Sample data
`sample-auth.log` is a made-up log file. The IP addresses are either reserved for documentation or private, so they do not belong to real systems.

## What I practiced
- Reading a file line by line
- Filtering lines with `if` and `in`
- Counting with a dictionary
- Finding a maximum value
- Using `with open` so the file is closed automatically
- Splitting code into functions with `def`, parameters and `return`
- Using a constant (`THRESHOLD`) and passing it to a function as a parameter

## Known limitations
- If two IPs have the same highest count, only the first one is shown.
- The script expects the IP address to be the 4th word from the end of the line.
  Other log formats will not work.
- The log file name is hardcoded in the script.
- The alert threshold is set in the code (`THRESHOLD`) and cannot be changed from the command line.