from typing import List

from real_constant_reader import ElementData

data = ElementData("D:\\ans_help_v182\\ans_elem\\Hlp_E_CONTA172.html")

text = "\n".join(data.create_class_str())

print(text)

with open("conta172.py", 'w', encoding="utf-8") as f:
    f.write(text)


# if __name__ == '__main__':
#     # note: real constant 26, 33, 34, missing in docu -> ""
#     constants172 = ["r1", "r2", "fkn", "ftoln", "icont", "pinb",
#                     "pzer", "czer", "taumax", "cnof", "fkop", "fkt",
#                     "cohe", "tcc", "fhtg", "sbct", "rdvf", "fwgt",
#                     "ecc", "fheg", "fact", "dc", "slto", "tnop",
#                     "tols", "", "ppcn", "fpat", "cor", "strm",
#                     "fdmn", "fdmt", "", "", "tbnd", "wbid",
#                     "pcc", "psee", "abpp", "fpft", "fpwt", "dcc",
#                     "dcon", "abdc"
#                     ]
#
#     text = create_element_class("RealConstant172", constants172)