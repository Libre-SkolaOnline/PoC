from auth import SkolaOnlineAuth
import json

def main():
    client = SkolaOnlineAuth()
    if not client.login(): return

    print("[*] Stahuji přijaté zprávy...")
    
    params = {
        "Pagination.PageNumber": 1,
        "Pagination.PageSize": 10
    }
    
    response = client.get("/v1/messages/received", params=params)
    
    if response.status_code == 200:
        print("\nZprávy")
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    else:
        print(f"Chyba: {response.status_code} - {response.text}")

if __name__ == "__main__":
    main()