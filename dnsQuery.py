"""
  A simple DNS calculator that returns host and whois data because the agents in my department are dumb.
  
  Author:     Shawn Carron
  Email:      shawn.carron@gmail.com
  Modified:   2021-10-16
  
"""
import PySimpleGUI as sg
import dns.resolver
import socket
import whois

##------------------------WINDOW AND LAYOUT------------------------##

# Set Theme
sg.theme("DefaultNoMoreNagging")

# Set Layout
layout = [
    [
        sg.Text("Domain Name: "), sg.InputText(key="-getHost-", background_color="LightGrey", 
        justification="left", text_color="black", default_text="",),
    ],
    [
        sg.Text("Select Lookup:"),
        sg.Radio("A-Record", "RADIO1", key="-radhost-"),
        sg.Radio("Whois", "RADIO1", key="-radwhois-"),
        sg.Radio("MX Records", "RADIO1", key="-radMX-"),
        sg.Radio("Full", "RADIO1", key="-radFull-", default=True),
    ],
    # [
    #     sg.Text("Select DNS:"),
    #     sg.Radio("TekSavvy DNS", "RADIO2", key="-radtek-", default=True),
    #     sg.Radio("Google DNS", "RADIO2", key="-radgoogle-"),
    # ],
    [sg.Submit("Submit"), sg.Button("Clear"), sg.Button("Exit")],
    [
        sg.Multiline(
            size=(80, 30),
            justification="l",
            key="-textbox-",
            pad=(10, 10, (10, 10)),
            background_color="LightGrey",
            disabled=False,
            text_color="black",
        )
    ],
]

# Create Window
window = sg.Window("DNS Tools", layout, size=(500, 400), resizable=False)

# ------------------------FUNCTIONS------------------------##

def host_lookup():
    try:
        # Get the IP address for the domain.
        hostName = values["-getHost-"]
        getIPAddr = socket.gethostbyname(f"{hostName}")
        # Reverse IP lookup.
        ptr = socket.gethostbyaddr(getIPAddr)[0]
        window["-textbox-"].print(f"The IP for {hostName} is: {getIPAddr}. \nThis domain is hosted on: {ptr}\n ")
    except Exception as err:
        window["-textbox-"].update(err)


def mx_lookup():
    # Get the MX records.
    try:
        hostName = values["-getHost-"]
        result = dns.resolver.resolve(hostName, "MX",)
        window["-textbox-"].print(f"The MX Records for {hostName} are:")
        for rdata in result:
            window["-textbox-"].print(rdata.exchange)
    except Exception as err:
        window["-textbox-"].update(err)


def whois_lookup():
    # Get Whois data
    try:
        hostName = values["-getHost-"]
        w = whois.whois(hostName)
        tld = hostName.split(".")[-1]
        if tld == "ca":
            nameservers = dns.resolver.resolve(hostName, "NS")
            window["-textbox-"].print("Registrar: ", w.registrar, "\nExpiration Date: ", w.expiration_date, "\n",)
            window["-textbox-"].print("Name Servers: ")
            for data in nameservers:
                window["-textbox-"].print(data)
        else:
            window["-textbox-"].print("Registrar: ", w.registrar, "\nExpiration Date: ", w.expiration_date, "\n",)
            window["-textbox-"].print("Name Servers:\n", ", ".join(w.name_servers[0:2]).lower())
    except Exception as err:
        window["-textbox-"].update(err)


def full_lookup():
    try:
        # Get the IP address for the domain.
        hostName = values["-getHost-"]
        getIPAddr = socket.gethostbyname(f"{hostName}")
        # Reverse IP lookup.
        ptr = socket.gethostbyaddr(getIPAddr)[0]
        window["-textbox-"].print(
            f"The IP for {hostName} is: {getIPAddr}. \nThis domain is hosted on: {ptr}\n "
        )
    except Exception as err:
        window["-textbox-"].update(err)
        window["-textbox-"].print("")
    except Exception as err:
        # Getting the MX Records.
        result = dns.resolver.resolve(
            hostName,
            "MX",
        )
        window["-textbox-"].print(f"The MX Records for {hostName} are:")
        for rdata in result:
            window["-textbox-"].print(rdata.exchange)
        window["-textbox-"].print(err)
        window["-textbox-"].print("")

        # Whois Section
    try:
        w = whois.whois(hostName)
        tld = hostName.split(".")[-1]
        if tld == "ca":
            nameservers = dns.resolver.resolve(hostName, "NS")
            window["-textbox-"].print("Registrar: ", w.registrar, w.expiration_date, "\n",)
            window["-textbox-"].print("Name Servers: ")
            for data in nameservers:
                window["-textbox-"].print(data)
        else:
            window["-textbox-"].print("Registrar: ", w.registrar, w.expiration_date,"\n",)
            window["-textbox-"].print("Name Servers:\n", ", ".join(w.name_servers[0:2]).lower()
            )
    except Exception as err:
        window["-textbox-"].print(err)


def clear_screen():
    window["-textbox-"].update("")


##---------------------EVENT LOOP---------------------##
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Submit" and values["-getHost-"] == "":
        window["-textbox-"].update("Domain Name field cannot be blank, enter a domain name and try again.")
        pass
    elif event == "Clear":
        window["-getHost-"].update("")
        clear_screen()
    elif event == "Submit" and values["-radhost-"] == True:
        clear_screen()
        host_lookup()
    elif event == "Submit" and values["-radwhois-"] == True:
        clear_screen()
        whois_lookup()
    elif event == "Submit" and values["-radMX-"] == True:
        clear_screen()
        mx_lookup()
    elif event == "Submit" and values["-radFull-"] == True:
        clear_screen()
        full_lookup()
    else:
        pass
window.close()
