import matplotlib.pyplot as plt
import numpy as np
import json
import common.config
import common.config as cfg
import datetime
import os

class Engine:
    def __init__(self):
        self.dump = []
        self.measures = {}
        self.node_ids = []

    def load_dumps(self):
        for node_id in os.listdir(common.config.SERVER_PROPERTIES["DATA_PATH"]):
            self.node_ids.append(node_id)
            with open(common.config.SERVER_PROPERTIES["DATA_PATH"]+node_id, "r") as node_dump:
                self.dump.append(json.load(node_dump))
        
        for i, values in enumerate(self.dump):
            for value in values:
                try:
                    self.dump[i][value] = np.array(self.dump[i][value]).astype(float)
                except:
                    continue
    
    def get_data(self):
        pass
        for i, node in enumerate(self.dump):
            data_array = {}
            for j, dt in enumerate(node):
                if dt == "TIMESTAMPS": continue
                data_array[dt] = np.array(node[dt]).astype(float)
            self.measures[self.node_ids[i]] = data_array
            self.measures["TIMESTAMPS"] = node["TIMESTAMPS"]

    def plot_graph(self):
        groups = []

        if cfg.SERVER_PROPERTIES["GROUPING_ENABLE"]:
            for i in self.dump:
                for j in i:
                    group = j[:2]
                    if group not in groups:
                        groups.append(group)
            del groups[len(groups)-1]
        group_sz = len(group)

        for j, node in enumerate(self.node_ids):

            
            for group in groups:
                fig, ax = plt.subplots()
                for n, i in enumerate(self.dump[j]):
                    if i[:2] != group: continue
                    print(i, group)
                    if n == len(self.dump[j])-1: break
                    ax.plot(self.dump[j][i], label=i)
                    
                    ax.legend()

                fig.subplots_adjust(bottom=0.15)

                plt.xticks(
                    ticks=[i for i in range(0, len(self.dump[j]["TIMESTAMPS"]), 10)],
                    labels=[self.dump[j]["TIMESTAMPS"][i] for i in range(0, len(self.dump[j]["TIMESTAMPS"]), 10)],
                    rotation=45
                )
                plt.savefig(f'{cfg.SERVER_PROPERTIES["OUT_PATH"]}{group}{node}_{str(datetime.datetime.now())[:19][11:]}.jpg')


