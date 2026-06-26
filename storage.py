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
        print("Error loading profiles: {0}".format(e))
        return []

def save_profiles(profiles):
    try:
        with open(HOSTS_FILE, 'w') as f:
            json.dump(profiles, f, indent=4)
    except Exception as e:
        print("Error saving profiles: {0}".format(e))

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


def export_profiles(filepath):
    """Export all profiles to a JSON file at the given path."""
    profiles = load_profiles()
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(profiles, f, indent=4, ensure_ascii=False)
        return True, "Exported {0} profiles.".format(len(profiles))
    except Exception as e:
        return False, "Export error: {0}".format(e)


def import_profiles(filepath, merge=True):
    """Import profiles from a JSON file.
    
    If merge=True, merges with existing profiles (no duplicate names).
    If merge=False, replaces the current list entirely.
    Returns (success, message).
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            imported = json.load(f)
    except Exception as e:
        return False, "Import error: {0}".format(e)

    if not isinstance(imported, list):
        return False, "Invalid format: expected a list of profiles."

    # Validate each entry has required fields
    for entry in imported:
        if not isinstance(entry, dict) or 'name' not in entry or 'ip' not in entry or 'port' not in entry:
            return False, "Invalid profile entry: each entry must have name, ip, and port."

    if merge:
        existing = load_profiles()
        existing_names = {p['name'] for p in existing}
        new_count = 0
        for entry in imported:
            if entry['name'] not in existing_names:
                existing.append(entry)
                existing_names.add(entry['name'])
                new_count += 1
            # else: skip duplicate name
        save_profiles(existing)
        return True, "Imported {0} new profiles ({1} skipped as duplicates).".format(new_count, len(imported) - new_count)
    else:
        save_profiles(imported)
        return True, "Replaced all profiles with {0} imported entries.".format(len(imported))
