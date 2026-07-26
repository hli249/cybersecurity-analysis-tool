keywords = ["failed login", "unauthorized access", "error"]
suspicious_entries = []

with open("sample.log", "r") as log_file:
    for line in log_file:
        if any(keyword in line.lower() for keyword in keywords):
            suspicious_entries.append(line.strip())

print("Potential security incidents:")

for entry in suspicious_entries:
    print(entry)

print("Total incidents found:", len(suspicious_entries))