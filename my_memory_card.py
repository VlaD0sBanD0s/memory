#создаювроде бы какое-то приложение
from PyQt5.QtCore import Qt
from random import shuffle
from random import randint    #импооорт всего сааамого нужного
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout,QMessageBox, QRadioButton, QGroupBox, QButtonGroup
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questionlist = []
questionlist.append(Question('Какой нации не существует?','Смурфики','Русские','Аляска','Все есть'))
questionlist.append(Question('Кто был на Марсе?','Никто','Путин','Илон Маск','Мишаня'))
questionlist.append(Question('ЧТО?','А НИЧТО','ЧТО','ЧТО???','ЧТО НАДО'))
questionlist.append(Question('В какой стране много островов?','Индонезия','Куба','Индия','Россия'))
questionlist.append(Question('Где ты живешь?','В РОССИИ','В Китае','В КНДР','В канаве'))
questionlist.append(Question('Столицей какой страны является Москва?','Россия','США','КНДР','Египет'))
questionlist.append(Question('Почему мы здесь?','Это Россия','Что?','Не знаю','Да'))
questionlist.append(Question('Какого острова не сущестувет?','Аля-Деревня','Мадагаскар','Шри-Ланка','Гавайи'))
questionlist.append(Question('Почему вода синяя?','...','....','.....','..........'))
questionlist.append(Question('Почему Земля круглая?','...','....','.....','......'))

app =  QApplication([])
window = QWidget()                      #здесь создается приложение(оконное) и его виджет
window.setWindowTitle('Memory Card!')

btn_ok = QPushButton('Ответить')
lb_question = QLabel('Какой национальности не существует?')             #типичный вопрос. таких много
RadBox = QGroupBox('Варианты ответов')
rbtn1 = QRadioButton('Энцы')
rbtn2 = QRadioButton('Чулымцы')
rbtn3 = QRadioButton('Смурфы')
rbtn4 = QRadioButton('Алеуты')

layout_A1 = QHBoxLayout()           #<--- на эти линии распологают варианты ответа
layout_A2 = QVBoxLayout()
layout_A3 = QVBoxLayout()

layout_A2.addWidget(rbtn1)
layout_A2.addWidget(rbtn2)
layout_A3.addWidget(rbtn3)          #<--- собственно привязка
layout_A3.addWidget(rbtn4)

layout_A1.addLayout(layout_A2)
layout_A1.addLayout(layout_A3)

RadBox.setLayout(layout_A1)

AnsGroupBox = QGroupBox('Результат теста')    #Вот эта штука выводит РЕЗУЛЬТАТ теста      
lb_Result = QLabel('А ТЫ УГАДАЛ?')          #Вместо вариантов ответа будет это
lb_Correct = QLabel('ОТВЕТ БУДЕТ ЗДЕСЬ!')       

layout_res = QVBoxLayout()          #создание еще одной линии( и ее расположение)
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment= Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()        #линии. Нужно для поставки вариантов ответа на линиях
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))      #распологаем на линиях виджеты
layout_line2.addWidget(RadBox)
layout_line2.addWidget(AnsGroupBox)
#эту строчку я удалил , чтобы проверить работу ответа

layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch=2)       #на 3 линии кнопка
layout_line3.addStretch(1)

layout_card = QVBoxLayout()     #снова линия( куда ниже к этой линии подключаем тоже линии )   # |

layout_card.addLayout(layout_line1, stretch=2)                                                 # |
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)

layout_card.addStretch(1)       #оно должно быть (вроде бы)
layout_card.addSpacing(5)

RadGroopa = QButtonGroup()      #Группа Кнопок на рукаве...
RadGroopa.addButton(rbtn1)
RadGroopa.addButton(rbtn2)
RadGroopa.addButton(rbtn3)
RadGroopa.addButton(rbtn4)
AnsGroupBox.hide()
window.setLayout(layout_card) 
def show_RESA():              #Функция перехода на ответ!
    RadBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Следующий вопрос')

def show_ANSWER():
    RadBox.show()
    AnsGroupBox.hide()
    btn_ok.setText('Ответить')
    RadGroopa.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadGroopa.setExclusive(True)

'''
def TEST():
    if 'Ответить' == btn_ok.text():
        show_RESA()
    else:
        show_ANSWER()'''
answers = [rbtn1,rbtn2,rbtn3,rbtn4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Correct.setText(q.right_answer)
    lb_question.setText(q.question)
    show_ANSWER()

def show_correct(res):
    lb_Result.setText(res)
    show_RESA()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        
        print('Статистика!!!\nВсего вопросов --- ', window.total,'\nПравильных --- ',window.score)
        print('РЕЙТИНГ!!!',((window.score/window.total)*100),'%')
        
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно!')
                
            print('Статистика!!!\nВсего вопросов --- ', window.total,'\nПравильных --- ',window.score)
            print('РЕЙТИНГ!!!',((window.score/window.total)*100),'%')

def next_question():
    window.total +=1

    print('ВОПРОС!!!\nВсего вопросов --- ', window.total,'\nПравильных --- ',window.score)

   # window.cur_question = window.cur_question + 1
    cur_question = randint(0, len(questionlist) - 1)
    q = questionlist[cur_question]
    ##    window.cur_question = 0
    #q = questionlist[window.cur_question]
    ask(q)


def click_OK():
    if btn_ok.text() == 'Ответить':
        check_answer()
    else:
        next_question()
 

window.cur_question = -1
btn_ok.clicked.connect(click_OK)
window.score = 0
window.total = 0
next_question()

window.show()
app.exec()

