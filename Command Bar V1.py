#libraries
import tkinter
from tkinter import messagebox

root=tkinter.Tk()
root.withdraw()

with open("FirstInfo.txt", 'r+') as f:
            FirstInfoV = f.read()
            if FirstInfoV == "false":
                messagebox.showinfo("Cmdbar V1", "Welcome to Command Bar V1! Please read README. Click 'ok' to continue.")
                f.truncate(0)
                f.close()

with open("propertyDebuggerStartupCBV1", 'r') as f:
            passwordp = f.read()
            f.close()
            if passwordp != "#2013215#":
                print("Click 'ok' to continue")
                messagebox.showinfo("Cmdbar V1", "Command Bar V1 by Misha.")

           

print("-----Command bar-----")
print("'help' for help")

def cmdbar():
    

    commandinput = input("-")


#help command

    if commandinput == "help":
        print("help- lists all commands")
        print("popup create- creates a popup")
        print("viewinfo- views version information")
        print("settings- changes the settings")
        print("file- changes variables about any txt or py file")
        print("end- ends the session")
        cmdbar()
    
    if commandinput == "popup create /help":
       print("/error, /warning, /information, or /question")
       cmdbar()
    if commandinput == "file /help":
        print("/write, /read, /create, or /clear. MUST BE A TXT OR PY FILE, WITHIN USER/.SPYDER-PY3!")
        cmdbar()
    if commandinput == "settings /help":
        print("/templatechange")
        cmdbar()
#popup create

#error
    if commandinput == "popup create /error":
        title = input("Popup title:")
        message = input("Popup text:")
    
        messagebox.showerror(title, message)
        cmdbar()
#warning
    if commandinput == "popup create /warning":
        title = input("Popup title:")
        message = input("Popup text:")
    
        messagebox.showwarning(title, message)
        cmdbar()
#info
    if commandinput == "popup create /information":
        title = input("Popup title:")
        message = input("Popup text:")
    
        messagebox.showinfo(title, message)
        cmdbar()
#question
    if commandinput == "popup create /question":
        title = input("Popup title:")
        message = input("Popup text:")
        options = input("Options (yesno', 'okcancel', 'yesnocancel', or 'retrycancel'):")
    
        if options == "yesno":
            messagebox.askyesno(title, message)
            cmdbar()
        if options == "okcancel":
            messagebox.askokcancel(title, message)
            cmdbar()
        if options == "yesnocancel":
            messagebox.askyesnocancel(title, message)
            cmdbar()
        if options == "retrycancel":
            messagebox.askretrycancel(title, message)
            cmdbar() 
#easter egg
    if commandinput == "selfdestruct":
        messagebox.showwarning("SELF DESTRUCT", "You asked for it (:")
        cmdbar()
    if commandinput == "fun":
        print("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        cmdbar()
#info

    if commandinput == "viewinfo":
        print("Cmdbar V1. Created by Misha. Product ID: mcb1#1")
        cmdbar()
#file
#file create

    if commandinput == "file /create":
        filename = input("File name:")
    
     
        with open(filename, 'a') as f:
                    f.write("---File created by Command bar V1---")
                    f.write('\n')
                    
                    print("File created")
                    f.close()
                    cmdbar()
#file read
    if commandinput == "file /read":
        filereadname = input("File name:")
        
      
        with open(filereadname, 'r') as f:
            filetext = f.read()
            print(filetext)
            f.close()
            cmdbar()
#file write
    if commandinput == "file /write":
        filewritename = input("File name:")
        

        filewritetext = input("Text:")
        
        
        with open(filewritename, 'a') as f:
                    f.write(filewritetext)
                    f.write('\n')
                    
                    f.close()
                    
                    cmdbar()
                    
#file clear
    if commandinput == "file /clear":
        fileclearname = input("File name:")
        
    
        file = open(fileclearname,"r+")
        file. truncate(0)
        
        
        print("File cleared.")
        cmdbar()
#settings

#template change
    if commandinput == "settings /templatechange":
        newtemplate = input("New template:")
    
        file = open("template.py","r+")
        file. truncate(0)
    
        with open("template.py", 'a') as f:
                for line in newtemplate:
                    f.write(line)
                    
                print("Tempalte changed.")
                f.close()
                cmdbar()
                
                
#misc

    if commandinput == "end":
        print("Session ended")
        return
                
cmdbar()
