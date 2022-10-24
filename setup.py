import os
import socket
from contextlib import closing


def find_free_port():
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(('', 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]

home = os.path.expanduser("~")
credentials = open(str(home)+"\\.streamlit\\credentials.toml", "w+")
config = open(str(home)+"\\.streamlit\\config.toml", "w+")

credentials.write("[general]\nemail = \"20h51a05a0@cmrcet.ac.in\"\n")
config.write("[server]\nheadless = false\nport = "+str(find_free_port())+"\n")
