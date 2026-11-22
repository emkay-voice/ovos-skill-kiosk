# <img src='res/icon.png' width='50' height='50' style='vertical-align:bottom'/> Kiosk

An [OpenVoiceOS](https://openvoiceos.org) skill for an assistant that lives
on a screen: a phone on its charger, a tablet on the wall, a Pi in kiosk
mode. By voice:

```
"Go full screen"                 "Fuld skærm"
"Exit full screen"               "Afslut fuld skærm"
"Keep the screen on"             "Hold skærmen tændt"
"Let the screen sleep"           "Lad skærmen sove"
"Install yourself as an app"     "Installer dig som app"
```

Made for [Emkay](https://github.com/emkay-voice/emkay), OpenVoiceOS in the
browser, in all twelve languages it ships (the translations other than
English and Danish are in [`tools/translations.py`](tools/translations.py)).

## How it works

The skill does not touch the screen itself. It asks over the bus, OVOS
style, and a PHAL plugin for the device's screen does it and answers:

| request | data | answer on `<type>.response` |
|---|---|---|
| `ovos.kiosk.fullscreen` | `{"enabled": true/false}` | the state below |
| `ovos.kiosk.keep_awake` | `{"enabled": true/false}` | |
| `ovos.kiosk.install` | `{}` | |
| `ovos.kiosk.status` | `{}` | |

```json
{"fullscreen": false, "keep_awake": true, "installed": false,
 "needs_tap": true, "supported": true, "ios": false}
```

A browser allows full screen and installing as an app only after a tap,
not on its own. So the page shows one big button ("Tap for full screen")
and answers `needs_tap`, and the skill says to tap it; `<type>.done`
follows once it is done. When nothing answers within three seconds, the
skill says this screen can't do that.

In Emkay, [ovos-phal-plugin-browser](https://github.com/emkay-voice/ovos-phal-plugin-browser)
answers these messages (with the page doing the part only a browser tab
can). A PHAL plugin for other hardware (a kiosk shell, a Mark II screen)
can take the same ones.

## In the control panel

The skill brings its own page for [ovos-control-panel](https://github.com/OpenVoiceOS/ovos-control-panel)
(`controlpanel.json`, under *Screen*): whether the screen is full screen, kept
on and installed as an app, with buttons for each. The page sends the same
`ovos.kiosk.*` messages as the skill, so the screen's client answers them
itself. In all of Emkay's languages.

## License

Apache-2.0
