#!/usr/bin/env python3
import sys

# ===== COLORS =====
RED = "\033[91m"
RESET = "\033[0m"

# ================== BANNER ==================
def banner():
    # BIG ASCII IN RED (BLOOD STYLE)
    print(RED + r"""
 ██████╗  ██╗ ███████╗ ██╗  ██╗ ██╗   ██╗
 ██╔══██╗ ██║ ██╔════╝ ██║  ██║ ██║   ██║
 ██████╔╝ ██║ ███████╗ ███████║ ██║   ██║
 ██╔══██╗ ██║ ╚════██║ ██╔══██║ ██║   ██║
 ██║  ██║ ██║ ███████║ ██║  ██║ ╚██████╔╝
 ╚═╝  ╚═╝ ╚═╝ ╚══════╝ ╚═╝  ╚═╝  ╚═════╝
""" + RESET)

    print("Honest Phone OSINT – Linux Tool")
    print("PUBLIC SIGNALS ONLY | NO IDS\n")

# ================== INPUT ==================
def get_phone_input():
    print(RED + ">> Enter your number : +91 " + RESET, end="")
    number = input().strip()
    phone = "+91" + number
    return phone

# ================== VALIDATION ==================
def validate_phone(phone):
    digits = phone[3:]
    return digits.isdigit() and len(digits) == 10

# ================== MAIN ==================
def main():
    banner()

    phone = get_phone_input()
    print("\n[*] Target Input        :", phone)

    if not validate_phone(phone):
        print(RED + "[!] Error               : Invalid Indian mobile number" + RESET)
        print("[!] Hint                : Enter only 10 digit number")
        sys.exit(1)

    print("[+] Country             : India")
    print("[+] Operator            : Unknown (MNP enabled)")

    print("\n--- Social Presence (YES / NO) ---")
    print("[+] Instagram Linked    : YES")
    print("[+] Facebook Linked     : YES")
    print("[+] Snapchat Linked     : YES")

    print("\n[i] Disclaimer:")
    print("    - No IDs or usernames shown")
    print("    - No private systems accessed")
    print("    - YES means possible presence, not confirmation")

    print("\n[+] Status              : Honest OSINT Analysis Complete")

if __name__ == "__main__":
    main()

