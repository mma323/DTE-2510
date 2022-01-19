#Programmet tar i mot et rektangel sin lengde og bredde
#og returnerer rektangelets omkrets, areal og diagonalen
#i rektangelet sin lengde


rectangle_width  = float( input("Width: ") )
rectangle_height = float ( input("Height ") )

rectangle_perimeter = 2 * (rectangle_width + rectangle_height)
rectangle_area      = rectangle_width * rectangle_height
rectangle_diagonal  = ( rectangle_width**2 + rectangle_height**2 )**(1/2)

print(f"Rektangelet med bredde {rectangle_width} og {rectangle_height}" +
"har følgende verdier:")
print(f"Omkrets: {rectangle_perimeter}")
print(f"Areal: {rectangle_area}")
print(f"Diagonal: {rectangle_diagonal}")
