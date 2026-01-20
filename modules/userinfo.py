from auth import SkolaOnlineAuth
import json

def main():
    client = SkolaOnlineAuth()
    if not client.login():
        return

    print(f"Získávám informace o uživateli")
    response = client.get("/v1/user")

    if response and response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        print("Nepodařilo se stáhnout data.")

if __name__ == "__main__":
    main()