from tkinter import *
import speedtest
import threading

def speedcheck():
    lab_down.config(text="Testing...")
    lab_up.config(text="Testing...")

    def run_test():
        try:
            sp = speedtest.Speedtest()
            sp.get_best_server()

            down = str(round(sp.download() / (10**6), 2)) + " Mbps"
            up = str(round(sp.upload() / (10**6), 2)) + " Mbps"

            app.after(0, lambda: update_ui(down, up))

        except Exception as e:
            print(e)
            app.after(0, lambda: update_ui("Error", "Error"))

    threading.Thread(target=run_test, daemon=True).start()


def update_ui(down, up):
    lab_down.config(text=down)
    lab_up.config(text=up)


app = Tk()
app.title("INTERNET SPEED TEST")
app.geometry("500x650")
app.config(bg="brown")

Label(app, text="INTERNET SPEED TEST",
      font=("Times New Roman", 20, "bold"),
      bg="brown", fg="white").place(x=60, y=40, height=50, width=380)

Label(app, text="DOWNLOAD SPEED",
      font=("Times New Roman", 20, "bold")).place(x=60, y=130, height=50, width=380)

lab_down = Label(app, text="00", font=("Times New Roman", 20, "bold"))
lab_down.place(x=60, y=200, height=50, width=380)

Label(app, text="UPLOAD SPEED",
      font=("Times New Roman", 20, "bold")).place(x=60, y=290, height=50, width=380)

lab_up = Label(app, text="00", font=("Times New Roman", 20, "bold"))
lab_up.place(x=60, y=360, height=50, width=380)

Button(app, text="CHECK SPEED",
       font=("Times New Roman", 20, "bold"),
       relief=RAISED, bg="black", fg="white",
       command=speedcheck).place(x=60, y=460, height=50, width=380)

app.mainloop()