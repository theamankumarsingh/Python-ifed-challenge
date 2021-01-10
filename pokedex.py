#import all necessary packages
import pokemon as pk, os, PySimpleGUI as sg

#code
layout = [  [sg.Text('Enter Pokemon:'), sg.Input(key='-INPUT-'),sg.Button('GO!')],
            [sg.Text(size=(50,25), key='-OUTPUT-',background_color='RED')],
            [sg.Button('About'),sg.Button('Quit')]] #window layout
sg.theme('Reds') #window theme
window = sg.Window('Pokedex', layout)
while True:
    event, values = window.read() #read events
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    message=''''''; color='WHITE' #message to be displayed and the color of the message's text
    if event=='GO!': #search pokemon
        pokemon=values['-INPUT-'].strip()
        if pokemon=='' or not pk.checkPokemon(pokemon): #check if the pokemon exists or not
            continue
        message="This is "+pokemon+". It is a "+pk.pokemonType(pokemon)+" type pokemon. It's abilities are "
        message+=', '.join(pk.pokemonAbilities(pokemon))
        message+='. It takes double damage from '
        message+=', '.join(pk.doubleDamageType(pokemon))
        message+=' type pokemons. Some of such pokemons to watch out for are  '
        message+=', '.join(pk.doubleDamageFrom(pokemon))
        message+='.'
        color='WHITE'  
    if event=='About': #about pokedex
        message='''I'm Dexter, a Pokédex programmed by Professor Oak for Pokémon Trainer Aman Singh of the town of Pallet. My function is to provide Aman with information and advice regarding Pokémon and their training. If lost or stolen, I cannot be replaced.'''
        color='GREEN'
    window['-OUTPUT-'].update(message,text_color=color) #display message
window.close() #close window