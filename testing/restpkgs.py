import os

def url(operation, namespace=None, apihost = None):
    """ create a url for connecting to OpenWhisk
    >>> import os
    >>> os.environ["__OW_API_HOST"]="http://api.host"
    >>> os.environ["__OW_NAMESPACE"]="namespace"
    >>> import restpkgs as r
    >>> r.url("actions")
    'http://api.host/api/v1/namespaces/namespace/actions'
    """
    namespace = namespace if namespace else os.environ["__OW_NAMESPACE"]
    apihost =  apihost if apihost else os.environ["__OW_API_HOST"]
    return "%s/api/v1/namespaces/%s/%s" % (
        apihost,
        namespace,
        operation
    )

def auth():
    """ Extract OpenWhisk authentication keys
    >>> os.environ["__OW_API_KEY"]="USERNAME:PASSWORD"
    >>> import restpkgs as r
    >>> r.auth()
    ('USERNAME', 'PASSWORD')
    """
    up = os.environ['__OW_API_KEY'].split(":")
    return (up[0], up[1])

import requests

def whisk_init():
    import os, os.path, json
    with open(os.path.expanduser("~/.wskprops"), "r") as f:
        for line in f.readlines():
            [k, v] = line.strip().split("=")
            if k == "APIHOST": os.environ["__OW_API_HOST"] = "https://%s:443" % v
            if k == "AUTH": os.environ["__OW_API_KEY"] = v
            if k == "NAMESPACE": os.environ["__OW_NAMESPACE"] = v

def whisk_get(operation):
    """
    >>> import restpkgs as r
    >>> r.whisk_init()
    >>> re = r.whisk_get("packages")
    >>> re
    <Response [200]>
    >>> type(re.json())
    <class 'list'>
    """
    return requests.get(
         url=url(operation), 
         auth=auth())

import json

def main(args):
    """
    >>>
    >>> import restpkgs as r, httpretty as h, json
    >>> h.enable()
    >>> r.whisk_init()
    >>> resp = json.dumps([{"name":"first"}, {"name":"second"}])
    >>> h.register_uri(h.GET, r.url("packages"), body=resp)
    >>> r.main({})
    {'packages': ['first', 'second']}
    >>> h.disable()
    """
    res = whisk_get("packages")
    js = json.loads(res.text)
    pkgs = [x["name"] for x in js] 
    return { "packages": pkgs }

if __name__ == "__main__":
    import doctest
    doctest.testmod()
