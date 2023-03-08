from tkhtmlview import html_parser
import PySimpleGUI as sg

def set_html(widget, html, strip=True):
    prev_state = widget.cget('state')
    widget.config(state=sg.tk.NORMAL)
    widget.delete('1.0', sg.tk.END)
    widget.tag_delete(widget.tag_names)
    html_parser.w_set_html(widget, html, strip=strip)
    widget.config(state=prev_state)


html = ''''''

with open('example.html', 'r') as file:
    html = file.read()

font = ("Courier New", 12, 'bold')
sg.theme("DarkBlue3")
sg.set_options(font=font)

layout_advertise = [
    [sg.Multiline(
        size=(50, 10),
        border_width=2,
        text_color='white',
        background_color='green',
        disabled=True,
        no_scrollbar=True,
        expand_x=True,
        expand_y=True,
        key='HTML')],
]

layout = [
    [
     sg.Frame("Content",  layout_advertise, expand_x=True, expand_y=True)],
]
window = sg.Window('Title', layout, finalize=True, use_default_focus=False)
for element in window.key_dict.values():
    element.block_focus()

display = window['HTML'].Widget
html_parser = html_parser.HTMLTextParser()
set_html(display, html)
width, height = display.winfo_width(), display.winfo_height()

while True:

    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    print(event, values)

window.close()