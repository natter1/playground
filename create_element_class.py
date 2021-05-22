from typing import List


def create_element_class(name: str, real_constants: List[str], keyopts: list = None) -> List[str]:
    ind = "    "
    ind2 = "        "
    empty_line = ""

    result = [
        f"class {name}:",
        f"{ind}def __init__(self):"
        ]
    for constant in real_constants:
        if constant:
            result.append(f"{ind2}self._{constant} = \"\"")

    result.append(empty_line)

    # add property
    for constant in real_constants:
        if constant:
            result.append(f"{ind}@property")
            result.append(f"{ind}def {constant}(self):")
            result.append(f"{ind2}return self._{constant}")
            result.append(empty_line)
            result.append(f"{ind}@{constant}.setter")
            result.append(f"{ind}def {constant}(self, value):")
            result.append(f"{ind2}self._{constant} = value")
            result.append(empty_line)

    # function to set all real constants
    result.append(f"{ind}def call_r(self):")
    result.append(f"{ind2}pass  # todo")

    result.append(empty_line)

    return result


if __name__ == '__main__':
    # note: real constant 26, 33, 34, missing in docu -> ""
    constants172 = ["r1", "r2", "fkn", "ftoln", "icont", "pinb",
                    "pzer", "czer", "taumax", "cnof", "fkop", "fkt",
                    "cohe", "tcc", "fhtg", "sbct", "rdvf", "fwgt",
                    "ecc", "fheg", "fact", "dc", "slto", "tnop",
                    "tols", "", "ppcn", "fpat", "cor", "strm",
                    "fdmn", "fdmt", "", "", "tbnd", "wbid",
                    "pcc", "psee", "abpp", "fpft", "fpwt", "dcc",
                    "dcon", "abdc"
                    ]

    text = create_element_class("RealConstant172", constants172)

    text = "\n".join(text)

    with open('real_constant_172.py', 'w') as file:
        file.write(str(text))

