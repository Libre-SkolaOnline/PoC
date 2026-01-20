from auth import SkolaOnlineAuth
import json

def main():
    client = SkolaOnlineAuth()
    if not client.login(): return
    user_resp = client.get("/v1/user")
    student_id = user_resp.json().get("personID")
    print(f"[*] Stahuji úkoly pro studenta {student_id}...")
    endpoint = f"/v1/students/{student_id}/homeworks"
    params = {"Filter": "all"} 
    
    response = client.get(endpoint, params=params)
    
    if response.status_code == 200:
        print("\nDomácí úkoly")
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    else:
        print(f"Chyba: {response.status_code} - {response.text}")

if __name__ == "__main__":
    main()