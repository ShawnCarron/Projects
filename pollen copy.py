'''
  A simple DNS calculator that returns host and whois data.
  
  Author:     Shawn Carron
  Email:      shawn.carron@gmail.com
  Modified:   2021-10-16
  
'''
import PySimpleGUI as sg
import dns.resolver
import socket
import whois

##-----WINDOW AND LAYOUT------------------------------##

# Set Theme
sg.theme('DefaultNoMoreNagging')

# Set Layout
layout = [  [sg.Text("Enter domain name: "), sg.InputText(key='-getHost-', background_color='LightGrey', justification='left',text_color='black')],
            [sg.Text('Select Lookup Type:'), 
            sg.Radio('A-Record', "RADIO1", key="-radhost-"), 
            sg.Radio('Whois', "RADIO1", key="-radwhois-"), 
            sg.Radio('MX Records', "RADIO1", key="-radMX-"),
            sg.Radio('Full', "RADIO1", key="-radFull-", default=True)],
            [sg.Submit('Submit'), sg.Button('Exit')],
            [sg.Multiline(size=(80, 30), justification='l', key='-textbox-', pad=(10, 10, (10, 10)), background_color='LightGrey', disabled=False, text_color='black')]
        ]

# Create Window
window = sg.Window('DNS Tools', layout, size = (500, 400))

global name_server, name_server2
name_server = '8.8.8.8' # Google's NS
name_server2 = '206.248.182.3' # Teksavvy NS


#-----FUNCTIONS--------------------------------------##
def host_lookup():
    # Get the IP address for the domain.
    hostName = values['-getHost-']
    getIPAddr = socket.gethostbyname(f"{hostName}")
    # Reverse IP lookup.
    ptr = socket.gethostbyaddr(getIPAddr)[0]
    window['-textbox-'].print(f"The A record for {hostName} is: {getIPAddr}\nThis is domain is hosted on: {ptr}\n " ) 
    
def mx_Check():   
    # Get the MX records.
    hostName = values['-getHost-']
    result = dns.resolver.resolve(hostName, 'MX',)
    window['-textbox-'].print(f"The MX Records for {hostName} are:\n")
    for rdata in result:
        window['-textbox-'].print(rdata.exchange)
    
def who_is_lookup():
    # Whois check and results
    hostName = values['-getHost-']
    w = whois.whois(hostName)
    window['-textbox-'].print(f"Registrar: ", w.registrar, "\nExpiration Date: ", w.expiration_date[-1], "\nName Servers: ", w.name_servers[0:2])
    
def clear_screen():
    window['-textbox-'].update('')
    
#-----MAIN EVENT LOOP--------------------------------##
while True:
    event, values = window.read() 
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == "Submit" and values["-radhost-"] == True:
        clear_screen()
        host_lookup()
    elif event == "Submit" and values["-radwhois-"] == True:
        clear_screen()
        who_is_lookup()
    elif event == "Submit" and values["-radMX-"] == True:
        clear_screen()
        mx_Check()
    elif event == "Submit" and values["-radFull-"] == True:
        clear_screen()
        host_lookup()
        mx_Check()
        who_is_lookup()   
    else: 
        pass # if the domain box is empty do nothing
        
 
window.close()