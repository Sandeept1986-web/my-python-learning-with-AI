# Assignment Solutions - Function Based Script

# 1. Convert list of server IPs into tuple
def convert_ips_to_tuple(ips):
    return tuple(ips)  # immutability prevents accidental modification

# 2. Convert dictionary {service: port} into string
def dict_to_string(service_dict):
    return str(service_dict)

# 3. Parse string into list of integers
def parse_ports(port_str):
    return list(map(int, port_str.split(",")))

# 4. Convert CPU usage string to float and compare with threshold
def check_cpu_usage(cpu_str, threshold=80.0):
    cpu_val = float(cpu_str)
    return cpu_val, cpu_val > threshold

# 5. Convert list of pod names into set
def unique_pods(pod_list):
    return set(pod_list)

# 6. Convert YAML-like dict port to integer
def convert_yaml_port(yaml_dict):
    yaml_dict["port"] = int(yaml_dict["port"])
    return yaml_dict

# 7. Convert list of strings to integers and calculate sum
def sum_string_numbers(num_list):
    nums = list(map(int, num_list))
    return sum(nums)

# 8. Convert boolean string to Python boolean
def str_to_bool(bool_str):
    return bool_str == "True"

# 9. Access first 3 server IPs
def first_three_ips(ip_list):
    return ip_list[:3]

# 10. Extract last 2 pod names
def last_two_pods(pod_list):
    return pod_list[-2:]

# 11. Slice log message to get "ERROR"
def extract_log_level(log_msg):
    return log_msg.split(":")[0]

# 12. Extract alternate and reverse service names
def alternate_and_reverse_services(services):
    return services[::2], services[::-1]

# 13. Slice date from log string
def extract_date(log_time):
    return log_time[:10]

# 14. Slice middle three ports
def middle_three_ports(port_list):
    return port_list[1:4]

# 15. Slice command string to extract "get pods"
def extract_command(command_str):
    return " ".join(command_str.split()[1:3])


# -------------------------------
# Example usage / testing
if __name__ == "__main__":
    print(convert_ips_to_tuple(["192.168.1.1", "192.168.1.2"]))
    print(dict_to_string({"nginx": 80, "mysql": 3306}))
    print(parse_ports("80,443,22"))
    print(check_cpu_usage("78.5"))
    print(unique_pods(["pod1", "pod2", "pod1"]))
    print(convert_yaml_port({"server": "app01", "port": "8080"}))
    print(sum_string_numbers(["10", "20", "30"]))
    print(str_to_bool("True"))
    print(first_three_ips(["10.0.0.1","10.0.0.2","10.0.0.3","10.0.0.4"]))
    print(last_two_pods(["podA","podB","podC","podD"]))
    print(extract_log_level("ERROR: Pod crashed at 10:00"))
    print(alternate_and_reverse_services(["nginx","mysql","redis","kafka","elasticsearch","prometheus","grafana"]))
    print(extract_date("2025-09-08T10:20:30Z"))
    print(middle_three_ports([22,80,443,3306,8080]))
    print(extract_command("kubectl get pods --namespace=prod"))