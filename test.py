#!/bin/env/ python
def mc_switch(switch):
    opt_invalid = False
    while not opt_invalid:
        opt = {1:"Vanilla,", 2:"Chocolate,", 3:"Other"}
        val_switch = opt.get(int(switch))
        print(val_switch)
        return opt.get(switch, "Invalid")
        if opt == "Invalid":
            continue
        else:
            break

SWI = str(input("What icecream flavor.\n1: Vanilla, 2: Chocolate, 3: Other\n~> "))
mc_switch(SWI)
