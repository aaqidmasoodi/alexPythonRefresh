CG_TABLE = ["AUD", "EXP", "SECRET", "ADMIN", "IS_SUPER_USER"]

#                    static method
cg_ref_codes = dict.fromkeys(CG_TABLE, '')

cg_ref_codes["AUD"] = "22-01-2.23 11:22:59"

print(cg_ref_codes)
