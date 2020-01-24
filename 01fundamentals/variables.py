# numeric data types

number: int = "74"

number_float: float = "1.23"

print(number)


# Boolean data type

boolean_true: bool = True # 1 - int(boolean_true)

boolean_false: bool = False # 0 - int(boolean_false)


# String data type


char = 'something' # Only short string
char = "something" # Only short string

char_long = """
  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed viverra sapien at rutrum fermentum. Nam sodales ligula ut eros pellentesque, vitae eleifend dui iaculis. Nam semper augue et sapien elementum, in commodo lectus hendrerit. Integer volutpat venenatis finibus. Aenean malesuada euismod magna, et fringilla arcu condimentum a. Maecenas vel leo nec justo dignissim facilisis in vel arcu. Aliquam erat volutpat.
""" # This format, allow long string

char_with_escape = "Hello \
world"


name = "Tito" # string
age = 17 # number
size = 1.84 # float

print("Name %s Age %d Size %f" % (name, age, size))