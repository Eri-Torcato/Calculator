import PySimpleGUI as sg


"""
[
    []
    []
    []
]
"""

layout = [
    [ sg.Input(size=(21, 1),
               font=('Helvetica', 18),
               text_color='black',
               background_color='white',
               justification='right',
               key='display',
               default_text='0') ],

    [sg.Output(key='output_operation', size=(21, 1),
               text_color='black',
               background_color='white')],

    [sg.Button('C', size=(5, 2), font=('Helvetica', 14)),
     sg.Button('()', size=(5, 2), font=('Helvetica', 14)),
     sg.Button('%', size=(5, 2), font=('Helvetica', 14)),
     sg.Button('/', size=(5, 2), font=('Helvetica', 14))],

    [sg.Button('7', size=(5, 2), font=('Helvetica', 14)),
     sg.Button('8', size=(5, 2), font=('Helvetica', 14)),
     sg.Button('9', size=(5, 2), font=('Helvetica', 14)),
     sg.Button('*', size=(5, 2), font=('Helvetica', 14))],

    [sg.Button('4', size=(5, 2), font=('Helvetica', 14)),
     sg.Button('5', size=(5, 2), font=('Helvetica', 14)),
     sg.Button('6', size=(5, 2), font=('Helvetica', 14)),
     sg.Button('-', size=(5, 2), font=('Helvetica', 14))],

    [sg.Button('1', size=(5, 2), font=('Helvetica', 14)),
     sg.Button('2', size=(5, 2), font=('Helvetica', 14)),
     sg.Button('3', size=(5, 2), font=('Helvetica', 14)),
     sg.Button('+', size=(5, 2), font=('Helvetica', 14))],

    [sg.Button('0', size=(5, 2), font=('Helvetica', 14)),
     sg.Button('.', size=(5, 2), font=('Helvetica', 14)),
     sg.Button('<x', key='del', size=(5, 2), font=('Helvetica', 14)),
     sg.Button('=', size=(5, 2), font=('Helvetica', 14))]
]


def calculate(expression):
    try:
        return eval(expression)
    except SyntaxError:
        print("Invalid expression. Please enter a valid mathematical formula.")
        sg.popup_error('Syntax error!', title='Error')
        return 0
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        sg.popup_error('ZeroDivisionError!', title='Error')
        return 0


def show_error_example():
    sg.popup_error('This is an error message!', title='Error')


# Create the window
window = sg.Window('Simple Calculator', layout, resizable=True)

current_expression = ""
output_text = ""

while True:

    button_pressed, values = window.read()

    if button_pressed == sg.WINDOW_CLOSED:
        break

    # button_pressed = values[event]  # Get the button that was clicked

    if button_pressed in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '+', '-', '*', '/'):
        # current_expression += button_pressed
        current_expression = current_expression + button_pressed
        output_text = current_expression

        window['display'].update(current_expression)
        continue

    if button_pressed == 'C':
        current_expression = ""
        output_text = ""
        window['display'].update('0')
        continue

    if button_pressed == 'DEL':  # Handle backspace-like functionality
        if current_expression:
            current_expression = current_expression[:-1]
            output_text = current_expression
        continue

    if button_pressed == '=':
        result = calculate(current_expression)
        current_expression = str(result)
        window['output_operation'].update(current_expression)
        continue



window.close()