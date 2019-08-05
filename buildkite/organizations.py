
class Organization:

    def __init__(self, data):
        self._api = data
    
    @property
    def id(self) -> str:
        return self._api['id']
    
    @property
    def url(self) -> str:
        return self._api['url']
    
    @property
    def web_url(self) -> str:
        return self._api['web_url']
    
    @property
    def name(self) -> str:
        return self._api['name']
    
    @property
    def slug(self) -> str:
        return self._api['slug']
    
    @property
    def pipelines_url(self) -> str:
        return self._api['pipelines_url']
    
    @property
    def agents_url(self) -> str:
        return self._api['agents_url']
    
    @property
    def emojis_url(self) -> str:
        return self._api['emojis_url']
    
    @property
    def created_at(self) -> str:
        return self._api['created_at']
    
    def __str__(self):
        return f"{self.slug}"
