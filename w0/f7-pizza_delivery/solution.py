from time import time
from datetime import datetime

files = []
saved = False
finish_not_saved_comfirm = False

def take(name, price):
    if name not in orders:
            orders[name] = 0
    orders[name] = orders[name] + float(price)
    print("Taking order from " + name + " for " + str(price))
    saved = False

def help_info():
    print('''Unknown command!
            Try one of the following:
            take <name> <price>
            status
            save
            list
            load <number>
            finish''')

def status():
    output = ''
    for key in orders:
        output = output + key + ' - ' + str(orders[key]) + '\n'

    return output


def save():
    ts = time()
    stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S') + '.txt'
    file = open(stamp, "w")
    file.write(str(status()))  
    file.close()
    files.append(stamp)
    saved = True

def list_show():
    for i in range(0, len(files)):
        print('[' + str(i+1) + '] - ' + files[i])

def load1(atrib):
    if saved:
        index = int(atrib)
        orders_tmp = {}
        temp_list = []
        file = open(files[index-1], "r")
        for line in file:
            temp_list = line.split(" - ")
            orders[temp_list[0]] = float(temp_list[1])
    else:
        print('''You have not saved the current order.
                If you wish to discard it, type load <number> again.''')


orders = {}


def main():
    while True:
        command = input("Enter command>")
        #commands = tuple(command.split(" "))
        commands = tuple(command.split(" "))

        if "take" in command:
            take(commands[1], commands[2])
            
        elif "status" in command:
            print(status())

        elif "save" in command:
            save()
        elif "list" in command:
            list_show()
        elif "load" in command:
            orders = load1(commands[1])
        elif "finish" in command:
            break
        else:
            help_info()



if __name__ == '__main__':
    main()