
import pyttsx3
import speech_recognition as sr
from tkinter import *

import buttons, AIassistent, random

TURN = 'user'
LAST = ""

# the only problem with this game is that whem the computer win then the says i won and close the game before it marks the last item that the computer marked .

def TicTacToe():
    """ 
    This class is a 'tic & toe' game -> the class will be activated when the user say to AI that he want to play a game .
    """
    root = Tk()
    root.title("Tic & Toe")
    root.geometry("520x580+350+200")
    root.resizable(False, False)

    empty_spots_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def check_game():
        """
        this function will be activated after every turn (users or computer) .
        the function will check if any of the rows, columns or diagonals marked with the same sign .
        the fucntion will check the buttons -> if somebody won -> the computer will say that the user or himself won -> and close the game .
        Returns: None
        """

        global TURN, LAST

        # list to check all the rows .
        button_rows_list = [
            [a_button, b_button, c_button],
            [d_button, e_button, f_button],
            [g_button, h_button, i_button],
        ]

        # list to check all the columns .
        button_column_list = [
            [a_button, d_button, g_button],
            [b_button, e_button, h_button],
            [c_button, f_button, i_button],
        ]
        
        # list to check diagonals .
        button_diagonal_list = [
            [a_button, e_button, i_button],
            [c_button, e_button, g_button],
        ]

        # check the rows .
        for row in button_rows_list:
            # couters for 'X' and 'O' .
            count_X = 0
            count_O = 0
            # if one of the spots is 'X' or 'O' then count it .
            for item in row:
                if item['text'] == 'X':
                    count_X += 1
                if item['text'] == 'O':
                    count_O += 1
                # when 'X' reach to 3 -> the row is marked with 'X' -> user won -> close the game . 
                if count_X == 3:
                    AIassistent.speak("You won sir . good game !")
                    TURN = "user"
                    LAST = ""
                    root.destroy()
                    return
                # when 'O' reach to 3 -> the row is marked with 'O' -> computer won -> close the game . 
                if count_O == 3:
                    AIassistent.speak("I won sir . good game !")
                    TURN = "user"
                    LAST = ""
                    root.destroy()
                    return

        # check the colums .
        for column in button_column_list:
            # couters for 'X' and 'O' .
            count_X = 0
            count_O = 0
            # if one of the spots is 'X' or 'O' then count it .
            for item in column:
                if item['text'] == 'X':
                    count_X += 1
                if item['text'] == 'O':
                    count_O += 1
                # when 'X' reach to 3 -> the column is marked with 'X' -> user won -> close the game . 
                if count_X == 3:
                    AIassistent.speak("You won sir . good game !")
                    TURN = "user"
                    LAST = ""
                    root.destroy()
                    return
                # when 'O' reach to 3 -> the column is marked with 'O' -> computer won -> close the game .
                if count_O == 3:
                    AIassistent.speak("I won sir . good game !")
                    TURN = "user"
                    LAST = ""
                    root.destroy()
                    return

        # check the diagonals .
        for diagonal in button_diagonal_list:
            # counters for 'X' and 'O' .
            count_X = 0
            count_O = 0
            # if one of the spots is 'X' or 'O' .
            for item in diagonal:
                if item['text'] == 'X':
                    count_X += 1
                if item['text'] == 'O':
                    count_O += 1
                # if the diagonal is 3 -> user won -> close the game .
                if count_X == 3:
                    AIassistent.speak("You won sir . good game !")
                    TURN = "user"
                    LAST = ""
                    root.destroy()
                    return
                # the diagonal is mark with 'O' -> computer won -> close the game .
                if count_O == 3:
                    AIassistent.speak("I won sir . good game !")
                    TURN = "user"
                    LAST = ""
                    root.destroy()
                    return

        return
        # end of function .

    def check_draw()->bool:
        """
        this fucntion will check if all the buttons are marked and there is no winner -> its a draw .
        Returns:
            [bool]: True/False .
        """
        list_of_buttons = [a_button, b_button, c_button, d_button, e_button, f_button, g_button, h_button, i_button]

        for button in list_of_buttons:
            if button['text'] != 'X' and button['text'] != 'O':
                return False

        return True
    # end of function .

    def assistent_turn():
        """
        this function will be activated after the user click on 'confirm turn' .
        this fucntion activates the computer turn .
        """
        global TURN

        AIassistent.speak("Ok sir .")
        AIassistent.speak("Now its my turn .")

        # rand one of the numbers on the list .
        assistent_choice = random.choice(empty_spots_list)

        # after that the computer will say witch spot he marked and mark it with red background and the letter 'O' .
        # it will also remove the specific number from the list -> cannot pick this again next turn .
        if assistent_choice == 1:
            AIassistent.speak("i choose A .")
            a_button.config(text='O', bg='red')
            empty_spots_list.remove(1)

        elif assistent_choice == 2:
            AIassistent.speak("i choose B .")
            b_button.config(text='O', bg='red')
            empty_spots_list.remove(2)

        elif assistent_choice == 3:
            AIassistent.speak("i choose C .")
            c_button.config(text='O', bg='red')
            empty_spots_list.remove(3)

        elif assistent_choice == 4:
            AIassistent.speak("i choose D .")
            d_button.config(text='O', bg='red')
            empty_spots_list.remove(4)

        elif assistent_choice == 5:
            AIassistent.speak("i choose E .")
            e_button.config(text='O', bg='red')
            empty_spots_list.remove(5)

        elif assistent_choice == 6:
            AIassistent.speak("i choose F .")
            f_button.config(text='O', bg='red')
            empty_spots_list.remove(6)

        elif assistent_choice == 7:
            AIassistent.speak("i choose G .")
            g_button.config(text='O', bg='red')
            empty_spots_list.remove(7)

        elif assistent_choice == 8:
            AIassistent.speak("i choose H")
            h_button.config(text='O', bg='red')
            empty_spots_list.remove(8)

        else:
            AIassistent.speak("i choose I")
            i_button.config(text='O', bg='red')
            empty_spots_list.remove(9)
        
        # the next turn is users turn .
        TURN = 'user'
        return
    # end of function .

    def checkGame_assistentTurn():
        """
        first is check the game :
        1. check if the user forggot to mark a spot .
        2. check if the game is draw using a function wrriten above .
        3. then activates users turn .
        """

        global TURN, LAST

        # 1.
        if TURN == 'user':
            AIassistent.speak("Sir . you forgot to mark a place .")
            return
        # 2.
        if check_draw() == True:
            AIassistent.speak("Its a draw . good game sir !")
            TURN = "user"
            LAST = ""
            root.destroy()
            return
        # 3.
        assistent_turn()
    # end of function .

    def mark_a():
        """ 
        user click on 'A' button -> mark 'A' spot in the game .
        """
        global TURN, LAST

        # this place is already taken .
        if a_button['text'] == 'X' or a_button['text'] == 'O':
            AIassistent.speak("Sir . that spot is taken ...")
            return
        
        # the user marked a spot and did not click on 'confirm button' .
        # user need to mark a spot -> click on 'confirm button' . 
        # if the user wants to cancel his mark and pick other spot -> click on 'uncheck' button -> pick another spot -> click on 'confirm button' .
        elif TURN == 'assistent':
            AIassistent.speak("Sir . you cannot pick two spots in one turn .")
            AIassistent.speak("Please pick one spot . then click on confirm button .")
            AIassistent.speak("If you want to pick other spot . click on uncheck button and pick another spot . then click on confirm button .")
            return

        # the button is un marked -> i mark this place .
        # remove it from 'empty_spots_list' so that spot cannot be picked in the next turns .
        # next is assistent turn .
        # the last users turn .
        a_button.config(text='X', bg='green')
        empty_spots_list.remove(1)
        TURN = 'assistent'
        LAST = 'A'
    # end of function 'mark_a'

    def mark_b():
        """ 
        user click on 'B' button -> mark 'B' spot in the game .
        """
        global TURN, LAST

        if b_button['text'] == 'X' or b_button['text'] == 'O':
            AIassistent.speak("Sir . that spot is taken ...")
            return

        elif TURN == 'assistent':
            AIassistent.speak("Sir . you cannot pick two spots in one turn .")
            AIassistent.speak("Please pick one spot . then click on confirm button .")
            AIassistent.speak("If you want to pick other spot . click on uncheck button and pick another spot . then click on confirm button .")
            return

        b_button.config(text='X', bg='green')
        empty_spots_list.remove(2)
        TURN = 'assistent'
        LAST = 'B'
    # end of function 'mark_b'

    def mark_c():
        """ 
        user click on 'C' button -> mark 'C' spot in the game .
        """
        global TURN, LAST

        if c_button['text'] == 'X' or c_button['text'] == 'O':
            AIassistent.speak("Sir . that spot is taken ...")
            return

        elif TURN == 'assistent':
            AIassistent.speak("Sir . you cannot pick two spots in one turn .")
            AIassistent.speak("Please pick one spot . then click on confirm button .")
            return

        c_button.config(text='X', bg='green')
        empty_spots_list.remove(3)
        TURN = 'assistent'
        LAST = 'C'
    # end of function 'mark_c' 

    def mark_d():
        """ 
        user click on 'D' button -> mark 'D' spot in the game .
        """
        global TURN, LAST

        if d_button['text'] == 'X' or d_button['text'] == 'O':
            AIassistent.speak("Sir . that spot is taken ...")
            return

        elif TURN == 'assistent':
            AIassistent.speak("Sir . you cannot pick two spots in one turn .")
            AIassistent.speak("Please pick one spot . then click on confirm button .")
            return

        d_button.config(text='X', bg='green')
        empty_spots_list.remove(4)
        TURN = 'assistent'
        LAST = 'D'
    # end of function 'mark_d'

    def mark_e():
        """ 
        user click on 'E' button -> mark 'E' spot in the game .
        """
        global TURN, LAST

        if e_button['text'] == 'X' or e_button['text'] == 'O':
            AIassistent.speak("Sir . that spot is taken ...")
            return

        elif TURN == 'assistent':
            AIassistent.speak("Sir . you cannot pick two spots in one turn .")
            AIassistent.speak("Please pick one spot . then click on confirm button .")
            return

        e_button.config(text='X', bg='green')
        empty_spots_list.remove(5)
        TURN = 'assistent'
        LAST = 'E'
    # end of function 'mark_e'

    def mark_f():
        """ 
        user click on 'F' button -> mark 'F' spot in the game .
        """
        global TURN, LAST

        if f_button['text'] == 'X' or f_button['text'] == 'O':
            AIassistent.speak("Sir . that spot is taken ...")
            return

        elif TURN == 'assistent':
            AIassistent.speak("Sir . you cannot pick two spots in one turn .")
            AIassistent.speak("Please pick one spot . then click on confirm button .")
            return

        f_button.config(text='X', bg='green')
        empty_spots_list.remove(6)
        TURN = 'assistent'
        LAST = 'F'
    # end of function 'mark_f'

    def mark_g():
        """ 
        user click on 'G' button -> mark 'G' spot in the game .
        """
        global TURN, LAST

        if g_button['text'] == 'X' or g_button['text'] == 'O':
            AIassistent.speak("Sir . that spot is taken ...")
            return

        elif TURN == 'assistent':
            AIassistent.speak("Sir . you cannot pick two spots in one turn .")
            AIassistent.speak("Please pick one spot . then click on confirm button .")
            return

        g_button.config(text='X', bg='green')
        empty_spots_list.remove(7)
        TURN = 'assistent'
        LAST = 'G'
    # end of function 'mark_g'

    def mark_h():
        """ 
        user click on 'H' button -> mark 'H' spot in the game .
        """
        global TURN, LAST

        if h_button['text'] == 'X' or h_button['text'] == 'O':
            AIassistent.speak("Sir . that spot is taken ...")
            return

        elif TURN == 'assistent':
            AIassistent.speak("Sir . you cannot pick two spots in one turn .")
            AIassistent.speak("Please pick one spot . then click on confirm button .")
            return

        h_button.config(text='X', bg='green')
        empty_spots_list.remove(8)
        TURN = 'assistent'
        LAST = 'H'
    # end of function 'mark_h'

    def mark_i():
        """ 
        user click on 'I' button -> mark 'I' spot in the game .
        """
        global TURN, LAST

        if i_button['text'] == 'X' or i_button['text'] == 'O':
            AIassistent.speak("Sir . that spot is taken ...")
            return

        elif TURN == 'assistent':
            AIassistent.speak("Sir . you cannot pick two spots in one turn .")
            AIassistent.speak("Please pick one spot . then click on confirm button .")
            return

        i_button.config(text='X', bg='green')
        empty_spots_list.remove(9)
        TURN = 'assistent'
        LAST = 'I'
    # end of function 'mark_i'

    def uncheck_spot():

        global TURN, LAST

        if TURN == 'user':
            return
        
        elif TURN == 'assistent':
            if LAST == 'A':
                a_button.config(text='A', bg='white')
                empty_spots_list.append(1)
                TURN = 'user'

            elif LAST == 'B':
                b_button.config(text='B', bg='white')
                empty_spots_list.append(2)
                TURN = 'user'

            elif LAST == 'C':
                c_button.config(text='C', bg='white')
                empty_spots_list.append(3)
                TURN = 'user'

            elif LAST == 'D':
                d_button.config(text='D', bg='white')
                empty_spots_list.append(4)
                TURN = 'user'

            elif LAST == 'E':
                e_button.config(text='E', bg='white')
                empty_spots_list.append(5)
                TURN = 'user'

            elif LAST == 'F':
                f_button.config(text='F', bg='white')
                empty_spots_list.append(6)
                TURN = 'user'

            elif LAST == 'G':
                g_button.config(text='G', bg='white')
                empty_spots_list.append(7)
                TURN = 'user'

            elif LAST == 'H':
                h_button.config(text='H', bg='white')
                empty_spots_list.append(8)
                TURN = 'user'

            elif LAST == 'I':
                i_button.config(text='I', bg='white')
                empty_spots_list.append(9)
                TURN = 'user'


    a_button = Button(root, text='A', font=buttons.button_font, width=buttons.button_width, height=buttons.button_height, bd=buttons.button_bd, bg=buttons.button_bg, command=lambda: [mark_a(), check_game()])
    a_button.grid(row=0, column=0)

    b_button = Button(root, text='B', font=buttons.button_font, width=buttons.button_width, height=buttons.button_height, bd=buttons.button_bd, bg=buttons.button_bg, command=lambda: [mark_b(), check_game()])
    b_button.grid(row=0, column=1)

    c_button = Button(root, text='C', font=buttons.button_font, width=buttons.button_width, height=buttons.button_height, bd=buttons.button_bd, bg=buttons.button_bg, command=lambda: [mark_c(), check_game()])
    c_button.grid(row=0, column=2)

    d_button = Button(root, text='D', font=buttons.button_font, width=buttons.button_width, height=buttons.button_height, bd=buttons.button_bd, bg=buttons.button_bg, command=lambda: [mark_d(), check_game()])
    d_button.grid(row=1, column=0)

    e_button = Button(root, text='E', font=buttons.button_font, width=buttons.button_width, height=buttons.button_height, bd=buttons.button_bd, bg=buttons.button_bg, command=lambda: [mark_e(), check_game()])
    e_button.grid(row=1, column=1)

    f_button = Button(root, text='F', font=buttons.button_font, width=buttons.button_width, height=buttons.button_height, bd=buttons.button_bd, bg=buttons.button_bg, command=lambda: [mark_f(), check_game()])
    f_button.grid(row=1, column=2)

    g_button = Button(root, text='G', font=buttons.button_font, width=buttons.button_width, height=buttons.button_height, bd=buttons.button_bd, bg=buttons.button_bg, command=lambda: [mark_g(), check_game()])
    g_button.grid(row=2, column=0)

    h_button = Button(root, text='H', font=buttons.button_font, width=buttons.button_width, height=buttons.button_height, bd=buttons.button_bd, bg=buttons.button_bg, command=lambda: [mark_h(), check_game()])
    h_button.grid(row=2, column=1)

    i_button = Button(root, text='I', font=buttons.button_font, width=buttons.button_width, height=buttons.button_height, bd=buttons.button_bd, bg=buttons.button_bg, command=lambda: [mark_i(), check_game()])
    i_button.grid(row=2, column=2)

    confirm_button = Button(root, text='Confirm Turn', font='Times 15 bold', width=30, height=1, bd=buttons.button_bd, command=lambda: [checkGame_assistentTurn(), check_game()])
    confirm_button.place(x=60, y=470)

    uncheck_button = Button(root, text='Uncheck', font='Times 15 bold', width=30, height=1, bd=buttons.button_bd, command=uncheck_spot)
    uncheck_button.place(x=60, y=520)

    root.mainloop()

    




