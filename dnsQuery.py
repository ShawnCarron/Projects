"""
A simple DNS calculator that returns host and whois data to assist frontline agents.
  
Author:     Shawn Carron
Email:      shawn.carron@gmail.com
Created:    2021-10-23
Modified:   2024-09-10
Version:    2.0

"""
import pyperclip as pc
import PySimpleGUI as sg
import dns.resolver
import socket
import whois

##------------------------WINDOW AND LAYOUT------------------------##

# Set Theme
sg.theme("DefaultNoMoreNagging")

# Right click Menu
right_click_menu = ['Copy', ['Paste']]

# Set Layout
layout = [
    [   sg.Text("Domain Name: "), 
        sg.InputText(key="-getHost-", background_color="Ivory", justification="left", text_color="black", right_click_menu=right_click_menu)
    ],

    [   sg.Text("Select Lookup:"),
        sg.Radio("A-Record", "radio1", key="-radHost-"),
        sg.Radio("MX Records", "radio1", key="-radMX-"),
        sg.Radio("Whois", "radio1", key="-radwhois-"), 
        sg.Radio("Full", "radio1", key="-radFull-", default=True) 
    ],

    [   sg.Submit("Submit", button_color="Blue"),
        sg.Button("Clear", button_color="Blue"), 
        #sg.Button("Parse", button_color="Green"), 
        sg.Button("Exit")
    ],

    [   sg.Multiline(key="-textbox-", background_color="Ivory", justification="left", text_color="black", size=(80, 30), pad=(10, 10, (10, 10)))
    ],
        ]

# Create Main Window
window = sg.Window("DNS Tools", layout, size=(500, 400), resizable=False)

# ------------------------FUNCTIONS------------------------##

def host_lookup(): 
    try:
        hostName = values["-getHost-"]
        getIPAddr = socket.gethostbyname(hostName) # Get the IP address for the domain.
        ptr = socket.gethostbyaddr(getIPAddr)[0] # Reverse IP lookup to see what server this host lives on.
        window["-textbox-"].print(f"The IP for {hostName} is: {getIPAddr}. \nThis domain is hosted on: {ptr}\n ")
    except Exception as err:
        window["-textbox-"].print(f"That domain name does not exist, check your spelling and try again: ", err)
    return()

##----------------------------------------------------------##

def mx_lookup():
    # Get MX records
    try: 
        hostName = values["-getHost-"]
        result = dns.resolver.resolve(hostName, "MX",)
        window["-textbox-"].print(f"The MX Records for {hostName} are:")
        for rdata in result:
            window["-textbox-"].print(rdata.exchange, f'This record has a priority of', rdata.preference)
    except Exception as err:
            window["-textbox-"].update(err)
    window["-textbox-"].print(f"")
    return()
##----------------------------------------------------------------##

def whois_lookup():
    # Get Whois data
    try:
        hostName = values["-getHost-"]
        w = whois.whois(hostName)
        tld = hostName.split(".")[-1]
        nameservers = dns.resolver.resolve(hostName, "NS")
        if tld == "ca":
            window["-textbox-"].print(f"Registrar: ", w.registrar, "\nExpiration Date: ", w.expiration_date, "\n",)
            window["-textbox-"].print(f"Name Servers: ")
            for data in nameservers:
                window["-textbox-"].print(data)
        else: # same for now but .ca and the other tld's are different in how they display their data.
            window["-textbox-"].print(f"Registrar: ", w.registrar, "\nExpiration Date: ", w.expiration_date, "\n",)
            window["-textbox-"].print(f"Name Servers: ")
            for data in nameservers:
                window["-textbox-"].print(data)
    except Exception as err:
        window["-textbox-"].update(err)
    return()
##----------------------------------------------------------------##

    # Return Full Lookup

def full_lookup():
    
    host_lookup() # Get domain IP
    mx_lookup() # Get MX records
    whois_lookup() # Get whois data

def clear_screen():
    window["-textbox-"].update("")
    return()

##---------------------EVENT LOOP---------------------##

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Submit" and values["-getHost-"] == "":
        window["-textbox-"].update("Domain Name field cannot be blank. Please enter a domain name and try again.")
    elif event == "Clear":
        window["-getHost-"].update("")
        clear_screen()
    elif event == "Submit" and values["-radHost-"] == True:
        clear_screen()
        host_lookup()
    elif event == "Submit" and values["-radMX-"] == True:
        clear_screen()
        mx_lookup()
    elif event == "Submit" and values["-radwhois-"] == True:
        clear_screen()
        whois_lookup()    
    else:
        clear_screen()
        full_lookup()
window.close()
