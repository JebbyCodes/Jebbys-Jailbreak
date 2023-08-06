## 22/7/23 V8 - Experimental/Stable    [https://github.com/JebbyCodes/Jebbys-Jailbreak]
import platform #sysinfo
import subprocess #wifi
import shutil #filefinder
from tkinter import *
import tkinter as tk
import platform
import threading
import os #jebbyscript
import sys #private file ref
import ctypes #wallpaper


#configs
font = "Cambria"
background = '#222027'
icon = os.path.join(sys.path[0], "Icon.ico")
iconAlt = os.path.join(sys.path[0], "IconAlt.ico")
#notes
#sys.path[0] = parent dir
#you may choose to not use the icons

window = Tk()
window.title("Jebby's Jailbreak")
window.iconbitmap(iconAlt)

#############################################################################################################
def clearMainhomeScreen():
    fetchWifibutton.forget()
    fetchInfobutton.forget()
    fetchExebutton.forget()
    jebbyScriptbutton.forget()
    canvasMain.pack_forget()
    canvasMain.forget()
    nextPagelabel.place_forget()
    forwardPagebutton.place_forget()
    backPagebutton.place_forget()
    
#############################################################################################################
def center_window(window, width, height):
    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the x and y coordinates for the window to be centered
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Set the window geometry to center it on the screen
    window.geometry(f"{width}x{height}+{x}+{y}")

window_width = 275
window_height = 325
center_window(window, window_width, window_height)
window.resizable(False, False)

window_frame = tk.Frame(window)
window_frame.pack(fill=tk.BOTH, expand=True)

def forget_all_widgets(window_frame):
    for widget in window_frame.winfo_children():
        widget.pack_forget()

#############################################################################################################
def fetchInfopressed():
    clearMainhomeScreen()

    homeButton.place(x=0, y=300)
    homeButton.config(command=homePressed)
   
    window_frame.pack_propagate(False)

    # Platform Processor
    platformprocessor = Label(window_frame, text=f"\nPlatform processor:\n {platform.processor()}", wraplength=200)
    platformprocessor.configure(font=(font, 8), bg=background, fg="white")
    platformprocessor.pack()

    #  System platform
    systemplatform = Label(window_frame, text=f"\nSystem platform:\n {platform.system()}", wraplength=200)
    systemplatform.configure(font=(font, 8), bg=background, fg="white")
    systemplatform.pack()

    # Node name (hostname)
    nodename = Label(window_frame, text=f"\nNode name (hostname):\n {platform.node()}", wraplength=200)
    nodename.configure(font=(font, 8), bg=background, fg="white")
    nodename.pack()

    # Release version
    releasever = Label(window_frame, text=f"\nSystem release:\n {platform.release()}", wraplength=200)
    releasever.configure(font=(font, 8), bg=background, fg="white")
    releasever.pack()

    # Processor architecture
    processorarc = Label(window_frame, text=f"\nProcessor architecture:\n {platform.machine()}", wraplength=200)
    processorarc.configure(font=(font, 8), bg=background, fg="white")
    processorarc.pack()

    # System OS
    sysos = Label(window_frame, text=f"\nPlatform processor:\n {platform.platform()}", wraplength=200)
    sysos.configure(font=(font, 8), bg=background, fg="white")
    sysos.pack()

    # Platform architecture
    platformarc = Label(window_frame,text=f"\nPlatform architecture:\n {platform.architecture()}", wraplength=200)
    platformarc.configure(font=(font, 8), bg=background, fg="white")
    platformarc.pack()
    

####################################################################################################################################
def fetch_wifi_thread():
    def fetch_wifi():
        homeButton.place(x=0, y=300)
        homeButton.config(command=homePressed)

        fetchWifibutton.config(state=tk.DISABLED)
        fetchInfobutton.config(state=tk.DISABLED)
        fetchExebutton.config(state=tk.DISABLED)
        jebbyScriptbutton.config(state=tk.DISABLED)
        nextPagelabel.config(state=tk.DISABLED)
        forwardPagebutton.config(state=tk.DISABLED)
        backPagebutton.config(state=tk.DISABLED)
        clearMainhomeScreen()

        

        wifiResultsframe = tk.Frame(window_frame, bg="RoyalBlue4")
        wifiResultsframe.pack(side=tk.BOTTOM,fill=tk.BOTH, expand=True)
        wifiResultsframe.pack_propagate(False)

        wifiUserindicateLabel = Label(window_frame, text="USERNAME:")
        wifiUserindicateLabel.config(bg=background, fg="white")
        wifiUserindicateLabel.pack(side=tk.LEFT, padx=5, pady=5)

        wifiPassindicateLabel = Label(window_frame, text="PASSWORD:")
        wifiPassindicateLabel.config(bg=background, fg="white")
        wifiPassindicateLabel.pack(side=tk.RIGHT, padx=5, pady=5)

        a = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="ignore").split('\n')
        a = [i.split(":")[1][1:-1] for i in a if "All User Profile" in i]
        for i in a:
            try:
                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="ignore").split('\n')
                results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                try:
                    WifiUsertext = tk.Text(wifiResultsframe, wrap=tk.WORD, height=1, width=30)
                    WifiUsertext.insert(tk.END, "{:<15}| {:<}".format(i, results[0]))
                    WifiUsertext.pack(pady=7)
                    WifiUsertext.config(state=tk.DISABLED, highlightthickness=0, bg=background, fg="white")
                except IndexError:
                    WifiUsertext = tk.Text(wifiResultsframe, wrap=tk.WORD, height=1, width=30)
                    WifiUsertext.insert(tk.END, "{:<15}|  {:<}".format(i, ""))
                    WifiUsertext.pack(pady=7)
                    WifiUsertext.config(state=tk.DISABLED, highlightthickness=0, bg=background, fg="white")
            except subprocess.CalledProcessError:
                WifiUsertext = tk.Text(wifiResultsframe, wrap=tk.WORD, height=1, width=30)
                WifiUsertext.insert(tk.END, "{:<15}|  {:<}".format(i, "ENCODING ERROR"))
                WifiUsertext.pack(pady=7)
                WifiUsertext.config(state=tk.DISABLED, highlightthickness=0, bg=background, fg="white")
        
        fetchWifibutton.config(state=tk.NORMAL)  # Enable the button after fetching
        fetchInfobutton.config(state=tk.NORMAL)
        fetchExebutton.config(state=tk.NORMAL)
        jebbyScriptbutton.config(state=tk.NORMAL)
        nextPagelabel.config(state=tk.NORMAL)
        forwardPagebutton.config(state=tk.NORMAL)
        backPagebutton.config(state=tk.NORMAL)

    thread = threading.Thread(target=fetch_wifi)
    thread.start()


####################################################################################################################################
def fetchExe():
    homeButton.place(x=0, y=300)
    homeButton.config(command=homePressed)

    clearMainhomeScreen()

    invisiLabel = Label(window_frame, text="")
    invisiLabel.pack(pady=15)
    invisiLabel.config(bg=background)

    exeEntry = Entry(window_frame)
    exeEntry.pack(side=tk.TOP, padx=30, fill=tk.X)


    def getExeentry():
    
        insertPath = exeEntry.get()
        path = shutil.which(insertPath) 

        if path is None:
            GotExePath.forget()
            NoExePath.config(text="Error: No Path Found", bg='white')
        else:
            GotExePath.config(state=tk.NORMAL, highlightthickness=0)
            GotExePath.delete("1.0", tk.END)
            GotExePath.insert(tk.END, f"Path to file: {path}")
            GotExePath.config(state=tk.DISABLED, highlightthickness=0)
            GotExePath.pack()
            NoExePath.config(text="", bg=background)

    subExebutton = Button(window_frame, text="Fetch Path", command=getExeentry)
    subExebutton.config(fg = "white", bg = "RoyalBlue4")
    subExebutton.pack()

    NoExePath = Label(window_frame, text="", wraplength=200)
    NoExePath.config(bg=background)
    NoExePath.pack()
    GotExePath = tk.Text(window_frame, wrap=tk.WORD, height=3, width=20)
    GotExePath.insert(tk.END, "")
    GotExePath.config(state=tk.DISABLED, highlightthickness=0)


####################################################################################################################################
def jebbyScriptpressed():
    homeButton.place(x=0, y=300)
    homeButton.config(command=homePressed)
    clearMainhomeScreen()

    invisiLabel = Label(window_frame, text="")
    invisiLabel.pack(pady=15)
    invisiLabel.config(bg=background)
    pathEntry = Entry(window_frame, width=30)
    pathEntry.pack(ipady=6)

    banSymbol = ['"', '|', '?', '/', '<', '>', '*']

    def jebButtonpressed():
        if any(symbol in pathEntry.get() for symbol in banSymbol):
            errorLabel = Label(window_frame,text="ERROR: Forbidden Symbols Used")
            errorLabel.pack()
        else:
            pathEntry.forget()
            jebbyButton.forget()
            seldesLabel = Label(window_frame,text="Select destination:")
            seldesLabel.pack()
            destEntry = Entry(window_frame, width = 15)
            destEntry.pack()

            def destGopressed():
                src_path = rf'{pathEntry.get()}'
                dst_path = rf'{destEntry.get()}'

                if not os.path.exists(dst_path) and not os.path.exists(src_path):
                    errorLabelBoth = Label(window_frame, text=f"Error: Source File Path not found at '{src_path}'\n \nError: Destination Path not found at '{dst_path}'", wraplength=200)
                    errorLabelBoth.pack() 
                    return

                elif not os.path.exists(src_path):
                    errorLabelSrc = Label(window_frame, text=f"Error: Source File Path not found at {src_path}")
                    errorLabelSrc.pack() 
                    return
                    
                elif not os.path.exists(dst_path):
                    errorLabelDst = Label(window_frame, text=f"Error: Destination Path not found at {dst_path}")
                    errorLabelDst.pack()
                    return
                    
                
                
                finalDestpath = os.path.join(dst_path, os.path.basename(src_path)) #finalDestination/wee/poo/foo.abc

                shutil.copy(src_path, finalDestpath) #oldDestination/what/when/foo.abc => finalDestination/wee/poo/foo.abc

                IsolatedFile = os.path.basename(finalDestpath) #foo.abc

                JustfileEx = os.path.splitext(IsolatedFile)[1] #.abc

                NewFileName = "Chrome" + JustfileEx #Chrome.abc

                #os.rename(get the original untouched final destination, renamed to the full directory of the original untouched final destination joined with the brand new file[Chrome.abc])
                os.rename(finalDestpath, os.path.join(os.path.dirname(finalDestpath), NewFileName))

                successLabel = Label(window_frame, text="Jailbroken Successfully!")
                successLabel.pack()
                

            destGobutton = Button(window_frame, text="Confirm", command=destGopressed, fg = "white", bg = "RoyalBlue4")
            destGobutton.pack()


    invisiLabel = Label(window_frame, text="")
    invisiLabel.pack(pady=1)
    invisiLabel.config(bg=background)
    jebbyButton = Button(window_frame, text="Jailbreak!", fg = "white", bg = "RoyalBlue4", command=jebButtonpressed)
    jebbyButton.config(width=15, height=2)
    jebbyButton.pack()

####################################################################################################################################

####################################################################################################################################

def ChangeBackground():
    forget_all_widgets(window_frame)
    nextPagelabel.place_forget()
    backPagebutton.place_forget()
    homeButton.place(x=0, y=300)
    homeButton.config(command=Page2Pressed)

    invisiLabel = Label(window_frame, text="")
    invisiLabel.config(bg=background)
    invisiLabel.pack(pady=5)

    bgPathEntry = Entry(window_frame)
    bgPathEntry.pack(side=tk.TOP, padx=30, fill=tk.X, ipady=5)

    errorExtensionLabel = Label(window_frame, text="Error: Extension is NOT a Supported Format")
    errorExtensionLabel.forget()

    chgBgDoingLabel = Label(window_frame, text="Successfully changed Desktop Background!")
    chgBgDoingLabel.forget()

    errorPathLabel = Label(window_frame, text="Error: Path Not Found")
    errorPathLabel.forget()

    def confirmBgPath(): 
        pathExtension = os.path.splitext(os.path.basename(bgPathEntry.get()))[1]
        extensionRequirementsNotMet = (
            pathExtension != ".png" and pathExtension != ".tif" and pathExtension != ".jpg" and pathExtension != ".jpeg" 
            and pathExtension != ".bmp" and pathExtension != ".gif" and pathExtension != ".tiff" )
        
        if extensionRequirementsNotMet and not os.path.exists(bgPathEntry.get()):
            chgBgDoingLabel.forget() #"path is okay"
            errorExtensionLabel.pack() #"Error: Extension is NOT a Supported Format" - Show
            errorPathLabel.pack() #"Error: Path Not Found" - Show

        elif extensionRequirementsNotMet:
            errorPathLabel.forget() #"Error: Path Not Found"
            chgBgDoingLabel.forget() #"path is okay"
            errorExtensionLabel.pack() #"Error: Extension is NOT a Supported Format" - Show

        elif not os.path.exists(bgPathEntry.get()):
            chgBgDoingLabel.forget() #"path is okay"
            errorExtensionLabel.forget() #"Error: Extension is NOT a Supported Format"
            errorPathLabel.pack() #"Error: Path Not Found" - Show

        else: #success
            errorExtensionLabel.forget() #"Error: Extension is NOT a Supported Format"
            errorPathLabel.forget() #"Error: Path Not Found"
            
            WALLPAPER_PATH = bgPathEntry.get()
            ctypes.windll.user32.SystemParametersInfoW(20, 0, WALLPAPER_PATH, 3)

            chgBgDoingLabel.pack() #"path is okay" - Show
        

    setBgButton = Button(window_frame, text="Set as background!", command=confirmBgPath)
    setBgButton.config(width=15, height=2, fg = "white", bg = "RoyalBlue4")
    setBgButton.pack()



####################################################################################################################################

fetchInfobutton = Button(window_frame, text="Fetch Sys Info", command=fetchInfopressed)
fetchInfobutton.config(width=15, height=2, fg = "white", bg = "RoyalBlue4")
fetchInfobutton.pack()

fetchWifibutton = Button(window_frame, text="Fetch WiFi Password", command=fetch_wifi_thread)
fetchWifibutton.config(width=20, height=2, fg = "white", bg = "RoyalBlue4")
fetchWifibutton.pack()

fetchExebutton = Button(window_frame, text="Fetch EXE Path", command=fetchExe)
fetchExebutton.config(width=15, height=2, fg = "white", bg = "RoyalBlue4")
fetchExebutton.pack()

jebbyScriptbutton = Button(window_frame, text="Jebby's Script", command=jebbyScriptpressed)
jebbyScriptbutton.config(width=15, height=2, fg = "white", bg = "RoyalBlue4", font=("Arial",9, "bold"))
jebbyScriptbutton.pack()

####################################################################################################################################

def homePressed():
    forget_all_widgets(window_frame)
    fetchInfobutton.pack()
    fetchWifibutton.pack()
    fetchExebutton.pack()
    jebbyScriptbutton.pack()
    canvasMain.pack()
    homeButton.place_forget()
    nextPagelabel.place(x=105, y=165)
    forwardPagebutton.place(x=168, y=165)


homeButton = Button(window, text="Home", command=homePressed)
homeButton.config(fg = "white", bg = "RoyalBlue4")
####################################################################################################################################
def Page2Pressed():
    forget_all_widgets(window_frame)
    homeButton.place_forget()
    clearMainhomeScreen()
    nextPagelabel.place(x=105, y=165)
    forwardPagebutton.place_forget()
    backPagebutton.place(x=79, y=165)
    canvasMain.pack_forget()
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    ChgBgButton = Button(window_frame, text="Change Desktop Background", command=ChangeBackground)
    ChgBgButton.config(width=25, height=2, fg = "white", bg = "RoyalBlue4")
    ChgBgButton.pack()
    
    invisiLabel = Label(window_frame, text="")
    invisiLabel.config(bg=background)
    invisiLabel.pack(pady=5)

    creditsButton = Button(window_frame, text="Credits")
    creditsButton.config(width=15, height=2, fg = "white", bg = "RoyalBlue4")
    creditsButton.pack()


def Page1Pressed():
    forget_all_widgets(window_frame) #forget the next page's widgets, then display the new stuff
    fetchInfobutton.pack()
    fetchWifibutton.pack()
    fetchExebutton.pack()
    jebbyScriptbutton.pack()
    forwardPagebutton.place(x=168, y=165)
    backPagebutton.place_forget()
    canvasMain.pack()
    

nextPagelabel = Label(window, text="Next Page")
nextPagelabel.config(fg = "white", bg = "RoyalBlue3")
nextPagelabel.place(x=105, y=165)

forwardPagebutton = Button(window, text="=>", command=Page2Pressed)
forwardPagebutton.config(width=2, height=1)
forwardPagebutton.place(x=168, y=165)

backPagebutton = Button(window, text="<=", command=Page1Pressed)
backPagebutton.config(width=2, height=1)
backPagebutton.place(x=79, y=165)
backPagebutton.place_forget()
####################################################################################################################################
window_frame['bg']='#222027'
canvasMain = Canvas(window_frame, bg='#222027', highlightthickness=0)
canvasMain.pack(fill=tk.BOTH, expand=True)


canvasMain.create_oval(0,265,275,60, fill="RoyalBlue4", outline="")

canvasMain.create_oval(50,115,75,130, fill="RoyalBlue1", outline="") #left eye
canvasMain.create_oval(150,115,175,130, fill="RoyalBlue1", outline="") #right eye

canvasMain.create_line(175,80,200,36, fill="RoyalBlue1", width=5) #right antenna
canvasMain.create_line(75,80,40,36, fill="RoyalBlue1", width=5) #left antenna
####################################################################################################################################


window.mainloop()
