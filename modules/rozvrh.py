from auth import SkolaOnlineAuth
import json
from datetime import datetime, timedelta

def get_current_week_range():
    today = datetime.now()
    start = today - timedelta(days=today.weekday())
    end = start + timedelta(days=6)                 
    return start.isoformat(), end.isoformat()

def main():
    client = SkolaOnlineAuth()
    if not client.login(): return
    user_resp = client.get("/v1/user")
    if user_resp.status_code != 200:
        print("Chyba při získávání uživatele")
        return
    student_id = user_resp.json().get("personID")
    date_from, date_to = get_current_week_range()
    print(f"Stahuji rozvrh pro ID {student_id} od {date_from[:10]} do {date_to[:10]}")

    params = {
        "StudentId": student_id,
        "DateFrom": date_from,
        "DateTo": date_to
    }
    
    response = client.get("/v1/timeTable", params=params)
    
    if response.status_code == 200:
        print("\nRozvrh hodin")
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    else:
        print(f"Chyba: {response.status_code} - {response.text}")

if __name__ == "__main__":
    main()