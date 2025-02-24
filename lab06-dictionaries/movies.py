from __future__ import annotations

from enum import Enum


class Change(Enum):
    """Represent a change in rank from one list to the next."""
    New, Up, Down, Same = range(4)

    def __str__(self):
        match self:
            case Change.Up:
                return "^"
            case Change.Down:
                return "v"
            case Change.Same:
                return "="
            case Change.New:
                return "+"


class Movie:
    """Represent a movie by title and release year."""
    def __init__(self, title: str, year: int):
        self.title: str = title
        self.year: int = year

    def __hash__(self):
        return hash((self.title, self.year))

    def __eq__(self, other: Movie):
        return self.title == other.title and self.year == other.year

    def __str__(self):
        return f"{self.title} ({self.year})"

    def __repr__(self):
        return f'Movie("{self.title}", {self.year})'


# Ranking are just list of movies
WeeklyRanking = list[Movie]

# Data from boxofficemojo.com

WEEK_11: WeeklyRanking = [
    Movie("Kung Fu Panda 4", 2024),
    Movie("Dune: Part Two", 2024),
    Movie("Imaginary", 2024),
    Movie("Cabrini", 2024),
    Movie("Bob Marley: One Love", 2024),
    Movie("Ordinary Angels", 2024),
    Movie("Migration", 2024),
    Movie("Madame Web", 2024),
    Movie("Yolo", 2024),
    Movie("The Chosen: S4 Episodes 7-8", 2024)
]

WEEK_10: WeeklyRanking = [
    Movie("Dune: Part Two", 2024),
    Movie("Bob Marley: One Love", 2024),
    Movie("Ordinary Angels", 2024),
    Movie("The Chosen: S4 Episodes 7-8", 2024),
    Movie("Madame Web", 2024),
    Movie("Migration", 2024),
    Movie("Demon Slayer: Kimetsu No Yaiba - To the Hashira Training", 2024),
    Movie("Wonka", 2024),
    Movie("Argylle", 2024),
    Movie("The Beekeeper", 2024)
]

WEEK_09: WeeklyRanking = [
    Movie("Bob Marley: One Love", 2024),
    Movie("Demon Slayer: Kimetsu No Yaiba - To the Hashira Training", 2024),
    Movie("Ordinary Angels", 2024),
    Movie("Madame Web", 2024),
    Movie("Argylle", 2024),
    Movie("Migration", 2024),
    Movie("Drive-Away Dolls", 2024),
    Movie("Wonka", 2024),
    Movie("The Chosen: S4 Episodes 4-6", 2024),
    Movie("The Beekeeper", 2024)
]


def changes(last: WeeklyRanking, current: WeeklyRanking) -> dict[Movie, Change]:
    """Calculate per movie the change in weekly ranking."""
    pass


def popular(rankings: list[WeeklyRanking]) -> set[Movie]:  # or list[Movie]
    """Which movies are on all the weekly rankings."""
    pass


if __name__ == "__main__":
    print("Changes from week 9 to week 10:")
    for movie, change in changes(WEEK_09, WEEK_10).items():
        print(f"\t{movie}: {change}")

    print()
    print("Movies on all box office rankings:")
    print(popular([WEEK_09, WEEK_10, WEEK_11]))
