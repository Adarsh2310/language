import PySimpleGUI as sg

sg.theme('DarkTeal9')

layout = [
    [sg.Text('Please find the sentence:')],
    [sg.Text('Button1', size=(15, 1)), sg.InputText(key='Word')],
    [sg.Text('Button2', size=(15, 1)), sg.InputText(key='Word')],
    [sg.Text('I speak', size=(15, 1)), sg.Checkbox('Hindi'),sg.Checkbox('English'),sg.Checkbox('Other Language'),],
    [sg.Text('Convert to Sanskrit', size=(15, 1)), sg.InputText(key='Word')],


    [sg.Submit(), sg.Exit()]

]
window = sg.Window('sanskrit rule conversion', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Submit':
        print(event, values)
window.close()
