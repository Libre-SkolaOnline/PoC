import requests
import getpass
import os

BASE_URL = "https://aplikace.skolaonline.cz/solapi/api"
CLIENT_ID = "test_client"

class SkolaOnlineAuth:
    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()
        self.token = None
        self.username = None

    def _get_credentials(self):
        print("\n--- Přihlášení do Škola Online API ---")
        username = input("Uživatelské jméno: ").strip()
        password = getpass.getpass("Heslo: ").strip()
        return username, password

    def login(self):
        username, password = self._get_credentials()
        self.username = username
        url = f"{self.base_url}/connect/token"
        payload = {
            "grant_type": "password",
            "client_id": CLIENT_ID,
            "username": username,
            "password": password,
            "scope": "openid offline_access profile sol_api"
        }

        print(f"[*] Přihlašuji se jako '{username}'...")
        try:
            response = self.session.post(url, data=payload)
            response.raise_for_status()
            data = response.json()
            self.token = data.get("access_token")
            self.session.headers.update({
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json"
            })
            print("[+] Přihlášení úspěšné.\n")
            return True

        except requests.exceptions.HTTPError as err:
            print(f"[-] Chyba přihlášení: {err}")
            if response.content:
                print(f"    Detail: {response.text}")
            return False
        except Exception as e:
            print(f"[-] Neočekávaná chyba: {e}")
            return False

    def get(self, endpoint, params=None):
        if not self.token:
            print("[-] Nejsi přihlášen. Volám login()...")
            if not self.login():
                return None
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url, params=params)