import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog

class SilkscreenWindow:
    def __init__(self, root):
        self.root = root
        self.back_ground = "#333"
        self.root.geometry("400x300+20+20")
        self.root.title("Silkscreen:")
        self.img_max_hight = 600
        self.img_max_width = 1200
        self.root.configure(bg=self.back_ground)

        self.path_label = tk.Label(root, text="Image_Path", bg="#333", fg="white")
        self.image_label = tk.Label(root, bg="#333")
        self.path_entry = tk.Entry(root)
        #self.load_button = tk.Button(root, text="Load Image", command=self.load_image, width=20, bg="#555", fg="white")
        #Поиск в файлах
        self.browse_button = tk.Button(root, text="Browse", command=self.browse_file, bg="#555", fg="white")



        self.path_label.grid(row=0, column=0, padx = 10, pady=3,sticky="nsew")
        self.root.grid_columnconfigure(1, weight=1)
        self.path_entry.grid(row=1, column=0,columnspan=3,padx=10,pady=3,sticky="nsew")
        self.browse_button.grid(row=1, column=3,padx=5,pady=3,sticky="nsew")
        self.image_label.grid(row=2, column=0,columnspan=4,sticky="nsew")


    def browse_file(self):
        filename = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
        if filename:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(tk.END, filename)
            self.load_image()

    def load_image(self):
        path = self.path_entry.get()
        try:
            image = Image.open(path)
            width, height = image.size
            if self.img_max_width > 1200 or height > self.img_max_hight:
                new_height = self.img_max_hight
                height_percent = (new_height / float(image.size[1]))
                new_width = int((float(image.size[0]) * float(height_percent)))
                image = image.resize((new_width, new_height))

            image = ImageTk.PhotoImage(image)
            self.image_label.config(image=image)
            self.image_label.image = image
            self.root.geometry(f"{image.width()}x{image.height() + 120}")  # Изменение размера окна


        except Exception as e:
            print("Error loading image:", e)



if __name__ == "__main__":
    root = tk.Tk()
    app = SilkscreenWindow(root)
    root.mainloop()
