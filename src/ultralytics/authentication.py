import requests
import json

def verifyAndFetch(email, api_key):
    auth = Authentication(email, api_key)
    return auth._verifyAPIKey()

class Authentication:

    _api_url = "https://us-central1-ultralytics-hub.cloudfunctions.net/validateApiKey"

    def __init__(self, email, api_key):
        self.email = email
        self.api_key = api_key
        return

    def _verifyAPIKey(self):
        """
        Verifies the supplied API key with the server.
        Returns models marked for training on success
        """
        payload = {"email" : self.email, "apiKey" : self.api_key}
        response = requests.post(self._api_url, data=payload)
        data = json.loads(response.text)

        if data and data["status"] == "Validated!":
            return data["models"]
        else:
            return False

    def logout():
        return
