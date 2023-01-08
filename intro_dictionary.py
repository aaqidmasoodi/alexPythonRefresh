# dictionary always has a key and a value
cg_ref_codes = {
    "AUD": "This referes to the auditions in the event model",
    "EXP": "12-01-2023 12:10:15",
    "SECRET": "saf4wfawq4fwf34fwrf",
}

cg_ref_codes.update({"AUD": "1234", "EXP": "78454", "CAR": "HONDA"})
cg_ref_codes["AUD"] = "Something"  # this will let you update or add one value
cg_ref_codes["USERS"] = 45
print(cg_ref_codes)


# print(dir(cg_ref_codes))
# print(cg_ref_codes.keys())
# print(cg_ref_codes.values())
# print(cg_ref_codes.items())

# if this users key were in the dict then it would update the value
# if it is not there it is going add it to the dict

# cg_ref_codes.pop("AUD")
# cg_ref_codes.popitem()  # removes the last one

# print(len(cg_ref_codes))
# print(cg_ref_codes["AUD"])
