import json

data = {
    "imdata": [
        {
            "l1PhysIf": {
                "attributes": {
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/33]",
                    "descr": "",
                    "speed": "inherit",
                    "mtu": "9150"
                }
            }
        },
        {
            "l1PhysIf": {
                "attributes": {
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/34]",
                    "descr": "",
                    "speed": "inherit",
                    "mtu": "9150"
                }
            }
        },
        {
            "l1PhysIf": {
                "attributes": {
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/35]",
                    "descr": "",
                    "speed": "inherit",
                    "mtu": "9150"
                }
            }
        }
    ]
}

print("Interface Status")
print("="*80)
print("DN".ljust(50), "Description".ljust(20), "Speed".ljust(8), "MTU")
print("-"*80)

for item in data["imdata"]:
    attr = item["l1PhysIf"]["attributes"]
    print(attr["dn"].ljust(50),
          attr["descr"].ljust(20),
          attr["speed"].ljust(8),
          attr["mtu"])
