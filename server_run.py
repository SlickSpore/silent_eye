from server import server
from server.decryptor import Brain
from gui.render_data import Engine

# Presenting Data Reports

engine = Engine()
engine.load_dumps()
engine.get_data()
engine.plot_graph()
exit()


# Running Server
try:
    brain = Brain("")
    server.asyncio.run(server.server())
except KeyboardInterrupt:
    print("Server Closing")
    