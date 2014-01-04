'''
A collection of color palettes for data visualization. 
In 1965, Kenneth Kelly presented a sequence of 22 colors
that maximize the contrast between individual colors.
The human visual system does not respond linearly to 
different colors and so selecting a palette of colors
evenly distributed throughout an RGB, HSV, or HSL
colorspace would result in some colors that appear
similar to the human visual system and possible cause
confusion. Scientific data visualization relies on
being able to communicate clearly and effectively with
colors. Hence this Python module.

Available palettes:

    kelly_22 -- The original 22 color sequence by Kelly
    
    kelly_20 -- The original minus black and white

    kelly_19 -- The original minus black, white, and gray

Calling sequence:

    >>> from color_palette import palette
    >>> my_colors = palette.kelly_22()

'''

def kelly_22():
    '''A maximally-contrasting palette of colors designed by Kenneth Kelly.'''
    palette = [\
               '#FFFFFF',\
               '#000000',\
               '#EAD846',\
               '#6F0989',\
               '#D9712A',\
               '#97C9E4',\
               '#B82035',\
               '#C3C385',\
               '#7F8082',\
               '#62AC49',\
               '#CE81AD',\
               '#476CB3',\
               '#DB8963',\
               '#491093',\
               '#DFAA36',\
               '#8F0189',\
               '#E7F45E',\
               '#7C1B15',\
               '#94B741',\
               '#6C3715',\
               '#D03227',\
               '#2B3916'\
               ]
    return palette

def kelly_20():
    '''A maximally-contrasting palette of colors designed by Kenneth Kelly, but without white or black'''
    palette = [\
               '#EAD846',\
               '#6F0989',\
               '#D9712A',\
               '#97C9E4',\
               '#B82035',\
               '#C3C385',\
               '#7F8082',\
               '#62AC49',\
               '#CE81AD',\
               '#476CB3',\
               '#DB8963',\
               '#491093',\
               '#DFAA36',\
               '#8F0189',\
               '#E7F45E',\
               '#7C1B15',\
               '#94B741',\
               '#6C3715',\
               '#D03227',\
               '#2B3916'\
               ]
    return palette

def kelly_19():
    '''A maximally-contrasting palette of colors designed by Kenneth Kelly, but without white, black, or gray.'''
    palette = [\
               '#EAD846',\
               '#6F0989',\
               '#D9712A',\
               '#97C9E4',\
               '#B82035',\
               '#C3C385',\
               '#62AC49',\
               '#CE81AD',\
               '#476CB3',\
               '#DB8963',\
               '#491093',\
               '#DFAA36',\
               '#8F0189',\
               '#E7F45E',\
               '#7C1B15',\
               '#94B741',\
               '#6C3715',\
               '#D03227',\
               '#2B3916'\
               ]
    return palette
