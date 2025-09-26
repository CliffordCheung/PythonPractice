region1 = eval(input())
region2 = eval(input())
region3 = eval(input())

# Write code here
shared_treasures = region1 & region2 & region3
unique_treasures_region1 = region1.difference(region2, region3)
all_treasures = region1 | region2 | region3
exclusive_treasures = region1.difference(region2, region3) | region2.difference(region1, region3) | region3.difference(region1, region2)

# Print the results
print("Shared treasures:", sorted(list(shared_treasures)))
print("Unique treasures in region1:", sorted(list(unique_treasures_region1)))
print("All treasures:", sorted(list(all_treasures)))
print("Exclusive treasures:", sorted(list(exclusive_treasures)))