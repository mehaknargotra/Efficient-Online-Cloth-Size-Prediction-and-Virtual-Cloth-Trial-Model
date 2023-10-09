
#!/usr/bin/env python
import PySimpleGUI as sg
import os
from PIL import Image, ImageTk
import io
# import GUI2
import resizeinputargs


"""
Simple Image Browser based on PySimpleGUI
--------------------------------------------
There are some improvements compared to the PNG browser of the repository:
1. Paging is cyclic, i.e. automatically wraps around if file index is outside
2. Supports all file types that are valid PIL images
3. Limits the maximum form size to the physical screen
4. When selecting an image from the listbox, subsequent paging uses its index
5. Paging performance improved significantly because of using PIL
Dependecies
------------
Python3
PIL
"""
folder= sg.popup_get_folder('Image folder to open', default_path='')
def get_folder():
# Get the folder containin:g the images from the user
    global folder
    folder = sg.popup_get_folder('Image folder to open', default_path='')
    if not folder:
        sg.popup_cancel('Cancelling')
        raise SystemExit()

# PIL supported image types
img_types = (".png", ".jpg", "jpeg", ".tiff", ".bmp")

# get list of files in folder
flist0 = os.listdir(folder)

# create sub list of image files (no sub folders, no wrong file types)
fnames = [f for f in flist0 if os.path.isfile(
    os.path.join(folder, f)) and f.lower().endswith(img_types)]

num_files = len(fnames)                # number of iamges found
if num_files == 0:
    sg.popup('No files in folder')
    raise SystemExit()

del flist0                             # no longer needed

# ------------------------------------------------------------------------------
# use PIL to read data of one image
# ------------------------------------------------------------------------------

# def call_GUI2():
#     #win2 = Toplevel(root)
#     print("personimage IN GUI2 IS=",personimage)
#     GUI2.GUI21()
#     return

def call_resize():
    #win2 = Toplevel(root)

    print("In function call_resize!!")
    #import fileexpnew m
    #root = fileexpnew.Root() m
    #root.mainloop() m
    #print("call_resize==",root.personimage) m
    # fileexp.__init__()
    # img=r'C:\Users\Mehek\Desktop\PROJECT\GUI\7.jpg'
    #print("Bande ka path ",img)
    #print("shirt path", personimage)
    import resizeinputargs
    from nandiniopenfilenew import filename
    resizeinputargs.resizeinput(personimage,filename)
    return



def get_img_data(f, maxsize=(500, 850), first=False):
    """Generate image data using PIL
    """
    img = Image.open(f)
    img.thumbnail(maxsize)
    if first:                     # tkinter is inactive the first time
        bio = io.BytesIO()
        img.save(bio, format="PNG")
        del img
        return bio.getvalue()
    return ImageTk.PhotoImage(img)
# ------------------------------------------------------------------------------


# make these 2 elements outside the layout as we want to "update" them later
# initialize to the first file in the list
personimage = os.path.join(folder, fnames[0])  # name of first file in list
image_elem = sg.Image(data=get_img_data(personimage, first=True))
personimage_display_elem = sg.Text(personimage, size=(80, 3))
file_num_display_elem = sg.Text('File 1 of {}'.format(num_files), size=(15, 1))

# define layout, show and read the form
col = [[personimage_display_elem],
       [image_elem]]

col_files = [[sg.Listbox(values=fnames, change_submits=True, size=(60, 30), key='listbox')],
             [sg.Button('Next', size=(8, 2),button_color=('white', 'green')),
              sg.Button('Prev', size=(8, 2),button_color=('white', 'green')),
             sg.Button('Output', size=(8, 2),button_color=('white', 'darkorange1')), file_num_display_elem]]

layout = [[sg.Column(col_files), sg.Column(col)]]

window = sg.Window('Image Browser', layout, return_keyboard_events=True,
                   location=(0, 0), use_default_focus=False)

# loop reading the user input and displaying image, personimage
i = 0
while True:
    # read the form
    event, values = window.read()
    print(event, values)
    # perform button and keyboard operations
    if event == sg.WIN_CLOSED:
        break
    elif event in ('Next', 'MouseWheel:Down', 'Down:40', 'Next:34'):
        i += 1
        if i >= num_files:
            i -= num_files
        personimage = os.path.join(folder, fnames[i])
    elif event in ('Prev', 'MouseWheel:Up', 'Up:38', 'Prior:33'):
        i -= 1
        if i < 0:
            i = num_files + i
        personimage = os.path.join(folder, fnames[i])
    elif event in ('Output'):
   		
    	call_resize()
    	print("resizeinput called")
    elif event == 'listbox':            # something from the listbox
        f = values["listbox"][0]            # selected personimage
        personimage = os.path.join(folder, f)  # read this file
        i = fnames.index(f)                 # update running index
    else:
        personimage = os.path.join(folder, fnames[i])

    # update window with new image

    print("personimage=======",personimage)

    image_elem.update(data=get_img_data(personimage, first=True))
    # update window with personimage
    personimage_display_elem.update(personimage)
    # update page display
    file_num_display_elem.update('File {} of {}'.format(i+1, num_files))

window.close()