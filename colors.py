class Colors:
    dark_grey = (26, 31, 40)
    pastel_green = (119, 221, 119)  
    pastel_pink = (255, 182, 193)  
    pastel_orange = (255, 179, 102)  
    pastel_yellow = (253, 253, 150)  
    pastel_purple = (177, 156, 217) 
    pastel_cyan = (178, 255, 255)
    pastel_blue = (174, 198, 207)
    white = (255, 255, 255)
    dark_blue = (44, 44, 127)
    light_blue = (59, 85, 162)

    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey, cls.pastel_green, cls.pastel_pink, cls.pastel_orange, cls.pastel_yellow, cls.pastel_purple, cls.pastel_cyan, cls.pastel_blue]
    