# Failed Login Analyzer

A simple Python script that reads an SSH authentication log and finds failed login attempts.

## What it does
- Counts all failed login attempts
- Finds the IP address with the most failed attempts
- Flags IP addresses that reach a configurable number of failed attempts
- Saves the results to a `report.txt` file
- Takes the log file name and the threshold from the command line

## How to run
Run the script from the folder that contains the log file:

```
python analyzer.py <log_file> [threshold]
```

Examples:

```
python analyzer.py sample-auth.log
python analyzer.py sample-auth.log 5
```

The threshold is optional. If you do not give one, the script uses the default value of 3.

After running, the results are also saved to `report.txt` in the folder where you ran the script.

## Example output
```
Most failed attempts: 203.0.113.50 (7 times)
Total failed logins: 13
Suspicious IPs (3+ failed attempts):
203.0.113.50 (7 times)
192.0.2.77 (3 times)
```

The report contains the same text as the terminal output.

## Sample data
`sample-auth.log` is a made-up log file. The IP addresses are either reserved for documentation or private, so they do not belong to real systems.

## What I practiced
- Reading a file line by line
- Filtering lines with `if` and `in`
- Counting with a dictionary
- Finding a maximum value
- Using `with open` so the file is closed automatically
- Splitting code into functions with `def`, parameters and `return`
- Using a constant (`THRESHOLD`) as a default value
- Writing to a file with `open` in `"w"` mode and `write()`
- Using `\n` to add line breaks
- Reading command-line arguments with `sys.argv`
- Converting text to a number with `int()`

## Known limitations
- If two IPs have the same highest count, only the first one is shown.
- The script expects the IP address to be the 4th word from the end of the line.
  Other log formats will not work.
- The report file name (`report.txt`) is hardcoded.
- The report is overwritten every time the script runs.
- The script does not check whether the threshold is a valid number.
- The script does not handle a missing log file.  