def is_posible(tablero_ordena, boat_size, dir, board_count, x,y):
   
    # funcion que se asegura de que no haya ya un barco donde se va a posicionar el barco nuevo 
    # segun sus coordinadas y la direccion 

    # input --> tablero_ordena = array 
    #           boat_size = int
    #           dir = str
    #           coordinadas = int(tupla)
    #                                   output --> booleano : True or False             
    import numpy as np
    aux = []
    
    # NORTE
    if dir.lower() == 'n' or dir.lower() == 'north':
        aux = tablero_ordena.copy()
        aux[x - (boat_size-1) : x+1, y]  = 'O'
    if np.count_nonzero(aux == 'O') == (board_count + boat_size):
        return True 
    # ESTE
    if dir.lower() == 'e' or dir.lower() == 'east':
        aux = tablero_ordena.copy()
        aux[x, y: y + (boat_size)]  = 'O'
        if np.count_nonzero(aux == 'O') == (board_count + boat_size):
            return True 
    # SUR
    if dir.lower() == 's' or dir.lower() == 'south':
        aux = tablero_ordena.copy()
        aux[x: x + (boat_size), y] = 'O'
        if np.count_nonzero(aux == 'O') == (board_count + boat_size):
            return True 
    # OESTE 
    if dir.lower() == 'w' or dir.lower() == 'west':
        aux = tablero_ordena.copy()
        aux[x, y-(boat_size-1): y+1]  = 'O'
        if np.count_nonzero(aux == 'O') == (board_count + boat_size):
            return True 

def is_direction(dir):
    return type(dir) == str and ( dir.lower() == 'n' or dir.lower() == 's' or dir.lower() == 'e' or dir.lower() == 'w' or dir.lower() == 'north' or dir.lower() == 'south' or dir.lower() == 'east' or dir.lower() == 'west')

