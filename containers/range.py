def range(a, b=None, c=None):
    '''
    This function should behave exactly like the built - in range function.
    For example:

    >>> list(range(5))
    [0, 1, 2, 3, 4]
    >>> list(range(1, 5))
    [1, 2, 3, 4]
    >>> list(range(1, 5, 2))
    [1, 3]

    HINT:
    If you can figure out how to use the built - in range fu
nction (without modifying the test cases!),
    then feel free to do so.
    That's fairly difficult to do, however, and it's much ea
sier to just implement this function normally using the yie
ld syntax.

    NOTE:
    For efficiency reasons, Python's built - in range object
 is written in the C programming language rather than nativ
ely in python.
    You can find the source code online at https: // hg.pyth
on.org / cpython / file / ee7b713fec71 / Objects / rangeobj
ect.c
    The link takes you to a file that is 1445 lines long,
    and all it does is implement this simple functionality.
    My easy to read Python implementation of this function i
s just 15 lines long.
    (And with some code golf I also wrote a less readable ve
rsion that is only 4 lines.)
    It is very common for C programs to be 100x longer than
their corresponding python programs.
    C code must manage lots of details about the computer ma
nually that python code automates for you.
    Carefully written C code can be faster than the correspo
nding python code because it can remove some of the overhea
d of this automation process,
    but the resulting code is much longer and harder to read / write.
    '''
    if b is None:
        top = a
        bot = 0
    else:
        top = b
        bot = a
    if c is None:
        increment = 1
    else:
        increment = c
    if increment > 0:
        up = True
    else:
        up = False

    while (bot < top and up) or (bot > top and not up):
        yield bot
        bot += increment
        print(bot)
