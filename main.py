import customtkinter as ctk
import json
import pyperclip


class App(ctk.CTk):
    def __init__(self):
        # initial setup
        super().__init__()
        self.title("ColorX")
        self.geometry('600x500')
        self.resizable(width=False, height=False)

        # layout
        self.rowconfigure(index=0, weight=1 ,uniform='a')
        self.columnconfigure(index=0, weight=1, uniform='a')
        self.columnconfigure(index=1, weight=2, uniform='a')

        # data
        self.r = ctk.IntVar(value=100)
        self.g = ctk.IntVar(value=100)
        self.b = ctk.IntVar(value=100)

        self.rgb = [self.r, self.g, self.b]
        self.hex_string = ctk.StringVar(value='#646464')
        
        # widgets
        ColorInfoDisplay(master=self, rgb=self.rgb, hex_string=self.hex_string)
        ColorDisplay(master=self, rgb=self.rgb, hex_string=self.hex_string)

        # run
        self.mainloop()

class ColorInfoDisplay(ctk.CTkFrame):
    def __init__(self, master, rgb, hex_string):
        # initial setup
        super().__init__(master=master)
        self.rgb = rgb
        self.hex_string = hex_string

        # layout
        self.rowconfigure(index=(0,1,2), weight=1, uniform='a')
        self.rowconfigure(index=3, weight=3, uniform='a')
        self.columnconfigure(index=0, weight=1, uniform='a')

        # widgets
        self.RGBDisplay().grid(row=2, column=0, sticky='nswe', padx=5, pady=5)
        self.CMYDisplay().grid(row=1, column=0, sticky='nswe', padx=5, pady=5)
        self.HEXDisplay().grid(row=0, column=0, sticky='nswe', padx=5, pady=5)
        self.Sliders().grid(row=3, column=0, sticky='nswe', padx=5, pady=5)

        # place
        self.grid(row=0, column=0, sticky='nswe', padx=5, pady=5)
    

    def RGBDisplay(self):
        frame = ctk.CTkFrame(master=self, corner_radius=5)

        # layout
        frame.rowconfigure(index=0, weight=1, uniform='a')
        frame.rowconfigure(index=1, weight=2, uniform='a')
        frame.columnconfigure(index=(0,1,2), weight=1, uniform='a')

        # data
        r_str = ctk.StringVar(value=str(self.rgb[0].get()))
        g_str = ctk.StringVar(value=str(self.rgb[1].get()))
        b_str = ctk.StringVar(value=str(self.rgb[2].get()))

        r_str.trace(mode='w', callback=lambda *args: self.rgb[0].set(int(r_str.get())) if r_str.get().isnumeric() and 0 <= int(r_str.get()) <= 255 else self.rgb[0].set(0))   
        g_str.trace(mode='w', callback=lambda *args: self.rgb[1].set(int(g_str.get())) if g_str.get().isnumeric() and 0 <= int(g_str.get()) <= 255 else self.rgb[1].set(0))   
        b_str.trace(mode='w', callback=lambda *args: self.rgb[2].set(int(b_str.get())) if b_str.get().isnumeric() and 0 <= int(b_str.get()) <= 255 else self.rgb[2].set(0))

        self.rgb[0].trace(mode='w', callback=lambda *args: r_str.set(str(self.rgb[0].get())))
        self.rgb[1].trace(mode='w', callback=lambda *args: g_str.set(str(self.rgb[1].get())))
        self.rgb[2].trace(mode='w', callback=lambda *args: b_str.set(str(self.rgb[2].get())))

        # widgets
        font_small = ctk.CTkFont(family='Ubuntu', size=14, weight='bold')
        ctk.CTkLabel(master=frame, text='RGB', fg_color='black', font=font_small).grid(row=0, column=0, columnspan=3, sticky='nswe')
        ctk.CTkEntry(master=frame, placeholder_text='255', textvariable=r_str, font=font_small).grid(row=1, column=0, sticky='nswe', padx=5, pady=5)
        ctk.CTkEntry(master=frame, placeholder_text='255', textvariable=g_str, font=font_small).grid(row=1, column=1, sticky='nswe', padx=5, pady=5)
        ctk.CTkEntry(master=frame, placeholder_text='255', textvariable=b_str, font=font_small).grid(row=1, column=2, sticky='nswe', padx=5, pady=5)

        # place
        return frame
    
    def CMYDisplay(self):
        frame = ctk.CTkFrame(master=self, corner_radius=5)

        # layout
        frame.rowconfigure(index=0, weight=1, uniform='a')
        frame.rowconfigure(index=1, weight=2, uniform='a')
        frame.columnconfigure(index=(0,1,2), weight=1, uniform='a')

        # data
        # c = 225 - r; m = 255 - g; y = 255 - b
        c_str = ctk.StringVar(value=str(255 - self.rgb[0].get()))
        m_str = ctk.StringVar(value=str(255 - self.rgb[1].get()))
        y_str = ctk.StringVar(value=str(255 - self.rgb[2].get()))

        c_str.trace(mode='w', callback=lambda *args: self.rgb[0].set(255 - int(c_str.get())) if c_str.get().isnumeric() and 0 <= int(c_str.get()) <= 255 else self.rgb[0].set(255))   
        m_str.trace(mode='w', callback=lambda *args: self.rgb[1].set(255 - int(m_str.get())) if m_str.get().isnumeric() and 0 <= int(m_str.get()) <= 255 else self.rgb[1].set(255))   
        y_str.trace(mode='w', callback=lambda *args: self.rgb[2].set(255 - int(y_str.get())) if y_str.get().isnumeric() and 0 <= int(y_str.get()) <= 255 else self.rgb[2].set(255))

        self.rgb[0].trace(mode='w', callback=lambda *args: c_str.set(str(255 - self.rgb[0].get())))
        self.rgb[1].trace(mode='w', callback=lambda *args: m_str.set(str(255 - self.rgb[1].get())))
        self.rgb[2].trace(mode='w', callback=lambda *args: y_str.set(str(255 - self.rgb[2].get())))

        # widgets
        font_small = ctk.CTkFont(family='Ubuntu', size=14, weight='bold')
        ctk.CTkLabel(master=frame, text='CMY', fg_color='black', font=font_small).grid(row=0, column=0, columnspan=3, sticky='nswe')
        ctk.CTkEntry(master=frame, placeholder_text='255', textvariable=c_str, font=font_small).grid(row=1, column=0, sticky='nswe', padx=5, pady=5)
        ctk.CTkEntry(master=frame, placeholder_text='255', textvariable=m_str, font=font_small).grid(row=1, column=1, sticky='nswe', padx=5, pady=5)
        ctk.CTkEntry(master=frame, placeholder_text='255', textvariable=y_str, font=font_small).grid(row=1, column=2, sticky='nswe', padx=5, pady=5)

        # place
        return frame

    def HEXDisplay(self):
        frame = ctk.CTkFrame(master=self, corner_radius=5)

        # layout
        frame.rowconfigure(index=0, weight=1, uniform='a')
        frame.rowconfigure(index=1, weight=2, uniform='a')
        frame.columnconfigure(index=0, weight=1, uniform='a')

        # data
        def rgb_to_hex(rgb):
            string = ('{:02X}' * 3).format(rgb[0].get(), rgb[1].get(), rgb[2].get())
            return '#' + string
        
        def is_hex_color(hex_string: str):
            if not hex_string.startswith('#'):
                return False
            
            if len(hex_string) != 7:
                return False
            
            for letter in hex_string[1:]:
                if not letter.upper().isnumeric() and letter not in ['A','B','C','D','E','F']:
                   return False
            
            return True
    
        def hex_to_rgb(hex_string):
            new_rgb = tuple(int(hex_string[i:i+2], 16) for i in (1, 3, 5))
            self.rgb[0].set(new_rgb[0])
            self.rgb[1].set(new_rgb[1])
            self.rgb[2].set(new_rgb[2])
        
        self.hex_string.trace(mode='w', callback=lambda *args: hex_to_rgb(self.hex_string.get()) if is_hex_color(self.hex_string.get()) else None)

        
        self.rgb[0].trace(mode='w', callback=lambda *args: self.hex_string.set(rgb_to_hex(self.rgb)))
        self.rgb[1].trace(mode='w', callback=lambda *args: self.hex_string.set(rgb_to_hex(self.rgb)))
        self.rgb[2].trace(mode='w', callback=lambda *args: self.hex_string.set(rgb_to_hex(self.rgb)))

        # widgets
        font_large = ctk.CTkFont(family='Ubuntu', size=20, weight='bold')
        font_small = ctk.CTkFont(family='Ubuntu', size=14, weight='bold')
        ctk.CTkLabel(master=frame, text='HEX', fg_color='black', font=font_small).grid(row=0, column=0, sticky='nswe')
        ctk.CTkEntry(master=frame, placeholder_text='#FFFFFF', justify='center', font=font_large, textvariable=self.hex_string).grid(row=1, column=0, sticky='nswe', padx=5, pady=5)

        # place
        return frame

    def Sliders(self):
        frame = ctk.CTkFrame(master=self)
        
        # layout
        frame.rowconfigure(index=0, weight=1, uniform='a')
        frame.columnconfigure(index=(0,1,2), weight=1, uniform='a')

        # widgets
        slider1 = ctk.CTkSlider(master=frame, orientation='vertical' , variable=self.rgb[0], from_=0, to=255, width=20, button_color='red', progress_color='#7f0000', button_hover_color='#7f0000')
        slider2 = ctk.CTkSlider(master=frame, orientation='vertical', variable=self.rgb[1], from_=0, to=255, width=20, button_color='green', progress_color='#005900', button_hover_color='#005900')
        slider3 = ctk.CTkSlider(master=frame, orientation='vertical', variable=self.rgb[2], from_=0, to=255, width=20, button_color='blue', progress_color='#00007f', button_hover_color='#00007f')

        # place
        slider1.grid(row=0, column=0, sticky='ns')
        slider2.grid(row=0, column=1, sticky='ns')
        slider3.grid(row=0, column=2, sticky='ns')

        return frame

class ColorDisplay(ctk.CTkFrame):
    def __init__(self, master, rgb, hex_string):
        # initial setup
        super().__init__(master=master)
        self.rgb = rgb
        self.hex_string = hex_string

        # layout
        self.rowconfigure(index=(0,1), weight=1, uniform='a')
        self.columnconfigure(index=0, weight=4, uniform='a')
        self.columnconfigure(index=1, weight=1, uniform='a')

        # widgets
        self.canvas().grid(row=0, column=0, sticky='nswe', padx=5, pady=5)
        self.daken_lighten_control().grid(row=0, column=1, sticky='nswe', padx=5, pady=5)
        ColorTools(master=self, hex_string=self.hex_string)

        # place
        self.grid(row=0, column=1, sticky='nswe', padx=5, pady=5)
    
    def canvas(self):
        canvas = ctk.CTkCanvas(master=self, bg=self.hex_string.get())
        self.hex_string.trace(mode='w', callback=lambda *args: canvas.configure(bg=self.hex_string.get()))
        return canvas
    
    def daken_lighten_control(self):
        frame = ctk.CTkFrame(master=self)
        
        # layout
        frame.rowconfigure(index=(0,1,2,3), weight=1, uniform='a')
        frame.columnconfigure(index=0, weight=1, uniform='a')

        # widgets
        font_large = ctk.CTkFont(family='Ubuntu', size=16, weight='bold')
        ctk.CTkButton(master=frame, text="+", font=font_large, command=lambda: self.update_rgb(rgb=[self.rgb[i].get() + 5 for i in range(3)])).grid(row=0, column=0, sticky='nswe', padx=10, pady=5)
        ctk.CTkButton(master=frame, text="+", font=font_large, command=lambda: self.update_rgb(rgb=[self.rgb[i].get() + 1 for i in range(3)])).grid(row=1, column=0, sticky='nswe', padx=15, pady=10)
        ctk.CTkButton(master=frame, text="-", font=font_large, command=lambda: self.update_rgb(rgb=[self.rgb[i].get() - 1 for i in range(3)])).grid(row=2, column=0, sticky='nswe', padx=15, pady=10)
        ctk.CTkButton(master=frame, text="-", font=font_large, command=lambda: self.update_rgb(rgb=[self.rgb[i].get() - 5 for i in range(3)])).grid(row=3, column=0, sticky='nswe', padx=10, pady=5)
        return frame

    def update_rgb(self, rgb):        
        for i, value in enumerate(rgb):
            if value > 255:
                value = 255
            if value < 0:
                value = 0
            self.rgb[i].set(value)

class ColorTools(ctk.CTkFrame):
    def __init__(self, master, hex_string):
        # initial setup
        super().__init__(master=master)
        self.hex_string = hex_string

        # layout
        self.rowconfigure(index=(0,1,2,3,4), weight=1, uniform='a')
        self.columnconfigure(index=(0,1,2,3,4,5,6,7), weight=1, uniform='a')

        # widgets
        self.color_grid = [[(ctk.StringVar(value='#000000'), ctk.CTkLabel(master=self, text='', corner_radius=5)) for _ in range(8)] for _ in range(5)]

        # place widgets
        for i in range(5):
            for j in range(8):
                color, label = self.color_grid[i][j]
                
                def make_lambda_copy(color):
                    return lambda event: self.copy_to_clipboard(event, color)
                
                label.bind('<Button-1>', make_lambda_copy(color))
                label.grid(row=i, column=j, sticky='nswe', padx=5, pady=5)
        
        
        self.load_grid()
        
        # place
        self.grid(row=1, column=0, columnspan=2, sticky='nswe', padx=5, pady=5)
    
    def load_grid(self):
        f = open('palettes.json', 'r')
        data = json.load(f)['colors']

        for i in range(5):
            for j in range(8):
                color, label = self.color_grid[i][j]
                color.set(data[i][j])
                label.configure(fg_color = color.get())
    
    def copy_to_clipboard(self, event, color):
        pyperclip.copy(color.get())
        self.hex_string.set(color.get())


if __name__ == '__main__':
    App()