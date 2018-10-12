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

if __name__ == "__main__":
    import sys, os, os.path, json
    with open(os.path.expanduser("~/.wskprops"), "r") as f:
        for line in f.readlines():
            [k, v] = line.strip().split("=")
            if k == "APIHOST": os.environ["__OW_API_HOST"] = "https://%s:443" % v
            if k == "AUTH": os.environ["__OW_API_KEY"] = v
            if k == "NAMESPACE": os.environ["__OW_NAMESPACE"] = v
    args = json.loads(sys.argv[1]) if len(sys.argv)>1 else {}   
    print(json.dumps(main(args)))           
