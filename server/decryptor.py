from common import encryption_utils
import json

def id_is_valid(data) -> bool:
    return True

class Brain:
    def __init__(self, database_path):
        self.path = database_path
        self.node_ids = []
        self.node_data = None
        self.dt = None
        self.id = None
        self.ts = None

    def sense(self, payload):
        self.payload = json.loads(encryption_utils.decrypt_message(payload))
        self.id = self.payload["id"]
        self.ts = self.payload["timestamp"]
        self.dt = self.payload["data"]
        print("="*30);
        print(f"Reading packet from ~> {[self.id]}")

    def dump_node_data(self):
        self.fname = f"{self.path+self.id}.json"

        if not id_is_valid(self.id): return 1

        if self.id not in self.node_ids:
            print(f"Adding node in known nodes ~> {[x for x in self.node_ids]}")
            self.node_ids.append(self.id)
            node_database = open(self.fname, "w+")

            f_struct = {x.upper():[] for x in self.dt}
            f_struct["TIMESTAMPS"] = []

            json.dump(
                f_struct, 
                node_database,
                indent=4
                )
            node_database.close()

    def read_data(self):    
        with open(self.fname, "r") as f_read:
            self.node_data = json.loads(f_read.read())
            f_read.close()
            
        print(f"Loading Database '{self.fname}'")

    def write_data(self):
        with open(self.fname, "w+") as f_write:
            self.node_data["TIMESTAMPS"].append(self.ts)
            for param in self.dt: 
                self.node_data[param.upper()] += [self.dt[param]]
            json.dump(
                self.node_data, 
                f_write,
                indent=4
            )
            f_write.close()
        print("~> Data Dump Completed")