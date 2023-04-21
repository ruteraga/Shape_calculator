class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    area = self.height * self.width
    print("The Area is:", area)

  def get_perimeter(self):
    perimeter = (2 * self.width) + (2 * self.height)
    print("The Perimeter is:", perimeter)

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      print("Too big for picture")

    else:
      for i in range(self.height):
        for j in range(self.width):
          print("*", end='')
        print("\n")

  def get_amount_inside(self, shape):
    shape_width = shape.width
    shape_height = shape.height
    if self.height >= shape.height and self.width >= shape.width:
      df_in_height = int(self.height) / int(shape.height)
      df_in_width = int(self.width) / int(shape.width)
      nbr_of_times = df_in_height * df_in_width
      print("The shape can be inside for ", nbr_of_times, " times")
    else:
      print("The shape is can not be inside the other shape as it is larger")

  def __str__(self):
    i = ("Rectangle(width={0}, height{1})").format(self.width, self.height)
    print(i)


class Square(Rectangle):

  def __init__(self, side):
    self.height = side
    self.width = side

  def set_side(self, side):
    self.side = side

  def __str__(self):
    i = ("Square(side={0})").format(self.width)
    print(i)

  def set_width(self, side):
    self.width = side

  def set_height(self, side):
    self.height = side
