from auth import SkolaOnlineAuth
import json

def main():
    client = SkolaOnlineAuth()
    if not client.login(): return
    user_resp = client.get("/v1/user")
    if user_resp.status_code != 200: return
    
    student_id = user_resp.json().get("personID")
    print(f"Stahuji známky pro studenta {student_id}")
    endpoint = f"/v1/students/{student_id}/marks/list"
    params = {"SigningFilter": "all"}

    response = client.get(endpoint, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"\nNalezeno {len(data.get('marks', []))} známek")
        print(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        print(f"Chyba: {response.status_code} - {response.text}")

if __name__ == "__main__":
    main()