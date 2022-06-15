import os
from motor.motor_asyncio import AsyncIOMotorClient
from py_easy_rest import PYRSanicAppBuilder
from py_easy_rest.service import PYRService
from py_easy_rest_mongo_motor_repo import PYRMongoRepo
from py_easy_rest_redis_cache import PYRRedisCache


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

# repo = PYRMongoRepo()
# cache = PYRRedisCache(os.environ["REDIS_CONNECTION_STRING"])
# service = PYRService(config, repo=repo, cache=cache)

service = PYRService(config)


sanic_app = PYRSanicAppBuilder.build(config, service)

# @sanic_app.listener('before_server_start')
# def init(app, loop):
#     mongo_db_instance = AsyncIOMotorClient(os.environ["MONGO_CONNECTION_STRING"])
#     db = mongo_db_instance.get_default_database()
#     repo.set_db_connection(db)

sanic_app.run(
    host='0.0.0.0',
    port=8000,
    debug=True,
    auto_reload=True,
)
