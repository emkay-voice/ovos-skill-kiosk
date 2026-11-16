"""Writes the intents and dialogs for the languages Emkay ships besides
English and Danish (those are in ovos_skill_kiosk/locale/ by hand), so they
can be reviewed and corrected in one place. From the repository root:

    python tools/translations.py
"""
import json
from pathlib import Path

INTENTS = ("fullscreen_on", "fullscreen_off", "keep_awake_on", "keep_awake_off", "install_app")
DIALOGS = ("no_screen", "tap_fullscreen", "fullscreen_on", "fullscreen_off", "keep_awake_on", "keep_awake_off",
           "already_app", "tap_install", "install_ios", "install_unsupported")

T = {
"de-DE": ([["vollbild", "geh in den vollbildmodus", "vollbild (an|ein)", "zeig es auf dem ganzen bildschirm"],
           ["vollbild (aus|beenden)", "verlass den vollbildmodus", "beende den vollbildmodus"],
           ["lass den bildschirm an", "schalte den bildschirm nicht aus", "bleib wach", "halte den bildschirm an"],
           ["lass den bildschirm schlafen", "du darfst den bildschirm ausschalten", "lass den bildschirm ausgehen"],
           ["installiere dich als app", "installiere die app", "leg dich auf den startbildschirm", "installiere emkay"]],
          ["Dieser Bildschirm kann das von hier aus nicht.", "Tippe auf den Knopf auf dem Bildschirm, dann gehe ich in den Vollbildmodus.",
           "Ich bin im Vollbildmodus.", "Der Vollbildmodus ist aus.", "Ich lasse den Bildschirm an.", "Der Bildschirm darf jetzt schlafen.",
           "Ich bin schon als App installiert.", "Tippe auf den Knopf auf dem Bildschirm, um mich als App zu installieren.",
           "Auf einem iPhone oder iPad: tippe auf Teilen und dann auf Zum Home-Bildschirm.", "Dieser Browser kann mich nicht als App installieren; versuch es mit Chrome oder Edge."],
          "Ein Assistent auf einem Bildschirm, per Stimme: Vollbild, Bildschirm anlassen, als App installieren.", ["Vollbild", "Lass den Bildschirm an", "Installiere dich als App"]),
"nl-NL": ([["volledig scherm", "ga naar volledig scherm", "volledig scherm aan", "toon het op het hele scherm"],
           ["volledig scherm uit", "verlaat volledig scherm", "stop volledig scherm"],
           ["houd het scherm aan", "zet het scherm niet uit", "blijf wakker", "laat het scherm aan"],
           ["laat het scherm slapen", "je mag het scherm uitzetten", "laat het scherm uitgaan"],
           ["installeer jezelf als app", "installeer de app", "zet jezelf op het beginscherm", "installeer emkay"]],
          ["Dit scherm kan dat van hieruit niet.", "Tik op de knop op het scherm, dan ga ik naar volledig scherm.",
           "Ik sta op volledig scherm.", "Volledig scherm is uit.", "Ik houd het scherm aan.", "Het scherm mag nu slapen.",
           "Ik ben al als app geïnstalleerd.", "Tik op de knop op het scherm om me als app te installeren.",
           "Op een iPhone of iPad: tik op Deel en dan op Zet op beginscherm.", "Deze browser kan me niet als app installeren; probeer Chrome of Edge."],
          "Een assistent op een scherm, met je stem: volledig scherm, scherm aan houden, als app installeren.", ["Volledig scherm", "Houd het scherm aan", "Installeer jezelf als app"]),
"fr-FR": ([["plein écran", "passe en plein écran", "active le plein écran", "affiche sur tout l'écran"],
           ["quitte le plein écran", "désactive le plein écran", "sors du plein écran"],
           ["garde l'écran allumé", "n'éteins pas l'écran", "reste éveillé", "laisse l'écran allumé"],
           ["laisse l'écran se mettre en veille", "tu peux éteindre l'écran", "laisse l'écran s'éteindre"],
           ["installe-toi comme application", "installe l'application", "ajoute-toi à l'écran d'accueil", "installe emkay"]],
          ["Cet écran ne peut pas faire ça d'ici.", "Touche le bouton à l'écran, et je passe en plein écran.",
           "Je suis en plein écran.", "Le plein écran est désactivé.", "Je garde l'écran allumé.", "L'écran peut se mettre en veille maintenant.",
           "Je suis déjà installé comme application.", "Touche le bouton à l'écran pour m'installer comme application.",
           "Sur un iPhone ou un iPad : touche Partager, puis Sur l'écran d'accueil.", "Ce navigateur ne peut pas m'installer comme application ; essaie Chrome ou Edge."],
          "Un assistant sur un écran, à la voix : plein écran, écran allumé, installation comme application.", ["Plein écran", "Garde l'écran allumé", "Installe-toi comme application"]),
"es-ES": ([["pantalla completa", "pon la pantalla completa", "activa la pantalla completa", "muéstralo en toda la pantalla"],
           ["sal de la pantalla completa", "quita la pantalla completa", "desactiva la pantalla completa"],
           ["mantén la pantalla encendida", "no apagues la pantalla", "quédate despierto", "deja la pantalla encendida"],
           ["deja que la pantalla se apague", "puedes apagar la pantalla", "deja que la pantalla duerma"],
           ["instálate como aplicación", "instala la aplicación", "ponte en la pantalla de inicio", "instala emkay"]],
          ["Esta pantalla no puede hacer eso desde aquí.", "Toca el botón de la pantalla y me pongo en pantalla completa.",
           "Estoy en pantalla completa.", "La pantalla completa está desactivada.", "Mantengo la pantalla encendida.", "La pantalla ya puede apagarse.",
           "Ya estoy instalado como aplicación.", "Toca el botón de la pantalla para instalarme como aplicación.",
           "En un iPhone o iPad: toca Compartir y luego Añadir a pantalla de inicio.", "Este navegador no puede instalarme como aplicación; prueba con Chrome o Edge."],
          "Un asistente en una pantalla, con la voz: pantalla completa, pantalla encendida, instalar como aplicación.", ["Pantalla completa", "Mantén la pantalla encendida", "Instálate como aplicación"]),
"it-IT": ([["schermo intero", "vai a schermo intero", "attiva lo schermo intero", "mostralo su tutto lo schermo"],
           ["esci dallo schermo intero", "disattiva lo schermo intero", "togli lo schermo intero"],
           ["tieni lo schermo acceso", "non spegnere lo schermo", "resta sveglio", "lascia lo schermo acceso"],
           ["lascia che lo schermo si spenga", "puoi spegnere lo schermo", "lascia dormire lo schermo"],
           ["installati come app", "installa l'app", "mettiti nella schermata home", "installa emkay"]],
          ["Questo schermo non può farlo da qui.", "Tocca il pulsante sullo schermo e passo a schermo intero.",
           "Sono a schermo intero.", "Lo schermo intero è disattivato.", "Tengo lo schermo acceso.", "Lo schermo può spegnersi ora.",
           "Sono già installato come app.", "Tocca il pulsante sullo schermo per installarmi come app.",
           "Su iPhone o iPad: tocca Condividi e poi Aggiungi alla schermata Home.", "Questo browser non può installarmi come app; prova Chrome o Edge."],
          "Un assistente su uno schermo, con la voce: schermo intero, schermo acceso, installare come app.", ["Schermo intero", "Tieni lo schermo acceso", "Installati come app"]),
"pt-BR": ([["tela cheia", "coloque em tela cheia", "ative a tela cheia", "mostre na tela inteira"],
           ["saia da tela cheia", "desative a tela cheia", "tire a tela cheia"],
           ["mantenha a tela ligada", "não desligue a tela", "fique acordado", "deixe a tela ligada"],
           ["deixe a tela dormir", "pode desligar a tela", "deixe a tela apagar"],
           ["instale-se como app", "instale o aplicativo", "coloque-se na tela inicial", "instale o emkay"]],
          ["Esta tela não consegue fazer isso daqui.", "Toque no botão da tela, e eu entro em tela cheia.",
           "Estou em tela cheia.", "A tela cheia está desligada.", "Vou manter a tela ligada.", "A tela pode dormir agora.",
           "Já estou instalado como app.", "Toque no botão da tela para me instalar como app.",
           "No iPhone ou iPad: toque em Compartilhar e depois em Adicionar à Tela de Início.", "Este navegador não consegue me instalar como app; experimente o Chrome ou o Edge."],
          "Um assistente numa tela, por voz: tela cheia, manter a tela ligada, instalar como app.", ["Tela cheia", "Mantenha a tela ligada", "Instale-se como app"]),
"pt-PT": ([["ecrã inteiro", "põe em ecrã inteiro", "ativa o ecrã inteiro", "mostra no ecrã todo"],
           ["sai do ecrã inteiro", "desativa o ecrã inteiro", "tira o ecrã inteiro"],
           ["mantém o ecrã ligado", "não desligues o ecrã", "fica acordado", "deixa o ecrã ligado"],
           ["deixa o ecrã dormir", "podes desligar o ecrã", "deixa o ecrã apagar"],
           ["instala-te como app", "instala a aplicação", "põe-te no ecrã principal", "instala o emkay"]],
          ["Este ecrã não consegue fazer isso daqui.", "Toca no botão no ecrã, e eu passo a ecrã inteiro.",
           "Estou em ecrã inteiro.", "O ecrã inteiro está desligado.", "Vou manter o ecrã ligado.", "O ecrã pode dormir agora.",
           "Já estou instalado como app.", "Toca no botão no ecrã para me instalares como app.",
           "Num iPhone ou iPad: toca em Partilhar e depois em Adicionar ao ecrã principal.", "Este navegador não me consegue instalar como app; experimenta o Chrome ou o Edge."],
          "Um assistente num ecrã, por voz: ecrã inteiro, manter o ecrã ligado, instalar como app.", ["Ecrã inteiro", "Mantém o ecrã ligado", "Instala-te como app"]),
"ca-ES": ([["pantalla completa", "posa la pantalla completa", "activa la pantalla completa", "mostra-ho a tota la pantalla"],
           ["surt de la pantalla completa", "desactiva la pantalla completa", "treu la pantalla completa"],
           ["mantén la pantalla encesa", "no apaguis la pantalla", "queda't despert", "deixa la pantalla encesa"],
           ["deixa que la pantalla s'apagui", "pots apagar la pantalla", "deixa dormir la pantalla"],
           ["instal·la't com a aplicació", "instal·la l'aplicació", "posa't a la pantalla d'inici", "instal·la emkay"]],
          ["Aquesta pantalla no ho pot fer des d'aquí.", "Toca el botó de la pantalla i em poso a pantalla completa.",
           "Estic a pantalla completa.", "La pantalla completa està desactivada.", "Mantinc la pantalla encesa.", "La pantalla ja pot dormir.",
           "Ja estic instal·lat com a aplicació.", "Toca el botó de la pantalla per instal·lar-me com a aplicació.",
           "En un iPhone o iPad: toca Comparteix i després Afegeix a la pantalla d'inici.", "Aquest navegador no em pot instal·lar com a aplicació; prova amb Chrome o Edge."],
          "Un assistent en una pantalla, amb la veu: pantalla completa, pantalla encesa, instal·lar com a aplicació.", ["Pantalla completa", "Mantén la pantalla encesa", "Instal·la't com a aplicació"]),
"gl-ES": ([["pantalla completa", "pon a pantalla completa", "activa a pantalla completa", "amósao en toda a pantalla"],
           ["sae da pantalla completa", "desactiva a pantalla completa", "quita a pantalla completa"],
           ["mantén a pantalla acesa", "non apagues a pantalla", "queda esperto", "deixa a pantalla acesa"],
           ["deixa que a pantalla se apague", "podes apagar a pantalla", "deixa durmir a pantalla"],
           ["instálate como aplicación", "instala a aplicación", "ponte na pantalla de inicio", "instala emkay"]],
          ["Esta pantalla non pode facer iso dende aquí.", "Toca o botón da pantalla e póñome en pantalla completa.",
           "Estou en pantalla completa.", "A pantalla completa está desactivada.", "Manteño a pantalla acesa.", "A pantalla xa pode durmir.",
           "Xa estou instalado como aplicación.", "Toca o botón da pantalla para instalarme como aplicación.",
           "Nun iPhone ou iPad: toca Compartir e despois Engadir á pantalla de inicio.", "Este navegador non me pode instalar como aplicación; proba con Chrome ou Edge."],
          "Un asistente nunha pantalla, coa voz: pantalla completa, pantalla acesa, instalar como aplicación.", ["Pantalla completa", "Mantén a pantalla acesa", "Instálate como aplicación"]),
"eu-ES": ([["pantaila osoa", "jarri pantaila osoan", "aktibatu pantaila osoa", "erakutsi pantaila osoan"],
           ["irten pantaila osotik", "desaktibatu pantaila osoa", "kendu pantaila osoa"],
           ["mantendu pantaila piztuta", "ez itzali pantaila", "egon esna", "utzi pantaila piztuta"],
           ["utzi pantaila lotan", "pantaila itzal dezakezu", "utzi pantaila itzaltzen"],
           ["instalatu zure burua aplikazio gisa", "instalatu aplikazioa", "jarri hasierako pantailan", "instalatu emkay"]],
          ["Pantaila honek ezin du hori hemendik egin.", "Sakatu pantailako botoia, eta pantaila osoan jarriko naiz.",
           "Pantaila osoan nago.", "Pantaila osoa desaktibatuta dago.", "Pantaila piztuta mantenduko dut.", "Pantaila lotara joan daiteke orain.",
           "Dagoeneko aplikazio gisa instalatuta nago.", "Sakatu pantailako botoia aplikazio gisa instalatzeko.",
           "iPhone edo iPad batean: sakatu Partekatu eta gero Gehitu hasierako pantailan.", "Nabigatzaile honek ezin nau aplikazio gisa instalatu; probatu Chrome edo Edge."],
          "Pantaila bateko laguntzailea, ahotsez: pantaila osoa, pantaila piztuta, aplikazio gisa instalatu.", ["Pantaila osoa", "Mantendu pantaila piztuta", "Instalatu zure burua aplikazio gisa"]),
}

ROOT = Path(__file__).parent.parent / "ovos_skill_kiosk" / "locale"
ICON = "https://raw.githubusercontent.com/emkay-voice/ovos-skill-kiosk/main/res/icon.png"
for lang, (intents, dialogs, desc, examples) in T.items():
    loc = ROOT / lang
    loc.mkdir(parents=True, exist_ok=True)
    for name, lines in zip(INTENTS, intents):
        (loc / f"{name}.intent").write_text("\n".join(lines) + "\n", encoding="utf-8")
    for name, text in zip(DIALOGS, dialogs):
        (loc / f"{name}.dialog").write_text(text + "\n", encoding="utf-8")
    (loc / "skill.json").write_text(json.dumps({
        "skill_id": "ovos-skill-kiosk.emkay-voice", "source": "https://github.com/emkay-voice/ovos-skill-kiosk",
        "name": "Kiosk", "description": desc, "examples": examples, "icon": ICON,
        "tags": ["kiosk", "screen", "emkay"]}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(lang)
