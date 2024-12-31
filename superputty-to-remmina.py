#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

# -------------------------------------------------------------------
# template of the configuration of remmina
# -------------------------------------------------------------------
REMMINA_TEMPLATE = """[remmina]
password=""
gateway_username=
notes_text=
vc=
window_height=480
disable-smooth-scrolling=0
preferipv6=0
ssh_tunnel_loopback=0
serialname=
audiblebell=0
websockets=0
printer_overrides=
ssh_auth=0
name=test
console=0
colordepth=99
security=
precommand=
sshsavesession=0
disable_fastpath=0
run_line=
postcommand=
ssh_color_scheme=0
sshlogname=
ssh_charset=
group=
server=
ssh_tunnel_certfile=
glyph-cache=0
ssh_tunnel_enabled=0
disableclipboard=0
audio-output=
parallelpath=
monitorids=
cert_ignore=0
ssh_stricthostkeycheck=0
serialpermissive=0
left-handed=0
protocol=SSH
old-license=0
ssh_kex_algorithms=
resolution_mode=0
ssh_proxycommand=
ssh_tunnel_password=
ssh_compression=0
pth=
disableautoreconnect=0
loadbalanceinfo=
ssh_ciphers=
clientbuild=
multitransport=0
clientname=
resolution_width=1024
drive=
gateway_server=
relax-order-checks=0
username=
base-cred-for-gw=0
gateway_domain=
profile-lock=0
network=none
rdp2tcp=
serialdriver=
rdp_reconnect_attempts=
gateway_password=
domain=
restricted-admin=0
exec=
serialpath=
multimon=0
ssh_hostkeytypes=
enable-autostart=0
smartcardname=
usb=
disablepasswordstoring=0
ssh_tunnel_passphrase=
shareprinter=0
viewmode=1
quality=0
span=0
shareparallel=0
parallelname=
ssh_tunnel_auth=0
keymap=
ssh_tunnel_username=
execpath=
shareserial=0
resolution_height=768
timeout=
useproxyenv=0
sharesmartcard=0
freerdp_log_filters=
microphone=
dvc=
ssh_tunnel_privatekey=
window_maximize=1
ssh_tunnel_server=
ignore-tls-errors=1
gwtransp=http
gateway_usage=0
sshlogenabled=0
window_width=640
sound=off
freerdp_log_level=INFO
ssh_passphrase=
"""

# -------------------------------------------------------------------
# name of the xml superputty configuration exported 
# -------------------------------------------------------------------
XML_FILE = "sessioni.xml"

def main():
    # Parsing XML
    tree = ET.parse(XML_FILE)
    root = tree.getroot()

    # search all the tags <SessionData>
    for sd in root.findall('SessionData'):
        session_id = sd.get('SessionId', '')
        username   = sd.get('Username', '')

        # replace characters that is not supported inside the name
        safe_session_id = session_id.replace('/', '-').replace(' ', '_')

        # create the .remmina with the name of the sessionid
        filename = f"group_ssh_{safe_session_id}_othername.remmina"

        # change name and isername based of the data
        file_content = REMMINA_TEMPLATE
        file_content = file_content.replace(
            "username=insert here what to change",
            f"username={username}"
        )
        file_content = file_content.replace(
            "name=giveitaname",
            f"name={safe_session_id}"
        )

        # save the file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(file_content)

        print(f"File created: {filename}")

if __name__ == "__main__":
    main()
