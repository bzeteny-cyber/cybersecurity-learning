# Failed Login Analyzer

A simple Python script that reads an SSH authentication log and finds failed login attempts.

## What it does
- Counts all failed login attempts
- Finds the IP address with the most failed attempts

## How to run
Put `analyzer.py` and `sample-auth.log` in the same folder, then run:

```
python analyzer.py
```

## Example output
```
Most failed attempts: 203.0.113.50 (7 times)
Total failed logins: 13
```

## Sample data
`sample-auth.log` is a made-up log file. The IP addresses come from ranges reserved for documentation, so they do not belong to real systems.

## What I practiced
- Reading a file line by line
- Filtering lines with `if` and `in`
- Counting with a dictionary
- Finding a maximum value

## Known limitations
- If two IPs have the same highest count, only the first one is shown.
- The script expects the IP address to be the 4th word from the end of the line.
  Other log formats will not work.
- The log file name is hardcoded in the script.
