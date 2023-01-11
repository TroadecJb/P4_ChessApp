import operator


class SwissSystem:
    def generate_inital_pairs(self, players_list):
        """
        Pair the players by their rank: top-half[i] with bottom-half[i].
        Returns a tuple for each pair.
        """

        players_number = int(len(players_list) / 2)
        sorted_players = sorted(
            players_list, key=operator.attrgetter("rank"), reverse=True
        )
        top_players = sorted_players[:players_number]
        bottom_players = sorted_players[players_number:]
        pairs = [list(pair) for pair in zip(top_players, bottom_players)]

        return pairs

    def generate_pairs(self, players_list, matchs_list):
        """
        Pair the players by the points they made after each round.
        player[n] with player[n+1].
        If same score points, they are paired according to rank.
        If the pair already occured, the next player in position is picked
        """

        players_number = len(players_list)
        sorted_players = sorted(
            players_list, key=operator.attrgetter("points", "rank"), reverse=True
        )

        pairs = []

        while sorted_players:
            pair_to_check = sorted(
                [sorted_players[0], sorted_players[1]],
                key=operator.attrgetter("doc_id"),
            )

            if len(sorted_players) > 2:
                idx = 2
                while pair_to_check in matchs_list:
                    try:
                        pair_to_check = sorted(
                            [sorted_players[0], sorted_players[idx]],
                            key=operator.attrgetter("doc_id"),
                        )
                        idx += 1
                    except IndexError:
                        break

            pair = [pair_to_check[0], pair_to_check[1]]
            sorted_players.remove(pair_to_check[0])
            sorted_players.remove(pair_to_check[1])

            pairs.append(pair)
            # matchs_list.append(pair)

        return pairs
