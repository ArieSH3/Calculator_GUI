'''
	Author: Stefan Popovic
	Date  : 20/05/2021

	About : Creating a calculator with Python and PySimpleGUI library

'''

import PySimpleGUI as sg

# default settings
bw = {'size':(7,2), 'button_color':('black', '#F8F8F8')}
bt = {'size':(7,2), 'button_color':('black', '#F1EABC')}
bo = {'size':(15,2), 'button_color':('black', '#ECA527'), 'focus':True}

layout = [
	[sg.Text('PyDataMath-II', size=(50,1), justification='right', background_color='#272533', text_color='white')],
	[sg.Text('0.0000', size=(36,1), justification='right', background_color='black', text_color='red')],
	[sg.Button('C',**bt), sg.Button('CE',**bt), sg.Button('%',**bt), sg.Button('/',**bt)],
	[sg.Button('7',**bw), sg.Button('8',**bw), sg.Button('9',**bw), sg.Button('*',**bt)],
	[sg.Button('4',**bw), sg.Button('5',**bw), sg.Button('6',**bw), sg.Button('-',**bt)],
	[sg.Button('1',**bw), sg.Button('2',**bw), sg.Button('3',**bw), sg.Button('+',**bt)],
	[sg.Button('0',**bw), sg.Button('.',**bw), sg.Button('=',**bo)]
]

window = sg.Window('PyDataMath-II', layout=layout, background_color='#272533', size=(300,310))

event, values = window.read()
window.close()