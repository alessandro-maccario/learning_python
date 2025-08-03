from PIL import Image, ImageDraw

# read ascii text from file
text_fp = "C:/solutions/learning_python/learning_python_udemy/course_100_days_of_code/section_3/imgs/ascii.txt"

with open(text_fp, "r") as f:
    ascii_text = f.read()

# Create a new Image
# make sure the dimensions (W and H) are big enough for the ascii art
W, H = (1000, 1000)  # 480, 300
im = Image.new("RGBA", (W, H), "black")

# Draw text to image
draw = ImageDraw.Draw(im)
w, h = draw.textsize(ascii_text)
# draws the text in the center of the image
draw.text(((W - w) / 2, (H - h) / 2), ascii_text, fill="green")


im.resize((1000, 1000))
# Save Image
im.save(
    "C:/solutions/learning_python/learning_python_udemy/course_100_days_of_code/section_3/imgs/treasure_chest.png",
    "PNG",
)
