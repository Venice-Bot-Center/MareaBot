H95 = """
*Linea 2* limitata da San Zaccaria a Tronchetto e da San Marco Giardinetti a P.le Roma.

*Linee 4.1 e 4.2* limitate alla tratta San Zaccaria - F.te Nove - Murano - Tre Archi con omissione San Zaccaria - Giudecca - P.le Roma - Tre Archi. Servizio spola bus tra P.le Roma e S. Marta e servizio spola motoscafo tra S. Marta e Sacca Fisola.

*Linea 5.1* limitata alla tratta Lido S.M.E. "A" - Ospedale - F.te Nove - Tre Archi

*Linea 5.2 e 6* dirottata via Canal Grande e limitata P.le Roma- Lido S.M.E.

*Linea 3 SOSPESA*

Nella fascia oraria notturna, dalle 20.00 alle 7.00, gli approdi di Murano Colonna “A” e “B” vengono sospese.
"""

H120 = (
    H95
    + """

Si sospende Zattere direzione San Marco-Lido per assenza passerelle di collegamento all’impianto.
"""
)

H130 = (
    H120
    + """

E' sospeso il collegamento delle _linee 4.1/4.2_ nel tratto Colonna–Venier.
"""
)
H140 = """
*Il servizio di trasporto pubblico di Linea viene sospeso nel suo complesso e vengono effettuati solamente i collegamenti con le isole dagli impianti che rimangono accessibili.*
"""


def get_actv(hight: int) -> (str,int) :
    if hight >= 140:
        return H140,140
    elif hight >= 130:
        return H130,130
    elif hight >= 120:
        return H120,120
    elif hight >= 95:
        return H95,95
    return "",0
