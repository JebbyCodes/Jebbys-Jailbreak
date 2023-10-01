## 22/7/23 V10 - Stable    [https://github.com/JebbyCodes/Jebbys-Jailbreak]
import platform #sysinfo
import subprocess #wifi
import shutil #filefinder
from tkinter import *
import tkinter as tk
from tkinter import filedialog #open file prompt
import threading
import os #jebbyscript
import sys #private file ref
import ctypes #wallpaper
import webbrowser #website opener (website bypass)

#############################################################################################################
###########[ CONFIGS ]###############[ CONFIGS ]############[ CONFIGS ]###########[ CONFIGS ]###############

#~~[ General Theming ]~~#
font = "Segoe UI"
boldFont = "Arial", "bold"
italicFont = "Arial", "italic"
WinBackground = '#222027'
WidgetBackground = "RoyalBlue4"
textColour = "white"
#~~[                 ]~~#
icon = os.path.join(sys.path[0], "Icon.ico")
iconAlt = os.path.join(sys.path[0], "IconAlt.ico")
iconTest = os.path.join(sys.path[0], "IconTest.ico")
filler = "\n*******************************\n"
exitKey = "<Alt-Key>" #Alt + a
window_width = 275
window_height = 350
ResizeX = False
ResizeY = False
saveFile = os.path.join(sys.path[0], "Save.jeb")
proxyWebsite = "https://usemetallic.com"
gameWebsite = "https://usemetallic.com/2.html"

##################################################################################################################################
########[ THEMES ]##########[ THEMES ]############[ THEMES ]#########[ THEMES ]#########[ THEMES ]#######[ THEMES ]###############
with open(saveFile, 'r') as file:
    lines = file.readlines()
#########################~~~~[ Dark Theme ]~~~~####################################
global darkTheme
def darkTheme():
    global WidgetBackground, textColour, WinBackground
    WidgetBackground = "#474747"
    textColour = "White"
    WinBackground = "Black"

    window_frame['bg']=WinBackground
    canvasMain['bg']=WinBackground
    canvas2['bg']=WinBackground

    with open(saveFile, "w") as file:
        for line in lines:
            if line.strip() == "Theme = default":
                file.write("Theme = dark" + '\n')
                #print("Theme = dark")
            else:
                file.write(line)
                #print(line, end="")

    buttonConfig(backPagebutton, w=2, h=1)
    buttonConfig(forwardPagebutton, w=2, h=1)
    buttonConfig(nextPagelabel, isText=True, w=8, h=1)
        
    for widget in window_frame.winfo_children(): #for every widget in window_frame
        if isinstance(widget, tk.Button): #if the widget is a button
            Font = widget.cget("font") #{
            OgW = widget.cget("width")   #    fetch original configs
            OgH = widget.cget("height")#                              }
            buttonConfig(widget)
            widget.config(font=Font, width=OgW, height=OgH)
            buttonConfig(homeButton, w=5, h=1)
            themeDarkButton.config(bg="Black")
            themeDefaultButton.config(bg="RoyalBlue4")

    for widget in titleBar.winfo_children(): #for every widget in titleBar
        if isinstance(widget, tk.Button): #if the widget is a button
            Font = widget.cget("font") #{
            w = widget.cget("width")   #    fetch original configs
            h = widget.cget("height")#                              }
            buttonConfig(widget)
            widget.config(font=Font, width=w, height=h)

    for widget in window_frame.winfo_children(): #for every widget in window_frame
        if isinstance(widget, tk.Label): #if the widget is a label
            def check_bg_color(widget):
                labelText = widget.cget("text")
                if labelText == " ":
                    widget.config(bg="Black") #make label's bg same as WinBackground
                else:
                    return
            check_bg_color(widget)

#########################~~~~[ Dark Theme ]~~~~####################################

#########################~~~~[ Default Theme ]~~~~#################################
global defaultTheme
def defaultTheme():
    global WidgetBackground, textColour, WinBackground
    WidgetBackground = "RoyalBlue4"
    textColour = "White"
    WinBackground = "#222027"

    window_frame['bg']=WinBackground
    canvasMain['bg']=WinBackground
    canvas2['bg']=WinBackground

    with open(saveFile, "w") as file:
        for line in lines:
            if line.strip() == "Theme = dark":
                file.write("Theme = default" + '\n')
                #print("Theme = default")
            else:
                file.write(line)
                #print(line, end="")

    buttonConfig(backPagebutton, w=2, h=1)
    buttonConfig(forwardPagebutton, w=2, h=1)
    buttonConfig(nextPagelabel, isText=True, w=8, h=1)

    for widget in window_frame.winfo_children(): #for every widget in window_frame
        if isinstance(widget, tk.Button): #if the widget is a button or label
            Font = widget.cget("font") #{
            OgW = widget.cget("width")   #    fetch original configs
            OgH = widget.cget("height")#                              }
            buttonConfig(widget)
            buttonConfig(homeButton, w=5, h=1)
            widget.config(font=Font, width=OgW, height=OgH)
            themeDarkButton.config(bg="Black")
        
    for widget in titleBar.winfo_children(): #for every widget in titleBar
        if isinstance(widget, tk.Button): #if the widget is a button
            Font = widget.cget("font") #{
            w = widget.cget("width")   #    fetch original configs
            h = widget.cget("height")#                              }
            buttonConfig(widget)
            widget.config(font=Font, width=w, height=h)

    for widget in window_frame.winfo_children(): #for every widget in window_frame
        if isinstance(widget, tk.Label): #if the widget is a label
            def check_bg_color(widget):
                labelText = widget.cget("text")
                if labelText == " ":
                    widget.config(bg="#222027") #make label's bg same as WinBackground
                else:
                    return
            check_bg_color(widget)

#########################~~~~[ Default Theme ]~~~~#################################

"""
# buttonComConfig(exampleButton) Calls Func, not bold, edits given button
                                Fulfills all args
# buttonComConfig(exampleButton, True) Now bold

# def buttonComConfig(button=None, requestBold=False): | create Func, with 2 args, 1st
                ||requestBold is False by default||     is custom keyword, 2nd is
                                                        object "button" (tkinter)
"""

def buttonConfig(button=None, requestBold=False, FontSize=None, Font=None, isText=False, isInvisi=False, w=None, h=None): #func allows button widgets

    if button: #if button request fulfilled

        if FontSize is None:
            FontSize = 9
        if Font is None:
            Font = font
        
        if w is None:
            w = 15
        if h is None:
            h = 2
            
        if requestBold: #if "requestBold" is True
            button.config(font=(boldFont, FontSize), fg = textColour, bg = WidgetBackground, width = w, height = h)
            return textColour, WidgetBackground
        else:
            button.config(font=(Font, FontSize), fg = textColour, bg = WidgetBackground, width = w, height = h)

        if isText:
            button.config(bg=WidgetBackground, fg=textColour, font=(Font, FontSize))
            return textColour, WidgetBackground, WinBackground
        if isInvisi:
            button.config(bg=WinBackground, fg=WinBackground)
            return WinBackground

#############################################################################################################
########[ NOTES ]##########[ NOTES ]############[ NOTES ]#########[ NOTES ]#########[ NOTES ]#######[ NOTES ]

#sys.path[0] = parent dir
#you may choose to not use the icons
#press enter instead of pressing the button in entry prompts
#arrow keys supported to change page
#event=None, accept event AND other stuff

#############################################################################################################
########[ WINDOW ]##########[ WINDOW ]############[ WINDOW ]#########[ WINDOW ]#########[ WINDOW ]###########

window = Tk()
window.title("Jebby's Jailbreak")
window.iconbitmap(iconTest)
window.resizable(ResizeX, ResizeY)

def toggle(event):
    if event.type == EventType.Map:
        window.deiconify()
        window.lift()
    else:
        window.withdraw()

top = Toplevel(window)
top.geometry('0x0+10000+10000')
top.protocol('WM_DELETE_WINDOW', window.destroy)
top.bind("<Map>", toggle)
top.bind("<Unmap>", toggle)
top.title("Jebby's Jailbreak")
top.iconbitmap(iconTest)

##################################################################################################################################
########[ TITLEBAR ]#######[ TITLEBAR ]############[ TITLEBAR ]#########[ TITLEBAR ]#########[ TITLEBAR ]#######[ TITLEBAR ]######

def moveWinPress(e):
    global x,y
    x, y = e.x, e.y

def moveWinDrag(e):
    window.geometry(f'+{e.x_root - x}+{e.y_root - y}')

def moveWinPressCanvas(e):
    global x,y
    x, y = e.x, e.y

def moveWinDragCanvas(e):
    yPos = round(e.y_root - (y*2)-50)
    window.geometry(f'+{e.x_root - x}+{yPos}')

window.overrideredirect(True) #Disable titlebar
titleBar = Frame(window, bd=0, bg="White", height=15)
titleBar.pack(fill=X)
titleBar.bind("<B1-Motion>", moveWinDrag)
titleBar.bind("<Button-1>", moveWinPress)

########[ TITLE BUTTONS ]#########[ TITLE BUTTONS ]################[ TITLE BUTTONS ]#############[ TITLE BUTTONS ]#################

exitButton = Button(titleBar, command=quit, text="X", activebackground="red", bd=0, compound="center")
buttonConfig(exitButton, h=1, w=2)
exitButton.pack(side=RIGHT)

minButton = Button(titleBar, command=top.iconify, text=" 🗕 ", activebackground="lightblue", bd=0, compound="center")
buttonConfig(minButton, h=1, w=2)
minButton.pack(side=RIGHT, padx=5)

titleLabel = Label(titleBar, text="Jebby's Jailbreak", bg="White", font=("Cascadia Code", 9))
titleLabel.bind("<B1-Motion>", moveWinDrag)
titleLabel.bind("<Button-1>", moveWinPress)
titleLabel.pack(side=LEFT)

#############################################################################################################
########[ EMERGENCY EXIT ]##########[ EMERGENCY EXIT ]##########[ EMERGENCY EXIT ]#########[ EMERGENCY EXIT ]

def emergency_exit(event): #must make function accept "events", like .bind
    window.quit()

window.bind(exitKey, emergency_exit)

#############################################################################################################
##########[ CLEAR PAGE 1 ]############[ CLEAR PAGE 1 ]############[ CLEAR PAGE 1 ]###########[ CLEAR PAGE 1 ]

def clearMainhomeScreen():
    fetchWifibutton.forget()
    fetchInfobutton.forget()
    fetchExebutton.forget()
    jebbyScriptbutton.forget()
    canvasMain.pack_forget()
    canvas2.pack_forget()
    nextPagelabel.place_forget()
    forwardPagebutton.place_forget()
    backPagebutton.place_forget()
    buttonConfig(backPagebutton, w=2, h=1)
    miscButton.place_forget()
    themeDarkButton.place_forget()
    themeDefaultButton.place_forget()
    window.unbind("<Right>")
    window.unbind("<Left>")

#############################################################################################################
#########[ CENTRE WINDOW ]###########[ CENTRE WINDOW ]###########[ CENTRE WINDOW ]##########[ CENTRE WINDOW ]

def center_window(window, width, height):
    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the x and y coordinates for the window to be centered
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Set the window geometry to center it on the screen
    window.geometry(f"{width}x{height}+{x}+{y}")

center_window(window, window_width, window_height)

#############################################################################################################
#########[ WINDOW_FRAME ]###########[ WINDOW_FRAME ]###########[ WINDOW_FRAME ]##########[ WINDOW_FRAME ]####

window_frame = tk.Frame(window)
window_frame.pack(fill=tk.BOTH, expand=True)
window_frame['bg']=WinBackground
window_frame.bind("<B1-Motion>", moveWinDrag)
window_frame.bind("<Button-1>", moveWinPress)

#############################################################################################################
#########[ CLEAR WINDOW_FRAME ]###########[ CLEAR WINDOW_FRAME ]###########[ CLEAR WINDOW_FRAME ]############

def forget_all_widgets(window_frame):
    for widget in window_frame.winfo_children():
        widget.pack_forget()

#####################################################################################################################
#########[ CLEAR PAGE 2 ]###########[ CLEAR PAGE 2 ]###########[ CLEAR PAGE 2]############[ CLEAR PAGE 2]############

def clearPage2():
    forget_all_widgets(window_frame)
    miscButton.place_forget()
    themeDarkButton.place_forget()
    themeDefaultButton.place_forget()
    backPagebutton.place_forget()
    forwardPagebutton.place_forget()
    nextPagelabel.place_forget()
    window.unbind("<Right>")
    window.unbind("<Left>")

#############################################################################################################
######[ START OF JAILBREAKS ]###############[ START OF JAILBREAKS ]#####################[ START OF JAILBREAKS ]#####################

def fetchInfopressed():
    clearMainhomeScreen()

    homeButton.place(x=233, y=325) #right
    homeButton.config(command=homePressed)

 
    sysInfo = Text(window_frame, wrap=tk.WORD)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    sysInfo.tag_configure("bold", font=(font, 9, "bold")) #this is what "bold" text will look like
    sysInfo.tag_configure("normal", font=(font, 9)) #this is what "normal" text will look like
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    sysInfo.insert("1.0", "Platform processor:", "bold") # Platform Processor
    sysInfo.insert("end", f"\n {platform.processor()}\n", "normal")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    sysInfo.insert("end", "\nSystem platform:", "bold") # System platform
    sysInfo.insert("end", f"\n {platform.system()}\n", "normal")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    sysInfo.insert("end", "\nNode name (hostname):", "bold") # Node name (hostname)
    sysInfo.insert("end", f"\n {platform.node()}\n", "normal")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    sysInfo.insert("end", "\nSystem release:", "bold") # Release version
    sysInfo.insert("end", f"\n {platform.system()} {platform.release()}\n", "normal")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    sysInfo.insert("end", "\nProcessor architecture:", "bold") # Processor architecture
    sysInfo.insert("end", f"\n {platform.machine()}\n", "normal")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    sysInfo.insert("end", "\nPlatform processor:", "bold") # System OS
    sysInfo.insert("end", f"\n {platform.platform()}\n", "normal")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    sysInfo.insert("end", "\nPlatform architecture:", "bold") # Platform architecture
    sysInfo.insert("end", f"\n {platform.architecture()}", "normal")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    sysInfo.configure(bg=WinBackground, fg="white")
    sysInfo.config(state=tk.DISABLED)
    sysInfo.pack()    

####################################################################################################################################
##########[ JAILBREAKS - GET WIFI ]###############[ JAILBREAKS  - GET WIFI ]#####################[ JAILBREAKS  - GET WIFI ]#########

def fetch_wifi_thread():
    def fetch_wifi():
        homeButton.place(x=0, y=325)
        homeButton.config(command=homePressed)

        fetchWifibutton.config(state=tk.DISABLED)
        fetchInfobutton.config(state=tk.DISABLED)
        fetchExebutton.config(state=tk.DISABLED)
        jebbyScriptbutton.config(state=tk.DISABLED)
        nextPagelabel.config(state=tk.DISABLED)
        forwardPagebutton.config(state=tk.DISABLED)
        backPagebutton.config(state=tk.DISABLED)
        clearMainhomeScreen()

        

        wifiResultsframe = tk.Frame(window_frame, bg=WidgetBackground)
        wifiResultsframe.pack(side=tk.BOTTOM,fill=tk.BOTH, expand=True)
        wifiResultsframe.pack_propagate(False)

        wifiUserindicateLabel = Label(window_frame, text="USERNAME:")
        wifiUserindicateLabel.config(bg=WinBackground, fg="white")
        wifiUserindicateLabel.pack(side=tk.LEFT, padx=5, pady=5)

        wifiPassindicateLabel = Label(window_frame, text="PASSWORD:")
        wifiPassindicateLabel.config(bg=WinBackground, fg="white")
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
                    WifiUsertext.config(state=tk.DISABLED, highlightthickness=0, bg=WinBackground, fg="white")
                except IndexError:
                    WifiUsertext = tk.Text(wifiResultsframe, wrap=tk.WORD, height=1, width=30)
                    WifiUsertext.insert(tk.END, "{:<15}|  {:<}".format(i, ""))
                    WifiUsertext.pack(pady=7)
                    WifiUsertext.config(state=tk.DISABLED, highlightthickness=0, bg=WinBackground, fg="white")
            except subprocess.CalledProcessError:
                WifiUsertext = tk.Text(wifiResultsframe, wrap=tk.WORD, height=1, width=30)
                WifiUsertext.insert(tk.END, "{:<15}|  {:<}".format(i, "ENCODING ERROR"))
                WifiUsertext.pack(pady=7)
                WifiUsertext.config(state=tk.DISABLED, highlightthickness=0, bg=WinBackground, fg="white")
        
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
######[ JAILBREAKS - GET EXE PATH ]###############[ JAILBREAKS - GET EXE PATH ]##################[ JAILBREAKS  - GET EXE PATH ]#####

def fetchExe():
    homeButton.place(x=0, y=325)
    homeButton.config(command=homePressed)

    clearMainhomeScreen()

    invisiLabel = Label(window_frame, text=" ")
    buttonConfig(invisiLabel, isInvisi=True)
    invisiLabel.pack(pady=15)

    exeEntry = Entry(window_frame)
    exeEntry.pack(side=tk.TOP, padx=30, fill=tk.X)


    def getExeentry(event=None): #accept "event" AND other stuff
    
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
            NoExePath.config(text=" ", bg=WinBackground)

    subExebutton = Button(window_frame, text="Fetch Path", command=getExeentry)
    
    subExebutton.config(fg = "white", bg = WidgetBackground)
    subExebutton.pack()

    NoExePath = Label(window_frame, text=" ", wraplength=200)
    NoExePath.config(bg=WinBackground)
    NoExePath.pack()
    GotExePath = tk.Text(window_frame, wrap=tk.WORD, height=3, width=20)
    GotExePath.insert(tk.END, " ")
    GotExePath.config(state=tk.DISABLED, highlightthickness=0)

    window.bind("<Return>", getExeentry)

####################################################################################################################################
######[ JAILBREAKS - JEBBY'S SCRIPT ]###############[ JAILBREAKS - JEBBY'S SCRIPT ]##################[ JAILBREAKS - JEBBY'S SCRIPT ]

def jebbyScriptpressed():
    homeButton.place(x=0, y=325)
    homeButton.config(command=homePressed)
    clearMainhomeScreen()

    invisiLabel = Label(window_frame, text=" ")
    invisiLabel.pack(pady=15)
    buttonConfig(invisiLabel, isInvisi=True)

    pathEntry = Entry(window_frame, width=30)
    pathEntry.pack(ipady=6)

    banSymbol = ['"', '|', '?', '<', '>', '*']

    def jebButtonpressed(event=None, exeMode=False):

        if any(symbol in pathEntry.get() for symbol in banSymbol):
            errorLabelSrc.config(text=" ", bg=WinBackground)
            errorLabel.config(text="ERROR: Forbidden Symbols Used", bg="White")

        elif not os.path.exists(pathEntry.get()):
            errorLabel.config(text=" ", bg=WinBackground)
            errorLabelSrc.config(text=f"ERROR: Source File Path not found at '{pathEntry.get()}'", bg="white")
            return
            
        else:
            pathEntry.forget()
            jebbyButton.forget()
            exeModeButton.forget()
            seldesLabel = Label(window_frame,text="Select destination:")
            seldesLabel.pack()
            destEntry = Entry(window_frame, width=30)
            destEntry.pack(ipady=6)
            jailbreakBrowseButton.forget()
            errorLabelSrc.forget()

            def browseForJailbreakDest():
                errorLabelDst.forget()
                jailbreakBrowse = str(filedialog.askdirectory())
                destEntry.delete(0, 'end')
                destEntry.insert(0, jailbreakBrowse)

            jailbreakBrowseDestButton = Button(window_frame, text="Browse Files", command=browseForJailbreakDest)
            buttonConfig(jailbreakBrowseDestButton, w=10, h=1)
            jailbreakBrowseDestButton.pack(pady=10)

            errorLabelDst = Label(window_frame, wraplength=200, bg=WinBackground)

            def destGopressed(event=None):
                src_path = rf'{pathEntry.get()}'
                dst_path = rf'{destEntry.get()}'

                if not os.path.exists(src_path):
                    errorLabelDst.forget()
                    return
                    
                elif not os.path.exists(dst_path):
                    errorLabelDst.config(text=f"Error: Destination Path not found at '{dst_path}'", bg="white")
                    errorLabelDst.pack()
                    return    
                
                finalDestpath = os.path.join(dst_path, os.path.basename(src_path)) #finalDestination/wee/poo/foo.abc

                shutil.copy(src_path, finalDestpath) #oldDestination/what/when/foo.abc => finalDestination/wee/poo/foo.abc

                IsolatedFile = os.path.basename(finalDestpath) #foo.abc

                if exeMode == False:
                    JustfileEx = os.path.splitext(IsolatedFile)[1]
                if exeMode == True:
                    JustfileEx = ".com" #.com

                NewFileName = "Chrome" + JustfileEx #Chrome.abc

                #os.rename(get the original untouched final destination, renamed to the full directory of the original untouched final destination joined with the brand new file[Chrome.abc])
                os.rename(finalDestpath, os.path.join(os.path.dirname(finalDestpath), NewFileName))

                errorLabelDst.forget()
                successLabel = Label(window_frame, text="Jailbroken Successfully!")
                successLabel.pack()
                

            destGobutton = Button(window_frame, text="Confirm", command=destGopressed)
            buttonConfig(destGobutton, w=10, h=2)
            destGobutton.pack(pady=5)
            window.bind("<Return>", destGopressed)

    jebbyButton = Button(window_frame, text="Jailbreak!", command=jebButtonpressed)
    buttonConfig(jebbyButton)
    jebbyButton.config(width=15, height=2)
    jebbyButton.pack(pady=15)

    exeModeButton = Button(window_frame, text="EXE Jailbreak!", command=lambda: jebButtonpressed(exeMode=True))
    buttonConfig(exeModeButton, h=1)
    exeModeButton.pack(pady=5)

    def browseForJailbreak():
        jailbreakBrowse = str(filedialog.askopenfilename())
        pathEntry.delete(0, 'end')
        pathEntry.insert(0, jailbreakBrowse)

    jailbreakBrowseButton = Button(window_frame, text="Browse Files", command=browseForJailbreak)
    buttonConfig(jailbreakBrowseButton, w=10, h=1)
    jailbreakBrowseButton.pack(pady=5)

    errorLabel = Label(window_frame,text=" ", bg=WinBackground)
    errorLabel.pack()

    errorLabelSrc = Label(window_frame,text=" ", wraplength=200, bg=WinBackground)
    errorLabelSrc.pack()
    

    window.bind("<Return>", jebButtonpressed)

#######################[ END OF JAILBREAKS - PAGE 1 ]#######################[ END OF JAILBREAKS - PAGE 1 ]##########################
####################################################################################################################################

####################################################################################################################################
######[ JAILBREAKS - BACKGROUND ]###############[ JAILBREAKS - BACKGROUND ]#####################[ JAILBREAKS - BACKGROUND ]##########

def ChangeBackground():
    clearPage2()
    homeButton.place(x=0, y=325)
    homeButton.config(command=Page2Pressed)

    invisiLabel = Label(window_frame, text=" ")
    buttonConfig(invisiLabel, isInvisi=True)
    invisiLabel.pack(pady=5)

    bgPathEntry = Entry(window_frame)
    bgPathEntry.pack(side=tk.TOP, padx=30, fill=tk.X, ipady=5)

    errorExtensionLabel = Label(window_frame, text="Error: Extension is NOT a Supported Format")
    errorExtensionLabel.forget()

    chgBgDoingLabel = Label(window_frame, text="Successfully changed Desktop Background!")
    chgBgDoingLabel.forget()

    errorPathLabel = Label(window_frame, text="Error: Path Not Found")
    errorPathLabel.forget()

    def confirmBgPath(event=None): 
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
    #setBgButton.config(width=15, height=2)
    buttonConfig(setBgButton, w=15, h=2)
    setBgButton.pack()
    window.bind("<Return>", confirmBgPath)

    def browseBg():
        selectedBg = str(filedialog.askopenfilename())

        errorPathLabel.forget()
        errorExtensionLabel.forget()
        chgBgDoingLabel.forget()

        bgPathEntry.delete(0, 'end')
        bgPathEntry.insert(0, selectedBg)

    browseBgButton = Button(window_frame, text="Browse Files", command=browseBg)
    buttonConfig(browseBgButton, w=10, h=1)
    browseBgButton.pack(pady=10)

####################################################################################################################################
######[ JAILBREAKS - PROXY ]###############[ JAILBREAKS - PROXY ]#####################[ JAILBREAKS - PROXY ]########################

def webBypassPressed():
    clearPage2()
    homeButton.place(x=0, y=325)
    homeButton.config(command=Page2Pressed)

    invisiLabel = Label(window_frame)
    buttonConfig(invisiLabel, isInvisi=True)
    invisiLabel.pack(pady=10)

    #addressEntry = Entry(window_frame)
    #addressEntry.config(width=30)
    #addressEntry.pack(ipady=3)

    def openProxy():
        webbrowser.open(proxyWebsite)

    def openUnblockedGames():
        webbrowser.open(gameWebsite)

    proxyGoButton = Button(window_frame, text="Open Website", command=openProxy)
    buttonConfig(proxyGoButton, w=15, h=2)
    proxyGoButton.pack(pady=13)

    unblockGamesButton = Button(window_frame, text="Unblocked Games Archive", command=openUnblockedGames)
    buttonConfig(unblockGamesButton, w=20, h=2)
    unblockGamesButton.pack(pady=10)

    redirectWarn = Label(window_frame, text="Warning: You will be redirected.")
    buttonConfig(redirectWarn, isText=True, w=25, h=1, Font=("Arial", "bold", "italic"), FontSize=7)
    redirectWarn.pack(pady=50)

#######################[ END OF JAILBREAKS - PAGE 2 ]#######################[ END OF JAILBREAKS - PAGE 2 ]##########################
####################################################################################################################################

####################################################################################################################################
######[ CREDITS CODE ]##############[ CREDITS CODE ]################[ CREDITS CODE ]###############[ CREDITS CODE ]#################

def Credits():
    clearPage2()
    homeButton.place(x=0, y=325)
    homeButton.config(command=Page2Pressed)
    window.unbind("<Right>")
    window.unbind("<Left>")

    creditText = f'''\n    Creator:  Jebby \n    Contributers:  PengeSal 
    {filler} Python Modules:\n     -Tkinter\n     -Platform\n     -Subprocess\n     -Shutil\n     -Threading\n     -OS\n     -Sys\n     -Ctypes\n     -Webbrowser
    {filler} Tools:\n     -Python\n     -Visual Studio Code\n     -Github\n     -{proxyWebsite}
    {filler} Icons:\n      -[Icon.ico] => imgbin\n   -[IconAlt.ico] => pngitem
    {filler}
    '''

    creditTextWidget = tk.Text(window_frame, wrap=tk.WORD, width=30, height=15) #create the text widget, allow wrapping
    creditTextWidget.insert("1.0", creditText) #insert the text into the widget

    creditTextWidget.tag_configure("creditTitle", font=(font,12, "bold"))
    creditTextWidget.tag_configure("creditEnd", font=(font,10, "italic"))
    creditTextWidget.tag_configure("squiggly", font=(font,10, "italic"))
    creditTextWidget.insert("1.0", f"                   **CREDITS:** \n************************************\n", "creditTitle")
    creditTextWidget.insert("end", "        Thank you for using this! :)", "creditEnd")
    creditTextWidget.insert("end", "\n             ~~~~~~~~~~~~~~~\n\n", "squiggly")

    # Create the Scrollbar widget and allow the scrollbar to move text pos
    creditScrollbar = tk.Scrollbar(window_frame, command=creditTextWidget.yview)

    # Configure the Text widget's yscrollcommand to remember the scroll bar pos and text pos
    creditTextWidget.configure(yscrollcommand=creditScrollbar.set)

    creditScrollbar.pack(side=tk.RIGHT, fill="y")
    creditTextWidget.pack(side=tk.LEFT, fill="both", expand=True)

    #creditTextWidget.config(bg=background, fg="white")
    buttonConfig(creditTextWidget, isText=True, FontSize=15)
    creditTextWidget.config(state=tk.DISABLED)

####################################################################################################################################
######[ PAGE 1 BUTTONS ]##############[ PAGE 1 BUTTONS ]##############[ PAGE 1 BUTTONS ]###############[ PAGE 1 BUTTONS ]###########

fetchInfobutton = Button(window_frame, text="Fetch Sys Info", command=fetchInfopressed)
buttonConfig(fetchInfobutton) #call Func, not bold, do Func for "fetchInfobutton"
#fetchInfobutton.config(width=15, height=2)
fetchInfobutton.pack()

fetchWifibutton = Button(window_frame, text="Fetch WiFi Password", command=fetch_wifi_thread)
buttonConfig(fetchWifibutton, w=20)
#fetchWifibutton.config(width=20, height=2)
fetchWifibutton.pack()

fetchExebutton = Button(window_frame, text="Fetch EXE Path", command=fetchExe)
buttonConfig(fetchExebutton)
##fetchExebutton.config(width=15, height=2)
fetchExebutton.pack()

jebbyScriptbutton = Button(window_frame, text="Jebby's Script", command=jebbyScriptpressed)
buttonConfig(jebbyScriptbutton, requestBold=True)
#jebbyScriptbutton.config(width=15, height=2)
jebbyScriptbutton.pack()

####################################################################################################################################
##########[ HOME BUTTON ]##############[ HOME BUTTONS ]##############[ HOME BUTTONS ]###############[ HOME BUTTONS ]################

def homePressed():
    forget_all_widgets(window_frame)
    fetchInfobutton.pack()
    fetchWifibutton.pack()
    fetchExebutton.pack()
    jebbyScriptbutton.pack()
    canvasMain.pack()
    homeButton.place_forget()
    nextPagelabel.place(x=105, y=190)
    forwardPagebutton.place(x=168, y=190)
    window.unbind("<Return>")
    window.bind("<Right>", Page2Pressed)
    miscButton.place(x=260, y=0)
    themeDarkButton.place(x=0, y=0)
    themeDefaultButton.place(x=15, y=0)


homeButton = Button(window, text="Home", command=homePressed)
buttonConfig(homeButton, w=5, h=1)

####################################################################################################################################
##########[ MISC BUTTON ]##############[ MISC BUTTONS ]##############[ MISC BUTTONS ]###############[ MISC BUTTONS ]################

def miscFunc():
    if nextPagelabel.cget("text") == "Next Page":   #.cget("text") - get text, if its equal to "Next Page"
        page=Page1Pressed
    elif nextPagelabel.cget("text") == "Go Back":
        page=Page2Pressed
    
    forget_all_widgets(window_frame)
    nextPagelabel.place_forget()
    forwardPagebutton.place_forget()
    backPagebutton.place_forget()
    buttonConfig(backPagebutton, w=2, h=1)
    miscButton.place_forget()
    homeButton.place(x=0, y=325)
    
    homeButton.config(command=page)

####################################################################################################################################
##########[ CHANGELOG ]##############[ CHANGELOG ]##############[ CHANGELOG ]##############[ CHANGELOG ]###############[ CHANGELOG ]

    def changeLog():
        fillerLong = '\n******************************************\n'

        ChangelogButton.forget()
        changelogText = tk.Text(window_frame)

        changelogText.insert("1.0", f'''{fillerLong}Version: 10{fillerLong}Changes:
    - Added new 'Bypass Web' feature
    - Fixed window movement issues
    - Fixed theming issues
    - Added 'EXE Jailbreak' in "Jebby's Jailbreak" button
    - Optimised/Cleaned up code''')
        
        changelogText.config(state="disabled")
        buttonConfig(changelogText, isText=True, w=34, h=17, FontSize=10)
        changelogText.pack(anchor='ne')

    ChangelogButton = Button(window_frame,text="Change Log", command=changeLog)
    buttonConfig(ChangelogButton)
    ChangelogButton.pack()

####################################################################################################################################


miscButton = Button(window_frame, text="!", command=miscFunc)
buttonConfig(miscButton, requestBold=True, w = 1, h=1)
miscButton.place(x=260, y=0)

####################################################################################################################################
#############[ CUSTOMISE BUTTONS ]################[ CUSTOMISE BUTTONS ]##################[ CUSTOMISE BUTTONS ]######################


themeDarkButton = Button(window_frame, text=" ", command=darkTheme)
themeDarkButton.config(bg="Black", width=1, height=1)
themeDarkButton.place(x=0, y=0)

themeDefaultButton = Button(window_frame, text=" ",command = defaultTheme)
buttonConfig(themeDefaultButton, w=1, h=1)
themeDefaultButton.place(x=15,y=0)


####################################################################################################################################
##########[ PAGE 2 ]##############[ PAGE 2 ]##############[ PAGE 2 ]###############[ PAGE 2 ]################[ PAGE 2 ]#############

def Page2Pressed(event=None):
    forget_all_widgets(window_frame)
    homeButton.place_forget()
    clearMainhomeScreen()
    nextPagelabel.place(x=110, y=190)
    nextPagelabel.config(text="Go Back")
    forwardPagebutton.place_forget()
    backPagebutton.place(x=84, y=190)
    buttonConfig(backPagebutton, w=2, h=1)
    canvasMain.pack_forget()
    window.unbind("<Return>")
    window.bind("<Left>", Page1Pressed)
    miscButton.place(x=260, y=0)
    themeDarkButton.place(x=0, y=0)
    themeDefaultButton.place(x=15, y=0)
    page = Page2Pressed
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    invisiLabel = Label(window_frame, text=" ")
    buttonConfig(invisiLabel, isInvisi=True, w=1, h=1)
    invisiLabel.pack(pady=3)

    ChgBgButton = Button(window_frame, text="Change Desktop Background", command=ChangeBackground)
    buttonConfig(ChgBgButton, w=25)
    ChgBgButton.pack()
    
    webBypassButton = Button(window_frame, text="Bypass Web", command=webBypassPressed)
    buttonConfig(webBypassButton, w=15)
    webBypassButton.pack()

    creditsButton = Button(window_frame, text="Credits", command=Credits)
    creditsButton.config(width=15, height=2)
    buttonConfig(creditsButton)
    creditsButton.pack()

    canvas2.pack()

####################################################################################################################################
##########[ PAGE 1 ]##############[ PAGE 1 ]##############[ PAGE 1 ]###############[ PAGE 1 ]################[ PAGE 1 ]#############

def Page1Pressed(event=None):
    forget_all_widgets(window_frame) #forget the next page's widgets, then display the new stuff
    fetchInfobutton.pack()
    fetchWifibutton.pack()
    fetchExebutton.pack()
    jebbyScriptbutton.pack()
    forwardPagebutton.place(x=170, y=190)
    buttonConfig(forwardPagebutton, w=2, h=1)
    backPagebutton.place_forget()
    buttonConfig(backPagebutton, w=2, h=1)
    nextPagelabel.place(x=105, y=190)
    buttonConfig(nextPagelabel, isText=True, w=8, h=1)
    nextPagelabel.config(text="Next Page")
    canvasMain.pack()
    canvas2.pack_forget()
    window.bind("<Right>", Page2Pressed)
    miscButton.place(x=260, y=0)
    themeDarkButton.place(x=0, y=0)
    themeDefaultButton.place(x=15, y=0)
    homeButton.place_forget()
    

nextPagelabel = Label(window, text="Next Page")
buttonConfig(nextPagelabel, isText=True, w=8, h=1)
nextPagelabel.place(x=105, y=190)

forwardPagebutton = Button(window, text="=>", command=Page2Pressed)
buttonConfig(forwardPagebutton, w=2, h=1)
forwardPagebutton.place(x=168, y=190)

backPagebutton = Button(window, text="<=", command=Page1Pressed)
buttonConfig(backPagebutton, w=2, h=1)
backPagebutton.place(x=79, y=190)
backPagebutton.place_forget()

window.bind("<Right>", Page2Pressed)
window.bind("<Left>", Page1Pressed)

####################################################################################################################################
##########[ THE DRAWING ROOM - PAGE 1 ]###############[ THE DRAWING ROOM - PAGE 1 ]#############[ THE DRAWING ROOM - PAGE 1 ]#######

canvasMain = Canvas(window_frame, bg=WinBackground, highlightthickness=0)
canvasMain.pack(fill=tk.BOTH, expand=True)

canvasMain.bind("<B1-Motion>", moveWinDragCanvas)
canvasMain.bind("<Button-1>", moveWinPressCanvas)

# x0 y0 x1 y1

canvasMain.create_oval(0,265,275,60, fill="RoyalBlue4", outline="")

canvasMain.create_oval(50,115,75,130, fill="RoyalBlue1", outline="") #left eye
canvasMain.create_oval(150,115,175,130, fill="RoyalBlue1", outline="") #right eye

canvasMain.create_line(175,80,200,36, fill="RoyalBlue1", width=5) #right antenna
canvasMain.create_line(75,80,40,36, fill="RoyalBlue1", width=5) #left antenna

####################################################################################################################################
##########[ THE DRAWING ROOM - PAGE 2 ]###############[ THE DRAWING ROOM - PAGE 2 ]#############[ THE DRAWING ROOM - PAGE 2 ]#######

canvas2 = Canvas(window_frame, bg=WinBackground, highlightthickness=0)
canvas2.pack(fill=tk.BOTH, expand=True)

canvas2.bind("<B1-Motion>", moveWinDragCanvas)
canvas2.bind("<Button-1>", moveWinPressCanvas)


canvas2.create_oval(0,500,275,60, fill="RoyalBlue4", outline="")

canvas2.create_oval(70,115,95,130, fill="RoyalBlue1", outline="") #left eye
canvas2.create_oval(150,115,175,130, fill="RoyalBlue1", outline="") #right eye

canvas2.create_line(175,80,200,36, fill="RoyalBlue1", width=5) #right antenna
canvas2.create_line(90,80,60,36, fill="RoyalBlue1", width=5) #left antenna


canvas2.create_arc(70,115,95,130, start=0, extent=200, fill="RoyalBlue4", outline="") #left eyeshadow
canvas2.create_arc(150,115,175,130, start=0, extent=200, fill="RoyalBlue4", outline="") #right eyeshadow

#############################################################################################################
########[ SAVE ]##########[ SAVE ]############[ SAVE ]#########[ SAVE ]#########[ SAVE ]#######[ SAVE ]######

with open(saveFile,"r") as file: # open the file in read mode, make it the "file" variable
        for line in file:
            line = line.strip() # strip the line so its just the line itself
            if line == "Theme = default":
                defaultTheme()
                break
            elif line == "Theme = dark":
                darkTheme()
                break
        else:
            print("ERROR")

####################################################################################################################################
##########[ DONT TOUCH ]############[ DONT TOUCH ]#############[ DONT TOUCH ]############[ DONT TOUCH ]#########[ DONT TOUCH ]######

window.mainloop()
