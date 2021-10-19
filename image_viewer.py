import PySimpleGUI as sg
import os.path

file_list_column = [
    [
        sg.Text("Image Folder"),
        sg.In(size=(25,1), enable_events=True, key="-folder-"),
        sg.FolderBrowse(),
        sg.Button("Exit")
    ],

    [
        sg.Listbox(
            values=[], enable_events=True, size=(40,20), 
            key="-file list-"
        )
    ],
]

image_viewer_column = [
    [sg.Text("Choose an image from the list on the left:")],
    [sg.Text(size=(40,1), key="-tout-")],
    [sg.Image(key="-image-")],
]

layout= [
    
    [
    sg.Column(file_list_column),
    sg.VSeparator(),
    sg.Column(image_viewer_column),
    ]
]
window = sg.Window("Image Viewer", layout)

while True:
    event, values, = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

if event == "-folder-":
    folder = values["-folder-"]
    try:
        file_list = os.listdir(folder)
    except:
        file_list = []
    fnames = [
        f 
        for f in file_list
        if os.path.isfile(os.path.join(folder, f))
        and f.lower().endswith((".png", ".gif"))
    ] 
    window["-file list-"].update(fnames)
elif event == "-file list-": 
    try:
        filename = os.path.join(
            values["-folder-"], values["-file -list-"] [0]
        )
        window["tout"].update(filename)
        window["-image-"].update(filename=filename)
    except:
        pass

window.close()

