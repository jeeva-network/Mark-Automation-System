from tkinter import *
import sqlite3
from tkinter import messagebox

# tk modul for creating gui

root = Tk()
root.title("STUDENT MARK SHEET")
root.geometry("570x230+500+250")
root.resizable(width=False, height=False)
root.config(bg="#2c3e50")

# VARIABLE DECLARATION

REG = StringVar()
SEM = StringVar()

# FRAME DESIGN

entries_frame = Frame(root, bg="#535c68")
entries_frame.pack()
title = Label(entries_frame, text="Mark Automation System", font=("Calibri", 20, "bold"), bg="#535c68", fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

# LABLE AND TEXT TAGS

lblREGNO1 = Label(entries_frame, text="Register Number", font=("Calibri", 18), bg="#535c68", fg="white")
lblREGNO1.grid(row=1, column=0, padx=10, pady=5, sticky="w")
txtREGNO1 = Entry(entries_frame, textvariable=REG, font=("Calibri", 18), width=8)
txtREGNO1.grid(row=1, column=1, padx=10, pady=5, sticky="w")

lblSEM = Label(entries_frame, text="Semester", font=("Calibri", 18), bg="#535c68", fg="white")
lblSEM.grid(row=2, column=0, padx=10, pady=5, sticky="w")
txtSEM = Entry(entries_frame, textvariable=SEM, font=("Calibri", 18), width=8)
txtSEM.grid(row=2, column=1, padx=10, pady=5, sticky="w")


# CONDITION FUNCTION TO USE DATA FETING AND VALIDATION

def show():

    # get input from user

    roll = len(REG.get())

    # IF CONDITION FOR CHECKING ROLL

    if 8 >= roll > 6:

        # DATABASE CONNECTION COMMAND

        connection = sqlite3.connect("database_1.db")
        connection.row_factory = lambda cursor, row: row[0]
        cur = connection.cursor()

        roll_no = REG.get()

        sem = SEM.get()

        global semester
        global sr

        if sem.isdigit():
            sem = int(sem)
            if sem == 1:
                semester = 'FIRST'
                sr = '1'
            elif sem == 2:
                semester = 'SECOND'
                sr = '2'
            elif sem == 3:
                semester = 'THIRD'
                sr = '3'
            elif sem == 4:
                semester = 'FOURTH'
                sr = '4'
            elif sem == 5:
                semester = 'FIFTH'
                sr = '5'
            elif sem == 6:
                semester = 'SIXTH'
                sr = '6'

            # change roll_no in uppercase
            roll_no = roll_no.upper()
            position_1 = roll_no[0:4] + '%'
            position_3 = roll_no[2:4] + '%'
            position_4 = roll_no[2:5]
            cur.execute("select NAME from student where REGNO='" + roll_no + "'")
            nam = cur.fetchall()
            n1 = (''.join(nam))
            name = n1[0:-10]
            db = n1[-9:-1]

            global REGNO

            for Z in cur.execute(
                    "select REGNO from student"):
                REGNO = cur.fetchall()
            # print(REGNO)

            if (roll_no in REGNO):
                if sem == 1 or sem == 2 or sem == 3 or sem == 4 or sem == 5 or sem == 6:

                    # validate subject per sem

                    val = []

                    subject = ""
                    for value in cur.execute(
                            "select SUBJECT_PER_SEM from subject where MAJOR_CODE LIKE'" + position_1 + "'"):
                        final = value.strip()
                        subject = final.split()

                    if sem == 1:
                        try:
                            first = subject[0]
                            last = subject[1]
                            for store in range(int(first), int(last)):
                                data = "SUB" + str(store)
                                val.append(data)
                        except IndexError:
                            messagebox.showerror("Error",
                                                 "sorry in the semester is unavailable.")

                    elif sem == 2:
                        try:
                            first = subject[1]
                            last = subject[2]
                            for store in range(int(first), int(last)):
                                data = "SUB" + str(store)
                                val.append(data)
                        except IndexError:
                            messagebox.showerror("Error",
                                                 "sorry in the semester is unavailable.")

                    elif sem == 3:
                        try:
                            first = subject[2]
                            last = subject[3]
                            for store in range(int(first), int(last)):
                                data = "SUB" + str(store)
                                val.append(data)
                        except IndexError:
                            messagebox.showerror("Error",
                                                 "sorry in the semester is unavailable.")

                    elif sem == 4:
                        try:
                            first = subject[3]
                            last = subject[4]
                            for store in range(int(first), int(last)):
                                data = "SUB" + str(store)
                                val.append(data)
                        except IndexError:
                            messagebox.showerror("Error",
                                                 "sorry in the semester is unavailable.")

                    elif sem == 5:
                        try:
                            first = subject[4]
                            last = subject[5]
                            for store in range(int(first), int(last)):
                                data = "SUB" + str(store)
                                val.append(data)
                        except IndexError:
                            if position_4 == '010' or position_4 == '020' or position_4 == '030' or position_4 == '040'\
                                    or position_4 == '04L' or position_4 == '050' or position_4 == '060' \
                                    or position_4 == '070' or position_4 == '080' or position_4 == '090' \
                                    or position_4 == '100' or position_4 == '110' or position_4 == '120' \
                                    or position_4 == '130':
                                messagebox.showerror("Error",
                                                     "Please Enter the semester in-between 1 to 4, including Both.")
                            else:
                                messagebox.showerror("Error", "sorry in the semester is unavailable.")

                    elif sem == 6:
                        try:
                            first = subject[5]
                            last = subject[6]
                            for store in range(int(first), int(last) + 1):
                                data = "SUB" + str(store)
                                val.append(data)

                        except IndexError:
                            if position_4 == '010' or position_4 == '020' or position_4 == '030' or position_4 == '040'\
                                    or position_4 == '04L' or position_4 == '050' or position_4 == '060' \
                                    or position_4 == '070' or position_4 == '080' or position_4 == '090' \
                                    or position_4 == '100' or position_4 == '110' or position_4 == '120' \
                                    or position_4 == '130':
                                messagebox.showerror("Error",
                                                     "Please Enter the semester in-between 1 to 4, including Both.")
                            else:
                                messagebox.showerror("Error", "sorry in the semester is unavailable.")

                    else:
                        messagebox.showerror("Error", "Please Enter the valid semester.")
                    # print("val", val)
                    if not val:
                        pass
                    else:

                        # subject code validation

                        global part
                        colm = []
                        sec = []

                        for sub in val:
                            cur.execute("select " + sub + " from subject where MAJOR_CODE LIKE'" + position_1 + "'")
                            col = cur.fetchall()
                            colm.append(','.join(col))
                            for secol in colm:
                                part = secol[2:4]
                            if part == "U1":
                                sec.append("I")
                            elif part == "U2":
                                sec.append("II")
                            elif part == "U4":
                                sec.append("IV")
                            elif part == "U5":
                                sec.append("V")
                            else:
                                sec.append("III")
                        # print("colm", colm)
                        # print("sec", sec)

                        # sno  number

                        a = []
                        for h in range(1, len(colm) + 1):
                            a.append(sr)

                        # for output to ens of sem

                        global endx
                        global endy

                        if len(a) == 1:
                            endx = 75
                            endy = 260
                        elif len(a) == 2:
                            endx = 75
                            endy = 280
                        elif len(a) == 3:
                            endx = 75
                            endy = 300
                        elif len(a) == 4:
                            endx = 75
                            endy = 320
                        elif len(a) == 5:
                            endx = 75
                            endy = 340
                        elif len(a) == 6:
                            endx = 75
                            endy = 360
                        elif len(a) == 7:
                            endx = 75
                            endy = 380
                        elif len(a) == 8:
                            endx = 75
                            endy = 400
                        elif len(a) == 9:
                            endx = 75
                            endy = 420
                        elif len(a) == 10:
                            endx = 75
                            endy = 440

                        # subject title and credit

                        cr = []
                        s_t = []
                        for sub in val:
                            cur.execute("select " + sub + " from subject where MAJOR_CODE LIKE'" + position_1 + "'")
                            st = cur.fetchall()

                            # title

                            for title in st:
                                cur.execute("select SUBJECT_TITLES from schema where SUBJECT_CODE='" + str(title) + "'")
                                sst = cur.fetchall()
                                # print(sst)
                                s_t.append(','.join(sst))

                            # credits

                            for credit in st:
                                cur.execute("select CREDITS from schema where SUBJECT_CODE='" + str(credit) + "'")
                                noc = cur.fetchall()
                                cr.append(','.join(noc))

                        # take mark from eos and cia in database

                        eos = []
                        cia = []
                        Eos = []
                        Cia = []

                        for sub in val:
                            cur.execute("select NEOS" + sub[3:5] + " from student, subject where MAJOR_CODE LIKE'" +
                                        position_1 + "' and REGNO='" + str(roll_no) + "'")
                            eos_mark = cur.fetchall()
                            for i in eos_mark:
                                if i == '':
                                    cur.execute(
                                        "select FEOS" + sub[3:5] + " from student, subject where MAJOR_CODE LIKE'" +
                                        position_1 + "' and REGNO='" + str(roll_no) + "'")
                                    t = cur.fetchall()
                                    Eos = (''.join(t))
                                else:
                                    Eos = (''.join(eos_mark))

                            eos.append(''.join(Eos))
                            cur.execute("select NCIA" + sub[3:5] + " from student, subject where MAJOR_CODE LIKE'" +
                                        position_1 + "' and REGNO='" + str(roll_no) + "'")
                            cia_mark = cur.fetchall()
                            for i in cia_mark:
                                if i == '':
                                    cur.execute(
                                        "select FCIA" + sub[3:5] + " from student, subject where MAJOR_CODE LIKE'" +
                                        position_1 + "' and REGNO='" + str(roll_no) + "'")
                                    t = cur.fetchall()
                                    Cia = (''.join(t))
                                else:
                                    Cia = (''.join(cia_mark))
                            cia.append(''.join(Cia))

                        co = sqlite3.connect("database.db")
                        co.row_factory = lambda cursor, row: row[0]
                        cu = co.cursor()
                        cu.execute("select MAJOR from major where MAJOR_CODE LIKE'" + position_3 + "'")
                        major = cu.fetchall()
                        # print(major)
                        DEP = (''.join(map(str, major)))
                        dep = DEP
                        co.commit()
                        co.close()

                        eos_minimum = []

                        for i in colm:
                            cur.execute("select EOS_MIN_MARKS from schema where SUBJECT_CODE='" + i + "'")
                            mini = cur.fetchall()
                            eos_minimum.append(','.join(mini))

                        eos_maximum = []

                        for i in colm:
                            cur.execute("select EOS_MAX_MARKS from schema where SUBJECT_CODE='" + i + "'")
                            maxi = cur.fetchall()
                            eos_maximum.append(','.join(maxi))

                        cia_minimum = []

                        for i in colm:
                            cur.execute("select CIA_MIN_MARKS from schema where SUBJECT_CODE='" + i + "'")
                            mini = cur.fetchall()
                            cia_minimum.append(','.join(mini))

                        cia_maximum = []

                        for i in colm:
                            cur.execute("select CIA_MAX_MARKS from schema where SUBJECT_CODE='" + i + "'")
                            maxi = cur.fetchall()
                            cia_maximum.append(','.join(maxi))

                        max_mark = []

                        for i in colm:
                            cur.execute("select MAX_MARKS from schema where SUBJECT_CODE='" + i + "'")
                            maxi = cur.fetchall()
                            max_mark.append(','.join(maxi))

                        min_mark = []
                        for i in colm:
                            cur.execute("select MIN_MARKS from schema where SUBJECT_CODE='" + i + "'")
                            min = cur.fetchall()
                            min_mark.append(','.join(min))

                        # print('min_mark', min_mark)
                        # print('cia min', cia_minimum)
                        # print('eos min', eos_minimum)
                        # print('eos mark', eos)
                        # print('cia mark', cia)

                        to = []
                        g_p = []
                        re = []

                        global gr0, gr1, gr2, gr3, gr4, gr5, gr6, gr7, gr8, gr9

                        for j in range(0, len(eos)):
                            global x
                            global y

                            for x in eos[j:j + 1]:
                                pass

                            for y in cia[j:j + 1]:
                                pass
                            if x.isdigit() and y.isdigit():
                                z = (int(x) + int(y))
                                to.append(''.join(str(z)))
                            else:
                                to.append('****')

                            global n
                            global nn
                            global mn

                            for n in eos_minimum[j:j + 1]:
                                pass
                            for nn in cia_minimum[j:j + 1]:
                                pass
                            for mn in min_mark[j:j + 1]:
                                pass

                            if x.isdigit() and y.isdigit():
                                if int(x) >= int(n) and int(y) >= int(nn):
                                    if (int(x) + int(y)) >= int(mn):
                                        g_p.append(str((int(x) + int(y)) / 10))
                                        re.append('pass')
                                    else:
                                        g_p.append('****')
                                        re.append('fail')
                                else:
                                    g_p.append('****')
                                    re.append('fail')
                            else:
                                g_p.append('****')
                                re.append('fail')

                            global gr
                            gr = []

                            for e in range(0, len(g_p)):
                                for u in to[e:e + 1]:
                                    if u.isdigit():

                                        if int(u) > 89:
                                            gr.append('O')
                                        elif 90 > int(u) > 79:
                                            gr.append('D+')
                                        elif 80 > int(u) > 74:
                                            gr.append('D')
                                        elif 75 > int(u) > 69:
                                            gr.append('A+')
                                        elif 70 > int(u) > 59:
                                            gr.append('A')
                                        elif 60 > int(u) > 49:
                                            gr.append('B')
                                        elif 50 > int(u) >= int(mn):
                                            gr.append('C')
                                        else:
                                            gr.append('RA')
                                    else:
                                        gr.append('ABST')

                            # grade values for output

                            gr01 = str(gr[0:1])
                            gr0 = gr01[2:-2]
                            gr11 = str(gr[1:2])
                            gr1 = gr11[2:-2]
                            gr21 = str(gr[2:3])
                            gr2 = gr21[2:-2]
                            gr31 = str(gr[3:4])
                            gr3 = gr31[2:-2]
                            gr41 = str(gr[4:5])
                            gr4 = gr41[2:-2]
                            gr51 = str(gr[5:6])
                            gr5 = gr51[2:-2]
                            gr61 = str(gr[6:7])
                            gr6 = gr61[2:-2]
                            gr71 = str(gr[7:8])
                            gr7 = gr71[2:-2]
                            gr81 = str(gr[8:9])
                            gr8 = gr81[2:-2]
                            gr91 = str(gr[9:10])
                            gr9 = gr91[2:-2]

                        # semester type 'I' value for output

                        a01 = str(a[0:1])
                        a0 = a01[2:-2]
                        a11 = str(a[1:2])
                        a1 = a11[2:-2]
                        a21 = str(a[2:3])
                        a2 = a21[2:-2]
                        a31 = str(a[3:4])
                        a3 = a31[2:-2]
                        a41 = str(a[4:5])
                        a4 = a41[2:-2]
                        a51 = str(a[5:6])
                        a5 = a51[2:-2]
                        a61 = str(a[6:7])
                        a6 = a61[2:-2]
                        a71 = str(a[7:8])
                        a7 = a71[2:-2]
                        a81 = str(a[8:9])
                        a8 = a81[2:-2]
                        a91 = str(a[9:10])
                        a9 = a91[2:-2]

                        # subject \ paper name to value for the output

                        s_t01 = str(s_t[0:1])
                        s_t0 = s_t01[2:-2]
                        s_t11 = str(s_t[1:2])
                        s_t1 = s_t11[2:-2]
                        s_t21 = str(s_t[2:3])
                        s_t2 = s_t21[2:-2]
                        s_t31 = str(s_t[3:4])
                        s_t3 = s_t31[2:-2]
                        s_t41 = str(s_t[4:5])
                        s_t4 = s_t41[2:-2]
                        s_t51 = str(s_t[5:6])
                        s_t5 = s_t51[2:-2]
                        s_t61 = str(s_t[6:7])
                        s_t6 = s_t61[2:-2]
                        s_t71 = str(s_t[7:8])
                        s_t7 = s_t71[2:-2]
                        s_t81 = str(s_t[8:9])
                        s_t8 = s_t81[2:-2]
                        s_t91 = str(s_t[9:10])
                        s_t9 = s_t91[2:-2]

                        # subject name broken to show another line

                        s_t0 = str(s_t0)
                        va00 = str(s_t0[0:30])
                        # print(va00)
                        va01 = str(s_t0[30:80])
                        # print(va01)
                        s_t1 = str(s_t1)
                        va10 = str(s_t1[0:30])
                        # print(va10)
                        va11 = str(s_t1[30:80])
                        # print(va11)
                        s_t2 = str(s_t2)
                        va20 = str(s_t2[0:30])
                        # print(va20)
                        va21 = str(s_t2[30:80])
                        # print(va21)
                        s_t3 = str(s_t3)
                        va30 = str(s_t3[0:30])
                        # print(va30)
                        va31 = str(s_t3[30:80])
                        # print(va31)
                        s_t4 = str(s_t4)
                        va40 = str(s_t4[0:30])
                        # print(va40)
                        va41 = str(s_t4[30:80])
                        # print(va41)
                        s_t5 = str(s_t5)
                        va50 = str(s_t5[0:30])
                        # print(va50)
                        va51 = str(s_t5[30:80])
                        # print(va51)
                        s_t6 = str(s_t6)
                        va60 = str(s_t6[0:30])
                        # print(va60)
                        va61 = str(s_t6[30:80])
                        # print(va61)
                        s_t7 = str(s_t7)
                        va70 = str(s_t7[0:30])
                        # print(va70)
                        va71 = str(s_t7[30:80])
                        # print(va71)
                        s_t8 = str(s_t8)
                        va80 = str(s_t8[0:30])
                        # print(va80)
                        va81 = str(s_t8[30:80])
                        # print(va81)
                        s_t9 = str(s_t9)
                        va90 = str(s_t9[0:30])
                        # print(va90)
                        va91 = str(s_t9[30:80])
                        # print(va91)

                        # eose mark for output

                        e01 = str(eos[0:1])
                        e0 = e01[2:-2]
                        e11 = str(eos[1:2])
                        e1 = e11[2:-2]
                        e21 = str(eos[2:3])
                        e2 = e21[2:-2]
                        e31 = str(eos[3:4])
                        e3 = e31[2:-2]
                        e41 = str(eos[4:5])
                        e4 = e41[2:-2]
                        e51 = str(eos[5:6])
                        e5 = e51[2:-2]
                        e61 = str(eos[6:7])
                        e6 = e61[2:-2]
                        e71 = str(eos[7:8])
                        e7 = e71[2:-2]
                        e81 = str(eos[8:9])
                        e8 = e81[2:-2]
                        e91 = str(eos[9:10])
                        e9 = e91[2:-2]

                        # cia mark for output

                        c01 = str(cia[0:1])
                        c0 = c01[2:-2]
                        c11 = str(cia[1:2])
                        c1 = c11[2:-2]
                        c21 = str(cia[2:3])
                        c2 = c21[2:-2]
                        c31 = str(cia[3:4])
                        c3 = c31[2:-2]
                        c41 = str(cia[4:5])
                        c4 = c41[2:-2]
                        c51 = str(cia[5:6])
                        c5 = c51[2:-2]
                        c61 = str(cia[6:7])
                        c6 = c61[2:-2]
                        c71 = str(cia[7:8])
                        c7 = c71[2:-2]
                        c81 = str(cia[8:9])
                        c8 = c81[2:-2]
                        c91 = str(cia[9:10])
                        c9 = c91[2:-2]

                        # total mark for output

                        to01 = str(to[0:1])
                        to0 = to01[2:-2]
                        to11 = str(to[1:2])
                        to1 = to11[2:-2]
                        to21 = str(to[2:3])
                        to2 = to21[2:-2]
                        to31 = str(to[3:4])
                        to3 = to31[2:-2]
                        to41 = str(to[4:5])
                        to4 = to41[2:-2]
                        to51 = str(to[5:6])
                        to5 = to51[2:-2]
                        to61 = str(to[6:7])
                        to6 = to61[2:-2]
                        to71 = str(to[7:8])
                        to7 = to71[2:-2]
                        to81 = str(to[8:9])
                        to8 = to81[2:-2]
                        to91 = str(to[9:10])
                        to9 = to91[2:-2]

                        # credits for output

                        cr01 = str(cr[0:1])
                        cr0 = cr01[2:-2]
                        cr11 = str(cr[1:2])
                        cr1 = cr11[2:-2]
                        cr21 = str(cr[2:3])
                        cr2 = cr21[2:-2]
                        cr31 = str(cr[3:4])
                        cr3 = cr31[2:-2]
                        cr41 = str(cr[4:5])
                        cr4 = cr41[2:-2]
                        cr51 = str(cr[5:6])
                        cr5 = cr51[2:-2]
                        cr61 = str(cr[6:7])
                        cr6 = cr61[2:-2]
                        cr71 = str(cr[7:8])
                        cr7 = cr71[2:-2]
                        cr81 = str(cr[8:9])
                        cr8 = cr81[2:-2]
                        cr91 = str(cr[9:10])
                        cr9 = cr91[2:-2]

                        # grade point for output

                        g_p01 = str(g_p[0:1])
                        g_p0 = g_p01[2:-2]
                        g_p11 = str(g_p[1:2])
                        g_p1 = g_p11[2:-2]
                        g_p21 = str(g_p[2:3])
                        g_p2 = g_p21[2:-2]
                        g_p31 = str(g_p[3:4])
                        g_p3 = g_p31[2:-2]
                        g_p41 = str(g_p[4:5])
                        g_p4 = g_p41[2:-2]
                        g_p51 = str(g_p[5:6])
                        g_p5 = g_p51[2:-2]
                        g_p61 = str(g_p[6:7])
                        g_p6 = g_p61[2:-2]
                        g_p71 = str(g_p[7:8])
                        g_p7 = g_p71[2:-2]
                        g_p81 = str(g_p[8:9])
                        g_p8 = g_p81[2:-2]
                        g_p91 = str(g_p[9:10])
                        g_p9 = g_p91[2:-2]

                        # result for output

                        re01 = str(re[0:1])
                        re0 = re01[2:-2]
                        re11 = str(re[1:2])
                        re1 = re11[2:-2]
                        re21 = str(re[2:3])
                        re2 = re21[2:-2]
                        re31 = str(re[3:4])
                        re3 = re31[2:-2]
                        re41 = str(re[4:5])
                        re4 = re41[2:-2]
                        re51 = str(re[5:6])
                        re5 = re51[2:-2]
                        re61 = str(re[6:7])
                        re6 = re61[2:-2]
                        re71 = str(re[7:8])
                        re7 = re71[2:-2]
                        re81 = str(re[8:9])
                        re8 = re81[2:-2]
                        re91 = str(re[9:10])
                        re9 = re91[2:-2]

                        # new window for frame result

                        from PIL import ImageTk, Image
                        ws = Toplevel()
                        ws.title('Result Statement')
                        ws.geometry('590x810+500+10')
                        ws.resizable(width=False, height=False)

                        # image resize

                        image = Image.open('D:\\Downloads\\page_1.png')
                        resize = image.resize((587, 801), Image.LANCZOS)
                        image_nw = ImageTk.PhotoImage(resize)

                        # for line separation in long subject name

                        x01 = 0
                        x02 = 0
                        x03 = 0
                        x04 = 0
                        x05 = 0
                        x06 = 0
                        x07 = 0
                        x08 = 0
                        x09 = 0
                        x00 = 0

                        if va01 == '':
                            pass
                            # print('yes')
                        else:
                            # print('no')
                            x01 = x01 + 10
                        if va11 == '':
                            pass
                            # print('yes')
                        else:
                            # print('no')
                            x02 = x02 + 10
                        if va21 == '':
                            pass
                            # print('yes')
                        else:
                            # print('no')
                            x03 = x03 + 10
                        if va31 == '':
                            pass
                            # print('yes')
                        else:
                            # print('no')
                            x04 = x04 + 10
                        if va41 == '':
                            pass
                            # print('yes')
                        else:
                            # print('no')
                            x05 = x05 + 10
                        if va51 == '':
                            pass
                            # print('yes')
                        else:
                            # print('no')
                            x06 = x06 + 10
                        if va61 == '':
                            pass
                            # print('yes')
                        else:
                            # print('no')
                            x07 = x07 + 10
                        if va71 == '':
                            pass
                            # print('yes')
                        else:
                            # print('no')
                            x08 = x08 + 10
                        if va81 == '':
                            pass
                            # print('yes')
                        else:
                            # print('no')
                            x09 = x09 + 10
                        if va91 == '':
                            pass
                            # print('yes')
                        else:
                            # print('no')
                            x00 = x00 + 10

                        rt0 = 260
                        rt1 = 280 + x01
                        rt2 = 300 + x01 + x02
                        rt3 = 320 + x01 + x02 + x03
                        rt4 = 340 + x01 + x02 + x03 + x04
                        rt5 = 360 + x01 + x02 + x03 + x04 + x05
                        rt6 = 380 + x01 + x02 + x03 + x04 + x05 + x06
                        rt7 = 400 + x01 + x02 + x03 + x04 + x05 + x06 + x07
                        rt8 = 420 + x01 + x02 + x03 + x04 + x05 + x06 + x07 + x08
                        rt9 = 440 + x01 + x02 + x03 + x04 + x05 + x06 + x07 + x08 + x09

                        canva = Canvas(ws, width=590, height=800)
                        canva.pack(fill="both", anchor=CENTER)
                        canva.create_image(0, 0, image=image_nw, anchor='nw')

                        # name of the student

                        canva.create_text(55, 143, text=name, fill='black', font=("Helvetica", 8), anchor='w')

                        # Data of birth

                        canva.create_text(335, 143, text=db, fill='black', font=("Helvetica", 8), anchor='w')

                        # Regno

                        canva.create_text(480, 143, text=roll_no, fill='black', font=("Helvetica", 8), anchor='w')

                        # course name

                        canva.create_text(70, 172, text=dep, fill='black', font=("Helvetica", 8), anchor='w')
                        canva.create_text(248, 172, text="MEDIUM OF INSTRUCTION : ENGLISH", fill='black',
                                          font=("Helvetica", 8), anchor='w')

                        # semester

                        canva.create_text(500, 172, text=semester, fill='black', font=("Helvetica", 8), anchor='w')

                        # paper1
                        # sem row

                        canva.create_text(23, rt0, text=a0, fill='black', font=("Helvetica", 8), anchor='w')

                        # part row

                        canva.create_text(55, rt0, text=sec[0], fill='black', font=("Helvetica", 8), anchor='w')

                        # subject/paper row

                        canva.create_text(75, rt0, text=va00, fill='black', font=("Helvetica", 8), anchor='w')
                        canva.create_text(75, rt0 + 10, text=va01, fill='black', font=("Helvetica", 8), anchor='w')

                        # eose row

                        canva.create_text(303, rt0, text=e0, fill='black', font=("Helvetica", 8), anchor='w')

                        # cia row

                        canva.create_text(335, rt0, text=c0, fill='black', font=("Helvetica", 8), anchor='w')

                        # total row

                        canva.create_text(380, rt0, text=to0, fill='black', font=("Helvetica", 8), anchor='w')

                        # no.of.credits row

                        canva.create_text(418, rt0, text=cr0, fill='black', font=("Helvetica", 8), anchor='w')

                        # grade points row

                        canva.create_text(458, rt0, text=g_p0, fill='black', font=("Helvetica", 8), anchor='w')

                        # grade row

                        canva.create_text(503, rt0, text=gr0, fill='black', font=("Helvetica", 8), anchor='w')

                        # result row

                        canva.create_text(540, rt0, text=re0, fill='black', font=("Helvetica", 8), anchor='w')

                        # paper2
                        # sem row

                        canva.create_text(23, rt1, text=a1, fill='black', font=("Helvetica", 8), anchor='w')

                        # part row

                        canva.create_text(55, rt1, text=sec[1], fill='black', font=("Helvetica", 8), anchor='w')

                        # subject/paper row

                        canva.create_text(75, rt1, text=va10, fill='black', font=("Helvetica", 8), anchor='w')
                        canva.create_text(75, rt1 + 10, text=va11, fill='black', font=("Helvetica", 8), anchor='w')

                        # eose row

                        canva.create_text(303, rt1, text=e1, fill='black', font=("Helvetica", 8), anchor='w')

                        # cia row

                        canva.create_text(335, rt1, text=c1, fill='black', font=("Helvetica", 8), anchor='w')

                        # total row

                        canva.create_text(380, rt1, text=to1, fill='black', font=("Helvetica", 8), anchor='w')

                        # no.of.credits row

                        canva.create_text(418, rt1, text=cr1, fill='black', font=("Helvetica", 8), anchor='w')

                        # grade points row

                        canva.create_text(458, rt1, text=g_p1, fill='black', font=("Helvetica", 8), anchor='w')

                        # grade row

                        canva.create_text(503, rt1, text=gr1, fill='black', font=("Helvetica", 8), anchor='w')

                        # result row

                        canva.create_text(540, rt1, text=re1, fill='black', font=("Helvetica", 8), anchor='w')

                        # paper3
                        # sem row

                        canva.create_text(23, rt2, text=a2, fill='black', font=("Helvetica", 8), anchor='w')

                        # part row

                        canva.create_text(55, rt2, text=sec[2], fill='black', font=("Helvetica", 8), anchor='w')

                        # subject/paper row

                        canva.create_text(75, rt2, text=va20, fill='black', font=("Helvetica", 8), anchor='w')
                        canva.create_text(75, rt2 + 10, text=va21, fill='black', font=("Helvetica", 8), anchor='w')

                        # eose row

                        canva.create_text(303, rt2, text=e2, fill='black', font=("Helvetica", 8), anchor='w')

                        # cia row

                        canva.create_text(335, rt2, text=c2, fill='black', font=("Helvetica", 8), anchor='w')

                        # total row

                        canva.create_text(380, rt2, text=to2, fill='black', font=("Helvetica", 8), anchor='w')

                        # no.of.credits row

                        canva.create_text(418, rt2, text=cr2, fill='black', font=("Helvetica", 8), anchor='w')

                        # grade points row

                        canva.create_text(458, rt2, text=g_p2, fill='black', font=("Helvetica", 8), anchor='w')

                        # grade row

                        canva.create_text(503, rt2, text=gr2, fill='black', font=("Helvetica", 8), anchor='w')

                        # result row

                        canva.create_text(540, rt2, text=re2, fill='black', font=("Helvetica", 8), anchor='w')

                        # paper4
                        # sem row

                        canva.create_text(23, rt3, text=a3, fill='black', font=("Helvetica", 8), anchor='w')

                        # part row

                        try:
                            canva.create_text(55, rt3, text=sec[3], fill='black', font=("Helvetica", 8), anchor='w')
                        except IndexError:
                            pass

                        # subject/paper row

                        canva.create_text(75, rt3, text=va30, fill='black', font=("Helvetica", 8), anchor='w')
                        canva.create_text(75, rt3 + 10, text=va31, fill='black', font=("Helvetica", 8), anchor='w')

                        # eose row

                        canva.create_text(303, rt3, text=e3, fill='black', font=("Helvetica", 8), anchor='w')

                        # cia row

                        canva.create_text(335, rt3, text=c3, fill='black', font=("Helvetica", 8), anchor='w')

                        # total row

                        canva.create_text(380, rt3, text=to3, fill='black', font=("Helvetica", 8), anchor='w')

                        # no.of.credits row

                        canva.create_text(418, rt3, text=cr3, fill='black', font=("Helvetica", 8), anchor='w')

                        # grade points row

                        canva.create_text(458, rt3, text=g_p3, fill='black', font=("Helvetica", 8), anchor='w')

                        # grade row

                        canva.create_text(503, rt3, text=gr3, fill='black', font=("Helvetica", 8), anchor='w')

                        # result row

                        canva.create_text(540, rt3, text=re3, fill='black', font=("Helvetica", 8), anchor='w')

                        # paper5
                        # sem row

                        canva.create_text(23, rt4, text=a4, fill='black', font=("Helvetica", 8), anchor='w')

                        # part row

                        try:
                            canva.create_text(55, rt4, text=sec[4], fill='black', font=("Helvetica", 8), anchor='w')
                        except IndexError:
                            pass

                        # subject/paper row

                        canva.create_text(75, rt4, text=va40, fill='black', font=("Helvetica", 8), anchor='w')
                        canva.create_text(75, rt4 + 10, text=va41, fill='black', font=("Helvetica", 8), anchor='w')

                        # eose row

                        canva.create_text(303, rt4, text=e4, fill='black', font=("Helvetica", 8), anchor='w')

                        # cia row

                        canva.create_text(335, rt4, text=c4, fill='black', font=("Helvetica", 8), anchor='w')

                        # total row

                        canva.create_text(380, rt4, text=to4, fill='black', font=("Helvetica", 8), anchor='w')

                        # no.of.credits row

                        canva.create_text(418, rt4, text=cr4, fill='black', font=("Helvetica", 8), anchor='w')

                        # grade points row

                        canva.create_text(458, rt4, text=g_p4, fill='black', font=("Helvetica", 8), anchor='w')

                        # grade row

                        canva.create_text(503, rt4, text=gr4, fill='black', font=("Helvetica", 8), anchor='w')

                        # result row

                        canva.create_text(540, rt4, text=re4, fill='black', font=("Helvetica", 8), anchor='w')

                        # paper6
                        # sem row

                        canva.create_text(23, rt5, text=a5, fill='black', font=("Helvetica", 8), anchor='w')

                        # part row

                        try:
                            canva.create_text(55, rt5, text=sec[5], fill='black', font=("Helvetica", 8), anchor='w')
                        except IndexError:
                            pass

                        # subject/paper row

                        canva.create_text(75, rt5, text=va50, fill='black', font=("Helvetica", 8), anchor='w')
                        canva.create_text(75, rt5 + 10, text=va51, fill='black', font=("Helvetica", 8), anchor='w')

                        # eose row

                        canva.create_text(303, rt5, text=e5, fill='black', font=("Helvetica", 8), anchor='w')

                        # cia row

                        canva.create_text(335, rt5, text=c5, fill='black', font=("Helvetica", 8), anchor='w')

                        # total row

                        canva.create_text(380, rt5, text=to5, fill='black', font=("Helvetica", 8), anchor='w')

                        # no.of.credits row

                        canva.create_text(418, rt5, text=cr5, fill='black', font=("Helvetica", 8), anchor='w')

                        # grade points row

                        canva.create_text(458, rt5, text=g_p5, fill='black', font=("Helvetica", 8), anchor='w')

                        # grade row

                        canva.create_text(503, rt5, text=gr5, fill='black', font=("Helvetica", 8), anchor='w')

                        # result row

                        canva.create_text(540, rt5, text=re5, fill='black', font=("Helvetica", 8), anchor='w')

                        # paper7
                        # sem row

                        canva.create_text(23, rt6, text=a6, fill='black', font=("Helvetica", 8), anchor='w')

                        # part row

                        try:
                            canva.create_text(55, rt6, text=sec[6], fill='black', font=("Helvetica", 8), anchor='w')
                        except IndexError:
                            pass

                        # subject/paper row

                        canva.create_text(75, rt6, text=va60, fill='black', font=("Helvetica", 8), anchor='w')
                        canva.create_text(75, rt6 + 10, text=va61, fill='black', font=("Helvetica", 8), anchor='w')

                        # eose row

                        canva.create_text(303, rt6, text=e6, fill='black', font=("Helvetica", 8), anchor='w')

                        # cia row

                        canva.create_text(335, rt6, text=c6, fill='black', font=("Helvetica", 8), anchor='w')

                        # total row

                        canva.create_text(380, rt6, text=to6, fill='black', font=("Helvetica", 8), anchor='w')

                        # no.of.credits row

                        canva.create_text(418, rt6, text=cr6, fill='black', font=("Helvetica", 8), anchor='w')

                        # grade points row

                        canva.create_text(458, rt6, text=g_p6, fill='black', font=("Helvetica", 8), anchor='w')

                        # grade row

                        canva.create_text(503, rt6, text=gr6, fill='black', font=("Helvetica", 8), anchor='w')

                        # result row

                        canva.create_text(540, rt6, text=re6, fill='black', font=("Helvetica", 8), anchor='w')

                        # paper8
                        # sem row

                        canva.create_text(23, rt7, text=a7, fill='black', font=("Helvetica", 8), anchor='w')

                        # part row

                        try:
                            canva.create_text(55, rt7, text=sec[7], fill='black', font=("Helvetica", 8), anchor='w')
                        except IndexError:
                            pass

                        # subject/paper row

                        canva.create_text(75, rt7, text=va70, fill='black', font=("Helvetica", 8), anchor='w')
                        canva.create_text(75, rt7 + 10, text=va71, fill='black', font=("Helvetica", 8), anchor='w')

                        # eose row

                        canva.create_text(303, rt7, text=e7, fill='black', font=("Helvetica", 8), anchor='w')

                        # cia row

                        canva.create_text(335, rt7, text=c7, fill='black', font=("Helvetica", 8), anchor='w')

                        # total row

                        canva.create_text(380, rt7, text=to7, fill='black', font=("Helvetica", 8), anchor='w')

                        # no.of.credits row

                        canva.create_text(418, rt7, text=cr7, fill='black', font=("Helvetica", 8), anchor='w')

                        # grade points row

                        canva.create_text(458, rt7, text=g_p7, fill='black', font=("Helvetica", 8), anchor='w')

                        # grade row

                        canva.create_text(503, rt7, text=gr7, fill='black', font=("Helvetica", 8), anchor='w')

                        # result row

                        canva.create_text(540, rt7, text=re7, fill='black', font=("Helvetica", 8), anchor='w')

                        # paper9
                        # sem row

                        canva.create_text(23, rt8, text=a8, fill='black', font=("Helvetica", 8), anchor='w')

                        # part row

                        try:
                            canva.create_text(55, rt8, text=sec[8], fill='black', font=("Helvetica", 8), anchor='w')
                        except IndexError:
                            pass

                        # subject/paper row

                        canva.create_text(75, rt8, text=va80, fill='black', font=("Helvetica", 8), anchor='w')
                        canva.create_text(75, rt8 + 10, text=va81, fill='black', font=("Helvetica", 8), anchor='w')

                        # eose row

                        canva.create_text(303, rt8, text=e8, fill='black', font=("Helvetica", 8), anchor='w')

                        # cia row

                        canva.create_text(335, rt8, text=c8, fill='black', font=("Helvetica", 8), anchor='w')

                        # total row

                        canva.create_text(380, rt8, text=to8, fill='black', font=("Helvetica", 8), anchor='w')

                        # no.of.credits row

                        canva.create_text(418, rt8, text=cr8, fill='black', font=("Helvetica", 8), anchor='w')

                        # grade points row

                        canva.create_text(458, rt8, text=g_p8, fill='black', font=("Helvetica", 8), anchor='w')

                        # grade row

                        canva.create_text(503, rt8, text=gr8, fill='black', font=("Helvetica", 8), anchor='w')

                        # result row

                        canva.create_text(540, rt8, text=re8, fill='black', font=("Helvetica", 8), anchor='w')

                        # paper10
                        # sem row

                        canva.create_text(23, rt9, text=a9, fill='black', font=("Helvetica", 8), anchor='w')

                        # part row

                        try:
                            canva.create_text(55, rt9, text=sec[9], fill='black', font=("Helvetica", 8), anchor='w')
                        except IndexError:
                            pass

                        # subject/paper row

                        canva.create_text(75, rt9, text=va90, fill='black', font=("Helvetica", 8), anchor='w')
                        canva.create_text(75, rt9, text=va91, fill='black', font=("Helvetica", 8), anchor='w')

                        # eose row

                        canva.create_text(303, rt9, text=e9, fill='black', font=("Helvetica", 8), anchor='w')

                        # cia row

                        canva.create_text(335, rt9, text=c9, fill='black', font=("Helvetica", 8), anchor='w')

                        # total row

                        canva.create_text(380, rt9, text=to9, fill='black', font=("Helvetica", 8), anchor='w')

                        # no.of.credits row

                        canva.create_text(418, rt9, text=cr9, fill='black', font=("Helvetica", 8), anchor='w')

                        # grade points row

                        canva.create_text(458, rt9, text=g_p9, fill='black', font=("Helvetica", 8), anchor='w')

                        # grade row

                        canva.create_text(503, rt9, text=gr9, fill='black', font=("Helvetica", 8), anchor='w')

                        # result row

                        canva.create_text(540, rt9, text=re9, fill='black', font=("Helvetica", 8), anchor='w')

                        # end of semester

                        endy0 = x01 + x02 + x03 + x04 + x05 + x06 + x07 + x08 + x09 + x00
                        canva.create_text(endx, endy + endy0 + 40, text='## END OF THE SEMESTER ##', fill='black',
                                          font=("Helvetica", 8), anchor='w')

                        ws.mainloop()

                    connection.commit()
                    connection.close()

                else:
                    messagebox.showerror('error', 'please enter the semester between 1 to 6')
            else:
                messagebox.showerror("Error", "Please check register number")
        else:
            messagebox.showerror("Error", "Please enter the semester number in integer")
    else:
        messagebox.showerror('error', 'please enter the register number between 7 to 8 character')


def clearAll():
    REG.set('')
    SEM.set('')


def Quit():
    root.quit()


btn_frame = Frame(entries_frame, bg="#535c68")
btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
btnsearch = Button(btn_frame, command=show, text="Search Details", width=15, font=("Calibri", 16, "bold"),
                   fg="white", bg="#16a085", bd=0)
btnsearch.grid(row=0, column=0)
btnclear = Button(btn_frame, command=clearAll, text="Clear Details", width=15, font=("Calibri", 16, "bold"),
                  fg="white", bg="#2980b9", bd=0)
btnclear.grid(row=0, column=1, padx=10)
btnquit = Button(btn_frame, command=Quit, text="Quit", width=15, font=("Calibri", 16, "bold"),
                 fg="white", bg="red", bd=0)
btnquit.grid(row=0, column=2, padx=10)

conn = sqlite3.connect("database.db")
cur = conn.cursor()

root.mainloop()
