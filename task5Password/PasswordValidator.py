import re

password = input("Print a password:")


def check_password(pas):
    if not bool(re.search(r"[a-z]", pas)):
        print("Lowercase doesn't present")
    if not bool(re.search(r"[A-Z]", pas)):
        print("Uppercase doesn't present")
    if not bool(re.search(r"[0-9]", pas)):
        print("Digit doesn't present")
    if not bool(re.search(r"[@$!%*?&]", pas)):
        print("Special char doesn't present")
    if not bool(re.fullmatch(r"[A-Za-z\d@$!%*?&]{8,10}", pas)):
        print("Length 8-10 should be and allowed chars")


check_password(password)
