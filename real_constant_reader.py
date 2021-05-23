import requests as requests
from bs4 import BeautifulSoup


class ElementData:
    def __init__(self, path: str):
        """
        
        :param path: Path to html docu file.
        """
        self.name_raw = None
        self.name = None
        self.description = None
        self.real_constant_table = None
        self._read(path)

    def _read(self, path: str):
        #req = requests.get(path)
        with open(path, 'r') as f:
            soup = BeautifulSoup(f.read(), "html.parser")  # , parse_only=parse_only)
    
        refentry_soup = soup.find("div", class_="refentry")
        self.name_raw = refentry_soup.attrs["title"]
        self.name = self.name_raw.lower()
        element_descritption_soup = refentry_soup.find("div", title=f"{self.name_raw} Element Description")
        self.description = element_descritption_soup.text.replace(
            f"{self.name_raw} Element Description", f"Control object for element {self.name}.\n\n"
        ).replace("\n", "\n    ")

        real_constant_table_soup = soup.find("table", summary=f"{self.name_raw} Real Constants")
        table_soup = real_constant_table_soup.find("tbody")
        #print(table_soup.prettify())
        real_constants = []
        for row in table_soup:
            print(row)
            rc_num = row.contents[0].string
            rc_short = row.contents[1].string.lower()
            rc_description = row.contents[2].text.replace("[1]", "").replace("[2]", "").replace("[3]", "").strip()
            real_constants.append((rc_num, rc_short, rc_description))
            real_constants
        self.real_constant_table = real_constants

    def create_class_str(self):
        ind = "    "
        ind2 = "        "
        empty_line = ""

        result = [f"class {self.name.capitalize()}:"]
        result.append(f"{ind}\"\"\"")
        result.append(f"{ind}{self.description}")
        result.append(f"{ind}\"\"\"")

        result.append(f"{ind}def __init__(self):")

        for row in self.real_constant_table:
            result.append(f"{ind2}self._{row[1]} = \"\"")

        result.append(empty_line)

        # add property
        for row in self.real_constant_table:
            result.append(f"{ind}@property")
            result.append(f"{ind}def {row[1]}(self):")
            result.append(f"{ind2}\"\"\"")
            result.append(f"{ind2}{row[2]}.")
            result.append(f"{ind2}\"\"\"")
            result.append(f"{ind2}return self._{row[1]}")
            result.append(empty_line)
            result.append(f"{ind}@{row[1]}.setter")
            result.append(f"{ind}def {row[1]}(self, value):")
            result.append(f"{ind2}self._{row[1]} = value")
            result.append(empty_line)

        # function to set all real constants
        result.append(f"{ind}def call_r(self):")
        result.append(f"{ind2}\"\"\"")
        result.append(f"{ind2}Set all real constants by calling r and rmore.")
        result.append(f"{ind2}\"\"\"")
        result.append(f"{ind2}pass  # todo")

        result.append(empty_line)

        return result

