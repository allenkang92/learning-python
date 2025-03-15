

def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

standard_arg(2)
# 2

standard_arg(arg=2)
# 2

pos_only_arg(1)
# 1

pos_only_arg(arg=1)
# line 24, in <module>
# pos_only_arg(arg=1)
# TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'

kwd_only_arg(3)
# line 29, in <module>
#     kwd_only_arg(3)
# TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given

combined_example(1, 2, 3)
# line 34, in <module>
#     combined_example(1, 2, 3)
# TypeError: combined_example() takes 2 positional arguments but 3 were given

combined_example(1, 2, kwd_only = 3)
# 1 2 3

combined_example(pos_only = 1, standard = 2, kwd_only = 3)
# line 42, in <module>
#     combined_example(pos_only = 1, standard = 2, kwd_only = 3)
# TypeError: combined_example() got some positional-only arguments passed as keyword arguments: 'pos_only'
