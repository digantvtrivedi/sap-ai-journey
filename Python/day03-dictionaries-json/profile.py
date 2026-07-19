profile = {
    "name" : "Digant",
    "experience" : 15,
    "current_role" : "SAP Developer",
    "target_role" : "Enterprise AI Developer",
    "skills" : [
                "Python", 
                "SAP ABAP", 
                "SAP Fiori", 
                "SAP HANA", 
                "SAP BTP", 
                "SAP AI Core", 
                "SAP AI Foundation",
                "Gen AI",
                "RAP"],}

# print(profile)
# print(profile["name"])
# print(profile["current_role"])
# print(profile["skills"])
# print(profile["skills"][1])

# profile["github"]  = "diganttrivedi"

# profile["current_role"] = "SAP AI Developer"

# print(profile) 

# print(profile["skills"][-1])

for keys, values in profile.items():
    print(f"{keys}: {values}")