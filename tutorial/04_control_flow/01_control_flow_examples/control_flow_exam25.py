

def concat(*args, sep = "/"):
    return sep.join(args)


concat("earth", "mars", "venus")
# earth/mars/venus

concat("earth", "mars", "venus", sep = ".")
# earth.mars.venus