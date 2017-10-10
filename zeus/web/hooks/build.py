from flask import request

from zeus.config import redis
from zeus.models import Build
from zeus.api import client

from .base import BaseHook


class BuildHook(BaseHook):
    def post(self, hook, build_xid):
        lock_key = 'hook:build:{hook_id}:{build_xid}'.format(
            hook_id=hook.id.hex,
            build_xid=build_xid,
        )
        with redis.lock(lock_key):
            build = Build.query.filter(
                Build.provider == hook.provider,
                Build.external_id == build_xid,
            ).first()

            json = request.get_json() or {}
            json['external_id'] = build_xid
            json['provider'] = hook.provider

            if build:
                response = client.put(
                    '/repos/{}/builds/{}'.format(
                        hook.repository.get_full_name(),
                        build.number,
                    ),
                    json=json
                )
            else:
                response = client.post(
                    '/repos/{}/builds'.format(
                        hook.repository.get_full_name(),
                    ),
                    json=json
                )

            return response
