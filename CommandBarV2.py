def FORCERESET():
    print("RESTARTING COMMANDBAR V2...")
    
    
    with open('CBV2background', 'r+') as f:
                    
                    f.truncate(0)
                    
                    for line in "White":
                        f.write(line)
                   
                    #fontcolor                
    with open('CBV2fontcolor', 'r+') as f:
        
                f.truncate(0)
        
                for line in "#00FF00":
                    f.write(line)
                    

    #fontbackground
    with open('CBV2fontbackground', 'r+') as f:
        
                f.truncate(0)
        
                for line in "Black":
                    f.write(line)
                   
    #font
    with open('CBV2font', 'r+') as f:
        
                f.truncate(0)
        
                for line in "Comic Sans":
                    f.write(line)
                   
    
    #fontsize
    with open('CBV2fontsize', 'r+') as f:
        
                f.truncate(0)
        
                for line in "25":
                    f.write(line)
                    
    
    #wwidth
    with open('CBV2windowwidth', 'r+') as f:
            
                f.truncate(0)
        
                for line in "700":
                    f.write(line)
                    
    
    
    #wheight
    with open('CBV2windowheight', 'r+') as f:
        
                f.truncate(0)
        
                for line in "400":
                    f.write(line)
                    
    print("Restart Complete!")

#--------------------------------------------#

with open('CBV2background', 'r') as f:
    SETTINGSbackground = f.read()
    
with open('CBV2font', 'r') as f:
    SETTINGSfont = f.read()

with open('CBV2fontbackground', 'r') as f:
    SETTINGSfontbackground = f.read()

with open('CBV2fontcolor', 'r') as f:
    SETTINGSfontcolor = f.read()
    
with open('CBV2fontsize', 'r') as f:
    SETTINGSfontsize = f.read()
    
with open('CBV2windowheight', 'r') as f:
    SETTINGSwindowheight = f.read()

with open('CBV2windowwidth', 'r') as f:
    SETTINGSwindowwidth = f.read()
    
print(SETTINGSbackground, SETTINGSfontbackground, SETTINGSfontcolor, SETTINGSfontsize, SETTINGSwindowheight, SETTINGSwindowwidth)

import tkinter as tk
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
#main cmd bar

ADVERTISEMENT = tk.Tk()

adlabel1 = tk.Label(ADVERTISEMENT, text="We accept donations! Copy and paste the link below to donate.", font=("Comic Sans", 40))
adlabel1.pack()

adlabel2 = tk.Label(ADVERTISEMENT, text="Donations give special perks, such as new features! (Close this window to continue)", font=("Comic Sans", 30))
adlabel2.pack()

canvas = tk.Canvas(ADVERTISEMENT, height=400, width=700)
canvas.pack()


CNPAD = Entry(ADVERTISEMENT, font=("Comic Sans", 35))
CNPAD.insert(0, "https://mishaleksanov.wixsite.com/mikhos-studios/donation-screen")
CNPAD.pack()

FORCERESETBUTOTN = tk.Button(ADVERTISEMENT, text="FORCE RESET", command=FORCERESET)
FORCERESETBUTOTN.pack()
ADVERTISEMENT.mainloop()

with open("README_2.txt", 'r') as f:
            READMETEXT = f.read()
            print("HELP COMMAND")
            f.close()

def inputwidget():
    commandinput = entry.get()
    print(commandinput)
    
    #error
    
    if commandinput == "popup create /error":
        def errorpopupcreate():
            errorroot.withdraw()
            titleerror = errortitle.get()
            messageerror = errormessage.get()
    
            messagebox.showerror(titleerror, messageerror)

        errorroot = tk.Tk()
        errorroot.config(bg=SETTINGSbackground)
        createerrorlabel1 = tk.Label(errorroot, text="COMMAND BAR V2")
        createerrorlabel1.pack()
        
        createerrorlabel2 = tk.Label(errorroot, text="POPUP CREATE /ERROR")
        createerrorlabel2.pack()
        
        canvas = tk.Canvas(errorroot, height=SETTINGSwindowheight, width=SETTINGSwindowwidth, bg=SETTINGSbackground)
        canvas.pack()
        
        errortitle = Entry(errorroot)
        errortitle.config(font=(SETTINGSfont, SETTINGSfontsize))
        errortitle.config(bg=SETTINGSfontbackground)
        errortitle.config(fg=SETTINGSfontcolor)
        errortitle.insert(0,'POPUP TITLE')
        errortitle.pack()
        
        errormessage = Entry(errorroot)
        errormessage.config(font=(SETTINGSfont, SETTINGSfontsize))
        errormessage.config(fg=SETTINGSfontcolor)
        errormessage.config(bg=SETTINGSfontbackground)
        errormessage.insert(0,'POPUP MESSAGE')
        errormessage.pack()
        
        saveerrorbutton = tk.Button(errorroot, text="CREATE POPUP", command=errorpopupcreate, fg=SETTINGSfontcolor, bg=SETTINGSfontbackground, font=(SETTINGSfont, SETTINGSfontsize))
        saveerrorbutton.pack()
        
        errorroot.mainloop()
    
       
#warning
    if commandinput == "popup create /warning":
    

        def warningpopupcreate():
            warningroot.withdraw()
            titlewarning = warningtitle.get()
            messagewarning = warningmessage.get()
            messagebox.showwarning(titlewarning, messagewarning)

        warningroot = tk.Tk()
        warningroot.config(bg=SETTINGSbackground)
    
        createwarninglabel1 = tk.Label(warningroot, text="COMMAND BAR V2")
        createwarninglabel1.pack()
    
        createwarninglabel2 = tk.Label(warningroot, text="POPUP CREATE /WARNING")
        createwarninglabel2.pack()
    
        canvas = tk.Canvas(warningroot, height=SETTINGSwindowheight, width=SETTINGSwindowwidth, bg=SETTINGSbackground)
        canvas.pack()
        
        warningtitle = Entry(warningroot)
        warningtitle.config(font=(SETTINGSfont, SETTINGSfontsize))
        warningtitle.config(bg=SETTINGSfontbackground)
        warningtitle.config(fg=SETTINGSfontcolor)
        warningtitle.insert(0,'POPUP TITLE')
        warningtitle.pack()
            
        warningmessage = Entry(warningroot)
        warningmessage.config(font=(SETTINGSfont, SETTINGSfontsize))
        warningmessage.config(fg=SETTINGSfontcolor)
        warningmessage.config(bg=SETTINGSfontbackground)
        warningmessage.insert(0,'POPUP MESSAGE')
        warningmessage.pack()
        
        savewarningbutton = tk.Button(warningroot, text="CREATE POPUP", command=warningpopupcreate, fg=SETTINGSfontcolor, bg=SETTINGSfontbackground, font=(SETTINGSfont, SETTINGSfontsize))
        savewarningbutton.pack()
        
        warningroot.mainloop()
      
#info
    if commandinput == "popup create /information":
    

        def informationpopupcreate():
            inforoot.withdraw()
            titleinfo = infotitle.get()
            messageinfo = infomessage.get()
            messagebox.showinfo(titleinfo, messageinfo)

        inforoot = tk.Tk()
        inforoot.config(bg=SETTINGSbackground)

        createinfolabel1 = tk.Label(inforoot, text="COMMAND BAR V2")
        createinfolabel1.pack()
    
        createinfolabel2 = tk.Label(inforoot, text="POPUP CREATE /INFORMATION")
        createinfolabel2.pack()
    
        canvas = tk.Canvas(inforoot, height=SETTINGSwindowheight, width=SETTINGSwindowwidth, bg=SETTINGSbackground)
        canvas.pack()
        
        infotitle = Entry(inforoot)
        infotitle.config(font=(SETTINGSfont, SETTINGSfontsize))
        infotitle.config(bg=SETTINGSfontbackground)
        infotitle.config(fg=SETTINGSfontcolor)
        infotitle.insert(0,'POPUP TITLE')
        infotitle.pack()
            
        infomessage = Entry(inforoot)
        infomessage.config(font=(SETTINGSfont, SETTINGSfontsize))
        infomessage.config(fg=SETTINGSfontcolor)
        infomessage.config(bg=SETTINGSfontbackground)
        infomessage.insert(0,'POPUP MESSAGE')
        infomessage.pack()
        
        saveinfobutton = tk.Button(inforoot, text="CREATE POPUP", command=informationpopupcreate, fg=SETTINGSfontcolor, bg=SETTINGSfontbackground, font=(SETTINGSfont, SETTINGSfontsize))
        saveinfobutton.pack()
        
        inforoot.mainloop()
#question
    if commandinput == "popup create /question":
        
       
        
       
        
       questionroot = tk.Tk()
       questionroot.config(bg=SETTINGSbackground)
    
            
       def questionpopupcreate():
            questionroot.withdraw()
        
            def YESNO():
                questionoptionroot.withdraw()
                titlequestion = questiontitle.get()
                messsagequestion = questionmessage.get()
                messagebox.askyesno(titlequestion, messsagequestion)
            
            def OKCANCEL():
                questionoptionroot.withdraw()
                titlequestion = questiontitle.get()
                messagequestion = questionmessage.get()
                messagebox.askokcancel(titlequestion, messagequestion)
            
            def RETRYCANCEL():
                questionoptionroot.withdraw()
                titlequestion = questiontitle.get()
                messagequestion = questionmessage.get()
                messagebox.askretrycancel(titlequestion, messagequestion)
            
            def YESNOCANCEL():
                questionoptionroot.withdraw()
                titlequestion = questiontitle.get()
                messagequestion = questionmessage.get()
                messagebox.askyesnocancel(titlequestion, messagequestion)
            
            questionoptionroot = tk.Tk()
            questionoptionroot.config(bg=SETTINGSbackground)
        
            optionlabel1 = tk.Label(questionoptionroot, text="COMMAND BAR V2")
            optionlabel1.pack()
        
            optionlabel2 = tk.Label(questionoptionroot, text="CHOOSE POPUP OPTIONS", font=("Comic Sans", 25))
            optionlabel2.pack()
        
            canvas = tk.Canvas(questionoptionroot, height=SETTINGSwindowheight, width=SETTINGSwindowwidth, bg=SETTINGSbackground)
            canvas.pack()
            
            questionoptionyesno = tk.Button(questionoptionroot, text="YES/NO", font=(SETTINGSfont, SETTINGSfontsize), command=YESNO, fg=SETTINGSfontcolor, bg=SETTINGSfontbackground)
            questionoptionyesno.pack()
            
            questionoptionokcancel = tk.Button(questionoptionroot, text="OK/CANCEL", font=(SETTINGSfont, SETTINGSfontsize),command=OKCANCEL, fg=SETTINGSfontcolor, bg=SETTINGSfontbackground)
            questionoptionokcancel.pack()
            
            questionoptionretrycancel = tk.Button(questionoptionroot, text="RETRY/CANCEL", font=(SETTINGSfont, SETTINGSfontsize), command=RETRYCANCEL,fg=SETTINGSfontcolor, bg=SETTINGSfontbackground)
            questionoptionretrycancel.pack()
            
            questionoptionyesnocancel = tk.Button(questionoptionroot, text="YES/NO/CANCEL", font=(SETTINGSfont, SETTINGSfontsize), command=YESNOCANCEL, fg=SETTINGSfontcolor, bg=SETTINGSfontbackground)
            questionoptionyesnocancel.pack()
            
            questionoptionroot.mainloop()
            
            
            
            questionlabel1 = tk.Label(questionroot, text="COMMAND BAR V2")
            questionlabel1.pack()
        
       questionlabel2 = tk.Label(questionroot, text="POPUP CREATE /QUESTION")
       questionlabel2.pack()
        
       canvas = tk.Canvas(questionroot, height=SETTINGSwindowheight, width=SETTINGSwindowwidth, bg=SETTINGSbackground)
       canvas.pack()
    
       questiontitle = Entry(questionroot)
       questiontitle.config(font=(SETTINGSfont, SETTINGSfontsize))
       questiontitle.config(bg=SETTINGSfontbackground)
       questiontitle.config(fg=SETTINGSfontcolor)
       questiontitle.insert(0, "POPUP TITLE")
       questiontitle.pack()
   
       questionmessage = Entry(questionroot)
       questionmessage.config(font=(SETTINGSfont, SETTINGSfontsize))
       questionmessage.config(bg=SETTINGSfontbackground)
       questionmessage.config(fg=SETTINGSfontcolor)
       questionmessage.insert(0, "POPUP MESSAGE")
       questionmessage.pack()
    
       questionsavebutton = tk.Button(questionroot, text="NEXT", command=questionpopupcreate)
       questionsavebutton.pack()
    
       questionroot.mainloop()
#easter egg
    if commandinput == "selfdestruct":
        messagebox.showwarning("SELF DESTRUCT", "You asked for it (:")
        destructlabel=tk.Label(text="SELF DESTRUCT")
        destructlabel.pack()
        destructcanvas=tk.Canvas(root, height=1000, width=1000)
        destructcanvas.pack()
    if commandinput == "fun":
        funroot = tk.Tk()
        funlabel = tk.Label(funroot, text="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        funlabel.pack()
        funroot.mainloop()
#info

    if commandinput == "viewinfo":
        messagebox.showinfo("COMMAND BAR V2", "Cmdbar V2. Created by Misha. Product ID: mcb1#0")
#file
#file create
    if commandinput == "file /create":
        
        filecroot = tk.Tk()
        filecroot.config(bg=SETTINGSbackground)
    
        clabel1 = tk.Label(filecroot, text="COMMAND BAR V2")
        clabel1.pack()
    
        clabel2 = tk.Label(filecroot, text="FILE /CREATE")
        clabel2.pack()
    
        canvas = tk.Canvas(filecroot, height=SETTINGSwindowheight, width=SETTINGSwindowwidth, bg=SETTINGSbackground)
        canvas.pack()
    
        FILECNAME = Entry(filecroot, bg=SETTINGSfontbackground, fg=SETTINGSfontcolor, font=(SETTINGSfont, SETTINGSfontsize))
        FILECNAME.insert(0, "FILENAME")
        FILECNAME.pack()
    
        def FILECREATE():
            filecroot.withdraw()
            print("file created")
        
            filecname = FILECNAME.get()
        
            with open(filecname, 'a') as f:
                for line in "---FILE CREATED BY COMMAND BAR V2---":
                    f.write(line)
    
        filecbutton = tk.Button(filecroot, text="CREATE FILE", command=FILECREATE, fg=SETTINGSfontcolor, bg=SETTINGSfontbackground, font=(SETTINGSfont, SETTINGSfontsize))
        filecbutton.pack()
    
        filecroot.mainloop()
#file read
    if commandinput == "file /read":
        
        filerroot = tk.Tk()
        filerroot.config(bg=SETTINGSbackground)
        
        rlabel1 = tk.Label(filerroot, text="COMMAND BAR V2")
        rlabel1.pack()
        
        rlabel2 = tk.Label(filerroot, text="FILE /READ")
        rlabel2.pack()
        
        canvas = tk.Canvas(filerroot, height=SETTINGSwindowheight, width=SETTINGSwindowwidth, bg=SETTINGSbackground)
        canvas.pack()
        
        FILERNAME = Entry(filerroot, bg=SETTINGSfontbackground, fg=SETTINGSfontcolor, font=(SETTINGSfont, SETTINGSfontsize))
        FILERNAME.insert(0, "FILE NAME")
        FILERNAME.pack()
        
        def FILEREAD():
            print("file read")
            
            filername = FILERNAME.get()
            
            with open(filername, 'r') as f:
                filertext = f.read()
                f.close()
                
            filerroot.withdraw()
            
            fileREADroot = tk.Tk()
            
            COMMANDBAR2LABELR = tk.Label(fileREADroot, text="COMMAND BAR 2")
            COMMANDBAR2LABELR.pack()
            
            COMMANDRLABEL = tk.Label(fileREADroot, text="FILE /READ")
            COMMANDRLABEL.pack()
            
            READLABEL1 = tk.Label(fileREADroot, text="FILE TEXT:", font=(SETTINGSfont, 11))
            READLABEL1.pack()
            

            READlabel = tk.Label(fileREADroot, text=filertext, font=(SETTINGSfont, 11))            
            READlabel.pack()
            
            print(filertext)
            
            fileREADroot.mainloop()
        
            
            
        filereadbutton = tk.Button(filerroot, text="READ FILE", command=FILEREAD, fg=SETTINGSfontcolor, bg=SETTINGSfontbackground, font=(SETTINGSfont, SETTINGSfontsize))
        filereadbutton.pack()
        
        filerroot.mainloop()
           
#file write
    if commandinput == "file /write":
        
          
        filewroot = tk.Tk()
        filewroot.config(bg=SETTINGSbackground)
 
        wlabel1 = tk.Label(filewroot, text="COMMAND BAR V2")
        wlabel1.pack()
 
        wlabel2 = tk.Label(filewroot, text="FILE /WRITE")
        wlabel2.pack()
 
        canvas = tk.Canvas(filewroot, height=SETTINGSwindowheight, width=SETTINGSwindowwidth, bg=SETTINGSbackground)
        canvas.pack()
     
        FILENAMEw = Entry(filewroot, bg=SETTINGSfontbackground, fg=SETTINGSfontcolor, font=(SETTINGSfont, SETTINGSfontsize))
        FILENAMEw.insert(0, "FILE NAME")
        FILENAMEw.pack()
 
        FILETEXTw = Entry(filewroot, bg=SETTINGSfontbackground, fg=SETTINGSfontcolor, font=(SETTINGSfont, SETTINGSfontsize))
        FILETEXTw.insert(0, "FILE TEXT")
        FILETEXTw.pack()
 
        def FILEWRITE():
     
            filewroot.withdraw()
            filewname = FILENAMEw.get()
            filewtext = FILETEXTw.get()
     
            with open(filewname, 'a') as f:
                for line in filewtext:
                    f.write(line)
             
                print("written in file")
 
        filewbutton1 = tk.Button(filewroot, text="WRITE", command=FILEWRITE, fg=SETTINGSfontcolor, bg=SETTINGSfontbackground, font=(SETTINGSfont, SETTINGSfontsize))
        filewbutton1.pack()
 
        filewroot.mainloop()          
                  
                    
#file clear
    if commandinput == "file /clear":
        CLEARROOT = tk.Tk()
        CLEARROOT.config(bg=SETTINGSbackground)
        
        FClabel1 = tk.Label(CLEARROOT, text="COMMAND BAR V2")
        FClabel1.pack()
        
        FClabel2 = tk.Label(CLEARROOT, text="FILE /CLEAR")
        FClabel2.pack()
        
        canvas = tk.Canvas(CLEARROOT, height=SETTINGSwindowheight, width=SETTINGSwindowwidth, bg=SETTINGSbackground)
        canvas.pack()
        
        FILECLEARNAME = Entry(CLEARROOT, bg=SETTINGSfontbackground, fg=SETTINGSfontcolor, font=(SETTINGSfont, SETTINGSfontsize))
        FILECLEARNAME.insert(0, "FILE NAME")
        FILECLEARNAME.pack()
        
        def CLEARFILE():
            print("File cleared")
            fileclearname = FILECLEARNAME.get()
            CLEARROOT.withdraw()
            
            file = open(fileclearname,"r+")
            file. truncate(0)
        
        CLEARBUTTON = tk.Button(CLEARROOT, text="CLEAR FILE", command=CLEARFILE, fg=SETTINGSfontcolor, bg=SETTINGSfontbackground, font=(SETTINGSfont, SETTINGSfontsize))
        CLEARBUTTON.pack()
        
        CLEARROOT.mainloop()
        
#settings

#template change
    if commandinput == "settings /templatechange":
        templateroot = tk.Tk()
        templateroot.config(bg=SETTINGSbackground)
    
        TEMPLATECHANGELABEL1 = tk.Label(templateroot, text="COMMAND BAR V2")
        TEMPLATECHANGELABEL1.pack()
        
        TEMPLATECHANGELABEL2 = tk.Label(templateroot, text="SETTINGS /TEMPLATECHANGE")
        TEMPLATECHANGELABEL2.pack()
        
        canvas = tk.Canvas(templateroot, height=SETTINGSwindowheight, width=SETTINGSwindowwidth)
        canvas.pack()
        
        TCFILENAME = Entry(templateroot, bg=SETTINGSfontbackground, fg=SETTINGSfontcolor, font=(SETTINGSfont, SETTINGSfontsize))
        TCFILENAME.insert(0, "NEW TEMPLATE")
        TCFILENAME.pack()
        
        def CHANGETEMPLATE():
            templateroot.withdraw()
            print("template changed")
            file = open("template.py","r+")
            file. truncate(0)
            
            newtemplate = TCFILENAME.get()
    
            with open("template.py", 'a') as f:
                for line in newtemplate:
                    f.write(line)
                    
                f.close()
        
        CHANGEBUTTON = tk.Button(templateroot, text="CHANGE TEMPLATE", command=CHANGETEMPLATE, fg=SETTINGSfontcolor, bg=SETTINGSfontbackground, font=(SETTINGSfont, SETTINGSfontsize))
        CHANGEBUTTON.pack()
    
        templateroot.mainloop()
                
#theme change
    if commandinput == "settings /themechange":
   
        themeroot = tk.Tk()
        themeroot.config(bg=SETTINGSbackground)

        themelabel1 = tk.Label(themeroot, text="COMMAND BAR V2")
        themelabel1.pack()

        themelabel2 = tk.Label(themeroot, text="SETTINGS /THEME")
        themelabel2.pack()
        
        importantthemelabel = tk.Label(themeroot, text="NOTE: NOT CHANGING THE OPTIONS WILL BREAK THE APPLICATION.")
        importantthemelabel.pack()
        
        canvas = tk.Canvas(themeroot, height=SETTINGSwindowheight, width=SETTINGSwindowwidth, bg=SETTINGSbackground)
        canvas.pack()
        
        bgcolorentry = Entry(themeroot, bg=SETTINGSfontbackground, fg=SETTINGSfontcolor, font=(SETTINGSfont, SETTINGSfontsize))
        bgcolorentry.insert(0, "BACKGROUND")
        bgcolorentry.pack()
        
        fontcolorentry = Entry(themeroot, bg=SETTINGSfontbackground, fg=SETTINGSfontcolor, font=(SETTINGSfont, SETTINGSfontsize))
        fontcolorentry.insert(0, "FONT COLOR")
        fontcolorentry.pack()
    
        fontsizeentry = Entry(themeroot, bg=SETTINGSfontbackground, fg=SETTINGSfontcolor, font=(SETTINGSfont, SETTINGSfontsize))
        fontsizeentry.insert(0, "FONT SIZE")
        fontsizeentry.pack()
        
        fontbackgroundentry = Entry(themeroot, bg=SETTINGSfontbackground, fg=SETTINGSfontcolor, font=(SETTINGSfont, SETTINGSfontsize))
        fontbackgroundentry.insert(0, "FONT BACKGROUND")
        fontbackgroundentry.pack()
    
        fontentry = Entry(themeroot, bg=SETTINGSfontbackground, fg=SETTINGSfontcolor, font=(SETTINGSfont, SETTINGSfontsize))
        fontentry.insert(0, "FONT")
        fontentry.pack()
    
        wheightentry = Entry(themeroot, bg=SETTINGSfontbackground, fg=SETTINGSfontcolor, font=(SETTINGSfont, SETTINGSfontsize))
        wheightentry.insert(0, "WINDOW HEIGHT")
        wheightentry.pack()
    
        wwidthentry = Entry(themeroot, bg=SETTINGSfontbackground, fg=SETTINGSfontcolor, font=(SETTINGSfont, SETTINGSfontsize))
        wwidthentry.insert(0, "WINDOW WIDTH")
        wwidthentry.pack()
    
        def EDITSETTINGS():
            editbackground = bgcolorentry.get()
            editfontcolor = fontcolorentry.get()
            editfontsize = fontsizeentry.get()
            editfontbackground = fontbackgroundentry.get()
            editfont = fontentry.get()
            editwheight = wheightentry.get()
            editwwidth = wwidthentry.get()
        
            #background
            with open('CBV2background', 'r+') as f:
                    
                    f.truncate(0)
                    
                    for line in editbackground:
                        f.write(line)
                   
                    #fontcolor                
            with open('CBV2fontcolor', 'r+') as f:
        
                f.truncate(0)
        
                for line in editfontcolor:
                    f.write(line)
                    

    #fontbackground
            with open('CBV2fontbackground', 'r+') as f:
        
                f.truncate(0)
        
                for line in editfontbackground:
                    f.write(line)
                   
    #font
            with open('CBV2font', 'r+') as f:
        
                f.truncate(0)
        
                for line in editfont:
                    f.write(line)
                   
    
    #fontsize
            with open('CBV2fontsize', 'r+') as f:
        
                f.truncate(0)
        
                for line in editfontsize:
                    f.write(line)
                    
    
    #wwidth
            with open('CBV2windowwidth', 'r+') as f:
            
                f.truncate(0)
        
                for line in editwwidth:
                    f.write(line)
                    
    
    
    #wheight
            with open('CBV2windowheight', 'r+') as f:
        
                f.truncate(0)
        
                for line in editwheight:
                    f.write(line)
                   
                    
                themeroot.withdraw()

        themesavebutton = tk.Button(themeroot, text="SAVE", command=EDITSETTINGS, fg=SETTINGSfontcolor, bg=SETTINGSfontbackground, font=(SETTINGSfont, SETTINGSfontsize))
        themesavebutton.pack()

        themeroot.mainloop()

#guicreate

    if commandinput == "guicreate":
        rootCREATE=tk.Tk()
        rootCREATE.config(bg=SETTINGSbackground)      
        GClabel1 = tk.Label(rootCREATE, text="COMMAND BAR V2")
        GClabel1
        
        GClabel2 = tk.Label(rootCREATE, text="GUICREATE")
        GClabel2.pack()
        
        canvas=tk.Canvas(rootCREATE, height=SETTINGSwindowheight, width=SETTINGSwindowwidth,  bg=SETTINGSbackground)
        canvas.pack()
        
        heightINPUT = Entry(rootCREATE, bg=SETTINGSfontbackground, fg=SETTINGSfontcolor, font=(SETTINGSfont, SETTINGSfontsize))
        heightINPUT.insert(0,"GUI HEIGHT")
        heightINPUT.pack()
        
        widthINPUT = Entry(rootCREATE, bg=SETTINGSfontbackground, fg=SETTINGSfontcolor, font=(SETTINGSfont, SETTINGSfontsize))
        widthINPUT.insert(0, "GUI WIDTH")
        widthINPUT.pack()
        
        def CREATEGUI():
            rootCREATE.withdraw()
            createguiroot = tk.Tk()
            
            canvashieght = heightINPUT.get()
            canvaswidth = widthINPUT.get()
            
            canvasCREATE = tk.Canvas(createguiroot, height=canvashieght, width=canvaswidth)
            canvasCREATE.pack()
            createguiroot.mainloop()
        
        createGUIbutton = tk.Button(rootCREATE, text="CREATE GUI", command=CREATEGUI, fg=SETTINGSfontcolor, bg=SETTINGSfontbackground, font=(SETTINGSfont, SETTINGSfontsize))
        createGUIbutton.pack()
        
        rootCREATE.mainloop()
        
#calculator

    if commandinput == "calculator":
        CALCULATORROOT = tk.Tk()
        CALCULATORROOT.config(bg=SETTINGSbackground)
    
        crlabel1 = tk.Label(CALCULATORROOT, text="COMMAND BAR V2")
        crlabel1.pack()
    
        crlabel2 = tk.Label(CALCULATORROOT, text="CALCULATOR")
        crlabel2.pack()
    
        canvas = tk.Canvas(CALCULATORROOT, height=SETTINGSwindowheight, width=SETTINGSwindowwidth, bg=SETTINGSbackground)
        canvas.pack()
        
        equationinput = Entry(CALCULATORROOT, bg=SETTINGSfontbackground, fg=SETTINGSfontcolor, font=(SETTINGSfont, SETTINGSfontsize))
        equationinput.insert(0, "EQUATION")
        equationinput.pack()
    
        def CALCULATEANSWER():
            CALCULATORROOT.withdraw()
            
            equationc = equationinput.get()
            REALequationanswer = eval(equationc)
            
            messagebox.showinfo("CALCULATOR", (equationc,"=",REALequationanswer))    
            
        calculatebutton = tk.Button(CALCULATORROOT, text="CALCULATE", command=CALCULATEANSWER, fg=SETTINGSfontcolor, bg=SETTINGSfontbackground, font=(SETTINGSfont, SETTINGSfontsize))
        calculatebutton.pack()
    
        CALCULATORROOT.mainloop()
        
        #plot
    if commandinput == "plot /create":
     plotRoot = tk.Tk()
     plotRoot.config(bg=SETTINGSbackground)
     plotLabel1 = tk.Label(plotRoot, text="COMMAND BAR V2", font=(SETTINGSfont, SETTINGSfontsize), fg=SETTINGSfontcolor, bg=SETTINGSfontbackground)
     plotLabel1.pack()

     plotLabel2 = tk.Label(plotRoot, text="PLOTCREATE", font=(SETTINGSfont, SETTINGSfontsize), fg=SETTINGSfontcolor, bg=SETTINGSfontbackground)
     plotLabel2.pack()
     
     canvas = tk.Canvas(plotRoot, height=SETTINGSwindowheight, width=SETTINGSwindowwidth, bg=SETTINGSbackground)
     canvas.pack()
     
     y_input = Entry(plotRoot, bg=SETTINGSfontbackground, fg=SETTINGSfontcolor, font=(SETTINGSfont, SETTINGSfontsize))
     y_input.insert(0, "Y")
     y_input.pack()
     
     x_input = Entry(plotRoot, bg=SETTINGSfontbackground, fg=SETTINGSfontcolor, font=(SETTINGSfont, SETTINGSfontsize))
     x_input.insert(0, "X")
     x_input.pack()

    def plot():

        

        plotRoot.withdraw()
#        he figure that will contain the plot
        fig = Figure(figsize = (5, 5),
				dpi = 100)
    
        createPlotRoot = tk.Tk()
    
        real_y = int(x_input.get())
        real_x = int(y_input.get())
        #ist of squares
        y = [i**real_y for i in range(real_x)]

	# adding the subplot
        plot1 = fig.add_subplot(111)

  

	# plotting the graph
        plot1.plot(y)

	# creating the Tkinter canvas
	# containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig,
							master = createPlotRoot)
        canvas.draw()

	# placing the canvas on the Tkinter window
        canvas.get_tk_widget().pack()

	# creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas,
								createPlotRoot)
        toolbar.update()

	# placing the toolbar on the Tkinter window
        canvas.get_tk_widget().pack()

        createPlotRoot.mainloop()

    createPlotButton = tk.Button(plotRoot, text="CREATE PLOT", command=plot, fg=SETTINGSfontcolor, bg=SETTINGSfontbackground, font=(SETTINGSfont, SETTINGSfontsize))
    createPlotButton.pack()

    plotRoot.mainloop()
    
def helpbutton():
    helproot=tk.Tk()
    
    helptext = tk.Label(helproot, text=READMETEXT)
    helptext.pack()
    
    helproot.mainloop()
    
root=tk.Tk()
root.config(bg=SETTINGSbackground)

labelmain = tk.Label(root, text="COMMAND BAR V2", bg=SETTINGSbackground)
labelmain.pack()


canvas = tk.Canvas(root, height=SETTINGSwindowheight, width=SETTINGSwindowwidth, bg=SETTINGSbackground)
canvas.pack()

mainframe = tk.Frame(root, bg=SETTINGSbackground)
mainframe.place(relwidth=0.8, relx=0.1, rely=0.1)


button1 = tk.Button(root, text="Run", padx=10, pady=5, command=inputwidget, fg=SETTINGSfontcolor, bg=SETTINGSfontbackground, font=(SETTINGSfont, SETTINGSfontsize))
button1.pack()

button2 = tk.Button(root, text="Help", padx=10, pady=5, command=helpbutton, fg=SETTINGSfontcolor, bg=SETTINGSfontbackground, font=(SETTINGSfont, SETTINGSfontsize))
button2.pack()



entry = Entry(mainframe)
entry.config(font=(SETTINGSfont, SETTINGSfontsize))
entry.config(bg=SETTINGSfontbackground)
entry.config(fg=SETTINGSfontcolor)
entry.pack()



root.mainloop()

print("Session ended.")
