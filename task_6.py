#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_3():
    i=1
    while i!=0:
        if wall_is_beneath()==False:
            move_right()
        else:
            i=0
    i=1
    while i!=0:
        if wall_is_beneath()==True:
            move_right()
        else:
            i=0


if __name__ == '__main__':
    run_tasks()
