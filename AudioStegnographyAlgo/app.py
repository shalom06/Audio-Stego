from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *

from AudioStegnographyAlgo.LSBAudioStego import LSBAudioStego
from AudioStegnographyAlgo.PhaseEncodingAudioStego import PhaseEncodingAudioStego

root = Tk()


# create window using from in Tkinter
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)
        # reference to the master widget, which is the tk window
        self.master = master


        self.init_window()

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("Audio Steganography")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)
        self.drawEnocoding()
        self.drawDecoding()

    def drawEnocoding(self):
        # encode Label
        self.encodeVar = StringVar()
        self.encodelabel = Label(root, textvariable=self.encodeVar)
        self.encodelabel.place(x=10, y=10)
        self.encodeVar.set("Encoding ")
        # select algo
        self.optionsVar = StringVar()
        self.optionsVar.set("Least Significant Bit")  # default value

        self.encodingOptionsMenu = OptionMenu(root, self.optionsVar, "Least Significant Bit", "Phase Coding")
        self.encodingOptionsMenu.place(x=10, y=50)
        # creating a button instance
        self.selectFileButton = Button(self, text="Select File  To Encode", command=self.selectFile)
        self.selectFileButton.place(x=10, y=100)

        # file location label
        self.var = StringVar()
        self.label = Label(root, textvariable=self.var, relief=RAISED)
        self.label.place(x=10, y=130)
        # placing the button on my window

        # entry box
        self.entryText = Entry(root)
        self.entryText.place(x=10, y=180)
        self.entryText.insert(0, "Enter String to encode ")
        # encode Button
        self.encodeButton = Button(self, text="Encode", command=self.encode)
        self.encodeButton.place(x=10, y=220)

        # encoded  location label
        self.enocdedLocation = StringVar()
        self.locationOfEncodeFile = Label(root, textvariable=self.enocdedLocation)
        self.locationOfEncodeFile.place(x=10, y=280)

    def drawDecoding(self):
        # decode Label
        self.decodeVar = StringVar()
        self.decodelabel = Label(root, textvariable=self.decodeVar)
        self.decodelabel.place(x=500, y=10)
        self.decodeVar.set("Decoding ")

        # select algo
        self.decodeOptionsVar = StringVar()
        self.decodeOptionsVar.set("Least Significant Bit")  # default value

        self.decodingOptionsMenu = OptionMenu(root, self.decodeOptionsVar, "Least Significant Bit", "Phase Coding")
        self.decodingOptionsMenu.place(x=500, y=50)
        # creating a button instance
        self.selectFileDecodeButton = Button(self, text="Select  File To Decode ", command=self.selectFileDecode)
        self.selectFileDecodeButton.place(x=500, y=100)
        #
        # file location label
        self.decodeFileVar = StringVar()
        self.decodeFileLabel = Label(root, textvariable=self.decodeFileVar, relief=RAISED)
        self.decodeFileLabel.place(x=500, y=140)

        self.decodeButton = Button(self, text="Decode", command=self.decode)
        self.decodeButton.place(x=500, y=200)
        #
        # decoded text label
        self.decodedString = StringVar()
        self.decodedStringlabel = Label(root, textvariable=self.decodedString, font=(None, 40))
        self.decodedStringlabel.place(x=500, y=350)

    def client_exit(self):
        exit()

    def selectFile(self):
        # file selection
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("jpeg files", "*.wav"), ("all files", "*.*")))
        self.fileSelected = root.filename
        self.var.set(root.filename)

    def selectFileDecode(self):
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("jpeg files", "*.wav"), ("all files", "*.*")))
        self.fileSelcetedForDecode = root.filename
        self.decodeFileVar.set(root.filename)

    def encode(self):
        # select algo to encode
        if self.optionsVar.get() == "Least Significant Bit":
            algo = LSBAudioStego()
        else:
            algo = PhaseEncodingAudioStego()
        result = algo.encodeAudio(self.fileSelected, self.entryText.get())

        self.enocdedLocation.set(result)

    def decode(self):
        # select algo to decode
        if self.decodeOptionsVar.get() == "Least Significant Bit":
            algo = LSBAudioStego()
        else:
            algo = PhaseEncodingAudioStego()

        result = algo.decodeAudio(self.fileSelcetedForDecode)
        self.decodedString.set(result)


# resolution
root.geometry("1000x700")

# creation of an instance of window
app = Window(root)

# mainloop
root.mainloop()
