from rembg import remove
from PIL import Image

input_path='input/kucing.jpeg'
output_path='output/newkucing.png'

input=Image.open(input_path)
output=remove(input)
output.save(output_path)