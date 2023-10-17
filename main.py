import tkinter as tk
import ttkbootstrap as ttk
import requests
from ttkbootstrap.constants import *
from settings import *
from PIL import Image, ImageTk
import random
from CTkMessagebox import CTkMessagebox

window = ttk.Window(themename='cyborg')
window.geometry('750x900')
window.resizable(False, False)

num = 0

style = ttk.Style()

wordle_label = ttk.Label(master=window, text='Wordle', font=('Montserrat', 24, 'bold'))
wordle_label.pack()

random_word = random.choice(five_letter_words)
print(random_word)

class WordleGame(ttk.Frame):
    def __init__(self, parent):
        super(WordleGame, self).__init__(master=parent)
        self.columnconfigure((0, 1, 2, 3, 4), uniform='a')
        self.rowconfigure((0, 1, 2, 3, 4, 5), uniform='a')

        self.go = True

        self.text_box = ttk.Label(self, width=2, font=('Montserrat', 30), background='#181918')
        self.text_box.grid(row=0, column=0, pady=15, padx=10)
        self.text_box2 = ttk.Label(self, width=2, font=('Montserrat', 30), background='#181918')
        self.text_box2.grid(row=0, column=1, pady=15, padx=10)
        self.text_box3 = ttk.Label(self, width=2, font=('Montserrat', 30), background='#181918')
        self.text_box3.grid(row=0, column=2, pady=15, padx=10)
        self.text_box4 = ttk.Label(self, width=2, font=('Montserrat', 30), background='#181918')
        self.text_box4.grid(row=0, column=3, pady=15, padx=10)
        self.text_box5 = ttk.Label(self, width=2, font=('Montserrat', 30), background='#181918')
        self.text_box5.grid(row=0, column=4, pady=15, padx=10)

        self.text_box6 = ttk.Label(self, width=2, font=('Montserrat', 30), background='#181918')
        self.text_box6.grid(row=1, column=0, pady=15, padx=10)
        self.text_box7 = ttk.Label(self, width=2, font=('Montserrat', 30), background='#181918')
        self.text_box7.grid(row=1, column=1, pady=15, padx=10)
        self.text_box8 = ttk.Label(self, width=2, font=('Montserrat', 30), background='#181918')
        self.text_box8.grid(row=1, column=2, pady=15, padx=10)
        self.text_box9 = ttk.Label(self, width=2, font=('Montserrat', 30), background='#181918')
        self.text_box9.grid(row=1, column=3, pady=15, padx=10)
        self.text_box10 = ttk.Label(self, width=2, font=('Montserrat', 30), background='#181918')
        self.text_box10.grid(row=1, column=4, pady=15, padx=10)

        self.text_box11 = ttk.Label(self, width=2, font=('Montserrat', 30), background='#181918')
        self.text_box11.grid(row=2, column=0, pady=15, padx=10)
        self.text_box12 = ttk.Label(self, width=2, font=('Montserrat', 30), background='#181918')
        self.text_box12.grid(row=2, column=1, pady=15, padx=10)
        self.text_box13 = ttk.Label(self, width=2, font=('Montserrat', 30), background='#181918')
        self.text_box13.grid(row=2, column=2, pady=15, padx=10)
        self.text_box14 = ttk.Label(self, width=2, font=('Montserrat', 30), background='#181918')
        self.text_box14.grid(row=2, column=3, pady=15, padx=10)
        self.text_box15 = ttk.Label(self, width=2, font=('Montserrat', 30), background='#181918')
        self.text_box15.grid(row=2, column=4, pady=15, padx=10)

        self.text_box16 = ttk.Label(self, width=2, font=('Montserrat', 30), background='#181918')
        self.text_box16.grid(row=3, column=0, pady=15, padx=10)
        self.text_box17 = ttk.Label(self, width=2, font=('Montserrat', 30), background='#181918')
        self.text_box17.grid(row=3, column=1, pady=15, padx=10)
        self.text_box18 = ttk.Label(self, width=2, font=('Montserrat', 30), background='#181918')
        self.text_box18.grid(row=3, column=2, pady=15, padx=10)
        self.text_box19 = ttk.Label(self, width=2, font=('Montserrat', 30), background='#181918')
        self.text_box19.grid(row=3, column=3, pady=15, padx=10)
        self.text_box20 = ttk.Label(self, width=2, font=('Montserrat', 30), background='#181918')
        self.text_box20.grid(row=3, column=4, pady=15, padx=10)

        self.text_box21 = ttk.Label(self, width=2, font=('Montserrat', 30), background='#181918')
        self.text_box21.grid(row=4, column=0, pady=15, padx=10)
        self.text_box22 = ttk.Label(self, width=2, font=('Montserrat', 30), background='#181918')
        self.text_box22.grid(row=4, column=1, pady=15, padx=10)
        self.text_box23 = ttk.Label(self, width=2, font=('Montserrat', 30), background='#181918')
        self.text_box23.grid(row=4, column=2, pady=15, padx=10)
        self.text_box24 = ttk.Label(self, width=2, font=('Montserrat', 30), background='#181918')
        self.text_box24.grid(row=4, column=3, pady=15, padx=10)
        self.text_box25 = ttk.Label(self, width=2, font=('Montserrat', 30), background='#181918')
        self.text_box25.grid(row=4, column=4, pady=15, padx=10)

        self.text_box26 = ttk.Label(self, background='#181918', width=2, font=('Montserrat', 30))
        self.text_box26.grid(row=5, column=0, pady=15, padx=10)
        self.text_box27 = ttk.Label(self, background='#181918', width=2, font=('Montserrat', 30))
        self.text_box27.grid(row=5, column=1, pady=15, padx=10)
        self.text_box28 = ttk.Label(self, background='#181918', width=2, font=('Montserrat', 30))
        self.text_box28.grid(row=5, column=2, pady=15, padx=10)
        self.text_box29 = ttk.Label(self, background='#181918', width=2, font=('Montserrat', 30))
        self.text_box29.grid(row=5, column=3, pady=15, padx=10)
        self.text_box30 = ttk.Label(self, background='#181918', width=2, font=('Montserrat', 30))
        self.text_box30.grid(row=5, column=4, pady=15, padx=10)

        self.label_widget_list_1 = []
        self.label_widget_list_2 = []
        self.label_widget_list_3 = []
        self.label_widget_list_4 = []
        self.label_widget_list_5 = []
        self.label_widget_list_6 = []

        self.label_widget_list_1.append(self.text_box)
        self.label_widget_list_1.append(self.text_box2)
        self.label_widget_list_1.append(self.text_box3)
        self.label_widget_list_1.append(self.text_box4)
        self.label_widget_list_1.append(self.text_box5)

        self.label_widget_list_2.append(self.text_box6)
        self.label_widget_list_2.append(self.text_box7)
        self.label_widget_list_2.append(self.text_box8)
        self.label_widget_list_2.append(self.text_box9)
        self.label_widget_list_2.append(self.text_box10)

        self.label_widget_list_3.append(self.text_box11)
        self.label_widget_list_3.append(self.text_box12)
        self.label_widget_list_3.append(self.text_box13)
        self.label_widget_list_3.append(self.text_box14)
        self.label_widget_list_3.append(self.text_box15)

        self.label_widget_list_4.append(self.text_box16)
        self.label_widget_list_4.append(self.text_box17)
        self.label_widget_list_4.append(self.text_box18)
        self.label_widget_list_4.append(self.text_box19)
        self.label_widget_list_4.append(self.text_box20)

        self.label_widget_list_5.append(self.text_box21)
        self.label_widget_list_5.append(self.text_box22)
        self.label_widget_list_5.append(self.text_box23)
        self.label_widget_list_5.append(self.text_box24)
        self.label_widget_list_5.append(self.text_box25)

        self.label_widget_list_6.append(self.text_box26)
        self.label_widget_list_6.append(self.text_box27)
        self.label_widget_list_6.append(self.text_box28)
        self.label_widget_list_6.append(self.text_box29)
        self.label_widget_list_6.append(self.text_box30)

        self.game = True

        self.is_word = False

        self.letters_guessed = []

        self.repeated_letters = []

        self.pack()

    def key_release(self, event):
        global num
        if event.keysym == 'Return':
            self.enter_method()

        elif event.keysym == 'BackSpace':
            self.delete_char()

        elif self.label_widget_list_1 and num < 5:
            pressed_key = event.keysym
            self.edit_label(self.label_widget_list_1, pressed_key)

        elif self.label_widget_list_2 and num < 5:
            pressed_key = event.keysym
            self.edit_label(self.label_widget_list_2, pressed_key)

        elif self.label_widget_list_3 and num < 5:
            pressed_key = event.keysym
            self.edit_label(self.label_widget_list_3, pressed_key)

        elif self.label_widget_list_4 and num < 5:
            pressed_key = event.keysym
            self.edit_label(self.label_widget_list_4, pressed_key)

        elif self.label_widget_list_5 and num < 5:
            pressed_key = event.keysym
            self.edit_label(self.label_widget_list_5, pressed_key)

        elif self.label_widget_list_6 and num < 5:
            pressed_key = event.keysym
            self.edit_label(self.label_widget_list_6, pressed_key)

    def restart(self):
        global random_word, num, count_counter
        random_word = random.choice(five_letter_words)
        print(random_word)

        self.repeated_letters = []

        self.go = True

        count_counter = 0

        num = 0

        self.label_widget_list_1.append(self.text_box)
        self.label_widget_list_1.append(self.text_box2)
        self.label_widget_list_1.append(self.text_box3)
        self.label_widget_list_1.append(self.text_box4)
        self.label_widget_list_1.append(self.text_box5)

        self.label_widget_list_2.append(self.text_box6)
        self.label_widget_list_2.append(self.text_box7)
        self.label_widget_list_2.append(self.text_box8)
        self.label_widget_list_2.append(self.text_box9)
        self.label_widget_list_2.append(self.text_box10)

        self.label_widget_list_3.append(self.text_box11)
        self.label_widget_list_3.append(self.text_box12)
        self.label_widget_list_3.append(self.text_box13)
        self.label_widget_list_3.append(self.text_box14)
        self.label_widget_list_3.append(self.text_box15)

        self.label_widget_list_4.append(self.text_box16)
        self.label_widget_list_4.append(self.text_box17)
        self.label_widget_list_4.append(self.text_box18)
        self.label_widget_list_4.append(self.text_box19)
        self.label_widget_list_4.append(self.text_box20)

        self.label_widget_list_5.append(self.text_box21)
        self.label_widget_list_5.append(self.text_box22)
        self.label_widget_list_5.append(self.text_box23)
        self.label_widget_list_5.append(self.text_box24)
        self.label_widget_list_5.append(self.text_box25)

        self.label_widget_list_6.append(self.text_box26)
        self.label_widget_list_6.append(self.text_box27)
        self.label_widget_list_6.append(self.text_box28)
        self.label_widget_list_6.append(self.text_box29)
        self.label_widget_list_6.append(self.text_box30)

        self.loop_list(self.label_widget_list_1)
        self.loop_list(self.label_widget_list_2)
        self.loop_list(self.label_widget_list_3)
        self.loop_list(self.label_widget_list_4)
        self.loop_list(self.label_widget_list_5)
        self.loop_list(self.label_widget_list_6)

    def check_list(self, a_list, index, word):
        if word[index] == random_word[index]:
            count = word.count(word[index])
            a_list[index].config(background=correct_color)
            if count == 2 and random_word.count(word[index]) == 1:
                if word[index] in word[:index]:
                    a_list[word[:index].index(word[index])].config(background=wrong_word)

        elif word[index] in random_word:
            count = word.count(word[index])
            if count == 2 and random_word.count(word[index]) == 1:
                if word[index] in word[:index]:
                    #why = a_list[word[:index].index(word[index])].cget('background')
                    a_list[index].config(background=wrong_word)
                    self.go = False

                if self.go:
                    print(self.letters_guessed)
                    self.repeated_letters.append(word[index])
                    if len(self.repeated_letters) == 1:
                        a_list[index].config(background=wrong_place_color)
                    elif len(self.repeated_letters) == 2:
                        a_list[index].config(background=wrong_word)
            else:
                a_list[index].config(background=wrong_place_color)
        elif word[index] not in random_word:
            a_list[index].config(background=wrong_word)
        if index == 4:
            a_list.clear()

    def loop_list(self, a_list):
        for label in a_list:
            label.config(background=default_color)
            label.config(text='')

    def edit_label(self, a_list, pressed_key):
        global num
        if self.game:
            if len(pressed_key) == 1 and pressed_key.isalpha():
                a_list[num].config(text=f'{pressed_key.upper()}')
                num += 1
                self.letters_guessed.append(pressed_key)

    def win_message_box(self, a_list):
        for label in a_list:
            label.config(background=correct_color)
        win_message = CTkMessagebox(message="You Win!\nDo you want to play again?", icon="question", option_1='No', option_2='Yes', title='You win!')
        a_list.clear()
        response = win_message.get()
        if response == 'Yes':
            self.restart()
        else:
            self.game = False

    def delete_char(self):
        global num
        if num > 0 and num <= 5:
            num -= 1
            self.letters_guessed.pop()
            if self.label_widget_list_1:
                self.label_widget_list_1[num].config(text='')
            elif self.label_widget_list_2:
                self.label_widget_list_2[num].config(text='')
            elif self.label_widget_list_3:
                self.label_widget_list_3[num].config(text='')
            elif self.label_widget_list_4:
                self.label_widget_list_4[num].config(text='')
            elif self.label_widget_list_5:
                self.label_widget_list_5[num].config(text='')
            elif self.label_widget_list_6:
                self.label_widget_list_6[num].config(text='')

    def enter_method(self):
        global num
        if num % 5 == 0 and num == 5:
            guessed_word = ''.join(self.letters_guessed).lower()
            url = 'https://api.dictionaryapi.dev/api/v2/entries/en/' + guessed_word
            data = requests.get(url).json()
            try:
                if data['title'] == 'No Definitions Found':
                    self.is_word = False
            except:
                self.is_word = True

            if self.is_word:
                if guessed_word == random_word:
                    if self.label_widget_list_1:
                        self.win_message_box(self.label_widget_list_1)
                    elif self.label_widget_list_2:
                        self.win_message_box(self.label_widget_list_2)
                    elif self.label_widget_list_3:
                        self.win_message_box(self.label_widget_list_3)
                    elif self.label_widget_list_4:
                        self.win_message_box(self.label_widget_list_4)
                    elif self.label_widget_list_5:
                        self.win_message_box(self.label_widget_list_5)
                    elif self.label_widget_list_6:
                        self.win_message_box(self.label_widget_list_6)
                else:
                    for i in range(0, 5):
                        if self.label_widget_list_1:
                            self.check_list(self.label_widget_list_1, i, guessed_word)
                        elif self.label_widget_list_2:
                            self.check_list(self.label_widget_list_2, i, guessed_word)
                        elif self.label_widget_list_3:
                            self.check_list(self.label_widget_list_3, i, guessed_word)
                        elif self.label_widget_list_4:
                            self.check_list(self.label_widget_list_4, i, guessed_word)
                        elif self.label_widget_list_5:
                            self.check_list(self.label_widget_list_5, i, guessed_word)
                        elif self.label_widget_list_6:
                            self.check_list(self.label_widget_list_6, i, guessed_word)
                            if not self.label_widget_list_6:
                                you_lost_message = CTkMessagebox(title='You lost!',
                                                                 message=f"The answer was '{random_word}'\nDo you want to play again?",
                                                                 icon='question', option_1='No', option_2='Yes')
                                response = you_lost_message.get()
                                if response == 'Yes':
                                    self.restart()
                                else:
                                    self.game = False
                num = 0
                self.letters_guessed = []
                self.repeated_letters = []
                self.go = True
            else:
                CTkMessagebox(message='That is not a word!', title='Error', option_1='ok')


class Keyboard(ttk.Frame):
    def __init__(self, parent, wordleframe):
        super(Keyboard, self).__init__(master=parent)
        # self.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), uniform='a', weight=1)
        self.rowconfigure((0, 1, 2), uniform='b', weight=1)

        custom_font = ('Montserrat', 16, 'bold')
        style.configure('my.TButton', font=custom_font)

        self.wordleframe = wordleframe

        self.top_frame = ttk.Frame(master=self)
        self.mid_frame = ttk.Frame(master=self)
        self.bottom_frame = ttk.Frame(master=self)

        self.back_image = Image.open('backsapce.png')
        self.scaled_back_img = self.back_image.resize((30, 30))
        self.scaled_back_img = ImageTk.PhotoImage(self.scaled_back_img)

        self.top_frame.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), uniform='a')
        self.mid_frame.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), uniform='b')
        self.bottom_frame.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), uniform='c')

        self.q_button = ttk.Button(self.top_frame, text='Q', bootstyle=LIGHT, style='my.TButton', command=lambda :self.letters_typed(self.q_button))
        self.w_button = ttk.Button(self.top_frame, text='W', bootstyle=LIGHT, style='my.TButton', command=lambda :self.letters_typed(self.w_button))
        self.e_button = ttk.Button(self.top_frame, text='E', bootstyle=LIGHT, style='my.TButton', command=lambda :self.letters_typed(self.e_button))
        self.r_button = ttk.Button(self.top_frame, text='R', bootstyle=LIGHT, style='my.TButton', command=lambda :self.letters_typed(self.r_button))
        self.t_button = ttk.Button(self.top_frame, text='T', bootstyle=LIGHT, style='my.TButton', command=lambda :self.letters_typed(self.t_button))
        self.y_button = ttk.Button(self.top_frame, text='Y', bootstyle=LIGHT, style='my.TButton', command=lambda :self.letters_typed(self.y_button))
        self.u_button = ttk.Button(self.top_frame, text='U', bootstyle=LIGHT, style='my.TButton', command=lambda :self.letters_typed(self.u_button))
        self.i_button = ttk.Button(self.top_frame, text='I', bootstyle=LIGHT, style='my.TButton', command=lambda :self.letters_typed(self.i_button))
        self.o_button = ttk.Button(self.top_frame, text='O', bootstyle=LIGHT, style='my.TButton', command=lambda :self.letters_typed(self.o_button))
        self.p_button = ttk.Button(self.top_frame, text='P', bootstyle=LIGHT, style='my.TButton', command=lambda :self.letters_typed(self.p_button))

        self.a_button = ttk.Button(self.mid_frame, text='A', bootstyle=LIGHT, style='my.TButton', command=lambda :self.letters_typed(self.a_button))
        self.s_button = ttk.Button(self.mid_frame, text='S', bootstyle=LIGHT, style='my.TButton', command=lambda :self.letters_typed(self.s_button))
        self.d_button = ttk.Button(self.mid_frame, text='D', bootstyle=LIGHT, style='my.TButton', command=lambda :self.letters_typed(self.d_button))
        self.f_button = ttk.Button(self.mid_frame, text='F', bootstyle=LIGHT, style='my.TButton', command=lambda :self.letters_typed(self.f_button))
        self.g_button = ttk.Button(self.mid_frame, text='G', bootstyle=LIGHT, style='my.TButton', command=lambda :self.letters_typed(self.g_button))
        self.h_button = ttk.Button(self.mid_frame, text='H', bootstyle=LIGHT, style='my.TButton', command=lambda :self.letters_typed(self.h_button))
        self.j_button = ttk.Button(self.mid_frame, text='J', bootstyle=LIGHT, style='my.TButton', command=lambda :self.letters_typed(self.j_button))
        self.k_button = ttk.Button(self.mid_frame, text='K', bootstyle=LIGHT, style='my.TButton', command=lambda :self.letters_typed(self.k_button))
        self.l_button = ttk.Button(self.mid_frame, text='L', bootstyle=LIGHT, style='my.TButton', command=lambda :self.letters_typed(self.l_button))

        self.q_button.grid(row=0, column=0, sticky='ew', padx=4, ipady=5)
        self.w_button.grid(row=0, column=1, sticky='ew', padx=4, ipady=5)
        self.e_button.grid(row=0, column=2, sticky='ew', padx=4, ipady=5)
        self.r_button.grid(row=0, column=3, sticky='ew', padx=4, ipady=5)
        self.t_button.grid(row=0, column=4, sticky='ew', padx=4, ipady=5)
        self.y_button.grid(row=0, column=5, sticky='ew', padx=4, ipady=5)
        self.u_button.grid(row=0, column=6, sticky='ew', padx=4, ipady=5)
        self.i_button.grid(row=0, column=7, sticky='ew', padx=4, ipady=5)
        self.o_button.grid(row=0, column=8, sticky='ew', padx=4, ipady=5)
        self.p_button.grid(row=0, column=9, sticky='ew', padx=4, ipady=5)

        self.a_button.grid(row=0, column=0, sticky='ew', padx=4, ipady=5)
        self.s_button.grid(row=0, column=1, sticky='ew', padx=4, ipady=5)
        self.d_button.grid(row=0, column=2, sticky='ew', padx=4, ipady=5)
        self.f_button.grid(row=0, column=3, sticky='ew', padx=4, ipady=5)
        self.g_button.grid(row=0, column=4, sticky='ew', padx=4, ipady=5)
        self.h_button.grid(row=0, column=5, sticky='ew', padx=4, ipady=5)
        self.j_button.grid(row=0, column=6, sticky='ew', padx=4, ipady=5)
        self.k_button.grid(row=0, column=7, sticky='ew', padx=4, ipady=5)
        self.l_button.grid(row=0, column=8, sticky='ew', padx=4, ipady=5)

        self.back_button = ttk.Button(self.bottom_frame, bootstyle=LIGHT, style='my.TButton', image=self.scaled_back_img, command=self.wordleframe.delete_char)
        self.z_button = ttk.Button(self.bottom_frame, text='Z', bootstyle=LIGHT, style='my.TButton', command=lambda :self.letters_typed(self.z_button))
        self.x_button = ttk.Button(self.bottom_frame, text='X', bootstyle=LIGHT, style='my.TButton', command=lambda :self.letters_typed(self.x_button))
        self.c_button = ttk.Button(self.bottom_frame, text='C', bootstyle=LIGHT, style='my.TButton', command=lambda :self.letters_typed(self.c_button))
        self.v_button = ttk.Button(self.bottom_frame, text='V', bootstyle=LIGHT, style='my.TButton', command=lambda :self.letters_typed(self.v_button))
        self.b_button = ttk.Button(self.bottom_frame, text='B', bootstyle=LIGHT, style='my.TButton', command=lambda :self.letters_typed(self.b_button))
        self.n_button = ttk.Button(self.bottom_frame, text='N', bootstyle=LIGHT, style='my.TButton', command=lambda :self.letters_typed(self.n_button))
        self.m_button = ttk.Button(self.bottom_frame, text='M', bootstyle=LIGHT, style='my.TButton', command=lambda :self.letters_typed(self.m_button))
        self.enter_button = ttk.Button(self.bottom_frame, text='Enter', bootstyle=LIGHT, style='my.TButton', command=self.wordleframe.enter_method)

        self.back_button.grid(row=0, column=0, sticky='ew', padx=4, ipady=5, columnspan=2)
        self.z_button.grid(row=0, column=2, sticky='ew', padx=4, ipady=5)
        self.x_button.grid(row=0, column=3, sticky='ew', padx=4, ipady=5)
        self.c_button.grid(row=0, column=4, sticky='ew', padx=4, ipady=5)
        self.v_button.grid(row=0, column=5, sticky='ew', padx=4, ipady=5)
        self.b_button.grid(row=0, column=6, sticky='ew', padx=4, ipady=5)
        self.n_button.grid(row=0, column=7, sticky='ew', padx=4, ipady=5)
        self.m_button.grid(row=0, column=8, sticky='ew', padx=4, ipady=5)
        self.enter_button.grid(row=0, column=9, sticky='ew', padx=4, ipady=5, columnspan=2)

        self.top_frame.pack(expand=False)
        self.mid_frame.pack(expand=False, pady=10)
        self.bottom_frame.pack(expand=False, pady=7)
        self.pack(expand=True, fill='both', pady=10)

    def letters_typed(self, button):
        global num
        if self.wordleframe.label_widget_list_1 and num < 5:
            self.wordleframe.letters_guessed.append(button.cget('text'))
            self.wordleframe.edit_label(self.wordleframe.label_widget_list_1, button.cget('text'))
            self.wordleframe.letters_guessed.pop()

        elif self.wordleframe.label_widget_list_2 and num < 5:
            self.wordleframe.letters_guessed.append(button.cget('text'))
            self.wordleframe.edit_label(self.wordleframe.label_widget_list_2, button.cget('text'))
            self.wordleframe.letters_guessed.pop()
        elif self.wordleframe.label_widget_list_3 and num < 5:
            self.wordleframe.letters_guessed.append(button.cget('text'))
            self.wordleframe.edit_label(self.wordleframe.label_widget_list_3, button.cget('text'))
            self.wordleframe.letters_guessed.pop()
        elif self.wordleframe.label_widget_list_4 and num < 5:
            self.wordleframe.letters_guessed.append(button.cget('text'))
            self.wordleframe.edit_label(self.wordleframe.label_widget_list_4, button.cget('text'))
            self.wordleframe.letters_guessed.pop()
        elif self.wordleframe.label_widget_list_5 and num < 5:
            self.wordleframe.letters_guessed.append(button.cget('text'))
            self.wordleframe.edit_label(self.wordleframe.label_widget_list_5, button.cget('text'))
            self.wordleframe.letters_guessed.pop()
        elif self.wordleframe.label_widget_list_6 and num < 5:
            self.wordleframe.letters_guessed.append(button.cget('text'))
            self.wordleframe.edit_label(self.wordleframe.label_widget_list_6, button.cget('text'))
            self.wordleframe.letters_guessed.pop()

wordle_frame = WordleGame(window)

keyboard = Keyboard(window, wordle_frame)

window.bind("<KeyRelease>", wordle_frame.key_release)

window.mainloop()