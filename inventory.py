'''inventory manager by: Khashayar Nariman.

This is very simple data manager, i tried to use simple list to keep and
manipulate data, for external database, i didn use CSV format or any module
and database, so the external files are simple text files, i used 2 separate
text files for load - save to and from the list in the program,for GUI i used
tkinter, and pack instead of grid.in this version i use clases '''

import tkinter, time ,os
import tkinter.messagebox 
import shutil 
import winsound

class Inventory:

	def __init__(self):
		
		# -- internal attributes 
		################
		self.container = []
		self.name = ""
		self.price = ""
		self.quantity = ""
		self.info = ""
		
		# Gui attributes 
		#################
		self.main_window = tkinter.Tk()
		self.main_window.title("Inventory manager v2")
		# create top frame 
		self.top_frame = tkinter.Frame(self.main_window)
		self.top_frame.pack()
		# create bottom frame 
		self.bottom_frame = tkinter.Frame(self.main_window)
		self.bottom_frame.pack()
		# create item label and entry 
		self.item_label = tkinter.Label(self.top_frame, text = "Add item")
		self.item_label.pack(side = "left")
		self.item_entry = tkinter.Entry(self.top_frame, width = 30)
		self.item_entry.pack(side = "left")
		# create price label and entry 
		self.price_label = tkinter.Label(self.top_frame, text = "Add price")
		self.price_label.pack(side = "left")
		self.price_entry = tkinter.Entry(self.top_frame, width = 10)
		self.price_entry.pack(side = "left")
		# create quantity label and entry 
		self.quan_label = tkinter.Label(self.top_frame, text = "Quantity")
		self.quan_label.pack(side = "left")
		self.quan_entry = tkinter.Entry(self.top_frame, width = 10)
		self.quan_entry.pack(side = "left")
		# create info label and entry 
		self.info_label = tkinter.Label(self.top_frame, text = "Info")
		self.info_label.pack(side = "left")
		self.info_entry = tkinter.Entry(self.top_frame, width = 30)
		self.info_entry.pack(side = "left")
		# create search label and entry 
		self.search_label = tkinter.Label(self.top_frame, text = "Search")
		self.search_label.pack(side = "left")
		self.search_entry = tkinter.Entry(self.top_frame, width = 15)
		self.search_entry.pack(side = "left")
		# Create buttons 
		b_add = tkinter.Button(self.bottom_frame, text = "Add", command = self.add_item)
		b_add.pack(side = "left")
		
		b_remove = tkinter.Button(self.bottom_frame, text = "Remove", \
		command = self.remove_item)
		b_remove.pack(side = "left")
		
		b_save = tkinter.Button(self.bottom_frame, text = "Save",\
		command = self.save_item)
		b_save.pack(side = "left")
		
		b_list = tkinter.Button(self.bottom_frame, text = "List",\
		command = self.list_items)
		b_list.pack(side = "left")
		
		b_search = tkinter.Button(self.bottom_frame, text = "Search",\
		command = self.search_item)
		b_search.pack(side = "left")
		
		b_load_backup = tkinter.Button(self.bottom_frame, text = "Load backup",\
		command = self.load_backup)
		b_load_backup.pack(side = "left")
		
		b_save_exit = tkinter.Button(self.bottom_frame, text = "Save/Exit",\
		command = self.save_exit)
		b_save_exit.pack(side = "left")
		# tk main loop 
		tkinter.mainloop()
		
	def add_item(self):
		self.name = self.item_entry.get()
		self.price = self.price_entry.get()
		self.quantity = self.quan_entry.get()
		self.info = self.info_entry.get()		
		
		data_check = [item for item in self.container if(str(item[0])) == str(self.name)]
		if len(data_check) == 0:
			self.container.append([self.name, self.price, self.quantity, self.info])
		else:
			tkinter.messagebox.showinfo("message", "Item is in inventory")
		data_check.clear()
			
		winsound.Beep(2500, 70)
		self.item_entry.delete(0, "end")
		self.price_entry.delete(0, "end")
		self.quan_entry.delete(0, "end")
		self.info_entry.delete(0, "end")
		

	def save_item(self):
		data_file = open("data.txt", "w")
		temp_data_file = open("temp_data.txt", "w")
		try:
			data_file.write("\n".join (str(item) for item in self.container))
			data_file.close()
			tkinter.messagebox.showinfo("Save", "Complete")
		except TypeError:
			tkinter.messagebox.showinfo("Eroor", " Type Error")
		try:
			if len(temp_data_file) != 0:
				temp_data_file.write()
			temp_data_file.close()
		except TypeError:
			pass
					
	def remove_item(self):
		search = self.search_entry.get()
		for item in self.container:
			if search in item:
				self.container.remove(item)
				self.search_entry.delete(0, "end")
				tkinter.messagebox.showinfo("Remove", "Complete")
	
	def list_items(self):
		root = tkinter.Tk()
		scrollbar = tkinter.Scrollbar(root)
		scrollbar.pack(side = "right")
		list_box = tkinter.Listbox(root)
		list_box.config(width = 30)
		list_box.pack()
		for item in self.container:
			list_box.insert("end", item)
		list_box.config(yscrollcommand = scrollbar.set)
		scrollbar.config(command = list_box.yview)
		
	def search_item(self):
		search = self.search_entry.get()
		available = [item for item in self.container if search in item]
		if len(available) != 0:
			tkinter.messagebox.showinfo("Search", "Item is available")
		else:
			tkinter.messagebox.showinfo("Search", "Item in not available")
		self.search_entry.delete(0, "end")
		available.clear()
		
	def load_backup(self):
			data_file = open("data.txt", "r")
			data_temp_file = open("temp_data.txt", "w")
			shutil.copy("data.txt", "temp_data.txt")
			for line in data_file.readlines():
				for item in line[0 : -1].split("\n"):
					self.container.append(item)
			data_file.close()
			tkinter.messagebox.showinfo("load", "Complete")
			winsound.Beep(2000, 100)
			try:
				data_file = open("data.txt", "w")
				data_file.write("")
				data_file.close()
				data_temp_file.close()
			except TypeError:
				tkinter.messagebox.showinfo("Load", "Error")
					
		
	def save_exit(self):
		data_file = open("data.txt", "w")
		temp_data_file = open("temp_data.txt", "w")
		try:
			data_file.write("\n".join (str(item) for item in self.container))
			data_file.close()
			tkinter.messagebox.showinfo("Save", "Complete")
		except TypeError:
			tkinter.messagebox.showinfo("Error", " Type Error")
		try:
			if len(temp_data_file) != 0:
				temp_data_file.write()
			temp_data_file.close()
		except TypeError:
			pass
		self.main_window.destroy()
		exit()

		
inventory = Inventory()



