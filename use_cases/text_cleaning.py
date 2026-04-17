from string import punctuation

bills = [
    "sb2034",
    "Hb 713",
    "hB 83",
    "SB037",
    "hb 3714",
    "sb7",
    "HB 13",
    " sb 1717",
    " hb 800 ",
    "sb-1234 ",
]


def clean_bill_names(bill):
    # Remove leading and trailing whitespace
    bill = bill.strip()
    # Convert to uppercase
    bill = bill.upper()
    # Remove spaces
    bill = bill.replace(" ", "")
    # Remove punctuation
    bill = bill.translate(str.maketrans("", "", punctuation))
    # Split into letters and numbers, then reformat
    a, b = bill[:2], bill[2:]
    # Ensure the bill number is 4 digits long
    b = b.zfill(4)
    return a + b


def familiar_bill_name(bill):
    # Remove leading and trailing whitespace
    bill = bill.strip()
    # Convert to uppercase
    bill = bill.upper()
    # Remove spaces
    bill = bill.replace(" ", "")
    # Remove punctuation
    bill = bill.translate(str.maketrans("", "", punctuation))
    # Split into letters and numbers, then reformat
    a, b = bill[:2], bill[2:]
    return f"{a} {b}"
    # return bill


for bill in bills:
    pad = 12
    cleaned_bill = clean_bill_names(bill)
    familiar_bill = familiar_bill_name(bill)
    print(f"{bill:<{pad}}{cleaned_bill:<{pad-2}} {familiar_bill}")
