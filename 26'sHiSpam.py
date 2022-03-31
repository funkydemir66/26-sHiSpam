import sys
from g_python.gextension import Extension
from g_python.hmessage import Direction
from time import sleep
import threading


extension_info = {
    "title": "26'sHiSpam",
    "description": "hic: on&off&cho&pla ",
    "version": "0.2",
    "author": "funkydemir66"
}

ext = Extension(extension_info, sys.argv, silent=True)
ext.start()

KATMER = "UseFurniture"

KASAR = "PassCarryItem"

kod = ""

kod2 = ""

sec_kod = sc = False

def konusma(msj):
    global sc, sec_kod, sec_player

    def main():
        while sc:
            for i in range(256):
                if sc:
                    ext.send_to_server('{out:'+str(KATMER)+'}{i:'+str(kod)+'}{i:0}')
                    sleep(0.1)
                    ext.send_to_server('{out:'+str(KASAR)+'}{i:'+str(kod2)+'}')
                    sleep(0.1)

    text = msj.packet.read_string()

    if text == ':his cho':
        msj.is_blocked = True
        sec_kod = True
        ext.send_to_client('{in:Chat}{i:123456789}{s:"Choose the furni from which you will buy the hand material"}{i:0}{i:30}{i:0}{i:0}')


    if text == ':his pla':
        msj.is_blocked = True
        sec_player = True
        ext.send_to_client('{in:Chat}{i:123456789}{s:"Give handitem to the person you are spamming"}{i:0}{i:30}{i:0}{i:0}')

    if text == ':his on':
        msj.is_blocked = True
        sc = True
        thread = threading.Thread(target=main)
        thread.start()
        ext.send_to_client('{in:Chat}{i:123456789}{s:"Script: on "}{i:0}{i:30}{i:0}{i:0}')

    if text == ':his off':
        msj.is_blocked = True
        sc = False
        ext.send_to_client('{in:Chat}{i:123456789}{s:"Script: off "}{i:0}{i:30}{i:0}{i:0}')

def yukle_kod(p):
    global kod, sec_kod

    if sec_kod:
        mobi_id, _, _ = p.packet.read("iii")
        kod = str(mobi_id)
        ext.send_to_client('{in:Chat}{i:123456789}{s:"idd: saved "}{i:0}{i:30}{i:0}{i:0}')
        sec_kod = False

def yukle_kod2(p):
    global kod2, sec_player

    if sec_player:
        player_id, _, _ = p.packet.read("iii")
        kod2 = str(player_id)
        ext.send_to_client('{in:Chat}{i:123456789}{s:"idd: saved "}{i:0}{i:30}{i:0}{i:0}')
        sec_player = False



ext.intercept(Direction.TO_SERVER, konusma, 'Chat')
ext.intercept(Direction.TO_SERVER, yukle_kod, 'UseFurniture')
ext.intercept(Direction.TO_SERVER, yukle_kod2, 'PassCarryItem')
