from appJar import gui
import clipboard
# from PIL import Image, ImageTk

multiclipboard = {"First": "", "Second": "", "Third": "", "Fourth": ""}


def reset():
    global multiclipboard
    clipboard.copy("")
    multiclipboard = {"First": "", "Second": "", "Third": "", "Fourth": ""}
    app.setRadioButton("mode", "Save")
    app.setLabel("status", "MultiClip")


def press(btn):
    mode = app.getRadioButton("mode")
    if mode == "Paste":
        clipboard.copy(multiclipboard[btn])
    else:
        multiclipboard[btn] = clipboard.paste()
        app.setRadioButton("mode","Paste")
        app.setLabel('status',"Saved!")

        
with gui("MultiClip", "400x400", bg='#282828', fg="white",
         font={'size': 16, 'family': "Roboto Light"}) as app:
    app.setPadding([10, 10])
    # app.setIcon("<icon goes here>")
    # photo = ImageTk.PhotoImage(Image.open("<image goes here>"))
    # app.addImageData("pic", photo, fmt="PhotoImage")
    app.setInPadding([10, 10])
    app.label("status", "MultiClip", font={'size': 20, 'family': "Roboto Light"}, colspan=3)
    app.radioButton("mode", "Save",  selectcolor="#282828", row=2, column=1)
    app.setRadioButton("mode","Save")
    app.radioButton("mode", "Paste", selectcolor="#282828", row=2, column=2)
    app.buttons(["First", "Second"], [press, press], colspan=3)
    app.buttons(["Third", "Fourth"], [press, press], colspan=3)
    app.buttons(["Clear", "Quit"], [reset, app.stop], colspan=3)
