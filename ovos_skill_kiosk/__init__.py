"""Kiosk: an assistant on a screen, by voice.

"Go full screen", "exit full screen", "keep the screen on", "let the screen
sleep", "install yourself as an app". The skill asks the screen through the
bus, and the screen's client does it:

    ovos.kiosk.fullscreen   {"enabled": bool}
    ovos.kiosk.keep_awake   {"enabled": bool}
    ovos.kiosk.install      {}
    ovos.kiosk.status       {}

and answers on <type>.response with what it is now:

    {"fullscreen": bool, "keep_awake": bool, "installed": bool,
     "needs_tap": bool, "supported": bool, "ios": bool}

`needs_tap`: a browser allows full screen and installing only after a tap,
so the screen shows one big button and the skill says to tap it. Without
an answer no screen client here handles kiosk requests, and the skill says
so. Emkay (OpenVoiceOS in the browser) answers them; another GUI client can
take the same messages.
"""
from ovos_bus_client.message import Message
from ovos_utils import classproperty
from ovos_utils.process_utils import RuntimeRequirements
from ovos_workshop.decorators import intent_handler
from ovos_workshop.skills import OVOSSkill

#: seconds to wait for the screen to answer
ANSWER_TIMEOUT = 3


class KioskSkill(OVOSSkill):

    @classproperty
    def runtime_requirements(self):
        return RuntimeRequirements(internet_before_load=False,
                                   network_before_load=False,
                                   gui_before_load=False,
                                   requires_internet=False,
                                   requires_network=False,
                                   requires_gui=False,
                                   no_internet_fallback=True,
                                   no_network_fallback=True,
                                   no_gui_fallback=True)

    def ask_screen(self, what: str, **data):
        """Send ovos.kiosk.<what>; the screen's answer, or None."""
        reply = self.bus.wait_for_response(Message(f"ovos.kiosk.{what}", data),
                                           f"ovos.kiosk.{what}.response", timeout=ANSWER_TIMEOUT)
        return reply.data if reply else None

    @intent_handler("fullscreen_on.intent")
    def handle_fullscreen_on(self, message: Message):
        state = self.ask_screen("fullscreen", enabled=True)
        if state is None:
            return self.speak_dialog("no_screen")
        if state.get("needs_tap"):
            return self.speak_dialog("tap_fullscreen")
        self.speak_dialog("fullscreen_on")

    @intent_handler("fullscreen_off.intent")
    def handle_fullscreen_off(self, message: Message):
        if self.ask_screen("fullscreen", enabled=False) is None:
            return self.speak_dialog("no_screen")
        self.speak_dialog("fullscreen_off")

    @intent_handler("keep_awake_on.intent")
    def handle_keep_awake_on(self, message: Message):
        if self.ask_screen("keep_awake", enabled=True) is None:
            return self.speak_dialog("no_screen")
        self.speak_dialog("keep_awake_on")

    @intent_handler("keep_awake_off.intent")
    def handle_keep_awake_off(self, message: Message):
        if self.ask_screen("keep_awake", enabled=False) is None:
            return self.speak_dialog("no_screen")
        self.speak_dialog("keep_awake_off")

    @intent_handler("install_app.intent")
    def handle_install_app(self, message: Message):
        state = self.ask_screen("install")
        if state is None:
            return self.speak_dialog("no_screen")
        if state.get("installed"):
            return self.speak_dialog("already_app")
        if state.get("needs_tap"):
            return self.speak_dialog("tap_install")
        self.speak_dialog("install_ios" if state.get("ios") else "install_unsupported")
