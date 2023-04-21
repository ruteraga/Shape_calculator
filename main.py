import shape_calculator as sc

rect = sc.Rectangle(10, 5)
rect.get_area()
rect.get_picture()

sq = sc.Square(5)
rect.get_amount_inside(sq)
sq.get_perimeter()
sq.__str__()