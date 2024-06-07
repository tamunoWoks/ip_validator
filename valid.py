import re

def main():
    ...

def validate(ip):
    #Regex to match a valid IPv4 address
    pattern = r'((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    #Use fullmatch to ensure the entir string matches the pattern
    if re.fullmatch(pattern, ip):
        return True
    else:
        return False


if __name__ == '__main__':
    main()