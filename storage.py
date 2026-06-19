import json
import os

HOSTS_FILE = os.path.expanduser("~/.telnet_hosts.json")

def load_profiles():
    if not os.path.exists(HOSTS_FILE):
        return []
    try:
        with open(HOSTS_FILE, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading profiles: {e}")
        return []

def save_profiles(profiles):
    try:
        with open(HOSTS_FILE, 'w') as f:
            json.dump(profiles, f, indent=4)
    except Exception as e:
        print(f"Error saving profiles: {e}")

def add_profile(name, ip, port):
    profiles = load_profiles()
    profiles.append({"name": name, "ip": ip, "port": port})
    save_profiles(profiles)

def edit_profile(index, name, ip, port):
    profiles = load_profiles()
    if 0 <= index < len(profiles):
        profiles[index] = {"name": name, "ip": ip, "port": port}
        save_profiles(profiles)

def delete_profile(index):
    profiles = load_profiles()
    if 0 <= index < len(profiles):
        profiles.pop(index)
        save_profiles(profiles)
