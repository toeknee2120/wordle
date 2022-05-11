class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    YELLOW = '\033[38;5;3m'     


print(f'{bcolors.GREEN}HELLO{bcolors.END}')
print('test')


# for i in range(0,16):
#     for j in range(0,16):
#         code = str(i * 16 + j)

#         print("001b[38;5;" + code + "m " + code + "\u001b[0m")
#         # print(u"\u001b[38;5;" + code + "m " + code + "\u001b[0m")
