THRESHOLD = 3


def read_log(filename):
    total_failed = 0
    ip_counts = {}

    with open(filename) as log_file:
        for line in log_file:
            if "Failed" in line:
                total_failed += 1
                parts = line.split()
                ip = parts[-4]
                if ip in ip_counts:
                    ip_counts[ip] = ip_counts[ip] + 1
                else:
                    ip_counts[ip] = 1

    return total_failed, ip_counts


def find_top_ip(ip_counts):
    max_count = 0
    top_ip = ""

    for ip in ip_counts:
        if ip_counts[ip] > max_count:
            max_count = ip_counts[ip]
            top_ip = ip

    return top_ip, max_count

def find_suspicious_ips(ip_counts, threshold):
    suspicious={}

    for ip in ip_counts:
        if ip_counts[ip]>=threshold:
            suspicious[ip]=ip_counts[ip]

    return suspicious
    

def main():
    total_failed, ip_counts = read_log("sample-auth.log")
    top_ip, max_count = find_top_ip(ip_counts)
    suspicious=find_suspicious_ips(ip_counts, THRESHOLD)
   
    print(f"Most failed attempts: {top_ip} ({max_count} times)")
    print(f"Total failed logins: {total_failed}")
    if suspicious:
        print(f"Suspicious IPs ({THRESHOLD}+ failed attempts):")
        for ip in suspicious:
            print(f"{ip} ({suspicious[ip]} times)")
    else:
        print(f"No suspicious IPs found (threshold: {THRESHOLD}).")

        
main()