# String Handling Assignment Solutions

# 1. Check if filename ends with .log
filename = "system.log"
print("Ends with .log?", filename.endswith(".log"))

# 2. Convert environment variable names to uppercase
env_var = "path"
print("Uppercase env var:", env_var.upper())

# 3. Replace "ERROR" with "WARN" in logs
log_line = "ERROR: Service failed"
print("Replaced log:", log_line.replace("ERROR", "WARN"))

# 4. Split into key-value pairs
status_str = "nginx:running,mysql:stopped"
pairs = [kv.split(":") for kv in status_str.split(",")]
print("Key-value pairs:", pairs)

# 5. Validate if input is numeric
user_input = "12345"
print("Is numeric?", user_input.isdigit())

# 6. Strip whitespace from config values
config_val = "   prod   "
print("Stripped config:", config_val.strip())

# 7. Validate API endpoint starts with http
api_endpoint = "https://api.example.com"
print("Starts with http?", api_endpoint.startswith("http"))

# 8. Remove special characters
db_str = "DB@server#1!"
cleaned = "".join(ch for ch in db_str if ch.isalnum())
print("Cleaned string:", cleaned)

# 9. Count occurrences of "restart"
deployment_log = "restart pod1; restart pod2; restart pod3"
print("Restart count:", deployment_log.count("restart"))

# 10. Check if container name is alphanumeric
container_name = "nginx01"
print("Is alphanumeric?", container_name.isalnum())

# 11. Validate log line length
log_line = "Pod restarted successfully"
print("Log length:", len(log_line))

# 12. Extract domain from URL
url = "https://devops.org/docs"
domain = url.split("/")[2]
print("Domain:", domain)

# 13. Use partition to split service & status
svc_status = "nginx:running"
service, sep, status = svc_status.partition(":")
print("Service:", service, "Status:", status)

# 14. Find index of "error" in log string
log_str = "Critical error occurred in pod"
print("Index of 'error':", log_str.find("error"))

# 15. Join list of IPs into a string
ips = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]
joined_ips = ",".join(ips)
print("Joined IPs:", joined_ips)