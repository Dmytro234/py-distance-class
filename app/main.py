class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance | float | int") -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented

    def __iadd__(self, other: "Distance | float | int") -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
        return self

    def __mul__(self, other: float | int) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __truediv__(self, other: float | int) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        return NotImplemented

    def _get_value(self, other: "Distance | float | int") -> float:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return other
        raise TypeError("Unsupported type")

    def __lt__(self, other: "Distance | float | int") -> bool:
        return self.km < self._get_value(other)

    def __gt__(self, other: "Distance | float | int") -> bool:
        return self.km > self._get_value(other)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, (Distance, int, float)):
            return False
        return self.km == (other.km if isinstance(other, Distance) else other)

    def __le__(self, other: "Distance | float | int") -> bool:
        return self.km <= self._get_value(other)

    def __ge__(self, other: "Distance | float | int") -> bool:
        return self.km >= self._get_value(other)
