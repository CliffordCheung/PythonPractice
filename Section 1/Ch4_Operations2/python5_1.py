# Initialize variables
has_license = True
has_experience = False
has_clean_record = True

# Calculate conditions
can_drive_car = (has_license and has_clean_record)
can_drive_truck = (has_license and has_experience and has_clean_record)
cannot_drive_any = (not has_license or not has_clean_record)

# Don't delete the lines below
print("Can drive car:", can_drive_car)
print("Can drive truck:", can_drive_truck)
print("Cannot drive any:", cannot_drive_any)