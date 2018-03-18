import logging

from telegram import KeyboardButton as KB

from start import mybot

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

start_buttons = [  # [KB('/elezioni')],
    [KB('/biblioteche'), KB('/segreterie')], [KB('/mensa'), KB('/info')]]
start_text = "Seleziona un comando dalla tastiera"

mybot.text_generator('start', start_text, start_buttons)
mybot.text_generator('home', start_text, start_buttons)
mybot.text_generator('info', "Questo bot è stato sviluppato da fundor333.com ed il sorgente è disponibile presso" +
                     " https://github.com/SamarcandaProject/helpunivebot.\n" +
                     "Questo Bot fa parte del Samarcanda Project a cui potete partecipare e collaborare. Per farlo basta andare https://samarcandaproject.github.io/\n" +
                     "Ringrazio https://t.me/isolachenoncearte per il supporto morale e non solo fornitomi",
                     [[KB('/home')]])
