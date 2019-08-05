import os
import requests 
from .organizations import Organization

class Buildkite:
    def __init__(self, token = None):
        self.url = "https://api.buildkite.com" 
        self.version = "v2"
        self.user_agent = "integralthread/buildkite-api"

        token = os.environ.get("BUILDKITE_TOKEN", token)

        if token:
            self.token = token
        else:
            raise RuntimeError("no authentication token")


    def get(self, resource, ):
        headers = {
            'user-agent': self.user_agent,
            "Authorization": f"Bearer {self.token}",
        }
        data = requests.get(
            f"{self.url}/{self.version}/{resource}", 
            headers=headers,
        )
        return data.json()

    def organizations(self):
        data = self.get("organizations")

        for o in data:
            yield Organization(o)
    
    def organization(self, slug):
        data = self.get(f"organizations/{slug}")
        return Organization(data)