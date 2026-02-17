import json

json_input = '{"name":"Bob","age":30}'
parsed = json.loads(json_input)
print(parsed["name"])
