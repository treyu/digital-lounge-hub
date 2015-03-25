from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.lang import Builder
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics.fbo import Fbo
from kivy.graphics import ClearBuffers, ClearColor

kv = '''
<FeedButton@Button>:
    font_size: 20
    size_hint: 0.25, 0.1
<HubFeed>:
    orientation: 'tb-rl'
    FeedButton:
        on_release: root.change_image(pool.text)
        StackLayout:
            pos: self.parent.pos
            size: self.parent.size
            orientation: 'lr-tb'
            padding: 10
            Image:
                id: pool_arrow
                size_hint: 0.20, 1
                source: 'images/arrow.png'
                opacity: 0
            Label:
                id: pool
                size_hint: 0.70, 1
                text: 'Pool'
    FeedButton:
        on_release: root.change_image(foosball.text)
        StackLayout:
            pos: self.parent.pos
            size: self.parent.size
            orientation: 'lr-tb'
            padding: 10
            Image:
                id: foosball_arrow
                size_hint: 0.20, 1
                source: 'images/arrow.png'
                opacity: 0
            Label:
                id: foosball
                size_hint: 0.70, 1
                text: 'Foosball'
    FeedButton:
        on_release: root.change_image(poker.text)
        StackLayout:
            pos: self.parent.pos
            size: self.parent.size
            orientation: 'lr-tb'
            padding: 10
            Image:
                id: poker_arrow
                size_hint: 0.20, 1
                source: 'images/arrow.png'
                opacity: 0
            Label:
                id: poker
                size_hint: 0.70, 1
                text: 'Poker'
    FeedButton:
        on_release: root.change_image(smash.text)
        StackLayout:
            pos: self.parent.pos
            size: self.parent.size
            orientation: 'lr-tb'
            padding: 10
            Image:
                id: smash_arrow
                size_hint: 0.20, 1
                source: 'images/arrow.png'
                opacity: 0
            Label:
                id: smash
                size_hint: 0.70, 1
                text: 'Smash'
    FeedButton:
        on_release: root.change_image(pingpong.text)
        StackLayout:
            pos: self.parent.pos
            size: self.parent.size
            orientation: 'lr-tb'
            padding: 10
            Image:
                id: pingpong_arrow
                size_hint: 0.20, 1
                source: 'images/arrow.png'
                opacity: 0
            Label:
                id: pingpong
                size_hint: 0.70, 1
                text: 'Ping Pong'
    Label:
        text: ''
        size_hint: 0.25, 0.4999999
        canvas.before:
            Color:
                rgba: 0.60, 0.60, 0.60, 1
            Rectangle:
                pos: self.pos
                size: self.size
    Image:
        id: currentEvent
        size_hint: 0.75, 1
        canvas:
            Clear
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                source: 'images/tournament-bracket.png'
                size: self.width, self.height
'''
Builder.load_string(kv)


class HubFeed(StackLayout):
    def change_image(self, txt):
        self.ids.currentEvent.canvas.clear()
        self.ids.currentEvent.size_hint = (0.75, 1)

        with self.ids.currentEvent.canvas:
            self.fbo = Fbo(size=self.size)
            self.rect = Rectangle(source='', size=(0.75*self.width, self.height))

        with self.fbo:
            ClearColor(0, 0, 0, 0)
            ClearBuffers()

        self.ids.pool_arrow.opacity = 0
        self.ids.foosball_arrow.opacity = 0
        self.ids.poker_arrow.opacity = 0
        self.ids.smash_arrow.opacity = 0
        self.ids.pingpong_arrow.opacity = 0

        if txt == 'Pool':
            self.rect.source = 'images/pool.jpg'
            self.ids.pool_arrow.opacity = 1
        elif txt == 'Foosball':
            self.rect.source = 'images/foosball.jpg'
            self.ids.foosball_arrow.opacity = 1
        elif txt == 'Poker':
            self.rect.source = 'images/poker.jpg'
            self.ids.poker_arrow.opacity = 1
        elif txt == 'Smash':
            self.rect.source = 'images/smash.jpg'
            self.ids.smash_arrow.opacity = 1
        elif txt == 'Ping Pong':
            self.rect.source = 'images/ping-pong.png'
            self.ids.pingpong_arrow.opacity = 1
        else:
            self.rect.source = 'images/tournament-bracket.png'
    pass

class CurrentEvent(AnchorLayout):
    pass


class HubApp(App):
    def build(self):
        return HubFeed()

if __name__ == '__main__':
    HubApp().run()
