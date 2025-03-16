

table = {k : str(v) for k, v in vars().items()}

message = " ".join([f'{k}: ' + '{' + k +'};' for k in table.keys()])

print(message.format(**table))
# __name__: __main__; __doc__: None; __package__: None; __loader__: <_frozen_importlib_external.SourceFileLoader object at 0x107c6eca0>; __spec__: None; __annotations__: {}; __builtins__: <module 'builtins' (built-in)>; __file__: /../../learning-python/practice-python/tutorial/07_io/07_io_examples/io_exam13.py; __cached__: None;