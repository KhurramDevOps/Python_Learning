import tkinter as tk
import tkinter.messagebox


def show_Mark_Sheet():
    # Data Validation for Marks Input
    # we will use try except block to handle invalid input for marks cuz before when we enter string instead of number it give error
    # on the terminal and also show message box but crash the program so now it will show error message box instead of crashing
    

    try:
        totalMarks = float(subject1Marks.get()) + float(subject2Marks.get()) + float(subject3Marks.get()) + float(subject4Marks.get()) + float(subject5Marks.get())
        # New Window
        printWindow = tk.Tk()
        printWindow.title("Marksheet")
        printWindow.geometry("250x350")
        
        # Heading

        tk.Label(printWindow, text="Marksheet").grid(row=0, columnspan=2, pady=15)

        # Mark Sheet Window Labels
        tk.Label(printWindow,text="Student Name").grid(row=1,padx=25, pady=5)
        tk.Label(printWindow, text="Father Name").grid(row=2)
        tk.Label(printWindow, text="Roll#").grid(row=3)
        tk.Label(printWindow, text="Address").grid(row=4)
        tk.Label(printWindow, text="Subject 1 Marks").grid(row=5)
        tk.Label(printWindow, text="Subject 2 Marks").grid(row=6)
        tk.Label(printWindow, text="Subject 3 Marks").grid(row=7)
        tk.Label(printWindow, text="Subject 4 Marks").grid(row=8)
        tk.Label(printWindow, text="Subject 5 Marks").grid(row=9)
        tk.Label(printWindow, text="Average Marks").grid(row=10)
        tk.Label(printWindow, text="Percentage").grid(row=11)
        tk.Label(printWindow, text="Grade").grid(row=12)

        # Mark Sheet Window Output Values
        tk.Label(printWindow,text=studentName.get()).grid(row=1,column=1, padx=50)
        tk.Label(printWindow, text=fatherName.get()).grid(row=2, column=1)
        tk.Label(printWindow,text=rollNo.get()).grid(row=3,column=1)
        tk.Label(printWindow,text=address.get()).grid(row=4,column=1)
        tk.Label(printWindow,text=subject1Marks.get()).grid(row=5,column=1)
        tk.Label(printWindow, text=subject2Marks.get()).grid(row=6, column=1)
        tk.Label(printWindow, text=subject3Marks.get()).grid(row=7, column=1)
        tk.Label(printWindow, text=subject4Marks.get()).grid(row=8, column=1)
        tk.Label(printWindow, text=subject5Marks.get()).grid(row=9, column=1)
        tk.Label(printWindow, text=culculate_Average(totalMarks)).grid(row=10, column=1)
        tk.Label(printWindow, text=str(calculate_Percentage(totalMarks))+"%").grid(row=11, column=1)
        tk.Label(printWindow, text=get_Grade(totalMarks)).grid(row=12, column=1)
    
    except ValueError:
        tkinter.messagebox.showerror("Invalid Input", "Please enter valid numeric marks for all subjects.")
def culculate_Average(totalMarks):
    return '%.1f'%((totalMarks)/5)

def calculate_Percentage(totalMarks):
    percent = '%.2f'%((totalMarks/500)*100)
    return percent

def get_Grade(totalMarks):
    if(float(calculate_Percentage(totalMarks))>= 50):
        return "Pass"
    else:
        return "Fail"

master = tk.Tk()
master.geometry("350x600")
master.title("Enter Marksheet Information")

# Input Text
studentName = tk.Entry(master)
fatherName = tk.Entry(master)
rollNo = tk.Entry(master)
address = tk.Entry(master)
subject1Marks = tk.Entry(master)
subject2Marks = tk.Entry(master)
subject3Marks = tk.Entry(master)
subject4Marks = tk.Entry(master)
subject5Marks = tk.Entry(master)

# Logo error on this part if image not found so we use try except to handle it
try:
    logo = tk.PhotoImage(file="itu_logo.png")       
    logo = logo.zoom(10)  # we use the subsample method to reduce the size of the image by half 
                                # cuz when its zoom(10) its make the image too big for the window so we reduce it
                                # if size is already small of logo then zoom 10 works fine. depends on image size
    tk.Label(master,image=logo).grid(row=0, columnspan=2, pady=15)
except Exception:
    tk.Label(master, text="[Logo Missing]", font=("Arial", 10, "italic")).grid(row=0, columnspan=2, pady=15)


# Heading
tk.Label(master,text="Marksheet").grid(row=1, columnspan=2, pady=15)

# Labels
tk.Label(master,text="Student Name").grid(row=2, padx=25)
tk.Label(master,text="Father Name").grid(row=3)
tk.Label(master,text="Roll#").grid(row=4)
tk.Label(master,text="Address").grid(row=5)
tk.Label(master,text="Subject 1 Marks").grid(row=6)
tk.Label(master,text="Subject 2 Marks").grid(row=7)
tk.Label(master,text="Subject 3 Marks").grid(row=8)
tk.Label(master,text="Subject 4 Marks").grid(row=9)
tk.Label(master,text="Subject 5 Marks").grid(row=10)

# Input Text set on Grid
studentName.grid(row=2, column=1, padx=50)
fatherName.grid(row=3,column=1)
rollNo.grid(row=4,column=1)
address.grid(row=5,column=1)
subject1Marks.grid(row=6,column=1)
subject2Marks.grid(row=7,column=1)
subject3Marks.grid(row=8,column=1)
subject4Marks.grid(row=9,column=1)
subject5Marks.grid(row=10,column=1)

# Buttons
tk.Button(master,text="Quit", command=quit, width=10).grid(row=11, column=0, pady=25)
tk.Button(master,text="Submit", command=show_Mark_Sheet, width=15).grid(row=11, column=1)

# Infinite Loop waits for Process to occur until closed
tk.mainloop()
