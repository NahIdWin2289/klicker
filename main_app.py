from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
 
class MainWin(Screen):
    def __init__(self, name = 'main'):
        super().__init__(name = name)
        VLayout = BoxLayout(orientation = 'vertical', spacing = 6)
        btn_play = Button(text = 'Играть', size_hint = (0.25, 0.20), pos_hint = {'center_x' : 0.5, 'y' : 0.55})
        btn_update = Button(text = 'Прокачка', size_hint = (0.25, 0.20), pos_hint = {'center_x' : 0.5, 'y' : 0.3})
        btn_skins = Button(text = 'Скины', size_hint = (0.25, 0.20), pos_hint = {'center_x' : 0.5, 'y' : 0.05} )
        self.add_widget(btn_play)
        self.add_widget(btn_update)
        self.add_widget(btn_skins)
        btn_play.on_press = self.next
        btn_update.on_press = self.next2
        btn_skins.on_press = self.next3
    def next(self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'game'

    def next2(self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'update'
    
    def next3(self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'skins'

class GameScr(Screen):
    def __init__(self, name = 'game'):
        super().__init__(name = name)
        self.btn_click = Button(text = 'Кликай', color = (0, 0, 0, 1), background_normal = global_fon, background_down = global_fon, size_hint = (0.30, 0.25), pos_hint = {'center_x' : 0.5, 'center_y' : 0.5})
        btn_back = Button(text = 'Назад', size_hint = (0.15, 0.10), pos_hint = {'x' : 0, 'top' : 1})
        self.score_label = Label(text = str(score), size_hint = (0.20, 0.15), pos_hint = {'right' : 1, 'top' : 1}, font_size = '35sp')
        self.add_widget(btn_back)
        self.add_widget(self.btn_click)
        self.add_widget(self.score_label)
        btn_back.on_press = self.back
        self.btn_click.on_press = self.scoreup
        self.on_enter = self.enter
    def back(self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'main'
    def scoreup(self):
        global score
        global click_score
        score += click_score
        self.score_label.text = str(score)
    def enter(self):
        global score
        global global_fon
        self.score_label.text = str(score)
        self.btn_click.background_normal = global_fon
        self.btn_click.background_down = global_fon
    
    
    

class UpdateScr(Screen):
    def __init__(self, name = 'update'):
        super().__init__(name = name)
        global score
        btn_back2 = Button(text = 'Назад', size_hint = (0.15, 0.10), pos_hint = {'x' : 0, 'top' : 1})
        self.btn_upgrade1 = Button(text = '+1 к Клику, Цена ' + str(prise_list1), size_hint = (0.25, 0.20), pos_hint = {'center_x' : 0.5, 'y' : 0.55})
        self.btn_upgrade1.on_press = self.uprgade1
        self.btn_upgrade2 = Button(text = '+10 к Клику, Цена ' + str(prise_list2), size_hint = (0.25, 0.20), pos_hint = {'center_x' : 0.5, 'y' : 0.3})
        self.btn_upgrade2.on_press = self.uprgade2
        self.btn_upgrade3 = Button(text = '+100 к Клику, Цена ' + str(prise_list3), size_hint = (0.25, 0.20), pos_hint = {'center_x' : 0.5, 'y' : 0.05})
        self.btn_upgrade3.on_press = self.uprgade3
        self.score_label = Label(text = str(score), size_hint = (0.20, 0.15), pos_hint = {'right' : 1, 'top' : 1}, font_size = '35sp')
        self.on_enter = self.enter
        self.add_widget(btn_back2)
        self.add_widget(self.score_label)
        self.add_widget(self.btn_upgrade1)
        self.add_widget(self.btn_upgrade2)
        self.add_widget(self.btn_upgrade3)

        btn_back2.on_press = self.back
    def back(self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'main'
    def enter(self):
        global score
        self.score_label.text = str(score)

    def uprgade1(self):
        global score
        global click_score
        global prise_list1
        if score >= prise_list1:
            score -= prise_list1
            click_score += 1
            self.score_label.text = str(score)
            prise_list1 = prise_list1 + 100
            self.btn_upgrade1.text = '+1 к Клику, Цена ' + str(prise_list1)


    def uprgade2(self):
        global score
        global click_score
        global prise_list2
        if score >= prise_list2:
            score -= prise_list2
            click_score += 10
            self.score_label.text = str(score)
            prise_list2 = prise_list2 + 1000
            self.btn_upgrade2.text = '+10 к Клику, Цена ' + str(prise_list2)
    
    def uprgade3(self):
        global score
        global click_score
        global prise_list3
        if score >= prise_list3:
            score -= prise_list3
            click_score += 100
            self.score_label.text = str(score)
            prise_list3 = prise_list3 + 10000
            self.btn_upgrade3.text = '+100 к Клику, Цена ' + str(prise_list3)
    

class ScinsScr(Screen):
    def __init__(self, name = 'skins'):
        super().__init__(name = name)
        global score
        global global_fon
        btn_back3 = Button(text = 'Назад', size_hint = (0.15, 0.10), pos_hint = {'x' : 0, 'top' : 1})
        self.add_widget(btn_back3)
        btn_back3.on_press = self.back
        btn_skins1 = Button(text = 'Фушигуро Тоджи (1000000)', background_normal = 'тоджи.png', background_down = 'тоджи.png', color = (0, 0, 0, 1), size_hint = (0.25, 0.20), pos_hint = {'center_x' : 0.35, 'center_y' : 0.20 })
        btn_skins2 = Button(text = 'Сугуру Гетто (100000)', background_normal = 'сугуру.png', background_down = 'сугуру.png', color = (0, 0, 0, 1), size_hint = (0.25, 0.20), pos_hint = {'center_x' : 0.35, 'center_y' : 0.45 })
        btn_skins3 = Button(text = 'Итадори Юдзи (10000)', background_normal = 'итадори.png', background_down = 'итадори.png', color = (0, 0, 0, 1), size_hint = (0.25, 0.20), pos_hint = {'center_x' : 0.35, 'center_y' : 0.70 })
        btn_skins4 = Button(text = 'Рёмэн Сукуна (2000000)', background_normal = 'сукуна.png', background_down = 'сукуна.png', color = (0.5, 0, 1, 1), size_hint = (0.25, 0.20), pos_hint = {'center_x' : 0.65, 'center_y' : 0.20 })
        btn_skins5 = Button(text = 'Годжо Сатору (1500000)', background_normal = 'годжо.png', background_down = 'годжо.png', color = (0, 1, 0.8, 1), size_hint = (0.25, 0.20), pos_hint = {'center_x' : 0.65, 'center_y' : 0.45 })
        btn_skins6 = Button(text = 'Махорага (1200000)', background_normal = 'махарага.png', background_down = 'махарага.png', color = (0, 0, 0, 1), size_hint = (0.25, 0.20), pos_hint = {'center_x' : 0.65, 'center_y' : 0.70 })
        self.score_label = Label(text = str(score), size_hint = (0.20, 0.15), pos_hint = {'right' : 1, 'top' : 1}, font_size = '35sp')
        self.add_widget(self.score_label)
        self.add_widget(btn_skins1)
        self.add_widget(btn_skins2)
        self.add_widget(btn_skins3)
        self.add_widget(btn_skins4)
        self.add_widget(btn_skins5)
        self.add_widget(btn_skins6)
        self.on_enter = self.enter
        btn_skins3.on_press = self.scinsbuy_1
        btn_skins2.on_press = self.scinsbuy_2
        btn_skins1.on_press = self.scinsbuy_3
        btn_skins6.on_press = self.scinsbuy_4
        btn_skins5.on_press = self.scinsbuy_5
        btn_skins4.on_press = self.scinsbuy_6
    def back(self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'main'
    def enter(self):
        global score
        self.score_label.text = str(score)
    def scinsbuy_1(self):
        global score
        global global_fon
        if 'итадори.png' in have_scins:
            global_fon = 'итадори.png'
        elif score >= 10000:
            score -= 10000
            global_fon = 'итадори.png'
            have_scins.append('итадори.png')
            self.score_label.text = str(score)
    def scinsbuy_2(self):
        global score
        global global_fon
        if 'сугуру.png' in have_scins:
            global_fon = 'сугуру.png'
        elif score >= 100000:
            score -= 100000
            global_fon = 'сугуру.png'
            have_scins.append('сугуру.png')
            self.score_label.text = str(score)
    def scinsbuy_3(self):
        global score
        global global_fon
        if 'тоджи.png' in have_scins:
            global_fon = 'тоджи.png'
        elif score >= 1000000:
            score -= 1000000
            global_fon = 'тоджи.png'
            have_scins.append('тоджи.png')
            self.score_label.text = str(score)
    def scinsbuy_4(self):
        global score
        global global_fon
        if 'махарага.png' in have_scins:
            global_fon = 'махарага.png'
        elif score >= 1200000:
            score -= 1200000
            global_fon = 'махарага.png'
            have_scins.append('махарага.png')
            self.score_label.text = str(score)
    def scinsbuy_5(self):
        global score
        global global_fon
        if 'годжо.png' in have_scins:
            global_fon = 'годжо.png'
        elif score >= 1500000:
            score -= 1500000
            global_fon = 'годжо.png'
            have_scins.append('годжо.png')
            self.score_label.text = str(score)
    def scinsbuy_6(self):
        global score
        global global_fon
        if 'сукуна.png' in have_scins:
            global_fon = 'сукуна.png'
        elif score >= 2000000:
            score -= 2000000
            global_fon = 'сукуна.png'
            have_scins.append('сукуна.png')
            self.score_label.text = str(score)

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainWin())
        sm.add_widget(GameScr())
        sm.add_widget(UpdateScr())
        sm.add_widget(ScinsScr())
        return sm 
score = 0
click_score = 1
global_fon = 'пэ(обр).png'
have_scins = []
prise_list1 = 100
prise_list2 = 1000
prise_list3 = 10000



app = MyApp()
app.run()