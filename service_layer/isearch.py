from movie_ranking.domain.movie import  Movie


class ISearch:
    def search(self, name) -> [Movie]:
        pass
