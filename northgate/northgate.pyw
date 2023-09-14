
import platform, random
import subprocess
import shutil
import tkinter as tk
import threading
import os
import sys
import ctypes
from tkinter import *
from tkinter.ttk import Style, Frame as fp
from tkinter import scrolledtext, ttk, filedialog
from inspect import getsourcefile
from os.path import abspath


background="black"
text="white"
light="#474747"
dark="#212121"
font="cambria"
border=0

icon = os.path.join(sys.path[0], "Icon.ico")
iconAlt = os.path.join(sys.path[0], "IconAlt.ico")
iconTest = os.path.join(sys.path[0], "IconTest.ico")

root = Tk()
root['bg']=background

def toggle(event):
    if event.type == EventType.Map:
        root.deiconify()
        root.lift()
    else:
         root.withdraw()

top = Toplevel(root)
top.geometry('0x0+10000+10000') 
top.protocol('WM_DELETE_WINDOW', root.destroy)
top.bind("<Map>", toggle)
top.bind("<Unmap>", toggle)
top.title("Jebby's Jailbrəak")
top.iconbitmap(iconTest)

width=int(2560/3.5)
height=int(1440/1.5)
root.geometry(f"{width}x{height}")
root.overrideredirect(True)
root.title("Jebby's Jailbrəak")
 
buttonframe=Frame(root)

buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)
buttonframe.columnconfigure(4, weight=1)

def on_mouse_press(evt):
    global xp, yp
    xp = evt.x
    yp = evt.y

def on_mouse_drag(evt):
    deltax = evt.x - xp
    deltay = evt.y - yp
    x = root.winfo_x() + deltax
    y = root.winfo_y() + deltay
    root.geometry(f"+{x}+{y}")

def quitpy():
    root.destroy()

def notfullscreen():
    width=int(2560/3.5)
    height=int(1440/1.5)
    output2.configure(height = 1000, width = int(width/20.5))
    mycanva.configure(width=int(width/2.3), height=int(width))
    root.overrideredirect(True) 
    root.attributes('-fullscreen', False)
    button2.config(width=3, height=0, text=" □ ", borderwidth=border, command=fullscreen)

def fullscreen():
    width=int(root.winfo_screenwidth())
    height=int(root.winfo_screenheight())
    output2.configure(height = 1000, width = int(width/12))
    mycanva.configure(width=int(width/1.28), height=int(width)) 
    root.overrideredirect(False)
    root.attributes('-fullscreen', True)
    button2.config(width=3, height=0, text=" 🗗 ", borderwidth=border, command=notfullscreen)

 
buttonframe.bind('<B1-Motion>', on_mouse_drag)
buttonframe.bind('<ButtonPress-1>', on_mouse_press)

buttonframe.pack(padx=0, pady=0, fill="x")
buttonframe.config(width=3, height=0, bg = dark, borderwidth=0)

button1=Button(buttonframe, text=" × ", font=("arial", 13))
button1.config(width=3, height=0, fg = text, bg = dark, activebackground="red", activeforeground=text, borderwidth=border, command=quitpy)
button1.grid(row=0, column=7)

button2=Button(buttonframe, text=" □ ", font=("arial", 13))
button2.config(width=3, height=0, fg = text, bg = dark, activebackground=light, activeforeground=text, borderwidth=border, command=fullscreen)
button2.grid(row=0, column=6)

button3=Button(buttonframe, text=" - ", font=("arial", 13))
button3.config(width=3, height=0, fg = text, bg = dark, activebackground=light, activeforeground=text, borderwidth=border, command=top.iconify)
button3.grid(row=0, column=5)

text=Label(root, text="Jebby's Jailbrəak", font=(font, 12 ,"bold"), fg = light, bg = dark)
text.place(x=10,y=2)





wrapper=LabelFrame(root)
wrapper['bg']='black'
wrapper.configure(borderwidth=0)

style = ttk.Style()
style.theme_use('clam')

style.configure("Vertical.TScrollbar", gripcount=0, background="#474747", darkcolor="#212121", lightcolor="#212121", troughcolor="#212121", bordercolor="#212121", arrowcolor="white")

mycanvas=Canvas(wrapper, width=int(width/1.9),height=200, bg="white")
mycanvas.pack(side=RIGHT, fill="both", expand="no")

yscrollbar=ttk.Scrollbar(wrapper, orient="vertical", command=mycanvas.yview)
yscrollbar.pack(side=RIGHT, fill="y")

mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas['bg']='black'
mycanvas.bind("<Configure>", lambda e: mycanvas.configure(scrollregion= mycanvas.bbox("all")))
mycanvas.configure(borderwidth=0, highlightthickness=0)

myframe=Frame(mycanvas)
myframe['bg']='black'
myframe.configure(borderwidth=0)
mycanvas.create_window((0,0), window=myframe, anchor="ne")

wrapper.pack(fill="both", expand="yes")



title1=Label(myframe, text="System Information:", font=("cambria 28 bold"), bg="black", fg="#474747")
title1.pack(padx=0,pady=10)

def fetchInfopressed():
    output2.delete("1.0", "end")
    
    output2.insert("1.0", f"\nPlatform processor:", "bold") 
    output2.insert("end", f"\n  {platform.processor()}\n", "normal")

    output2.insert("end", "\nSystem platform:", "bold")
    output2.insert("end", f"\n    {platform.system()}\n", "normal")

    output2.insert("end", "\nNode name (hostname):", "bold")
    output2.insert("end", f"\n    {platform.node()}\n", "normal")

    output2.insert("end", "\nSystem release:", "bold")
    output2.insert("end", f"\n    {platform.system()} {platform.release()}\n", "normal")

    output2.insert("end", "\nProcessor architecture:", "bold")
    output2.insert("end", f"\n    {platform.machine()}\n", "normal")

    output2.insert("end", "\nPlatform processor:", "bold")
    output2.insert("end", f"\n    {platform.platform()}\n", "normal")

    output2.insert("end", "\nPlatform architecture:", "bold") 
    output2.insert("end", f"\n    {platform.architecture()}", "normal")

fetchInfobutton=Button(myframe, text="Fetch Sys Info", font=("cambria 24"), bg="#212121", fg="white", activebackground="#474747", activeforeground="white", borderwidth=0, command=fetchInfopressed, width=20)
fetchInfobutton.pack(padx=int(width/100), pady=20)

def fetch_wifi_thread():
    def fetch_wifi():
        fetchWifibutton.config(state=tk.DISABLED)
        fetchInfobutton.config(state=tk.DISABLED)
        fetchExebutton.config(state=tk.DISABLED)
        jebbybutton.config(state=tk.DISABLED)
        fetchExebutton1.config(state=tk.DISABLED)
        fetchExebutton2.config(state=tk.DISABLED)
        fetchExebutton3.config(state=tk.DISABLED)
        lightbutton.config(state=tk.DISABLED)
        bluebutton.config(state=tk.DISABLED)
        darkbutton.config(state=tk.DISABLED)
        creditsbutton.config(state=tk.DISABLED)
        wallpaperbutton.config(state=tk.DISABLED)
        powershellbutton.config(state=tk.DISABLED)
        corianderbutton.config(state=tk.DISABLED)
        
        
        a = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="ignore").split('\n')
        a = [i.split(":")[1][1:-1] for i in a if "All User Profile" in i]
        output2.delete("1.0", "end")
        output2.insert(tk.END, f"\nUSERNAME    | PASSWORD\n \n", "bold")
        for i in a:
            try:
                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="ignore").split('\n')
                results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                try:
                    output2.insert(tk.END, "\n{:<15}| {:<}\n".format(i, results[0]))
                except IndexError:
                    output2.insert(tk.END, "\n{:<15}|  {:<}\n".format(i, ""))
            except subprocess.CalledProcessError:
                output2.insert(tk.END, "\n{:<15}|  {:<}\n".format(i, "ENCODING ERROR"))
        
        fetchWifibutton.config(state=tk.NORMAL)   
        fetchInfobutton.config(state=tk.NORMAL)
        fetchExebutton.config(state=tk.NORMAL)
        jebbybutton.config(state=tk.NORMAL)
        fetchExebutton1.config(state=tk.NORMAL)
        fetchExebutton2.config(state=tk.NORMAL)
        fetchExebutton3.config(state=tk.NORMAL)
        lightbutton.config(state=tk.NORMAL)
        bluebutton.config(state=tk.NORMAL)
        darkbutton.config(state=tk.NORMAL)
        creditsbutton.config(state=tk.NORMAL)
        wallpaperbutton.config(state=tk.NORMAL)
        powershellbutton.config(state=tk.NORMAL)
        corianderbutton.config(state=tk.NORMAL)
            
    thread = threading.Thread(target=fetch_wifi)
    thread.start()

fetchWifibutton=Button(myframe, text="Fetch Wifi Passwords *", font=("cambria 24"), bg="#212121", fg="white", activebackground="#474747", activeforeground="white", borderwidth=0, command=fetch_wifi_thread, width=20)
fetchWifibutton.pack()

warning=Label(myframe, text="* use at own risk", font=("arial 20"), bg="black", fg="#212121")
warning.pack()

def fetchExe():
    insertPath = entry.get()
    path = shutil.which(insertPath)

    if path is None:
        output2.delete("1.0", "end")
        output2.insert(tk.END, "\nERROR: No Path Found\n")
    else:
        output2.delete("1.0", "end")
        output2.insert(tk.END, f"\nPath to file: {path}\n" )


o=Label(myframe, text="", font=("arial 10"), bg="black", fg="#212121")
o.pack()

fetchExebutton=Button(myframe, text="Fetch EXE Path", font=("cambria 24"), bg="#212121", fg="white", activebackground="#474747", activeforeground="white", borderwidth=0, command=fetchExe, width=20)
fetchExebutton.pack()

button_border4 = tk.Frame(myframe, highlightbackground = "black", highlightthickness = 0, bd=2, bg="#212121")
button_border4.pack(padx=0,pady=10)

entry=Entry(button_border4, font=("arial 20"), bg="black", fg="white", borderwidth=0)
entry.pack()

def powershell():
    dst_path=str(abspath(getsourcefile(lambda:0)))
    name="northgate.pyw"
    dst_path=dst_path.replace(f"\{name}", "")
    entry2.delete(0, END)
    entry2.insert(tk.END, dst_path)
    
    src_path= str(shutil.which("powershell"))
    entry3.delete(0, END)
    entry3.insert(tk.END, src_path)

    src_path=entry3.get()
    dst_path=entry2.get()

    entry2.delete(0, END)
    entry3.delete(0, END)
    
    output2.delete("1.0", tk.END)
    banSymbol = []
    if any(symbol in dst_path for symbol in banSymbol):
        output2.insert(tk.END, "\nERROR: Something Went Wrong")

    elif any(symbol in src_path for symbol in banSymbol):
        output2.insert(tk.END, "\nERROR: Something Went Wrong")
        
    else:
        if not os.path.exists(dst_path) and not os.path.exists(src_path):
            output2.insert(tk.END, f"\nERROR: Something Went Wrong")
            return

        elif not os.path.exists(src_path):
            output2.insert(tk.END, f"\nERROR: Something Went Wrong")
            return
            
        elif not os.path.exists(dst_path):
            output2.insert(tk.END, f"\nERROR: Something Went Wrong")
            return

    try:
        finalDestpath = os.path.join(dst_path, os.path.basename(src_path)) #finalDestination/wee/poo/foo.abc

        shutil.copy(src_path, finalDestpath) #oldDestination/what/when/foo.abc => finalDestination/wee/poo/foo.abc
        IsolatedFile = os.path.basename(finalDestpath) #foo.abc

        JustfileEx = os.path.splitext(IsolatedFile)[1] #.abc

        NewFileName = "Chrome" + JustfileEx #Chrome.abc

        #os.rename(get the original untouched final destination, renamed to the full directory of the original untouched final destination joined with the brand new file[Chrome.abc])
        os.rename(finalDestpath, os.path.join(os.path.dirname(finalDestpath), NewFileName))

        os.startfile(f"{dst_path}\Chrome.EXE")
        output2.insert(tk.END, "\nPowershell Opened Sucessfully!")

    except FileExistsError:
        os.remove("powershell.exe")
        os.startfile(f"{dst_path}\Chrome.EXE")
        output2.insert(tk.END, "\nPowershell Opened Sucessfully!")

    except shutil.SameFileError:
        os.remove("powershell.exe")
        os.startfile(f"{dst_path}\Chrome.EXE")
        output2.insert(tk.END, "\nPowershell Opened Sucessfully!")
        
    

powershellbutton=Button(myframe, text="Open Powershell", font=("cambria 24"), bg="#212121", fg="white", activebackground="#474747", activeforeground="white", borderwidth=0, command=powershell, width=20)
powershellbutton.pack(padx=int(width/100), pady=20)

title2=Label(myframe, text="", font=("cambria 48 bold"), bg="black", fg="white")
title2.pack(padx=0,pady=10)

title3=Label(myframe, text="Jebby's Script:", font=("cambria 28 bold"), bg="black", fg="#474747")
title3.pack()

def jebButtonpressed():
    src_path=entry2.get()
    dst_path=entry3.get()
    output2.delete("1.0", "end")
    banSymbol = []
    if any(symbol in dst_path for symbol in banSymbol):
        output2.insert(tk.END, "\nERROR: Forbidden Symbols Used")

    elif any(symbol in src_path for symbol in banSymbol):
        output2.insert(tk.END, "\nERROR: Forbidden Symbols Used")
        
    else:
        if not os.path.exists(dst_path) and not os.path.exists(src_path):
            output2.insert(tk.END, f"\nError: Source File Path not found at '{src_path}'\n \nError: Destination Path not found at '{dst_path}'")
            return

        elif not os.path.exists(src_path):
            output2.insert(tk.END, f"\nError: Source File Path not found at '{src_path}'")
            return
            
        elif not os.path.exists(dst_path):
            output2.insert(tk.END, f"\nError: Destination Path not found at '{dst_path}'")
            return

        finalDestpath = os.path.join(dst_path, os.path.basename(src_path)) #finalDestination/wee/poo/foo.abc

        shutil.copy(src_path, finalDestpath) #oldDestination/what/when/foo.abc => finalDestination/wee/poo/foo.abc
        IsolatedFile = os.path.basename(finalDestpath) #foo.abc

        JustfileEx = os.path.splitext(IsolatedFile)[1] #.abc

        NewFileName = "Chrome" + JustfileEx #Chrome.abc

        #os.rename(get the original untouched final destination, renamed to the full directory of the original untouched final destination joined with the brand new file[Chrome.abc])
        os.rename(finalDestpath, os.path.join(os.path.dirname(finalDestpath), NewFileName))

        output2.insert(tk.END, "\nJailbroken Successfully!\n\nCheck output folder")

def choosefile():
    entry2.delete(0, END)

    file = str(filedialog.askopenfilenames())

    file = file.replace(",", "")
    file = file.replace("')", "")
    file = file.replace("('", "")

    entry2.insert(tk.END, file)
    
    
def choosefile2():
    entry3.delete(0, END)
    
    destination = str(filedialog.askdirectory())

    destination = destination.replace(",", "")
    destination = destination.replace("')", "")
    destination = destination.replace("('", "")

    entry3.insert(tk.END, destination)


jebbybutton=Button(myframe, text="Jailbrəak!", font=("cambria 24"), bg="#212121", fg="white", activebackground="#474747", activeforeground="white", borderwidth=0, command=jebButtonpressed, width=20)
jebbybutton.pack(padx=int(width/100), pady=20)


button_border3 = tk.Frame(myframe, highlightbackground = "black", highlightthickness = 0, bd=2, bg="#212121")
button_border3.pack(padx=0,pady=10)

entry2=Entry(button_border3, font=("arial 20"), bg="black", fg="white", borderwidth=0)
entry2.pack()

fetchExebutton1=Button(myframe, text="Choose File", font=("arial 15"), bg="#212121", fg="white", activebackground="#474747", activeforeground="white", borderwidth=0, command=choosefile, width=16)
fetchExebutton1.pack()


title4=Label(myframe, text="", font=("cambria 1 bold"), bg="black", fg="white")
title4.pack(padx=0,pady=10)


button_border2 = tk.Frame(myframe, highlightbackground = "black", highlightthickness = 0, bd=2, bg="#212121")
button_border2.pack(padx=0,pady=10)

entry3=Entry(button_border2, font=("arial 20"), bg="black", fg="white", borderwidth=0)
entry3.pack()

fetchExebutton2=Button(myframe, text="Choose Destination", font=("arial 15"), bg="#212121", fg="white", activebackground="#474747", activeforeground="white", borderwidth=0, command=choosefile2, width=16)
fetchExebutton2.pack()

title5=Label(myframe, text="", font=("cambria 48 bold"), bg="black", fg="white")
title5.pack(padx=0,pady=10)




title=Label(myframe, text="Cosmetic Features:", font=("cambria 28 bold"), bg="black", fg="#474747")
title.pack(padx=0,pady=10)

def wallpaper():
        pathExtension = os.path.splitext(os.path.basename(entry4.get()))[1]
        extensionRequirementsNotMet = (
            pathExtension != ".PNG" and pathExtension != ".tif" and pathExtension != ".jpg" and pathExtension != ".jpeg" 
            and pathExtension != ".bmp" and pathExtension != ".gif" and pathExtension != ".tiff" )
        
        if extensionRequirementsNotMet and not os.path.exists(entry4.get()):
            output2.delete(1.0, tk.END) #"Error: Extension is NOT a Supported Format" - Show
            output2.insert(tk.END, "\nError: Extension is NOT a Supported Format\n")

        elif extensionRequirementsNotMet:
            output2.delete(1.0, tk.END) #"Error: Extension is NOT a Supported Format" - Show
            output2.insert(tk.END, "\nError: Extension is NOT a Supported Format\n")

        elif not os.path.exists(entry4.get()):
            output2.delete(1.0, tk.END) #"Error: Extension is NOT a Supported Format" - Show
            output2.insert(tk.END, "\nError: Extension is NOT a Supported Format\n")

        else:            
            WALLPAPER_PATH = entry4.get()
            ctypes.windll.user32.SystemParametersInfoW(20, 0, WALLPAPER_PATH, 3)

            output2.delete(1.0, tk.END) #"Error: Extension is NOT a Supported Format" - Show
            output2.insert(tk.END, "\nWallpaper Successfully changed\n")

wallpaperbutton=Button(myframe, text="Change Wallpaper", font=("cambria 24"), bg="#212121", fg="white", activebackground="#474747", activeforeground="white", borderwidth=0, command=wallpaper, width=20)
wallpaperbutton.pack(padx=int(width/100), pady=20)

button_border = tk.Frame(myframe, highlightbackground = "black", highlightthickness = 0, bd=2, bg="#212121")
button_border.pack(padx=0,pady=10)

def wallpaperfile():
    entry4.delete(0, END)

    file = str(filedialog.askopenfilenames())

    file = file.replace(",", "")
    file = file.replace("'", "")
    file = file.replace(")", "")
    file = file.replace("(", "")

    entry4.insert(tk.END, file)

entry4=Entry(button_border, font=("arial 20"), bg="black", fg="white", borderwidth=0)
entry4.pack()

fetchExebutton3=Button(myframe, text="Choose Image", font=("arial 15"), bg="#212121", fg="white", activebackground="#474747", activeforeground="white", borderwidth=0, command=wallpaperfile, width=16)
fetchExebutton3.pack()

title6=Label(myframe, text="", font=("cambria 12 bold"), bg="black", fg="white")
title6.pack()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

mycanva=Canvas(wrapper, width=int(width/2.3),height=200, bg="black")
mycanva.pack(side=RIGHT, fill="both", expand="no")

yscrollbar2=ttk.Scrollbar(wrapper, orient="vertical", command=mycanva.yview)
yscrollbar2.pack(side=RIGHT, fill="y")

mycanva.configure(yscrollcommand=yscrollbar2.set)
mycanva['bg']='black'
mycanva.bind("<Configure>", lambda e: mycanva.configure(scrollregion= mycanva.bbox("all")))

if root.winfo_screenheight()==1080:
    mycanva.configure(borderwidth=-3, highlightthickness=0)

else:
    mycanva.configure(borderwidth=0, highlightthickness=0)

myframe2=Frame(mycanva)
myframe2['bg']='black'
myframe2.configure(borderwidth=0)
mycanva.create_window((0,0), window=myframe2, anchor="ne")

wrapper.pack(fill="both", expand="yes")

output2=Text(myframe2, height = 1000, width = int(width/20.5), borderwidth=0, fg = "white", bg = "black", font='arial 13', highlightthickness=0, wrap='word')
output2.pack()



def dark():
    f= open('theme.txt', "r+")
    f.truncate(0)
    f.write("dark")
    f.close()
    
    title8.config(bg="black", fg="white")
    creditsbutton.config(font=("cambria 24"), bg="#212121", fg="white", activebackground="#474747", activeforeground="white", borderwidth=0)
    title7.config(bg="black", fg="white")
    output2.config(borderwidth=0, fg = "white", bg = "black", font='arial 13')
    myframe2['bg']='black'
    myframe['bg']='black'
    wrapper['bg']='black'
    root['bg']='black'
    mycanva['bg']='black'
    mycanvas['bg']='black'
    text.config(fg="#474747", bg="#212121")
    style.configure("Vertical.TScrollbar", gripcount=0, background="#474747", darkcolor="#212121", lightcolor="#212121", troughcolor="#212121", bordercolor="#212121", arrowcolor="white")
    buttonframe.config(bg = "#212121")
    button1.config(fg = "white", bg = "#212121", activebackground="red", activeforeground="white", borderwidth=0)
    button2.config(fg = "white", bg = "#212121", activebackground="#474747", activeforeground="white", borderwidth=0)
    button3.config(fg = "white", bg = "#212121", activebackground="#474747", activeforeground="white", borderwidth=0)
    title6.config(bg="black", fg="white")
    title5.config(bg="black", fg="#474747")
    title4.config(bg="black", fg="#474747")
    title3.config(bg="black", fg="#474747", font=("cambria 28 bold"))
    title2.config(bg="black", fg="#474747")
    title.config(bg="black", fg="#474747", font=("cambria 28 bold"))
    title1.config(bg="black", fg="#474747", font=("cambria 28 bold"))
    o.config(bg="black", fg="#474747")
    warning.config(bg="black", fg="#474747")
    fetchExebutton3.config(font=("arial 15"), bg="#212121", fg="white", activebackground="#474747", activeforeground="white", borderwidth=0)
    fetchExebutton2.config(font=("arial 15"), bg="#212121", fg="white", activebackground="#474747", activeforeground="white", borderwidth=0)
    fetchExebutton1.config(font=("arial 15"), bg="#212121", fg="white", activebackground="#474747", activeforeground="white", borderwidth=0)
    entry.config(font=("arial 20"), bg="black", fg="white", borderwidth=0)
    entry2.config(font=("arial 20"), bg="black", fg="white", borderwidth=0)
    entry3.config(font=("arial 20"), bg="black", fg="white", borderwidth=0)
    entry4.config(font=("arial 20"), bg="black", fg="white", borderwidth=0)
    button_border.config(highlightbackground = "black", highlightthickness = 0, bd=2, bg="#212121")
    button_border2.config(highlightbackground = "black", highlightthickness = 0, bd=2, bg="#212121")
    button_border3.config(highlightbackground = "black", highlightthickness = 0, bd=2, bg="#212121")
    button_border4.config(highlightbackground = "black", highlightthickness = 0, bd=2, bg="#212121")
    fetchWifibutton.config(font=("cambria 24"), bg="#212121", fg="white", activebackground="#474747", activeforeground="white", borderwidth=0)   
    fetchInfobutton.config(font=("cambria 24"), bg="#212121", fg="white", activebackground="#474747", activeforeground="white", borderwidth=0)
    fetchExebutton.config(font=("cambria 24"), bg="#212121", fg="white", activebackground="#474747", activeforeground="white", borderwidth=0)
    corianderbutton.config(font=("cambria 24"), bg="#212121", fg="white", activebackground="#474747", activeforeground="white", borderwidth=0)
    jebbybutton.config(font=("cambria 24"), bg="#212121", fg="white", activebackground="#474747", activeforeground="white", borderwidth=0)
    wallpaperbutton.config(font=("cambria 24"), bg="#212121", fg="white", activebackground="#474747", activeforeground="white", borderwidth=0)
    wrapper.config(borderwidth=0)
    root.config(borderwidth=0)
    lightbutton.config(bg="white", activebackground="gainsboro")
    darkbutton.config(bg="#212121", activebackground="#474747")
    powershellbutton.config(font=("cambria 24"), bg="#212121", fg="white", activebackground="#474747", activeforeground="white", borderwidth=0)
    canvasMain.pack_forget()




darkbutton=Button(myframe, text="Dark Theme", font=("cambria 24"), bg="#212121", fg="white", activebackground="#474747", activeforeground="white", borderwidth=0, command=dark, width=20)
darkbutton.pack(padx=int(width/100), pady=20)

def light():
    f= open('theme.txt', "r+") 
    f.truncate(0)
    f.write("light")
    f.close()
    
    title8.config(bg="white", fg="#999999")
    creditsbutton.config(font=("cambria 24"), bg="gainsboro", fg="black", activebackground="white", activeforeground="black", borderwidth=0)
    title7.config(bg="white", fg="#999999")
    output2.config(borderwidth=0, fg = "black", bg = "white", font='arial 13')
    myframe2['bg']='white'
    myframe['bg']='white'
    wrapper['bg']='white'
    root['bg']='white'
    mycanva['bg']='white'
    mycanvas['bg']='white'
    wrapper.config(borderwidth=1)
    style.configure("Vertical.TScrollbar", gripcount=0, background="white", darkcolor="gainsboro", lightcolor="gainsboro", troughcolor="gainsboro", bordercolor="gainsboro", arrowcolor="black")
    buttonframe.config(bg = "white")
    text.config(fg="#999999", bg="white")
    button1.config(fg = "black", bg = "white", activebackground="red", activeforeground="white", borderwidth=0)
    button2.config(fg = "black", bg = "white", activebackground="gainsboro", activeforeground="white", borderwidth=0)
    button3.config(fg = "black", bg = "white", activebackground="gainsboro", activeforeground="white", borderwidth=0)
    title6.config(bg="white", fg="black")
    root.config(borderwidth=1)
    title5.config(bg="white", fg="#707070")
    title4.config(bg="white", fg="#707070")
    title3.config(bg="white", fg="#707070", font=("cambria 28 bold"))
    title2.config(bg="white", fg="#707070")
    title.config(bg="white", fg="#707070", font=("cambria 28 bold"))
    title1.config(bg="white", fg="#707070", font=("cambria 28 bold"))
    o.config(bg="white", fg="gainsboro")
    warning.config(bg="white", fg="gainsboro")
    fetchExebutton3.config(font=("arial 15"), bg="gainsboro", fg="black", activebackground="white", activeforeground="black", borderwidth=0)
    fetchExebutton2.config(font=("arial 15"), bg="gainsboro", fg="black", activebackground="white", activeforeground="black", borderwidth=0)
    fetchExebutton1.config(font=("arial 15"), bg="gainsboro", fg="black", activebackground="white", activeforeground="black", borderwidth=0)
    entry.config(font=("arial 20"), bg="white", fg="black", borderwidth=0)
    entry2.config(font=("arial 20"), bg="white", fg="black", borderwidth=0)
    entry3.config(font=("arial 20"), bg="white", fg="black", borderwidth=0)
    entry4.config(font=("arial 20"), bg="white", fg="black", borderwidth=0)
    button_border.config(highlightbackground = "black", highlightthickness = 0, bd=2, bg="#707070")
    button_border2.config(highlightbackground = "black", highlightthickness = 0, bd=2, bg="#707070")
    button_border3.config(highlightbackground = "black", highlightthickness = 0, bd=2, bg="#707070")
    button_border4.config(highlightbackground = "black", highlightthickness = 0, bd=2, bg="#707070")
    fetchWifibutton.config(font=("cambria 24"), bg="gainsboro", fg="black", activebackground="white", activeforeground="black", borderwidth=0)   
    fetchInfobutton.config(font=("cambria 24"), bg="gainsboro", fg="black", activebackground="white", activeforeground="black", borderwidth=0)
    fetchExebutton.config(font=("cambria 24"), bg="gainsboro", fg="black", activebackground="white", activeforeground="black", borderwidth=0)
    corianderbutton.config(font=("cambria 24"), bg="gainsboro", fg="black", activebackground="white", activeforeground="black", borderwidth=0)
    jebbybutton.config(font=("cambria 24"), bg="gainsboro", fg="black", activebackground="white", activeforeground="black", borderwidth=0)
    wallpaperbutton.config(font=("cambria 24"), bg="gainsboro", fg="black", activebackground="white", activeforeground="black", borderwidth=0)
    canvasMain.pack_forget()
    powershellbutton.config(font=("cambria 24"), bg="gainsboro", fg="black", activebackground="white", activeforeground="black", borderwidth=0)
    lightbutton.config(bg="gainsboro", activebackground="white")
    darkbutton.config(bg="#212121", activebackground="#474747")

lightbutton=Button(myframe, text="Light Theme", font=("cambria 24"), bg="white", fg="black", activebackground="gainsboro", activeforeground="black", borderwidth=0, command=light, width=20)
lightbutton.pack(padx=int(width/100), pady=0)

def blue():
    f= open('theme.txt', "r+")
    f.truncate(0)
    f.write("blue")
    f.close()

    title8.pack_forget()
    creditsbutton.pack_forget()
    title7.pack_forget()
    title6.pack_forget()
    title5.pack_forget()
    title4.pack_forget()
    title3.pack_forget()
    corianderbutton.pack_forget()
    title2.pack_forget()
    title.pack_forget()
    title1.pack_forget()
    o.pack_forget()
    warning.pack_forget()
    fetchExebutton3.pack_forget()
    fetchExebutton2.pack_forget()
    fetchExebutton1.pack_forget()
    entry.pack_forget()
    entry2.pack_forget()
    entry3.pack_forget()
    entry4.pack_forget()
    button_border.pack_forget()
    button_border2.pack_forget()
    button_border3.pack_forget()
    button_border4.pack_forget()
    fetchWifibutton.pack_forget()
    fetchInfobutton.pack_forget()
    fetchExebutton.pack_forget()
    powershellbutton.pack_forget()
    jebbybutton.pack_forget()
    wallpaperbutton.pack_forget()
    lightbutton.pack_forget()
    bluebutton.pack_forget()
    darkbutton.pack_forget()
    canvasMain.pack(fill=tk.BOTH, expand=True)    
    title1.pack(padx=0,pady=10)
    fetchInfobutton.pack(padx=int(width/100), pady=20)
    fetchWifibutton.pack()
    warning.pack()
    o.pack()
    fetchExebutton.pack()
    button_border4.pack(padx=0,pady=10)
    entry.pack()
    powershellbutton.pack(padx=int(width/100), pady=20)
    title2.pack(padx=0,pady=10)
    title3.pack()
    jebbybutton.pack(padx=int(width/100), pady=20)
    button_border3.pack(padx=0,pady=10)
    entry2.pack()
    fetchExebutton1.pack()
    title4.pack(padx=0,pady=10)
    button_border2.pack(padx=0,pady=10)
    entry3.pack()
    fetchExebutton2.pack()
    title5.pack(padx=0,pady=10)
    title.pack(padx=0,pady=10)
    wallpaperbutton.pack(padx=int(width/100), pady=20)
    button_border.pack(padx=0,pady=10)
    entry4.pack()
    fetchExebutton3.pack()
    title6.pack()
    darkbutton.pack(padx=int(width/100), pady=20)
    lightbutton.pack(padx=int(width/100), pady=0)
    bluebutton.pack(padx=int(width/100), pady=20)
    corianderbutton.pack(padx=0, pady=50)
    title7.pack(padx=0,pady=200)
    creditsbutton.pack(padx=int(width/100), pady=40)
    title8.pack()

    
    title8.config(bg="#222027", fg="white")
    creditsbutton.config(font=("arial 23"), bg="RoyalBlue4", fg="white", activebackground="white", activeforeground="black", borderwidth=2)
    title7.config(bg="#222027", fg="white")
    output2.config(borderwidth=0, fg = "white", bg = "#222027", font='arial 13')
    myframe2['bg']='#222027'
    myframe['bg']='#222027'
    wrapper['bg']='#222027'
    root['bg']='#222027'
    mycanva['bg']='#222027'
    mycanvas['bg']='#222027'
    text.config(fg="RoyalBlue1", bg= "RoyalBlue4")
    style.configure("Vertical.TScrollbar", gripcount=0, background="RoyalBlue1", darkcolor="RoyalBlue4", lightcolor="RoyalBlue4", troughcolor="RoyalBlue4", bordercolor="RoyalBlue4", arrowcolor="white")
    buttonframe.config(bg = "RoyalBlue4")
    button1.config(fg = "white", bg = "RoyalBlue4", activebackground="red", activeforeground="white", borderwidth=0)
    button2.config(fg = "white", bg = "RoyalBlue4", activebackground="white", activeforeground="black", borderwidth=0)
    button3.config(fg = "white", bg = "RoyalBlue4", activebackground="white", activeforeground="black", borderwidth=0)
    title6.config(bg="#222027", fg="white")
    title5.config(bg="#222027", fg="RoyalBlue4")
    title4.config(bg="#222027", fg="RoyalBlue4")
    title3.config(bg="#222027", fg="RoyalBlue4", font=("arial 27 bold"))
    title2.config(bg="#222027", fg="RoyalBlue4")
    title.config(bg="#222027", fg="RoyalBlue4", font=("arial 27 bold"))
    title1.config(bg="#222027", fg="RoyalBlue4", font=("arial 27 bold"))
    o.config(bg="#222027", fg="RoyalBlue4")
    warning.config(bg="#222027", fg="RoyalBlue4")
    fetchExebutton3.config(font=("arial 15"), bg="RoyalBlue4", fg="white", activebackground="white", activeforeground="black", borderwidth=2)
    fetchExebutton2.config(font=("arial 15"), bg="RoyalBlue4", fg="white", activebackground="white", activeforeground="black", borderwidth=2)
    fetchExebutton1.config(font=("arial 15"), bg="RoyalBlue4", fg="white", activebackground="white", activeforeground="black", borderwidth=2)
    entry.config(font=("arial 20"), bg="black", fg="white", borderwidth=2)
    entry2.config(font=("arial 20"), bg="black", fg="white", borderwidth=2)
    entry3.config(font=("arial 20"), bg="black", fg="white", borderwidth=2)
    entry4.config(font=("arial 20"), bg="black", fg="white", borderwidth=2)
    button_border.config(highlightbackground = "black", highlightthickness = 0, bd=0, bg="#212121")
    button_border2.config(highlightbackground = "black", highlightthickness = 0, bd=0, bg="#212121")
    button_border3.config(highlightbackground = "black", highlightthickness = 0, bd=0, bg="#212121")
    button_border4.config(highlightbackground = "black", highlightthickness = 0, bd=0, bg="#212121")
    fetchWifibutton.config(font=("arial 23"), bg="RoyalBlue4", fg="white", activebackground="white", activeforeground="black", borderwidth=2)
    fetchInfobutton.config(font=("arial 23"), bg="RoyalBlue4", fg="white", activebackground="white", activeforeground="black", borderwidth=2)
    fetchExebutton.config(font=("arial 23"), bg="RoyalBlue4", fg="white", activebackground="white", activeforeground="black", borderwidth=2)
    jebbybutton.config(font=("arial 23"), bg="RoyalBlue4", fg="white", activebackground="white", activeforeground="black", borderwidth=2)
    corianderbutton.config(font=("arial 23"), bg="RoyalBlue4", fg="white", activebackground="white", activeforeground="black", borderwidth=2)
    wallpaperbutton.config(font=("arial 23"), bg="RoyalBlue4", fg="white", activebackground="white", activeforeground="black", borderwidth=2)
    wrapper.config(borderwidth=0)
    root.config(borderwidth=0)
    lightbutton.config(bg="white", activebackground="gainsboro")
    darkbutton.config(bg="black", activebackground="#212121")
    powershellbutton.config(font=("arial 23"), bg="RoyalBlue4", fg="white", activebackground="white", activeforeground="black", borderwidth=2)  

    

bluebutton=Button(myframe, text="Original Theme", font=("arial 23"), bg="RoyalBlue4", fg="white", activebackground="white", activeforeground="black", borderwidth=2, command=blue, width=20)
bluebutton.pack(padx=int(width/100), pady=20)

def pet():
    class Win(tk.Tk):
        def __init__(self):
            super().__init__()
            ranx =random.randint(0, root.winfo_screenwidth())
            rany =random.randint(0, root.winfo_screenheight())
            super().geometry(f"128x128+{ranx}+{rany}")
            super().attributes('-topmost', True)
            super().overrideredirect(True)
            self._offsetx = 0
            self._offsety = 0
            super().bind("<Button-1>" ,self.clickwin)
            super().bind("<B1-Motion>", self.dragwin)

        def dragwin(self,event):
            x = super().winfo_pointerx() - self._offsetx
            y = super().winfo_pointery() - self._offsety
            super().geometry(f"+{x}+{y}")

        def clickwin(self,event):
            self._offsetx = super().winfo_pointerx() - super().winfo_rootx()
            self._offsety = super().winfo_pointery() - super().winfo_rooty()
            
    window = Win()

    petskin=["skin1.png", "skin2.png", "skin1.png"]

    bg = PhotoImage(master = window, file= random.choice(petskin))
    frame = Label(window, image=bg)
    window.overrideredirect(True)
    frame.pack(fill=tk.BOTH, expand=True)
    
    window.mainloop()
    
corianderbutton=Button(myframe, text="Coriander Pet", font=("cambria 24"), bg="#212121", fg="white", activebackground="#474747", activeforeground="white", borderwidth=0, command=pet, width=20)
corianderbutton.pack(padx=0, pady=50)

title7=Label(myframe, text="", font=("cambria 48 bold"), bg="black", fg="white")
title7.pack()

def showcredits(): 
    output2.delete(1.0, tk.END)
    filler = "\n*******************************\n"
    creditText = f'''\n    Creator:  Jebby (obvs) \n    Contributers:  PengeSal 
    {filler} Python Modules:\n     -Tkinter\n     -Platform\n     -Subprocess\n     -Shutil\n     -Threading\n     -OS\n     -Sys\n     -Ctypes\n     -Sys\n
    {filler} Tools:\n     -Python\n     -Visual Studio Code\n     -Github
    {filler} Icons:\n      -[Icon.ico] => imgbin\n   -[IconAlt.ico] => pngitem
    {filler}
    '''
    output2.insert(tk.END, creditText)

creditsbutton=Button(myframe, text="Credits", font=("cambria 24"), bg="#212121", fg="white", activebackground="#474747", activeforeground="white", borderwidth=0, command=showcredits, width=20)
creditsbutton.pack(padx=int(width/100), pady=40)

title8=Label(myframe, text="", font=("cambria 48 bold"), bg="black", fg="white")
title8.pack()


canvasMain = Canvas(myframe, bg=background, highlightthickness=0)
canvasMain.pack(fill=tk.BOTH, expand=True)

canvasMain.create_arc(40,500,363,150, start=0, extent=180, fill="RoyalBlue4", outline="")

canvasMain.create_oval(100,215,125,230, fill="RoyalBlue1", outline="") 
canvasMain.create_oval(200,215,225,230, fill="RoyalBlue1", outline="") 

canvasMain.create_line(225,180,275,90, fill="RoyalBlue1", width=7) 
canvasMain.create_line(125,180,50,100, fill="RoyalBlue1", width=7)

canvasMain["bg"]="#222027"

canvasMain.pack_forget()


with open('theme.txt', "r") as f:
    lines = str(f.readlines())
    if lines=="['dark']":
        dark()
    elif lines=="['light']":
        light()
    elif lines=="['blue']":
        blue()
    else:
        dark()

root.mainloop()
