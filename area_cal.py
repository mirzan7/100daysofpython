def estimate_number_of_can(length,bredth,coverage):
    area = length * bredth
    total_can_needed = area / coverage
    return (round(total_can_needed))

length = int(input("Enter the total length of the wall that need to be painted  :"))
width = int(input("Enter the total width   :"))
coverage = 5
print(estimate_number_of_can(length,width,coverage))