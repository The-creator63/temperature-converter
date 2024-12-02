from tkinter import*
#function converting celsius to fareheit
def ctof():
   temp = celsius_txt.get()
   if temp.replace(".","",1).isdigit():
    error_msg.grid_forget()
    f = (float(temp) * 9/5) + 32
    farenheit_output.config(text = "Farenheit is "+ str(f))
   else:
    error_msg.grid(row = 1,column = 1)
 


root = Tk()
root.geometry("500x250")
root.title("Celsius to Fahrenheit Converter")

main_hd = Label(root,text = "Celsius -> Fahrenheit",fg = "Black",font = ("Times",20,"bold"))
main_hd.pack()

frame = Frame(root)
frame.pack(pady = 20)
celsius_lbl = Label(frame,text = "Enter temperature in Celsius: ",font = ("Times",10,"bold"))
celsius_lbl.grid(row = 0,column = 0)
celsius_txt = Entry(frame)
celsius_txt.grid(row = 0,column = 1)
farenheit_output = Label(frame,font = ("Times", 12,"bold"))
farenheit_output.grid(row = 2, column = 0,columnspan = 2,pady = 10)
error_msg = Label(frame,text = "Please enter a valid input",font = ("Times",8,"bold"),fg = "red")
submit_btn = Button(frame,text = "Submit here",bg = "grey",fg = "black",font = ("Times",12,"bold"),width = 30,padx = 20,pady = 10,command = ctof)
submit_btn.grid(row = 3,column = 0,columnspan = 2,pady = 10)

root.mainloop()