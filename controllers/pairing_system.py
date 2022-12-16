import operator


class Swiss_system:
    def generate_inital_pairs(self, players_list):
        """
        Pair the players by their rank: top-half[i] with bottom-half[i].
        Returns a tuple for each pair.
        """

        players_number = int(len(players_list) / 2)
        sorted_players = sorted(players_list, key=operator.attrgetter("rank"))
        top_players = sorted_players[players_number:]
        bottom_players = sorted_players[:players_number]
        pairs = [list(pair) for pair in zip(top_players, bottom_players)]

        return pairs

    def generate_pairs(self, players_list, matchs_list):
        """
        Pair the players by the points they made after each round.
        player[n] with player[n+1].
        If same score points, they are paired according to rank.
        If paired already occured, the next in position is picked
        """

        players_number = len(players_list)
        sorted_players = sorted(players_list, key=operator.attrgetter("points", "rank"))
        pairs = []

        for idx, player in enumerate(sorted_players[::2]):
            new_pair = (player, sorted_players[idx + 1])

            while new_pair in matchs_list:
                index = idx + 2
                new_pair = (player, sorted_players[index])
            else:
                pass

            sorted_players.remove(new_pair[O], new_pair[1])
            pairs.append(new_pair)

        return pairs
