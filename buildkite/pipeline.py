from .buildkite import Buildkite
from .buildkite import BuildkiteList

class Pipeline(Buildkite):
    
    def get(self, org_slug, pipeline_slug):
        self._resource = f"organizations/{org_slug}/pipelines/{pipeline_slug}"
        self._api = self.fetch()
        return self
    
    @property
    def id(self) -> str:
        return self._api['id']        
    
    def builds(self):
        pass

    def build(self, build_number):
        pass

class Pipelines(BuildkiteList):
    _item = Pipeline