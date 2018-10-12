import os, requests, json

def url(operation):
    return "%s/api/v1/namespaces/%s/%s" % (
        os.environ["__OW_API_HOST"],
        os.environ["__OW_NAMESPACE"],
        operation
    )

def auth():
    up = os.environ['__OW_API_KEY'].split(":")
    return (up[0], up[1])

def whisk_trigger(trigger, args):
    invoke = url("triggers/%s" % trigger)
    resp = requests.post(
        url=invoke, 
        auth=auth(),
        json=args
    )
    return json.loads(resp.text)

def main(args):
    #print(args)
    input = {"lines": args["text"].split(" ")}
    return whisk_trigger("python-trigger", input)

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
