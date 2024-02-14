# Author: Stefan DeWolfe
# Date: 4 / 2021
# Last Modified: 2 / 14 / 2024
# import os,sys,time
class CONST():
    SEPERATOR_BAR="========================================================"
#--------------------------------------------------------------------------------------
class Interface():
    short_pause_delay = 1
    pause_delay = 1
    text_delay = 0.01# 0.03
    lineWidth = 70
    @staticmethod
    def print_there(x, y, text):
        sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (y, x, text))
        sys.stdout.flush()
    @staticmethod
    def move_cursor(x,y):
        #sys.stdout.write("\033[%d;%df" % (y, x))
        #sys.stdout.flush()
        print("\033[%d;%dH" % (y, x))
    #--------------------------------------------------------------------------------------
    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    #------------------------------------------------------------
    @staticmethod
    def wait():
        input("")
    #--------------------------------------------------------------------------------------
    @staticmethod
    def PressEntertoContinue():
        input("Press Enter to Continue...")
    @staticmethod
    def PETC():
        input(" > ")
    @staticmethod
    def space(extraLine=True):
        Interface.pprint(text="", extraLine=extraLine)
    #--------------------------------------------------------------------------------------
    @staticmethod
    def pause():
        time.sleep(Interface.pause_delay)
    @staticmethod
    def wait_for_seconds(num_secs):
        time.sleep(num_secs)
    #--------------------------------------------------------------------------------------
    @staticmethod
    def shortPause():
        time.sleep(Interface.short_pause_delay)
    #--------------------------------------------------------------------------------------
    @staticmethod
    def dialog(voice=None, text=None, wait=False, pause = True, extraLine=True):
        Interface.pprint(text="{0}: \"{1}\"".format(str(voice), str(text)), extraLine=extraLine)
        if wait: 
            Interface.PETC()
        elif pause:
            Interface.pause()
    @staticmethod
    def thought(voice=None, text=None, wait=False, extraLine=True):
        Interface.pprint(text="{0}: '{1}'".format(str(voice), str(text)), extraLine=extraLine)
        if wait: 
            Interface.PETC()
        #Interface.clear()
    @staticmethod
    def narration(text="",wait=False, pause = True, extraLine=True):
        Interface.pprint(text="{0}".format(str(text)), extraLine=extraLine)
        if wait: 
            Interface.PETC()
        elif pause:
            Interface.pause()
    @staticmethod
    def soundEffect(origin=None,text="",extraLine=True):
        if origin == None:
            Interface.pprint(text="*{0}*".format(str(text)), extraLine=extraLine)
        else:
            Interface.pprint(text="{0}: *{1}*".format(str(origin), str(text)), extraLine=extraLine)
        #Interface.clear()
    #--------------------------------------------------------------------------------------
    ''' This method prints a string all at once within a set width
    '''
    @staticmethod
    def rprint(text=None):
        if text == None: return None
        p = 0
        for i in text:
            p += 1
            sys.stdout.write('%s' % i)
            sys.stdout.flush()
            if ((p > Interface.lineWidth and i == " ") or i == "\n"):
                sys.stdout.write('\n')
                sys.stdout.flush()
                p = 0
            
        sys.stdout.write('\n')
        sys.stdout.flush()
    @staticmethod
    def rprint_there(x, y, text=None, width=None):
        if(width is not None):
            Interface.lineWidth = width
        else:
            Interface.lineWidth = 70
        Interface.move_cursor(x ,y)
        sys.stdout.flush()
        #Interface.print_there(x, y, text)
        Interface.rprint(text=text)
        Interface.lineWidth = 70
    #--------------------------------------------------------------------------------------
    ''' This method prints a string one character at a time within a set width
    '''
    @staticmethod
    def pprint(text=None, extraLine=False):
        if text == None: return None
        p = 0
        for i in text:
            if i == "\n":
                p=0
            p += 1
            if i == "\n":
                p = 0
            sys.stdout.write('%s' % i)
            sys.stdout.flush()
            time.sleep(Interface.text_delay)
            if p > Interface.lineWidth and i == " ":
                sys.stdout.write('\n')
                sys.stdout.flush()
                p = 0
        if extraLine:
            sys.stdout.write('\n')
            sys.stdout.flush()
        #Interface.clear()
        #
    #--------------------------------------------------------------------------------------
    @staticmethod
    def getAmount(prompt="Choose an option: ", confirm=False):
        while True:
            i = 0
            opt = ""
            opt = input(prompt)
            if opt ==  "" or opt == "\n":
                return 0
            try:
                i = int(opt)
                if confirm and not Interface.confirm(prompt="Are you sure you want {}? ".format(i), confirm=False):  # You said no.
                    continue
                return i
            except Exception:
                Interface.pprint(text="<\"{}\" == invalid input.  >".format(opt), extraLine=False)
                continue
    #--------------------------------------------------------------------------------------
    @staticmethod
    def chooseOption(options=[], prompt="Choose an option: ", confirm=False, split=False):
        """
        Returns index of option
        None otherwise
        """
        if options == None:
            return None
        if len(options) < 1:
            return None
        if len(options) == 1:
            return 0
        while True:
            i = 0
            #print prompt
            text = ""

            for option in options:
                i += 1
                text += "{0:2}) {1:30}".format(i, str(option))
                
                if not split:
                    text += "\n"
                elif i %3 == 0 and split:
                    text += "\n"
            print (text)
            # Interface.pprint(text=text, extraLine=False)
            opt = ""
            opt = input(prompt)
            if opt ==  "" or opt == "\n":
                return 0
            try:
                i = int(opt)-1
                if confirm and not Interface.confirm(prompt="Are you sure you want {}? ".format(options[i])):  # You said no.
                    continue
                if i < 0:
                    i = 0
                if i > len(options) -1:
                    i = len(options) -1
                    if i == -1:
                        i = 0
                return i
            except Exception:
                try:
                    if options[0][0] == options[0][0].upper():
                        opt = opt[0].upper() + opt[1:]
                    if confirm and not Interface.confirm(prompt="Are you sure you want {}? ".format(opt), confirm=False):  # You said no.
                        continue
                    return options.index(opt)
                except Exception:
                    Interface.pprint(text="<\"{}\" == invalid input.  >".format(opt), extraLine=False)
                    opt = ""
    #--------------------------------------------------------------------------------------
    @staticmethod
    def makeUppercase(text=None):
        text = text.split(" ")
        upper_text = ""
        for word in text:
            upper_text += word[0].upper() + word[1:] + " "
        upper_text = upper_text[:-1]
        #print "\"{}\"".format(upper_text)
        return upper_text
    @staticmethod
    def textInput(prompt="Type in an option? ", make_uppercase=False, confirm=False):
        opt = ""
        opt = input(prompt)
        if make_uppercase:
            opt = Interface.make_uppercase(text=opt)
        return opt
    #--------------------------------------------------------------------------------------
    @staticmethod
    def confirm(options=["yes", "no"], prompt="Are you sure? ", confirm=False):
        return options[Interface.chooseOption(options=options, prompt=prompt)] == options[0]
    #--------------------------------------------------------------------------------------  
    #--------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------