import os, requests, json

def url(operation):
    url = "%s/api/v1/namespaces/%s/%s" % (
        os.environ["__OW_API_HOST"],
        os.environ["__OW_NAMESPACE"],
        operation
    )
    return url 

def auth():
    up = os.environ['__OW_API_KEY'].split(":")
    return (up[0], up[1])

def whisk_activation(id):
    return json.loads(
      requests.get(
          url=url("activations/%s" % id),
          auth=auth()
      ).text)

def whisk_activations():
    return json.loads(
      requests.post(
         url=url("activations?limit=3"),
         auth=auth()
      ).text)

def main(args):
  id = args.get("activationId")
  if id:
    return whisk_activation(id)['response']['result']
  return {"error": "missing activationId"}
