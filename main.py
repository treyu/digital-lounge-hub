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
        id: pool
        text: 'Pool'
        on_release: root.change_image(pool.text)
    FeedButton:
        id: foosball
        text: 'Foosball'
        on_release: root.change_image(foosball.text)
    FeedButton:
        id: poker
        text: 'Poker'
        on_release: root.change_image(poker.text)
    FeedButton:
        id: smash
        text: 'Smash'
        on_release: root.change_image(smash.text)
    FeedButton:
        id: pingpong
        text: 'Ping Pong'
        on_release: root.change_image(pingpong.text)
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
        canvas:
            Clear
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                source: 'images/tournament-bracket.png'
                size: 0.75*self.width, self.height
'''
Builder.load_string(kv)


class HubFeed(StackLayout):
    def change_image(self, txt):
        self.ids.currentEvent.canvas.clear()
        with self.ids.currentEvent.canvas:
            self.fbo = Fbo(size=self.size)
            self.rect = Rectangle(source='', size=(0.75*self.width, self.height))

        with self.fbo:
            ClearColor(0, 0, 0, 0)
            ClearBuffers()

        if txt == 'Pool':
            self.rect.source = 'images/pool.jpg'
        elif txt == 'Foosball':
            self.rect.source = 'images/foosball.jpg'
        elif txt == 'Poker':
            self.rect.source = 'images/poker.jpg'
        elif txt == 'Smash':
            self.rect.source = 'images/smash.jpg'
        elif txt == 'Ping Pong':
            self.rect.source = 'images/ping-pong.png'
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
