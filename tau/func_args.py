def user_info(name,age=0,city="Tucson"):
    '''This function prints name,age and city
    from an arguement provided to the function.'''

    print("{} is {} years old, from {}".format(name,age,city))

user_info("Janet",58,"Oklahoma City")
# user_info(34,"New York")
user_info(("Micah"))
user_info(age=56,name="Kadeem")