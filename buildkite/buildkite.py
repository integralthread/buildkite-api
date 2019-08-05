import os
import requests 

class Meta:
    _resource = None

    def _meta(self):
        url = "https://api.buildkite.com"
        version = "v2"
        user_agent = "integralthread/buildkite-api"
        token = os.environ['BUILDKITE_TOKEN']

        headers = {
            'user-agent': user_agent,
            "Authorization": f"Bearer {token}",
        }

        endpoint = f"{url}/{version}/{self._resource}"
        return endpoint, headers
    
    def fetch(self, url = None):
        endpoint, headers = self._meta()
        if url is not None:
            endpoint = url
        data = requests.get(endpoint, headers=headers)
        return data.json()
    
class Buildkite(Meta):
    _api = {}

    def get(self, resource):
        self._resource = resource
        self._api = self.fetch()
        return self
    
    def create(self):
        raise NotImplementedError('this method is not implemented and may not be supported')
    
    def update(self):
        pass
    
    def delete(self):
        pass
    
    def load(self, data):
        self._api = data
        return self

class BuildkiteList(Meta):
    _item = None

    def list(self, url=None):
        if self._item is None:
            raise NotImplementedError('must specify item class')

        data = self.fetch(url)
        for o in data:
            i = self._item()
            yield i.load(o)
    
    # todo : data pagination
