log_file=open("sample-auth.log")

total_failed=0
ip_counts={}
for line in log_file:
    if "Failed" in line:
        total_failed+=1
        parts=line.split()
        if parts[-4] in ip_counts:
            ip_counts[parts[-4]]=ip_counts[parts[-4]]+1
        else:
            ip_counts[parts[-4]]=1

max_count=0
top_ip=""
for ip in ip_counts:
    if ip_counts[ip]>max_count:
        max_count=ip_counts[ip]   
        top_ip=ip        




print(f"Most failed attempts: {top_ip} ({max_count} times)")
print(f"Total failed logins: {total_failed}")



log_file.close()