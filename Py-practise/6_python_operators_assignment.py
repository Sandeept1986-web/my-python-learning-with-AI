# Use the arithmetic operators to calculate the sum, 
#  average CPU load given  cpu_loads = [40, 60, 80]

# input data : cpu_loads = [40, 60, 80]

cpu_loads = [40, 60, 80]

print("CPU Loads:", type(cpu_loads))

for load in cpu_loads:
    print("CPU Load:", load)
total_load = sum(cpu_loads) 
average_load = total_load / len(cpu_loads)

print("\nSum of CPU loads:", total_load)
print("\nAverage CPU load:", average_load)

print("#" * 60)
# with using sum
total_load = 0
for load in cpu_loads:
    total_load += load
average_load = total_load / len(cpu_loads)

print("\nSum of CPU loads using loop:", total_load)
print("\nAverage CPU load using loop:", average_load)

# use comparison operators to check if disk space is above 80%.

# input data : disk_space = 85  

disk_usage = 85

# check if disk usage is above 80%
is_above_80 = disk_usage > 80

# Expected Output:
# Disk usage above 80%: True

print("\nDisk usage is above 80%:", is_above_80)

disk_usage = 75
is_above_80 = disk_usage > 80
print("\nDisk usage is above 80%:", is_above_80)

# use logical operators(and, or, not) to check if (CPU > 70 and Disk > 80)

# Input data :
cpu_usage = 75
memory_usage = 85

# check if CPU > 70 and Disk > 80
condition = (cpu_usage > 70) and (memory_usage > 80)

# Expected Output:
# Condition (CPU > 70 and Disk > 80): True
print("\nCondition (CPU > 70 and Disk > 80):", condition)

cpu_usage = 65
memory_usage = 85
condition = (cpu_usage > 70) and (memory_usage > 80)
print("\nCondition (CPU > 70 and Disk > 80):", condition)   

# use the identity operators (is, is not) to check if two service configs reference the same object in memory.

# Input data :
config1 = {"service": "web", "port": 80}
config2 = {"service": "http", "port": 443}

# Check if config1 and config2 are the same object in memory.
are_same_object = config1 is config2

# Expected Output:
# Configurations are the same object in memory: True
print("\nConfig1 and config2 are the same object in memory:", are_same_object)

print("#" * 60)

# use the membership operators (in, not in) to check if a specific service is running in the list of active services. 

running_services = ["nginx", "mysql", "redis"]

# Check if 'nginx' service is running
is_nginx_running = "nginx"  in running_services

# Expected Output:
# nginx is running: True
print("\nnginx is running:", is_nginx_running)

# second way 

import operator
is_nginx_running_operator = operator.contains(running_services, "nginx")
print("\nnginx is running (using operator module):", is_nginx_running)

