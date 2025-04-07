#!/usr/bin/env python3
import os
import time

LOG_FILE = "firewall.log"

def log_action(message):
    timestamp = time.strftime("[%Y-%m-%d %H:%M:%S]")
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"{timestamp} {message}\n")

def activate_standard_ports():
    os.system("sudo ufw allow 22")
    os.system("sudo ufw allow 80")
    log_action("Enable standard ports (22 - SSH, 80 - HTTP)")
    print("Done, ports 22 (SSH) and 80 (HTTP) have been enabled!")

def block_all_connections():
    os.system("sudo ufw default deny incoming")
    log_action("All connections have been blocked.")
    print("Done, all connections have been blocked!")

def show_active_rules():
    print("Active rules:")
    os.system("sudo ufw status verbose")
    log_action("Show active rules")

def reset_firewall():
    os.system("echo y | sudo ufw reset")
    log_action("Rules have been reset to default.")
    print("Done, firewall settings have been reset!")

def add_custom_rule():
    port = input("Enter the port: ")
    protocol = input("Protocol (TCP/UDP): ").lower()
    if protocol not in ['tcp', 'udp']:
        print("Error, protocol invalid!")
        return
    rule = f"sudo ufw allow {port}/{protocol}"
    os.system(rule)
    log_action(f"User added the rule: allow {port}/{protocol}")
    print(f"Done, rule for port {port}/{protocol} has been added!")

def show_menu():
    print("\n═══ FIREWALL CONFIGURATOR ═══\n")
    print("1. Enable standard ports (22 – SSH, 80 – HTTP)")
    print("2. Block all connections")
    print("3. Show active rules")
    print("4. Revert to default settings")
    print("5. Add custom rule")
    print("6. Exit")

def main():
    while True:
        show_menu()
        choice = input("\nChoose an option (1-6): ")

        if choice == "1":
            activate_standard_ports()
        elif choice == "2":
            block_all_connections()
        elif choice == "3":
            show_active_rules()
        elif choice == "4":
            reset_firewall()
        elif choice == "5":
            add_custom_rule()
        elif choice == "6":
            log_action("User has exited the application!")
            print("Leaving..")
            break
        else:
            print("Invalid option! Please try again!")

if __name__ == "__main__":
    main()

