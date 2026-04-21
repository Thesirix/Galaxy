"""Menu overlay widget for the Galaxy game."""

from kivy.uix.relativelayout import RelativeLayout


class MenuWidget(RelativeLayout):
    """Semi-transparent overlay that intercepts touch events when visible."""

    def on_touch_down(self, touch):
        if self.opacity == 0:
            return False
        return super(RelativeLayout, self).on_touch_down(touch)
