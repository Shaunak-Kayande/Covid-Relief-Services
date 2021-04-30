from tkinter import *
from tkinter import messagebox

# from PIL import Image, ImageTk
root = Tk()

root.geometry("1300x1300")
root.title("COVID RELIEF SERVICES")
root.iconbitmap(r'logo.ico')
root['bg'] = '#bcf5bc'

l1 = Label(root, text="NGO", bg='#bcf5bc')
l1.configure(font=("Sans", 45))
l1.pack()
l2 = Label(root, text="COVID RELIEF SERVICES", bg='#bcf5bc')
l2.configure(font=("Sans", 50))
l2.pack()

intro = """Welcome to our  NGO, Covid Relief Services. 

         Here, we help you find assistance related to all
         Covid-19 medical emergencies.

         We believe that if we fight this virus together, we can defeat it.

         So,

         ~We Isolate Now

         So That Next Time We Gather

         Nobody Is Missing~


         It is crucial to help each other, during these times.

         So, If you want to help the society, you can enroll in 
         our volunteering programmes too. """

l3 = Label(root, justify=LEFT, padx=10, text=intro, bg='#bcf5bc')
l3.configure(font=("Arca Majora", 15))
l3.place(x=30, y=180)


# volunteers window
def openvolunWindow():
    volunWindow = Toplevel(root)  # Toplevel object which will be treated as a new window
    volunWindow.geometry("1300x1300")  # sets dimensions of new window
    volunWindow.title("WELCOME VOLUNTEERS")
    volunWindow.iconbitmap(r'logo.ico')
    volunWindow['bg'] = '#bcf5bc'

    registration = """ Do you want to register to be 
      a volunteer at CRS?"""
    l4 = Label(volunWindow, justify=LEFT, padx=10, text=registration, bg='#bcf5bc')
    l4.configure(font=("Geo Sans Light", 20))
    l4.place(x=250, y=180)

    existing = """ Existing Volunteer?"""
    l44 = Label(volunWindow, justify=LEFT, padx=10, text=existing, bg='#bcf5bc')
    l44.configure(font=("Geo Sans Light", 20))
    l44.place(x=800, y=180)

    reg = Button(volunWindow, text="Registration Form", height=3, width=25,
                 command=openregistrationWindow)  # a button widget which will open a new window on button click
    reg.place(x=330, y=300)

    l5 = Label(volunWindow, text="Please enter login details", bg='#bcf5bc')
    l5.configure(font=("Geo Sans Light", 20))
    l5.place(x=780, y=250)

    l6 = Label(volunWindow, text="Username", bg='#bcf5bc')
    l6.configure(font=("Geo Sans Light", 20))
    l6.place(x=780, y=350)

    username_login_entry = Entry(volunWindow, textvariable="username")
    username_login_entry.place(x=950, y=360)

    l7 = Label(volunWindow, text="Password", bg='#bcf5bc')
    l7.configure(font=("Geo Sans Light", 20))
    l7.place(x=780, y=450)

    password__login_entry = Entry(volunWindow, textvariable="password", show='*')
    password__login_entry.place(x=950, y=460)
    Label(volunWindow, text="").pack()

    logbtn = Button(volunWindow, text="Login", width=10, height=1, command=openloginWindow)
    logbtn.place(x=900, y=500)


# after logging in
def openloginWindow():
    loginWindow = Toplevel(volunWindow)  # Toplevel object which will be treated as a new window
    loginWindow.geometry("1300x1300")  # sets dimensions of new window
    loginWindow.title("THANK YOU FOR VOLUNTEERING")
    loginWindow.iconbitmap(r'logo.ico')
    loginWindow['bg'] = '#bcf5bc'

    l8 = Label(loginWindow, text="Which window do you want to access?", bg='#bcf5bc')
    l8.configure(font=("Geo Sans Light", 20))
    l8.place(x=420, y=200)

    info = Button(loginWindow, text="Covid Information", height=3, width=25,
                  command=opencovidInformation)  # a button widget which will open a new window on button click
    info.place(x=800, y=300)

    res = Button(loginWindow, text="Covid Resources", height=3, width=25,
                 command=opencovidResources)  # a button widget which will open a new window on button click
    res.place(x=330, y=300)


def opencovidResources():
    covidResources = Toplevel(volunWindow)  # Toplevel object which will be treated as a new window
    covidResources.geometry("1300x1300")  # sets dimensions of new window
    covidResources.title("THANK YOU FOR VOLUNTEERING")
    covidResources.iconbitmap(r'logo.ico')
    covidResources['bg'] = '#bcf5bc'

    cc = Label(covidResources, text="Which window do you want to access?", bg='#bcf5bc')
    cc.configure(font=("Geo Sans Light", 20))
    cc.pack()

    c11 = Button(covidResources, text="Centre Details", height=3, width=25,
                 command=opencovidcentreDetails)  # a button widget which will open a new window on button click
    c11.place(x=550, y=50)

    c22 = Button(covidResources, text="Bed Centre", height=3, width=25,
                 command=openBedsdetails)  # a button widget which will open a new window on button click
    c22.place(x=550, y=150)

    c33 = Button(covidResources, text="Testing Labs", height=3, width=25,
                 command=opentestingLabs)  # a button widget which will open a new window on button click
    c33.place(x=550, y=250)

    c44 = Button(covidResources, text="Plasma", height=3, width=25,
                 command=openPlasma)  # a button widget which will open a new window on button click
    c44.place(x=550, y=350)

    c55 = Button(covidResources, text="Injections", height=3, width=25,
                 command=openInjections)  # a button widget which will open a new window on button click
    c55.place(x=550, y=450)

    c66 = Button(covidResources, text="Vaccine", height=3, width=25,
                 command=openVaccine)  # a button widget which will open a new window on button click
    c66.place(x=550, y=550)


def opencovidcentreDetails():
    covidcentreDetails = Toplevel(volunWindow)  # Toplevel object which will be treated as a new window
    covidcentreDetails.geometry("1300x1300")  # sets dimensions of new window
    covidcentreDetails.title("CENTRE DETAILS")
    covidcentreDetails.iconbitmap(r'logo.ico')
    covidcentreDetails['bg'] = '#bcf5bc'

    global cname
    global cno
    global cadd
    global ctype
    cname = StringVar()
    cno = StringVar()
    cadd = StringVar()
    ctype = StringVar()

    ccc = Label(covidcentreDetails, text="CENTRE DETAILS", bg='#bcf5bc')
    ccc.configure(font=("Geo Sans Light", 30))
    ccc.pack()

    cname_lable = Label(covidcentreDetails, text="Centre Name", bg='#bcf5bc')
    cname_lable.place(x=500, y=100)
    cname_entry = Entry(covidcentreDetails, textvariable=cname)
    cname_entry.place(x=700, y=100)

    cno_lable = Label(covidcentreDetails, text="Centre Phone Number", bg='#bcf5bc')
    cno_lable.place(x=500, y=150)
    cno_entry = Entry(covidcentreDetails, textvariable=cno)
    cno_entry.place(x=700, y=150)

    cadd_lable = Label(covidcentreDetails, text="Centre Address", bg='#bcf5bc')
    cadd_lable.place(x=500, y=200)
    cadd_entry = Entry(covidcentreDetails, textvariable=cadd)
    cadd_entry.place(x=700, y=200)

    ctype_lable = Label(covidcentreDetails, text="Centre Type", bg='#bcf5bc')
    ctype_lable.place(x=500, y=250)
    # ctype_entry = Entry(covidcentreDetails, textvariable=cadd)
    # ctype_entry.place(x=700, y=250)

    '''def viewSelected():
        choice = var.get()
        if choice == 1:
            output = "Bed Centre"

        elif choice == 2:
            output = "Testing Centre"

        elif choice == 3:
            output = "Arts"
        else:
            output = "Invalid selection"

        return messagebox.showinfo('PythonGuides', f'You Selected {output}.')'''

    var = IntVar()
    ra1 = Radiobutton(covidcentreDetails, text="Bed Centre", variable=var, value=1)  # , command=viewSelected)
    ra1.place(x=700, y=250)
    ra2 = Radiobutton(covidcentreDetails, text="Testing Centre", variable=var, value=2)  # , command=viewSelected)
    ra2.place(x=700, y=280)
    ra3 = Radiobutton(covidcentreDetails, text="Plasma Centre", variable=var, value=3)  # , command=viewSelected)
    ra3.place(x=700, y=310)
    ra4 = Radiobutton(covidcentreDetails, text="Plasma Donation Centre", variable=var,
                      value=4)  # , value=3, command=viewSelected)
    ra4.place(x=700, y=340)
    ra5 = Radiobutton(covidcentreDetails, text="Injection Distributor", variable=var,
                      value=5)  # , value=3, command=viewSelected)
    ra5.place(x=700, y=370)
    ra6 = Radiobutton(covidcentreDetails, text="Vaccination Centre", variable=var,
                      value=6)  # , value=3, command=viewSelected)
    ra6.place(x=700, y=400)

    add = Button(covidcentreDetails, text="Add", width=10, height=2, bg="blue")
    add.place(x=520, y=450)

    upd = Button(covidcentreDetails, text="Update", width=10, height=2, bg="blue")
    upd.place(x=620, y=450)

    dele = Button(covidcentreDetails, text="Delete", width=10, height=2, bg="blue")
    dele.place(x=720, y=450)


def openBedsdetails():
    Bedsdetails = Toplevel(volunWindow)  # Toplevel object which will be treated as a new window
    Bedsdetails.geometry("1300x1300")  # sets dimensions of new window
    Bedsdetails.title("BED CENTRE")
    Bedsdetails.iconbitmap(r'logo.ico')
    Bedsdetails['bg'] = '#bcf5bc'

    global cnorm
    global coxy
    global ctot
    global cnam
    cnorm = StringVar()
    coxy = StringVar()
    ctot = StringVar()
    cnam = StringVar()

    cccc = Label(Bedsdetails, text="BED CENTRE", bg='#bcf5bc')
    cccc.configure(font=("Geo Sans Light", 30))
    cccc.pack()

    cnam_lable = Label(Bedsdetails, text="Centre Name", bg='#bcf5bc')
    cnam_lable.place(x=500, y=100)
    cnam_entry = Entry(Bedsdetails, textvariable=cnam)
    cnam_entry.place(x=700, y=100)

    cnorm_lable = Label(Bedsdetails, text="Normal Beds", bg='#bcf5bc')
    cnorm_lable.place(x=500, y=200)
    cnorm_entry = Entry(Bedsdetails, textvariable=cnorm)
    cnorm_entry.place(x=700, y=200)

    coxy_lable = Label(Bedsdetails, text="Oxygen Beds", bg='#bcf5bc')
    coxy_lable.place(x=500, y=300)
    coxy_entry = Entry(Bedsdetails, textvariable=coxy)
    coxy_entry.place(x=700, y=300)

    ctot_lable = Label(Bedsdetails, text="Total Beds", bg='#bcf5bc')
    ctot_lable.place(x=500, y=400)
    ctot_entry = Entry(Bedsdetails, textvariable=ctot)
    ctot_entry.place(x=700, y=400)

    add1 = Button(Bedsdetails, text="Add", width=10, height=2, bg="blue")
    add1.place(x=520, y=500)

    upd1 = Button(Bedsdetails, text="Update", width=10, height=2, bg="blue")
    upd1.place(x=620, y=500)

    dele1 = Button(Bedsdetails, text="Delete", width=10, height=2, bg="blue")
    dele1.place(x=720, y=500)


def opentestingLabs():
    testingLabs = Toplevel(volunWindow)  # Toplevel object which will be treated as a new window
    testingLabs.geometry("1300x1300")  # sets dimensions of new window
    testingLabs.title("TESTING LABS")
    testingLabs.iconbitmap(r'logo.ico')
    testingLabs['bg'] = '#bcf5bc'

    global cna
    global ctest

    cna = StringVar()
    ctest = StringVar()

    cccc1 = Label(testingLabs, text="TESTING LABS", bg='#bcf5bc')
    cccc1.configure(font=("Geo Sans Light", 30))
    cccc1.pack()

    cna_lable = Label(testingLabs, text="Lab Name", bg='#bcf5bc')
    cna_lable.place(x=500, y=100)
    cna_entry = Entry(testingLabs, textvariable=cna)
    cna_entry.place(x=700, y=100)

    ctest_lable = Label(testingLabs, text="Test Name", bg='#bcf5bc')
    ctest_lable.place(x=500, y=150)

    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()

    ra1 = Checkbutton(testingLabs, text="RTPCR TEST", variable=var1)  # , command=viewSelected)
    ra1.place(x=700, y=150)
    ra2 = Checkbutton(testingLabs, text="RAPID ANTIGEN TEST", variable=var2)  # , command=viewSelected)
    ra2.place(x=700, y=180)
    ra3 = Checkbutton(testingLabs, text="CRP", variable=var3)  # , command=viewSelected)
    ra3.place(x=700, y=210)
    ra4 = Checkbutton(testingLabs, text="FERRITIN", variable=var4)  # , value=3, command=viewSelected)
    ra4.place(x=700, y=240)
    ra5 = Checkbutton(testingLabs, text="DDMIER", variable=var5)  # , value=3, command=viewSelected)
    ra5.place(x=700, y=270)
    ra6 = Checkbutton(testingLabs, text="CBC", variable=var6)  # , value=3, command=viewSelected)
    ra6.place(x=700, y=300)
    ra7 = Checkbutton(testingLabs, text="CT SCAN", variable=var7)  # , value=3, command=viewSelected)
    ra7.place(x=700, y=330)

    add1 = Button(testingLabs, text="Add", width=10, height=2, bg="blue")
    add1.place(x=520, y=420)

    upd1 = Button(testingLabs, text="Update", width=10, height=2, bg="blue")
    upd1.place(x=620, y=420)

    dele1 = Button(testingLabs, text="Delete", width=10, height=2, bg="blue")
    dele1.place(x=720, y=420)


def openPlasma():
    Plasma = Toplevel(volunWindow)  # Toplevel object which will be treated as a new window
    Plasma.geometry("1300x1300")  # sets dimensions of new window
    Plasma.title("PLASMA DETAILS")
    Plasma.iconbitmap(r'logo.ico')
    Plasma['bg'] = '#bcf5bc'

    global cname1
    global cblood
    cname1 = StringVar()
    cblood = StringVar()

    ccc = Label(Plasma, text="PLASMA DETAILS", bg='#bcf5bc')
    ccc.configure(font=("Geo Sans Light", 30))
    ccc.pack()

    cname1_lable = Label(Plasma, text="Centre Name", bg='#bcf5bc')
    cname1_lable.place(x=500, y=100)
    cname1_entry = Entry(Plasma, textvariable=cname1)
    cname1_entry.place(x=700, y=100)

    cblood_lable = Label(Plasma, text="Blood Group", bg='#bcf5bc')
    cblood_lable.place(x=500, y=150)

    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()
    var8 = IntVar()

    ra1 = Checkbutton(Plasma, text="A+", variable=var1)  # , command=viewSelected)
    ra1.place(x=700, y=150)
    ra2 = Checkbutton(Plasma, text="A-", variable=var2)  # , command=viewSelected)
    ra2.place(x=700, y=180)
    ra3 = Checkbutton(Plasma, text="B+", variable=var3)  # , command=viewSelected)
    ra3.place(x=700, y=210)
    ra4 = Checkbutton(Plasma, text="B-", variable=var4)  # , value=3, command=viewSelected)
    ra4.place(x=700, y=240)
    ra5 = Checkbutton(Plasma, text="O+", variable=var5)  # , value=3, command=viewSelected)
    ra5.place(x=700, y=270)
    ra6 = Checkbutton(Plasma, text="O-", variable=var6)  # , value=3, command=viewSelected)
    ra6.place(x=700, y=300)
    ra7 = Checkbutton(Plasma, text="AB+", variable=var7)  # , value=3, command=viewSelected)
    ra7.place(x=700, y=330)
    ra8 = Checkbutton(Plasma, text="AB-", variable=var8)  # , value=3, command=viewSelected)
    ra8.place(x=700, y=370)

    add = Button(Plasma, text="Add", width=10, height=2, bg="blue")
    add.place(x=520, y=420)

    upd = Button(Plasma, text="Update", width=10, height=2, bg="blue")
    upd.place(x=620, y=420)

    dele = Button(Plasma, text="Delete", width=10, height=2, bg="blue")
    dele.place(x=720, y=420)


def openInjections():
    Injections = Toplevel(volunWindow)  # Toplevel object which will be treated as a new window
    Injections.geometry("1300x1300")  # sets dimensions of new window
    Injections.title("INJECTION DETAILS")
    Injections.iconbitmap(r'logo.ico')
    Injections['bg'] = '#bcf5bc'

    global cna1
    global cinj1
    global cinj2
    cna1 = StringVar()
    cinj1 = StringVar()
    cinj2 = StringVar()

    ccc = Label(Injections, text="INJECTION DETAILS", bg='#bcf5bc')
    ccc.configure(font=("Geo Sans Light", 30))
    ccc.pack()

    cname1_lable = Label(Injections, text="Centre Name", bg='#bcf5bc')
    cname1_lable.place(x=450, y=100)
    cname1_entry = Entry(Injections, textvariable=cna1)
    cname1_entry.place(x=600, y=100)

    cblood_lable = Label(Injections, text="Injection Name", bg='#bcf5bc')
    cblood_lable.place(x=450, y=150)

    ccost1_lable = Label(Injections, text="Cost- ", bg='#bcf5bc')
    ccost1_lable.place(x=700, y=150)
    ccost1_entry = Entry(Injections, textvariable=cinj1)
    ccost1_entry.place(x=750, y=150)
    cname1_lable = Label(Injections, text="Cost- ", bg='#bcf5bc')
    cname1_lable.place(x=700, y=180)
    cname1_entry = Entry(Injections, textvariable=cinj2)
    cname1_entry.place(x=750, y=180)

    var = IntVar()
    ra1 = Radiobutton(Injections, text="Remdesivir", variable=var, value=1)  # , command=viewSelected)
    ra1.place(x=600, y=150)

    ra2 = Radiobutton(Injections, text="Tocilizumab", variable=var, value=2)  # , command=viewSelected)
    ra2.place(x=600, y=180)

    add = Button(Injections, text="Add", width=10, height=2, bg="blue")
    add.place(x=520, y=300)

    upd = Button(Injections, text="Update", width=10, height=2, bg="blue")
    upd.place(x=620, y=300)

    dele = Button(Injections, text="Delete", width=10, height=2, bg="blue")
    dele.place(x=720, y=300)


def openVaccine():
    Vaccine = Toplevel(volunWindow)  # Toplevel object which will be treated as a new window
    Vaccine.geometry("1300x1300")  # sets dimensions of new window
    Vaccine.title("VACCINATION DETAILS")
    Vaccine.iconbitmap(r'logo.ico')
    Vaccine['bg'] = '#bcf5bc'

    global cn1
    global cvac1
    global cvac2
    cn1 = StringVar()
    cvac1 = StringVar()
    cvac2 = StringVar()

    ccc = Label(Vaccine, text="VACCINATION DETAILS", bg='#bcf5bc')
    ccc.configure(font=("Geo Sans Light", 30))
    ccc.pack()

    cn1_lable = Label(Vaccine, text="Centre Name", bg='#bcf5bc')
    cn1_lable.place(x=450, y=100)
    cn1_entry = Entry(Vaccine, textvariable=cn1)
    cn1_entry.place(x=600, y=100)

    cblood_lable = Label(Vaccine, text="Vaccine Name", bg='#bcf5bc')
    cblood_lable.place(x=450, y=150)

    ccost1_lable = Label(Vaccine, text="Cost- ", bg='#bcf5bc')
    ccost1_lable.place(x=700, y=150)
    ccost1_entry = Entry(Vaccine, textvariable=cvac1)
    ccost1_entry.place(x=750, y=150)
    cname1_lable = Label(Vaccine, text="Cost- ", bg='#bcf5bc')
    cname1_lable.place(x=700, y=180)
    cname1_entry = Entry(Vaccine, textvariable=cvac2)
    cname1_entry.place(x=750, y=180)

    var = IntVar()
    ra11 = Radiobutton(Vaccine, text="Covishield", variable=var, value=1)  # , command=viewSelected)
    ra11.place(x=600, y=150)

    ra22 = Radiobutton(Vaccine, text="Covaxin", variable=var, value=2)  # , command=viewSelected)
    ra22.place(x=600, y=180)

    add = Button(Vaccine, text="Add", width=10, height=2, bg="blue")
    add.place(x=520, y=300)

    upd = Button(Vaccine, text="Update", width=10, height=2, bg="blue")
    upd.place(x=620, y=300)

    dele = Button(Vaccine, text="Delete", width=10, height=2, bg="blue")
    dele.place(x=720, y=300)


def opencovidInformation():
    covidInformation = Toplevel(volunWindow)  # Toplevel object which will be treated as a new window
    covidInformation.geometry("1300x1300")  # sets dimensions of new window
    covidInformation.title("COVID INFORMATION")
    covidInformation.iconbitmap(r'logo.ico')
    covidInformation['bg'] = '#bcf5bc'

    global que
    global ans
    que = StringVar()
    ans = StringVar()

    ccc = Label(covidInformation, text="COVID INFORMATION", bg='#bcf5bc')
    ccc.configure(font=("Geo Sans Light", 30))
    ccc.pack()

    que_lable = Label(covidInformation, text="QUESTION: ", bg='#bcf5bc')
    que_lable.place(x=550, y=100)
    que_entry = Entry(covidInformation, textvariable=que)
    que_entry.place(x=650, y=100)

    ans_lable = Label(covidInformation, text="ANSWER: ", bg='#bcf5bc')
    ans_lable.place(x=550, y=200)
    ans_entry = Entry(covidInformation, textvariable=ans)
    ans_entry.place(x=650, y=200)

    add = Button(covidInformation, text="Add", width=10, height=2, bg="blue")
    add.place(x=520, y=300)

    upd = Button(covidInformation, text="Update", width=10, height=2, bg="blue")
    upd.place(x=620, y=300)

    dele = Button(covidInformation, text="Delete", width=10, height=2, bg="blue")
    dele.place(x=720, y=300)


# new volunteers registration window
def openregistrationWindow():
    registrationWindow = Toplevel(volunWindow)  # Toplevel object which will be treated as a new window
    registrationWindow.geometry("1300x1300")  # sets dimensions of new window
    registrationWindow.title("REGISTRATION FORM")
    registrationWindow.iconbitmap(r'logo.ico')
    registrationWindow['bg'] = '#bcf5bc'

    global username
    global password
    global fname
    global fmiddle
    global flast
    global age
    global add
    global num
    global username_entry
    global password_entry
    global username_info
    global password_info
    username = StringVar()
    password = StringVar()
    fname = StringVar()
    fmiddle = StringVar()
    flast = StringVar()
    age = StringVar()
    add = StringVar()
    num = StringVar()

    def register_user():
        username_info = username.get()
        password_info = password.get()

        file = open(username_info, "w")
        file.write(username_info + "\n")
        file.write(password_info)
        file.close()

        username_entry.delete(0, END)
        password_entry.delete(0, END)

        r2 = Label(registrationWindow, text="Registration Success", fg="green", font=("calibri", 11))
        r2.place(x=150, y=600)

    r = Label(registrationWindow, text="REGISTRATION FORM", bg='#bcf5bc')
    r.configure(font=("Sans", 35))
    r.pack()
    # r.place(x=50, y=50)

    r1 = Label(registrationWindow, text="Please enter details below", bg="blue")
    r1.place(x=150, y=100)

    butt = Button(registrationWindow, text="Register", width=10, height=1, bg="blue", command=register_user)
    butt.place(x=150, y=550)

    password_lable = Label(registrationWindow, text="Password", bg='#bcf5bc')
    password_lable.place(x=150, y=500)
    password_entry = Entry(registrationWindow, textvariable=password, show='*')
    password_entry.place(x=270, y=500)

    username_lable = Label(registrationWindow, text="Username", bg='#bcf5bc')
    username_lable.place(x=150, y=450)
    username_entry = Entry(registrationWindow, textvariable=username)
    username_entry.place(x=270, y=450)

    address_lable = Label(registrationWindow, text="Address", bg='#bcf5bc')
    address_lable.place(x=150, y=400)
    address_entry = Entry(registrationWindow, textvariable=add)
    address_entry.place(x=270, y=400)

    mobile_lable = Label(registrationWindow, text="Mobile", bg='#bcf5bc')
    mobile_lable.place(x=150, y=350)
    mobile_entry = Entry(registrationWindow, textvariable=num)
    mobile_entry.place(x=270, y=350)

    age_lable = Label(registrationWindow, text="Age", bg='#bcf5bc')
    age_lable.place(x=150, y=300)
    age_entry = Entry(registrationWindow, textvariable=age)
    age_entry.place(x=270, y=300)

    last_lable = Label(registrationWindow, text="Last Name", bg='#bcf5bc')
    last_lable.place(x=150, y=250)
    last_entry = Entry(registrationWindow, textvariable=flast)
    last_entry.place(x=270, y=250)

    middle_lable = Label(registrationWindow, text="Middle Name", bg='#bcf5bc')
    middle_lable.place(x=150, y=200)
    middle_entry = Entry(registrationWindow, textvariable=fmiddle)
    middle_entry.place(x=270, y=200)

    first_lable = Label(registrationWindow, text="First Name", bg='#bcf5bc')
    first_lable.place(x=150, y=150)
    first_entry = Entry(registrationWindow, textvariable=fname)
    first_entry.place(x=270, y=150)


volunWindow = Button(root, text="Volunteers", height=3, width=25,
                     command=openvolunWindow)  # a button widget which will open a new window on button click
volunWindow.place(x=650, y=550)


# viewers window
def openviewWindow():
    viewWindow = Toplevel(root)  # Toplevel object which will be treated as a new window
    viewWindow.geometry("1300x1300")  # sets dimensions of new window
    viewWindow.title("WELCOME VIEWERS")
    viewWindow.iconbitmap(r'logo.ico')
    viewWindow['bg'] = '#bcf5bc'


viewbtn = Button(root, text="Viewers", height=3, width=25,
                 command=openviewWindow)  # a button widget which will open a new window on button click
viewbtn.place(x=950, y=550)

root.mainloop()