import networkx as nx
import matplotlib.pyplot as plt

class Player:
    def __init__(self):
        self.id = id
        self.score = None
        self.move = None

    def getPlayer(self):
        return self

    def makeMove(self):
        return None



class Graph:
    def __init__(self):
        self.g = nx.Graph()
        self.p = Player()

    def fillBoard(self):
        self.g.add_node(0, id=0, nombre="0", pos=[1, 9], color="orange")
        self.g.add_node(1, id=1, nombre="1", pos=[2, 9], color="orange")
        self.g.add_node(2, id=2, nombre="2", pos=[3, 9], color="orange")
        self.g.add_node(3, id=3, nombre="3", pos=[4, 9], color="orange")
        self.g.add_node(4, id=4, nombre="4", pos=[5, 9], color="orange")
        self.g.add_node(5, id=5, nombre="5", pos=[6, 9], color="orange")
        self.g.add_node(6, id=6, nombre="6", pos=[7, 9], color="orange")
        self.g.add_node(7, id=7, nombre="7", pos=[8, 9], color="orange")
        self.g.add_node(8, id=8, nombre="8", pos=[9, 9], color="orange")

        self.g.add_node(9, id=9, nombre="9", pos=[1, 8], color="orange")
        self.g.add_node(10, id=10, nombre="10", pos=[2, 8], color='orange')
        self.g.add_node(11, id=11, nombre="11", pos=[3, 8], color='orange')
        self.g.add_node(12, id=12, nombre="12", pos=[4, 8], color='orange')
        self.g.add_node(13, id=13, nombre="13", pos=[5, 8], color='orange')
        self.g.add_node(14, id=14, nombre="14", pos=[6, 8], color='orange')
        self.g.add_node(15, id=15, nombre="15", pos=[7, 8], color='orange')
        self.g.add_node(16, id=16, nombre="16", pos=[8, 8], color='orange')
        self.g.add_node(17, id=17, nombre="17", pos=[9, 8], color='orange')

        self.g.add_node(18, id=18, nombre="18", pos=[1, 7], color="orange")
        self.g.add_node(19, id=19, nombre="19", pos=[2, 7], color="orange")
        self.g.add_node(20, id=20, nombre="20", pos=[3, 7], color="orange")
        self.g.add_node(21, id=21, nombre="21", pos=[4, 7], color="orange")
        self.g.add_node(22, id=22, nombre="22", pos=[5, 7], color="orange")
        self.g.add_node(23, id=23, nombre="23", pos=[6, 7], color="orange")
        self.g.add_node(24, id=24, nombre="24", pos=[7, 7], color="orange")
        self.g.add_node(25, id=25, nombre="25", pos=[8, 7], color="orange")
        self.g.add_node(26, id=26, nombre="26", pos=[9, 7], color="orange")

        self.g.add_node(27, id=27, nombre="27", pos=[1, 6], color="orange")
        self.g.add_node(28, id=28, nombre="28", pos=[2, 6], color="orange")
        self.g.add_node(29, id=29, nombre="29", pos=[3, 6], color="orange")
        self.g.add_node(30, id=30, nombre="30", pos=[4, 6], color="orange")
        self.g.add_node(31, id=31, nombre="31", pos=[5, 6], color="orange")
        self.g.add_node(32, id=32, nombre="32", pos=[6, 6], color="orange")
        self.g.add_node(33, id=33, nombre="33", pos=[7, 6], color="orange")
        self.g.add_node(34, id=34, nombre="34", pos=[8, 6], color="orange")
        self.g.add_node(35, id=35, nombre="35", pos=[9, 6], color="orange")

        self.g.add_node(36, id=36, nombre="36", pos=[1, 5], color="orange")
        self.g.add_node(37, id=37, nombre="37", pos=[2, 5], color="orange")
        self.g.add_node(38, id=38, nombre="38", pos=[3, 5], color="orange")
        self.g.add_node(39, id=39, nombre="39", pos=[4, 5], color="orange")
        self.g.add_node(40, id=40, nombre="40", pos=[5, 5], color="orange")
        self.g.add_node(41, id=41, nombre="41", pos=[6, 5], color="orange")
        self.g.add_node(42, id=42, nombre="42", pos=[7, 5], color="orange")
        self.g.add_node(43, id=43, nombre="43", pos=[8, 5], color="orange")
        self.g.add_node(44, id=44, nombre="44", pos=[9, 5], color="orange")

        self.g.add_node(45, id=45, nombre="45", pos=[1, 4], color="orange")
        self.g.add_node(46, id=46, nombre="46", pos=[2, 4], color="orange")
        self.g.add_node(47, id=47, nombre="47", pos=[3, 4], color="orange")
        self.g.add_node(48, id=48, nombre="48", pos=[4, 4], color="orange")
        self.g.add_node(49, id=49, nombre="49", pos=[5, 4], color="orange")
        self.g.add_node(50, id=50, nombre="50", pos=[6, 4], color="orange")
        self.g.add_node(51, id=51, nombre="51", pos=[7, 4], color="orange")
        self.g.add_node(52, id=52, nombre="52", pos=[8, 4], color="orange")
        self.g.add_node(53, id=53, nombre="53", pos=[9, 4], color="orange")

        self.g.add_node(54, id=54, nombre="54", pos=[1, 3], color="orange")
        self.g.add_node(55, id=55, nombre="55", pos=[2, 3], color="orange")
        self.g.add_node(56, id=56, nombre="56", pos=[3, 3], color="orange")
        self.g.add_node(57, id=57, nombre="57", pos=[4, 3], color="orange")
        self.g.add_node(58, id=58, nombre="58", pos=[5, 3], color="orange")
        self.g.add_node(59, id=59, nombre="59", pos=[6, 3], color="orange")
        self.g.add_node(60, id=60, nombre="60", pos=[7, 3], color="orange")
        self.g.add_node(61, id=61, nombre="61", pos=[8, 3], color="orange")
        self.g.add_node(62, id=62, nombre="62", pos=[9, 3], color="orange")

        self.g.add_node(63, id=63, nombre="63", pos=[1, 2], color="orange")
        self.g.add_node(64, id=64, nombre="64", pos=[2, 2], color="orange")
        self.g.add_node(65, id=65, nombre="65", pos=[3, 2], color="orange")
        self.g.add_node(66, id=66, nombre="66", pos=[4, 2], color="orange")
        self.g.add_node(67, id=67, nombre="67", pos=[5, 2], color="orange")
        self.g.add_node(68, id=68, nombre="68", pos=[6, 2], color="orange")
        self.g.add_node(69, id=69, nombre="69", pos=[7, 2], color="orange")
        self.g.add_node(70, id=70, nombre="70", pos=[8, 2], color="orange")
        self.g.add_node(71, id=71, nombre="71", pos=[9, 2], color="orange")

        self.g.add_node(72, id=72, nombre="72", pos=[1, 1], color="orange")
        self.g.add_node(73, id=73, nombre="73", pos=[2, 1], color="orange")
        self.g.add_node(74, id=74, nombre="74", pos=[3, 1], color="orange")
        self.g.add_node(75, id=75, nombre="75", pos=[4, 1], color="orange")
        self.g.add_node(76, id=76, nombre="76", pos=[5, 1], color="orange")
        self.g.add_node(77, id=77, nombre="77", pos=[6, 1], color="orange")
        self.g.add_node(78, id=78, nombre="78", pos=[7, 1], color="orange")
        self.g.add_node(79, id=79, nombre="79", pos=[8, 1], color="orange")
        self.g.add_node(80, id=80, nombre="80", pos=[9, 1], color="orange")

        self.g.add_edges_from([(0, 1), (0, 9),
                          (1, 2), (1, 10),
                          (2, 3), (2, 11),
                          (3, 4), (3, 12),
                          (4, 5), (4, 13),
                          (5, 6), (5, 14),
                          (6, 7), (6, 15),
                          (7, 8), (7, 16),
                          (8, 17)
                          ])

        self.g.add_edges_from([
            (9, 10), (9, 18),
            (10, 11), (10, 19),
            (11, 12), (11, 20),
            (12, 13), (12, 21),
            (13, 14), (13, 22),
            (14, 15), (14, 23),
            (15, 16), (15, 24),
            (16, 17), (16, 25),
            (17, 26)
        ])

        self.g.add_edges_from([
            (18, 19), (18, 27),
            (19, 20), (19, 28),
            (20, 21), (20, 29),
            (21, 22), (21, 30),
            (22, 23), (22, 31),
            (23, 24), (23, 32),
            (24, 25), (24, 33),
            (25, 26), (25, 34),
            (26, 35)
        ])

        self.g.add_edges_from([
            (27, 28), (27, 36),
            (28, 29), (28, 37),
            (29, 30), (29, 38),
            (30, 31), (30, 39),
            (31, 32), (31, 40),
            (32, 33), (32, 41),
            (33, 34), (33, 42),
            (34, 35), (34, 43),
            (35, 44)
        ])

        self.g.add_edges_from([
            (36, 37), (36, 45),
            (37, 38), (37, 46),
            (38, 39), (38, 47),
            (39, 40), (39, 48),
            (40, 41), (40, 49),
            (41, 42), (41, 50),
            (42, 43), (42, 51),
            (43, 44), (43, 52),
            (44, 53)
        ])

        self.g.add_edges_from([
            (45, 46), (45, 54),
            (46, 47), (46, 55),
            (47, 48), (47, 56),
            (48, 49), (48, 57),
            (49, 50), (49, 58),
            (50, 51), (50, 59),
            (51, 52), (51, 60),
            (52, 53), (52, 61),
            (53, 62)
        ])

        self.g.add_edges_from([
            (54, 55), (54, 63),
            (55, 56), (55, 64),
            (56, 57), (56, 65),
            (57, 58), (57, 66),
            (58, 59), (58, 67),
            (59, 60), (59, 68),
            (60, 61), (60, 69),
            (61, 62), (61, 70),
            (62, 71)
        ])

        self.g.add_edges_from([
            (63, 64), (63, 72),
            (64, 65), (64, 73),
            (65, 66), (65, 74),
            (66, 67), (66, 75),
            (67, 68), (67, 76),
            (68, 69), (68, 77),
            (69, 70), (69, 78),
            (70, 71), (70, 79),
            (71, 80)
        ])

        self.g.add_edges_from([
            (72, 73),
            (73, 74),
            (74, 75),
            (75, 76),
            (76, 77),
            (77, 78),
            (78, 79),
            (79, 80)
        ])

    def printBoard(self):
        plt.figure(1, figsize=(10, 10))
        pos_nodos = [(x, y) for x, y in nx.get_node_attributes(self.g, 'pos').values()]
        nx.draw_networkx_nodes(self.g, pos_nodos, node_size=1000, node_color="gray")
        nx.draw_networkx_labels(self.g, pos_nodos)
        nx.draw_networkx_edges(self.g, pos_nodos)
        plt.axis('off')
        plt.show()

    def getPossibleMoves(self):
        return None

    def getWinner(self):
        return None

    def lastMove(self):
        return None

    def miniMax(self, isMaxTurn, maximizerMark, board):
        state = None
        if (state is None):
            return None
        elif (state is None):
            return None if self.getWinner() is maximizerMark else -1
        scores = []
        for self.p.move in self.getPossibleMoves():
            self.p.makeMove()
            scores.append(self.miniMax(not isMaxTurn, maximizerMark, board))
            self.lastMove()
        return max(scores) if isMaxTurn else min(scores)

    def makeBestMove(self):
        bestScore = -999
        bestMove = None
        for self.p.move in self.getPossibleMoves():
            self.p.makeMove(self.p.move)
            self.p.score = self.miniMax(False, None, None)
            self.lastMove()
            if (self.p.score > bestScore):
                bestScore = self.p.score
                bestMove = self.p.move
        self.p.makeMove(bestMove)




