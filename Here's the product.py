import tkinter as tk

root = tk.Tk()
root.title("window")
L3 = tk.Label(root, text="Answer:")
cmd = lambda: L3.config(text=f"Product: {int(E1.get()) * int(E2.get())}")
tk.Label(root, text="Number 1:").pack()
E1 = tk.Entry(root)
E1.pack()

tk.Label(root, text="Number 2:").pack()
E2 = tk.Entry(root)
E2.pack()
tk.Button(root, text="Multiply", command=cmd).pack()

L3.pack()

root.mainloop()