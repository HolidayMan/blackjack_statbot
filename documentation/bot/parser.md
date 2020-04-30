###Use:

    parser = Parser('login', 'password') # credentials for cbets.su
    parser.get_json() # get json with games
    parser.get_games() # get serialized json from the website
    
    # parser.get_json() -> dict object
    # parser.get_games() -> <Games> object
    
    parsed_games = parser.get_games()
    print(parsed_games.games)
> [<Game 234372320>, <Game 234371979>, <Game 234371780>, <Game 234371576>, <Game 234371395>, <Game 234371196>, <Game 234370964>, <Game 234370816>, <Game 234370563>, <Game 234370339>]

