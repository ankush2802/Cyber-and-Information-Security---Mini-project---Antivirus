from tkinter import *
from tkinter import filedialog
import random
import os
import time
import engine


os.startfile("C:\\Users\\student\\Desktop\\Antivirus\\src\\real-time-protection_setting.bat")
#os.system('cmd /c "real-time-protection_setting.bat"')


window = Tk()

window.title("Cyber and Information Security Mini Project")
window.geometry('1100x600')
window.maxsize("1100","600")
window.minsize("1100","600")

nj = Frame(window, width=1100, height = 600)
nj.pack()
nj.pack_propagate(0)

def mainFrameNj():

    global opring
    global quickScanImg
    global junkFileRemoverImg
    global ramBoosterImg
    global photoScan
    global nj

    nj.destroy()

    nj = Frame(window, width=1100, height = 600)
    nj.pack()
    nj.pack_propagate(0)


    def junkFileRemoverFunc():
        ri = engine.CacheFileRemover
        ri()

    def ramBoosterFunc():
        ri = engine.ramBooster
        ri()

    def customScanFunc():
        source_path = filedialog.askdirectory(title='Select the Parent Directory')
        print(source_path)
        ri = engine.virusScanner
        ri(source_path)

    def writeFile(write):
        switch_check = open("C:\\Users\\student\\Desktop\\Antivirus\\src\\real-time_switch.blink","w")
        switch_check.write(write)
        switch_check.close()

    def AV_switch():
        switch_check = open("C:\\Users\\student\\Desktop\\Antivirus\\src\\real-time_switch.blink","r")
        Pos = switch_check.readline()
        switch_check.close()    
    

        if Pos == 1 or Pos == "1" :
            print(Pos)
            writeFile("0")
        
            tls.configure(image = photog)
        
    
        elif Pos == 0 or Pos == "0":
            print(Pos)
            writeFile("1")
        
            tls.configure(image = photoi)

    opring = 5

    def buleAnimation_():
        global opring

        buleAnimationPlus00.configure(image = buleAnimationPlusList[opring])


        if opring == 0:
            opring = 5

        opring -= 1

        buleAnimationPlus00.after(200,buleAnimation_)



    photoi = PhotoImage(file = "C:\\Users\\student\\Desktop\\Antivirus\\res\\0.png").subsample(3,3)
    photog = PhotoImage(file = "C:\\Users\\student\\Desktop\\Antivirus\\res\\0 a.png").subsample(3,3)
    photoScan = PhotoImage(file = "C:\\Users\\student\\Desktop\\Antivirus\\res\\scan l.png").subsample(4,4)
    junkFileRemoverImg = PhotoImage( file = "C:\\Users\\student\\Desktop\\Antivirus\\res\\junk file remover.png").subsample(4,4)
    quickScanImg = PhotoImage(file ="C:\\Users\\student\\Desktop\\Antivirus\\res\\quick scan.png").subsample(4,4)
    ramBoosterImg = PhotoImage(file = "C:\\Users\\student\\Desktop\\Antivirus\\res\\ram booster.png").subsample(4,4)

    buleAnimationPlus0 = PhotoImage( file = "C:\\Users\\student\\Desktop\\Antivirus\\res\\blue ani\\0.png").subsample(21,21)
    buleAnimationPlus1 = PhotoImage( file = "C:\\Users\\student\\Desktop\\Antivirus\\res\\blue ani\\1.png").subsample(21,21)
    buleAnimationPlus2 = PhotoImage( file = "C:\\Users\\student\\Desktop\\Antivirus\\res\\blue ani\\2.png").subsample(21,21)
    buleAnimationPlus3 = PhotoImage( file = "C:\\Users\\student\\Desktop\\Antivirus\\res\\blue ani\\3.png").subsample(21,21)
    buleAnimationPlus4 = PhotoImage( file = "C:\\Users\\student\\Desktop\\Antivirus\\res\\blue ani\\4.png").subsample(21,21)
    buleAnimationPlus5 = PhotoImage( file = "C:\\Users\\student\\Desktop\\Antivirus\\res\\blue ani\\5.png").subsample(21,21)


    buleAnimationPlusList = [buleAnimationPlus0,buleAnimationPlus1,buleAnimationPlus2,buleAnimationPlus3,buleAnimationPlus4,buleAnimationPlus5]




    MainLabel = Label(nj, text = "PC Antivirus", font = "Times 30 bold")
    MainLabel.pack(side = TOP, pady = 20)

    tls = Button(nj, text = 'Click Me !', image = photoi, bd=0, command=AV_switch)
    tls.pack(side = TOP, pady = 0)
    RealMainLabel = Label(nj, text = "Real Time Protection", font = "Times 20 bold")
    RealMainLabel.place( x = 420 , y = 330)

    quickScan = Button(nj, image = quickScanImg, bd = 0, command = quickScanFrame)
    quickScan.place( x = 90 , y = 410)
    QuickMainLabel = Label(nj, text = "Quick Scan", font = "Times 15 bold")
    QuickMainLabel.place( x = 105 , y = 540)
    
    fscan = Button(nj, image = photoScan, bd = 0, command = customScanFunc)
    fscan.place(x = 350 , y = 410)
    FolderMainLabel = Label(nj, text = "Folder Scanner", font = "Times 15 bold")
    FolderMainLabel.place( x = 350 , y = 540)

    junkFileRemover = Button(nj, image = junkFileRemoverImg ,bd = 0, command = junkFileRemoverFunc)
    junkFileRemover.place( x = 610 , y = 410)
    JunkMainLabel = Label(nj, text = "Cache File Remover", font = "Times 15 bold")
    JunkMainLabel.place( x = 600 , y = 540)

    ramBooster = Button(nj, image = ramBoosterImg , bd = 0, command = ramBoosterFunc)
    ramBooster.place( x = 870 , y = 410)
    TaskMainLabel = Label(nj, text = "Task Killer", font = "Times 15 bold")
    TaskMainLabel.place( x = 900 , y = 540)

    buleAnimationPlus00 = Label(nj, image = buleAnimationPlus0)
    buleAnimationPlus00.place(x = 50, y = 10)

    buleAnimation_()


def quickScanFrame():
    global nj
    global backButtonImg
    global prog0
    global prog1
    global prog2
    global prog3
    global prog4
    global prog5
    global io
    global ranHashShower
    global samB
    global rMVirus

    with open("C:\\Users\\student\\Desktop\\Antivirus\\src\\DataBase\\HashDataBase\\Sha256\\virusHash.txt", "r") as nr:
        samB = nr.readlines()
        nr.close()



    nj.destroy()

    nj = Frame(window, width=1100, height = 600)
    nj.pack()
    nj.pack_propagate(0)

    io = 0

    def removeVirusBtn():
        try : 
            with open("switch_virusscanner.bb","r") as bb:
                io = list(bb.readlines())
                bb.close()
        except:pass

        try:
            for i in io:
                i = i[0:len(i)-1]
                print(i," Removed")
                os.remove(i)
        except:pass


    def progressBarAni():
        global io
        
        progLabel.configure(image = progList[io])

        io += 1

        

        id = progLabel.after(500, progressBarAni)

        if io == 5:
            io = 0
            try : 
                with open("switch_io.bb","r") as nri:
                    xxc = nri.read()
                    nri.close()
                
                if xxc == "1" or xxc == 1:
                    progLabel.after_cancel(id)
            
            except:pass

    def textShower():
        global samB

        ranHashShower.configure(state='normal')
        ranHashShower.delete("1.0",END)
        ranHashShower.insert(INSERT,samB[random.randint(0,len(samB)-1)])

        id = ranHashShower.after(100, textShower)

        try : 
            with open("switch_io.bb","r") as nri:
                xxc = nri.read()
                nri.close()
                
            if xxc == "1" or xxc == 1:
                ranHashShower.after_cancel(id)
            
        except:pass

    def VirusFoundPathX():

        try:
            with open ("switch_virusscanner.bb","r") as X:
                cc = X.readlines()
                X.close()
        

            virusFoundPaths.configure(state='normal')
            virusFoundPaths.delete("1.0",END)
            virusFoundPaths.insert(INSERT,cc)


        except:pass

        id = virusFoundPaths.after(200, VirusFoundPathX)

    backButtonImg = PhotoImage(file = "C:\\Users\\student\\Desktop\\Antivirus\\res\\back button.png").subsample(4,4)
    prog0 = PhotoImage( file = "C:\\Users\\student\\Desktop\\Antivirus\\res\\progress bar\\0.png").subsample(1,3)
    prog1 = PhotoImage( file = "C:\\Users\\student\\Desktop\\Antivirus\\res\\progress bar\\1.png").subsample(1,3)
    prog2 = PhotoImage( file = "C:\\Users\\student\\Desktop\\Antivirus\\res\\progress bar\\2.png").subsample(1,3)
    prog3 = PhotoImage( file = "C:\\Users\\student\\Desktop\\Antivirus\\res\\progress bar\\3.png").subsample(1,3)
    prog4 = PhotoImage( file = "C:\\Users\\student\\Desktop\\Antivirus\\res\\progress bar\\4.png").subsample(1,3)
    prog5 = PhotoImage( file = "C:\\Users\\student\\Desktop\\Antivirus\\res\\progress bar\\5.png").subsample(1,3)
    progList = [prog0,prog1,prog2,prog3,prog4,prog5]

    bitLinkMainLabel = Label(nj, text = "Quick Scan", font = "Times 21 bold")
    bitLinkMainLabel.pack(side = TOP, pady = 20)

    backButton = Button(nj, image = backButtonImg, bd = 0, command = mainFrameNj)
    backButton.place(x = 10 , y = 10)

    progLabel = Label(nj, image = prog0)
    progLabel.place(x = 250, y = 70)


    pathLabel = Label(nj, text = "Virus Scanner", font = "Times 20 bold")
    pathLabel.place(x = 350, y = 130)

    ranHashShower = Text(nj, width=50, height=1, bd = 0, font= ('Sans Serif', 13, 'bold'),foreground="green")
    ranHashShower.place( x = 350 , y = 170)
    ranHashShower.insert(INSERT, "Write Something About Yourself")
    ranHashShower.configure(state='disabled')

    virusDetet = Label(nj, text = "Virus Found", font = "Times 20 bold")
    virusDetet.place(x = 350, y = 230)

    virusFoundPaths = Text(nj, width=100, height=10, bd = 0, font= ('Sans Serif', 13, 'bold'),foreground="red")
    virusFoundPaths.place( x = 50 , y = 290)
    virusFoundPaths.insert(INSERT, "No Virus Found")
    virusFoundPaths.configure(state='disabled')

    rMVirus = Button(nj, text = "Remove Virus", font = "Times 20 bold", command = removeVirusBtn)
    rMVirus.place(x = 350, y = 230)

    textShower()

    progressBarAni()

    os.startfile("C:\\Users\\student\\Desktop\\Antivirus\\src\\scannerStartQuick.bat")
    #os.system('cmd /c "scannerStartQuick.bat"')

    VirusFoundPathX()


    # Get the list of all files in directory tree at given path

mainFrameNj()

window.mainloop()