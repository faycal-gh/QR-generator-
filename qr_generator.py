import tkinter as tk;
from tkinter import ttk;
from tkinter import messagebox as mb
from PIL import ImageTk, Image; # pip install pillow
import os;
import qrcode; # pip install qrcode

class view:
	def genera_code(self,frame,Name, Age,isStudent):

		if Name != "" and Age != "":
			
			if isStudent == "Yes":
			
				isStudent = "I am student";
			else:
				isStudent = "I am not student";

			qr = qrcode.QRCode(
			 version = 1,
			 error_correction = qrcode.constants.ERROR_CORRECT_Q, # About 35% or less errors can be corrected
			 box_size = 6,
			 border = 2,
			)
			qr.add_data('My Name is '+Name+' -- My age is '+Age+'\n and '+isStudent); # Url or information that will contain the qr code
		
			qr.make(fit = True);
			
			img = qr.make_image(fill_color = "black", black_color = "black");

			
			output = open("output.png", "wb");
			img.save(output);

			self.QR_Show(frame)

			output.close();

		else:
			mb.showerror("Warning !","Fill all the fields");

	def QR_Show(self,f):
		
		self.canvas = tk.Canvas(f, width = 280, height = 280, bg = "white");
		self.canvas.place(x = 7, y = 10);
		self.img = tk.PhotoImage(file="output.png");
		self.canvas.create_image(140,140, image = self.img);
		

	def ViewGenerateQR(self):
		
		root  = tk.Tk();
		root.resizable(0,0);
		root.title("QR Generator")
		
		f = tk.Frame(root, bg  = "white", bd = 1, width = 300, height = 300);
		f.grid(row=0, column=0, sticky ="NW");
		f.grid_propagate(0)
		f.update()
		
		
		f2 = tk.Frame(root, bd = 1, width = 300, height = 150);
		f2.grid(row=1, column=0, sticky ="NW");
		f2.grid_propagate(0)
		f2.update()
		

		lblName = tk.Label(f2, text = "Your Name: ", font =("Verdana",12));
		lblName.place(x = 60 ,y = 10, anchor = "center");
		txtName = tk.Entry(f2);
		txtName.place(x = 120, y = 0, width=145);			


		lblAge= tk.Label(f2, text = "Age :", font =("verdana", 12));
		lblAge.place(x = 65, y = 40, anchor ="center");

		txtAge = tk.Entry(f2);
		txtAge.place(x = 120, y = 30, width=145);
		
		lblStudent= tk.Label(f2, text = "Student? : ", font =("verdana", 12));
		lblStudent.place(x = 66, y = 70, anchor ="center");

		cbxShow = ttk.Combobox(f2,state="readonly",values=["No","Yes"]);
		cbxShow.current(0)
		cbxShow.place(x = 120, y = 60);

		btnGenerar = tk.Button(f2, text ="Generar QR", command = lambda: self.genera_code(f, txtName.get(), txtAge.get(), cbxShow.get()));

		btnGenerar.place(x = 75, y = 115);
		btnGenerar.config(width=20, height=1);

		root.mainloop();
		

if __name__ == '__main__':

	objView = view();
	objView.ViewGenerateQR();
