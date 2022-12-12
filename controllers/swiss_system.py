import operator


def generate_inital_pairs(players_list):
    """
    Pair the players by their rank: top-half[i] with bottom-half[i].
    Returns a tuple for each pair.
    """

    players_number = len(players_list)
    sorted_players = sorted(players_list, key=operator.attrgetter("rank"))
    top_players = sorted_players[players_number:]
    bottom_players = sorted_players[:players_number]
    pairs = zip(top_players, bottom_players)

    return pairs


def generate_pairs(players_list):
    """
    Pair the players by the points they made after each round.
    player[n] with player[n+1].
    If same score points, they are paired according to rank.
    """

    players_number = len(players_list)
    sorted_players = sorted(players_list, key=operator.attrgetter("points", "rank"))
    pairs = []
    for idx, player in enumerate(sorted_players[::2]):
        pairs.append((player, sorted_players[idx + 1]))

    return pairs
