# Day 2 - Lists
skills = ["Python", "SAP ABAP", "CDS", "GenAI" , "SAP Fiori", "SAP HANA", "SAP BTP"
          ]
skills.append("SAP AI Core")
skills.append("SAP AI Foundation")
skills.append("SAP AI Launchpad")
print("======== Initial Skills ========")
print(skills)

skills.remove("SAP ABAP")
print("======== Skills after removing SAP ABAP ========")
print(skills)

skills.sort()
print("======== Skills after sorting ========")
print(skills)

for skill in skills:
    print(skill)    

print(f"Total skills: {len(skills)}")    

ai_tools = ["ChatGPT", "Bard", "Claude", "LLaMA", "Mistral", "Gemini"]
print("======== AI Tools ========")
print(ai_tools) 

print("======== AI Tools after sorting ========")
ai_tools.sort()
print(ai_tools)