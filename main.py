import os
from sanic_ext import Extend
from py_easy_rest import PYRSanicAppBuilder
from py_easy_rest.service import PYRService
from py_easy_rest.caches import PYRDummyCache
from py_easy_rest.repos import PYRMemoryRepo


config = {
    "name": "ProjectExample",
    "schemas": [{
        "name": "Companies",
        "slug": "companies",
        "properties": {
            "name": {"type": "string"},
            "size": {"type": "integer"},
            "industry": {"type": "string"},
        },
        "required": ["name"],
    }, {
        "name": "Industries",
        "slug": "industries",
        "properties": {
            "name": {"type": "string"},
        },
        "required": ["name"],
    }, {
        "name": "Personal Interests",
        "slug": "personal-interests",
        "properties": {
            "name": {"type": "string"},
        },
        "required": ["name"],
    }, {
        "name": "Technical Skills",
        "slug": "tech-skills",
        "properties": {
            "name": {"type": "string"},
        },
        "required": ["name"],
    }]
}


class MyCustomService(PYRService):
    def __init__(
        self,
        api_config,
        repo=PYRMemoryRepo(),
        cache=PYRDummyCache(),
        cache_list_seconds_ttl=10,
        cache_get_seconds_ttl=60 * 30,  # thirty minutes
    ):
        super().__init__(config, repo=repo, cache=cache)

    async def get(self, slug, id):
        # do some custom stuff
        data = await super().get(slug, id)

        data["custom_field"] = "custom_value"

        return data


service = MyCustomService(config)

sanic_app = PYRSanicAppBuilder.build(config, service)

sanic_app.config.update({
    "CORS_ORIGINS": "*"
})

Extend(sanic_app)

sanic_app.run(
    host='0.0.0.0',
    port=8000,
    debug=True,
    auto_reload=True,
)
