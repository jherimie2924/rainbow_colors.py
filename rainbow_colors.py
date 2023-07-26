rainbow_colors = ['красный', 'оранжевый', 'желтый', 'зеленый', 'голубой', 'синий', 'фиолетовый']
brightness = 50

for color in rainbow_colors:
    r, g, b = (0, 0, 0)
    
    if color == 'красный':
        r = 255
    elif color == 'оранжевый':
        r = 255
        g = 165
    elif color == 'желтый':
        r = 255
        g = 255
    elif color == 'зеленый':
        g = 128
    elif color == 'голубой':
        g = 255
        b = 255
    elif color == 'синий':
        b = 255
    elif color == 'фиолетовый':
        r = 128
        b = 128
    
    r = int(r * brightness / 100)
    g = int(g * brightness / 100)
    b = int(b * brightness / 100)
    
    print(f"{color}: ({r}, {g}, {b})").


