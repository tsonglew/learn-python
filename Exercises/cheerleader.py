#-*- coding: UTF-8 -*-
import time
import curses

stdscr = curses.initscr()

def display_info(str, x, y, colorpair=2):
    global stdscr
    stdscr.addstr(y, x,str, curses.color_pair(colorpair))
    stdscr.refresh()

def get_ch_and_continue():
    global stdscr
    stdscr.nodelay(0)
    ch=stdscr.getch()
    stdscr.nodelay(1)
    return True

def set_win():
    global stdscr
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.noecho()
    curses.cbreak()
    stdscr.nodelay(1)

def unset_win():
    global stdstr
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
    curses.endwin()

if __name__=='__main__':
    pic1 = """
     -------
    | @ | @ |
     --- ---     im a programmer cheerleader from Muxi Studio!
  ^ \   |   /^
      ------
        |
      __/\__
    """
    pic2 = """
     -------
    | @ | @ |
     --- ---     Hello World!
        |
 --***-----***--
        |
      __/\__
    """
    pic3 = """
     -------
    | @ | @ |
     --- ---     Hello bHps!
        |
     -------
  ^_/   |   \_^
      __/\__
    """
    try:
        set_win()
        start = time.time()
        end = time.time()

        while(end-start<5):
            stdscr.clear()
            display_info(pic1,0,5)
            time.sleep(0.1)
            stdscr.clear()
            display_info(pic2,0,5,1)
            time.sleep(0.1)
            stdscr.clear()
            display_info(pic3,0,5)
            time.sleep(0.1)
            end = time.time()

        stdscr.clear()
        display_info('Press any key to continue...',10,10)
        get_ch_and_continue()
    except Exception,e:
        raise e
    finally:
        unset_win()
