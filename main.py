import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
import silkscreen

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
        self.browse_button = tk.Button(root, text="Browse", command=self.browse_file, bg="#555", fg="white")


        self.color_amount_label = tk.Label(root, text="colors_amount", bg="#333", fg="white")
        self.color_amount_entry = tk.Entry(root)

        self.save_folder_name_label = tk.Label(root, text="save_folder_path", bg="#333", fg="white")
        self.save_folder_name_entry = tk.Entry(root)

        self.start_button = tk.Button(root, text="Start", command=self.start, bg="#555", fg="white")








        self.path_label.grid(row=0, column=0, padx = 10, pady=3,sticky="nsew")
        self.root.grid_columnconfigure(1, weight=1)
        self.path_entry.grid(row=1, column=0,columnspan=3,padx=10,pady=3,sticky="nsew")
        self.browse_button.grid(row=1, column=3,padx=5,pady=3,sticky="nsew")
        self.image_label.grid(row=2, column=0,columnspan=4,pady=3,sticky="nsew")

    def start(self):
        image_path = self.path_entry.get()
        colors_amount = int(self.color_amount_entry.get())
        save_folder_name = self.save_folder_name_entry.get()
        clustered_img_path = save_folder_name + "\\clustered_image.jpg"
        silkscreen.save_color_layers(image_path = image_path, output_folder = save_folder_name, clustered_img_path = clustered_img_path, num_colors = colors_amount)

        print("Start")

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
            self.root.geometry(f"{image.width()}x{image.height() + 140}")  # Изменение размера окна

            self.save_folder_name_label.grid(row=3, column=0,padx=10,pady=3,sticky="nsew")
            self.save_folder_name_entry.grid(row=3, column=1,columnspan=3,padx=10,pady=3,sticky="nsew")


            self.color_amount_label.grid(row=4, column=0,pady=3,sticky="nsew")
            self.color_amount_entry.grid(row=4, column=1,padx=10,pady=3,sticky="nsew")

            self.start_button.grid(row=4, column=2,padx=10,pady=3,columnspan=3,sticky="nsew")




        except Exception as e:
            print("Error loading image:", e)



if __name__ == "__main__":
    root = tk.Tk()
    app = SilkscreenWindow(root)
    root.mainloop()
