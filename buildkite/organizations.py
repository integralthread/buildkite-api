from .buildkite import Buildkite
from .buildkite import BuildkiteList
from .pipeline import Pipelines

class Organization(Buildkite):

    def get(self, slug):
        self._resource = f"organizations/{slug}"
        self._api = self.fetch()
        return self        
    
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
    def org_slug(self) -> str:
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
        return f"{self.org_slug}"
    
    def pipelines(self):
        pipelines = Pipelines()
        for p in pipelines.list(url=self.pipelines_url):
            yield p
    
    def pipeline(self, pipeline_slug):
        p = Pipeline()
        return p.get(self.org_slug, pipeline_slug)
    
    # def builds(self, organization=None):
    #     pass
    
    # def agents(self, organization):
    #     pass
    
    # def agent(self, organization, agent_id):
    #     pass
    
    # def emojis(self, organization):
    #     pass

class Organizations(BuildkiteList):
    _item = Organization
    _resource = "organizations"
