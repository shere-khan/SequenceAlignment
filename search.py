class Search:
    @staticmethod
    def search_matrix(M, max):
        locs = list()
        for i, k in enumerate(M):
            for j, l in enumerate(k):
                if l[0] == max:
                    locs.append((i, j))

        return locs
