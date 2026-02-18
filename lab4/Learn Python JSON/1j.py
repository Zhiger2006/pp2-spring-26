import json

with open("sample-data.json") as f:
    data = json.load(f)

print("Interface Status")
print("=" * 80)
print("DN                                                 Description           Speed    MTU")
print("-" * 80)

for intf in data["imdata"]:
    attr = intf["l1PhysIf"]["attributes"]
    dn = attr.get("dn", "")
    descr = attr.get("descr", "inherit")
    speed = attr.get("speed", "")
    mtu = attr.get("mtu", "")
    
    print(dn, descr, speed, mtu)
