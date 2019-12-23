H95 = """
linea 2 limitata alla tratta San Zaccaria "B"- Tronchetto via Canale della Giudecca e San Marco Giardinetti- P.le Roma via Canal Grande, servizio spola tramite mezzo acqueo fino ad altezza di marea a +135 cm, successivamente o in alternativa con autobus sostitutivo nel tratto P.le Roma - Tronchetto. Inoltre la stessa tratta può essere percorsa utilizzando il People Mover in partenza ogni 10 minuti.

linee 4.1 e 4.2 limitate alla tratta San Zaccaria "C" e "D"- Ospedale - F.te Nove - Murano - Tre Archi e viceversa con omissione del servizio San Zaccaria-Giudecca - P.le Roma - Ferrovia - Tre Archi e viceversa. Servizio spola tramite autobus sostitutivo tra P.le Roma e Santa Marta e servizio spola tramite mezzo acqueo tra Santa Marta e Sacca Fisola.

linea 5.1 limitata alla tratta Lido S.M.E. "A" - Ospedale - F.te Nove - Tre Archi e viceversa

linea 5.2 dirottata via Canal Grande e limitata alla tratta P.le Roma "D"- Lido S.M.E. "B" e viceversa

linea 6 dirottata via Canal Grande e limitata alla tratta P.le Roma "D" - Lido S.M.E. "B" e viceversa

NB: a Ferrovia le linee 5.1/5.2 fermano all'approdo "C" in direzione P.le Roma e all’approdo "D" in direzione Lido.

linea 3 SOSPESA

Nella fascia oraria notturna, dalle 20.00 alle 7.00, gli approdi di Murano Colonna “A” e “B” vengono sospese.
"""
H105 = (
    H95
    + """

Si sospende Rialto “B” causa pendenza passerella.
"""
)
H120 = (
    H105
    + """

Oltre alle precedenti disposizioni previste per marea superiore a 105 cm si sospende Zattere direzione San Marco-Lido per assenza passerelle di collegamento all’impianto.
"""
)
H125 = (
    H120
    + """

Oltre alle precedenti disposizioni della marea superiore a 120 cm non sono più agibili le passerelle di entrata agli impianti e al punto vendita di Rialto Linea 2 (approdi "C" e "D"), viene mantenuta l’accessibilità dell’impianto dalle uscite sino a 140 cm.
"""
)
H130 = (
    H125
    + """

Viene interdetto il transito sotto il ponte Vivarini di Murano e pertanto è sospeso il collegamento delle linee 4.1/4.2 nel tratto Colonna–Venier (Via Serenella).  Questo piano dei servizi è mantenuto sino all’altezza marea + 140 cm
"""
)
H140 = """
Il servizio di trasporto pubblico di linea viene sospeso nel suo complesso e vengono effettuati solamente i collegamenti con le isole dagli impianti che rimangono accessibili.
"""


def get_actv(hight: int) -> str:
    if hight >= 140:
        return H140
    elif hight >= 130:
        return H130
    elif hight >= 125:
        return H125
    elif hight >= 120:
        return H120
    elif hight >= 105:
        return H105
    elif hight >= 95:
        return H95
    return ""
