import os

def url(operation):
    return "%s/api/v1/namespaces/%s/%s" % (
        os.environ["__OW_API_HOST"],
        os.environ["__OW_NAMESPACE"],
        operation
    )

def auth():
    up = os.environ['__OW_API_KEY'].split(":")
    return (up[0], up[1])

import requests

def whisk_get(operation):
    return requests.get(
         url=url(operation), 
         auth=auth())

import json

def main(args):
    res = whisk_get("packages")
    js = json.loads(res.text)
    pkgs = [x["name"] for x in js] 
    return { "packages": pkgs }

