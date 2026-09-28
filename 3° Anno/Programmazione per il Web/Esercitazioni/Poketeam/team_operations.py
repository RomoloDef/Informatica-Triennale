import requests
from requests.exceptions import RequestException

# Simula un database in memoria per semplicità
TEAMS_DATABASE = {}
NEXT_TEAM_ID = 1


def create_team(body):
    """
    Implementa l'operazione 'create_team' definita nell'OpenAPI YAML.

    Connexion si occupa di:
    1. Validare il 'body' della richiesta contro lo schema 'NewTeamRequest'.
       Se la validazione fallisce (es. 'name' mancante), la funzione non viene nemmeno chiamata
       e Connexion restituisce automaticamente un errore 400.
    2. Passare il corpo deserializzato della richiesta come un dizionario Python (body).
    """
    global NEXT_TEAM_ID

    # 1. Estrai i dati validati da Connexion
    team_name = body.get('name')
    trainer_name = body.get('trainer')
    pokemon_names = body.get('pokemon_names', [])

    # 2. Logica di Business
    if len(pokemon_names) > 6:
        # Anche se c'è 'maxItems: 6' nello schema, aggiungiamo una verifica esplicita
        # per logiche più complesse che non possono essere coperte solo dallo schema.
        # Connexion gestisce già la maggior parte degli errori di validazione dello schema.
        return {"error": "Un team non può avere più di 6 Pokémon."}, 400

    team_id = NEXT_TEAM_ID

    # 3. Salva i dati simulati nel "database"
    new_team = {
        "id": team_id,
        "name": team_name,
        "trainer": trainer_name,
        "pokemon_names": pokemon_names,
        "members_count": len(pokemon_names)
    }

    TEAMS_DATABASE[team_id] = new_team
    NEXT_TEAM_ID += 1

    # 4. Prepara la risposta (Connexion serializza questo dict in JSON e
    #    lo valida contro lo schema 'Team' definito per il 201)
    response_data = {
        "id": new_team["id"],
        "name": new_team["name"],
        "trainer": new_team["trainer"],
        "members_count": new_team["members_count"]
    }

    # Restituisci l'oggetto e il codice di stato HTTP
    return response_data, 201

# Aggiungi qui altre funzioni come get_team_by_id, update_team, ecc.

def get_team_by_id(team_id):
    """ 
    Implementa l'operazione 'get_team_by_id' definita nell'OpenAPI YAML.
    """ 
    team = TEAMS_DATABASE.get(team_id)
    if not team:
        return {"error": "Team non trovato."}, 404

    response_data = {
        "id": team["id"],
        "name": team["name"],
        "trainer": team["trainer"],
        "members_count": team["members_count"]
    }

    return response_data, 200

def get_pokemon_details(team_id, pokemon_name):
    """
    Implementa l'operazione 'get_pokemon_details' definita nell'OpenAPI YAML.
    Logica Piggybacking: verifica interna del Team e chiamata a PokéAPI.
    """
    # 1. Verificare l'esistenza del Team interno (team_operations.get_team_by_id)
    team = TEAMS_DATABASE.get(team_id)
    if not team:
        return {"error": f"Team con ID {team_id} non trovato."}, 404

    # 2. Verificare se il Pokémon è nel Team
    # Assumendo che 'pokemon_names' contenga una lista di stringhe con i nomi
    pokemon_found = any(p['name'].lower() == pokemon_name.lower() 
                        for p in team.get('pokemon_names', []))
    
    if not pokemon_found:
        return {"error": f"Il Pokémon '{pokemon_name}' non è nel Team ID {team_id}."}, 404

    # 3. Effettuare una chiamata GET alla PokéAPI
    # L'API Pokémon usa nomi in minuscolo
    pokeapi_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"

    try:
        response = requests.get(pokeapi_url)
        
        if response.status_code == 404:
            # Il Team esiste, il Pokémon è nel Team, ma PokéAPI non lo conosce
            return {"error": f"Pokémon '{pokemon_name}' non trovato su PokéAPI."}, 404
            
        response.raise_for_status() # Solleva un'eccezione per gli errori HTTP (es. 5xx)
        pokeapi_data = response.json()

    except RequestException:
        # Errore di connessione o HTTP (es. timeout, 500 dell'API esterna)
        return {"error": "Impossibile recuperare i dati da PokéAPI."}, 502

    # 4. Combinare i dati ottenuti da PokéAPI con i dati interni del Team
    enriched_data = {
        "team_id": team_id,
        "pokemon_name": pokemon_name,
        "height": pokeapi_data.get('height'),  # Altezza in decimetri
        "weight": pokeapi_data.get('weight'),  # Peso in ettogrammi
        # Aggiungi qui altri dati che vuoi (es. types, abilities)
    }

    # 5. Restituire un JSON che contenga entrambe le informazioni
    return enriched_data, 200
