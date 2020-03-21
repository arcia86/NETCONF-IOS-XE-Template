
# User Input

# Please select the lab environment that you will be using today
#     sandbox - Cisco DevNet Always-On / Reserved Sandboxes
#     express - Cisco DevNet Express Lab Backend
#     custom  - Your Own "Custom" Lab Backend
ENVIRONMENT_IN_USE = "sandbox"

# Custom Lab Backend
DNA_CENTER = {
    "host": "",
    "username": "",
    "password": ""
}

# End User Input


# Set the 'Environment Variables' based on the lab environment in use
if ENVIRONMENT_IN_USE == "sandbox":

    # Values for the Always On IOS XE Sandbox
    IOS_XE_1 = {
        "host": "10.97.4.222",
        "username": "cisco",
        "password": "C1sco12345",
        "netconf_port": 830,
        "restconf_port": 443,
        "ssh_port": 22
    }

    # Values for the Reservable IOS XE Sandbox
    IOS_XE_2 = {
        "host": "10.10.20.48",
        "username": "developer",
        "password": "C1sco12345",
        "netconf_port": 830,
        "restconf_port": 443,
        "ssh_port": 22
    }

elif ENVIRONMENT_IN_USE == "express":
    DNA_CENTER = {
        "host": "sandboxdnac.cisco.com",
        "port": 443,
        "username": "devnetuser",
        "password": "Cisco123!"
    }

