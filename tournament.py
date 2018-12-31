import itertools


def run_tournament(checked_strategies, rounds, to_score):
    results = {}
    for strategy in checked_strategies:  # register players in checklist order
        results[strategy.name] = 0
    matchups = list(itertools.combinations(checked_strategies, 2))
    for game_num in range(rounds):
        # a tournament round begins here
        for matchup in matchups:
            # a game begins here
            players = []
            for player in matchup:
                # reinitialize each player with tournament to_score
                player.__init__(to_score)
                players.append(player)
            players[0].reg_opponent(players[1])
            players[1].reg_opponent(players[0])
            # change who goes first every other round, to give
            # greedy strategies a fair chance
            if game_num % 2 == 0:
                players = players[::-1]
            game_over = False
            while not game_over:
                for player in players:
                    val = player.turn()
                    if val == "win":
                        results[player.name] += 1
                        game_over = True
                        break
        progress = (game_num + 1) / rounds
        yield progress, results
