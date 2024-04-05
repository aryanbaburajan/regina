import re


def regina(code, ex):
    og_code = code
    for itr in range(10):
        for i in range(0, len(ex), 2):
            # print(ex[i], ex[i+1], code)
            code = re.sub(ex[i], ex[i+1], code)
        if code == og_code:
            break
        else:
            og_code = code
            # print(code)
    return code

# 00a1a2a


regex = [
    # add data
    r'(^[<>,.\[\]+\-]*)$', r'\g<1>00a1a2a',
    # >
    r'(^>[\>\<\,\.\[\]\+\-\s]*)2', r'\g<1>2',
    r'(^>[\>\<\,\.\[\]\+\-\s]*)1', r'\g<1>2',
    r'(^>[\>\<\,\.\[\]\+\-\s]*)0', r'\g<1>1',
    r'^>(.*)$', r'\1',
    # <
    r'(^<[\>\<\,\.\[\]\+\-\s]*)0', r'\g<1>0',
    r'(^<[\>\<\,\.\[\]\+\-\s]*)1', r'\g<1>0',
    r'(^<[\>\<\,\.\[\]\+\-\s]*)2', r'\g<1>1',
    r'^<(.*)$', r'\1',
    # +
    # r'([^<>,.\[\]+\-]).{\1}'

    # clear data
    # r'([^<>,.\[\]+\-]*)$', r'',
]

code = '>++++'
output = regina(code, regex)
print(code)
print(output)
