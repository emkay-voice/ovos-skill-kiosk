"""Kiosk asks the screen through the bus and says what happened."""
import sys
from pathlib import Path

import pytest
from ovos_bus_client.message import Message
from ovos_utils.fakebus import FakeBus

ROOT = Path(__file__).parent.parent / "ovos_skill_kiosk"
sys.path.insert(0, str(ROOT.parent))
import ovos_skill_kiosk as pkg  # noqa: E402

LANGS = ["en-US", "da-DK", "de-DE", "nl-NL", "fr-FR", "es-ES", "it-IT",
         "pt-BR", "pt-PT", "ca-ES", "gl-ES", "eu-ES"]
DIALOGS = ("no_screen", "tap_fullscreen", "fullscreen_on", "fullscreen_off", "keep_awake_on", "keep_awake_off",
           "already_app", "tap_install", "install_ios", "install_unsupported")
INTENTS = ("fullscreen_on", "fullscreen_off", "keep_awake_on", "keep_awake_off", "install_app")


@pytest.fixture
def skill(monkeypatch):
    monkeypatch.setattr(pkg, "ANSWER_TIMEOUT", 0.5)
    bus = FakeBus()
    spoken = []
    bus.on("speak", lambda m: spoken.append(Message.deserialize(m) if isinstance(m, str) else m))
    s = pkg.KioskSkill(bus=bus, skill_id="ovos-skill-kiosk.emkay-voice")
    s.spoken = spoken
    yield s
    s.shutdown()


def screen(skill, answers):
    """A screen client that answers ovos.kiosk.* with `answers[type]`."""
    asked = []
    for t, data in answers.items():
        def answer(message, t=t, data=data):
            m = Message.deserialize(message) if isinstance(message, str) else message
            asked.append((t, m.data))
            skill.bus.emit(m.reply(f"{t}.response", data))
        skill.bus.on(t, answer)
    return asked


def said(skill):
    return skill.spoken[-1].data["utterance"]


def test_no_screen_client(skill):
    skill.handle_fullscreen_on(Message("x"))
    assert "can't" in said(skill)


def test_fullscreen_needs_a_tap(skill):
    asked = screen(skill, {"ovos.kiosk.fullscreen": {"needs_tap": True, "fullscreen": False}})
    skill.handle_fullscreen_on(Message("x"))
    assert asked == [("ovos.kiosk.fullscreen", {"enabled": True})]
    assert "Tap" in said(skill)


def test_keep_awake_off(skill):
    asked = screen(skill, {"ovos.kiosk.keep_awake": {"keep_awake": False}})
    skill.handle_keep_awake_off(Message("x"))
    assert asked == [("ovos.kiosk.keep_awake", {"enabled": False})]
    assert "sleep" in said(skill)


def test_install_on_ios(skill):
    screen(skill, {"ovos.kiosk.install": {"installed": False, "supported": False, "ios": True}})
    skill.handle_install_app(Message("x"))
    assert "Home Screen" in said(skill)


@pytest.mark.parametrize("lang", LANGS)
def test_every_language_has_everything(lang):
    loc = ROOT / "locale" / lang
    code = (ROOT / "__init__.py").read_text()
    for i in INTENTS:
        assert (loc / f"{i}.intent").read_text(encoding="utf-8").strip(), i
        assert f'"{i}.intent"' in code
    for d in DIALOGS:
        assert (loc / f"{d}.dialog").read_text(encoding="utf-8").strip(), d


def test_the_panel_page_sends_only_what_the_screen_answers():
    import json
    page = json.loads((ROOT / "controlpanel.json").read_text())
    sent = set()

    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k in ("query", "send"):
                    sent.add(v)
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(page)
    assert sent == {"ovos.kiosk.status", "ovos.kiosk.fullscreen", "ovos.kiosk.keep_awake", "ovos.kiosk.install"}


@pytest.mark.parametrize("lang", LANGS)
def test_the_panel_page_in_every_language(lang):
    import json
    en = json.loads((ROOT / "locale" / "en-US" / "controlpanel.json").read_text())
    d = json.loads((ROOT / "locale" / lang / "controlpanel.json").read_text())
    assert set(d) == set(en) and all(d.values())
