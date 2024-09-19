

def color_SVG(color = "FF0000FF", width = 100, height = 100, x_pos = 10, y_pos = 10):
  svg_code = f"<svg width='{width}' height='{height}' xmlns='http://www.w3.org/2000/svg'>\n  <rect x='{x_pos}' y='{y_pos}' width='{width - 2*x_pos}' height='{height - 2*y_pos}' fill='#{color}' />\n</svg>"
  file = open(f"{color}.svg", "w")
  file.write(svg_code)
  file.close()

def text_generator(colors = []):
    text = ""
    first = True
    for i in colors:
        #color_SVG(color = i, width = 30, height = 50)
        if not first:
            text += ","
        text += f"<img src='stilvalg/svg/{i}.svg' alt='Fargeboks med kode' style='vertical-align: middle;'> #{i}"
    print(text)
    print()

text_generator(["228B22", "6B8E23", "8B4513", "87CEEB", "FFD700"])
text_generator(["4169E1", "708090", "C0C0C0", "00008B", "E0FFFF"])
text_generator(["FF6EC7", "1B03A3", "9400D3", "FF5F1F", "FFFF33"])
text_generator(["006994", "40E0D0", "F4A460", "2E8B57", "FF7F50"])
text_generator(["FF4500", "FFA500", "8B0000", "800080", "FF00FF"])
text_generator(["704214", "FFFDD0", "A0522D", "F5F5DC", "483C32"])
text_generator(["4B0082", "191970", "C0C0C0", "00CED1", "FF1493"])
text_generator(["FF0000", "FFFFFF", "000000", "FFD700", "000080"])
text_generator(["77DD77", "ADD8E6", "FFB6C1", "E6E6FA", "FFE5B4"])
text_generator(["FF0000", "0000FF", "FFFF00", "008000", "FFA500"])

text_generator(["000000", "FFFFFF", "808080", "FF0000", "00008B"])
text_generator(["654321", "6F4E37", "FFFDD0", "D4AF37", "C68E17"])
text_generator(["228B22", "8B4513", "87CEEB", "FFD700", "F5F5DC"])
text_generator(["000000", "1B03A3", "9400D3", "C0C0C0", "7DF9FF"])
text_generator(["FFFFE0", "FF69B4", "40E0D0", "32CD32", "FFA500"])
text_generator(["000000", "FFFFFF", "D3D3D3", "A9A9A9", "36454F"])
text_generator(["FF6EC7", "32CD32", "00BFFF", "FFA500", "800080"])
text_generator(["D4AF37", "C0C0C0", "9B111E", "0F52BA", "50C878"])
text_generator(["4B0082", "800080", "000000", "FF6EC7", "1B03A3"])