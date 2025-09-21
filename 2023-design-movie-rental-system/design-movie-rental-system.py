from sortedcontainers import SortedList

class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.price_map = {}          # (shop, movie) -> price
        self.avail = {}              # movie -> SortedList[(price, shop)]
        self.rented = SortedList()   # (price, shop, movie)
        
        for shop, movie, price in entries:
            self.price_map[(shop, movie)] = price
            if movie not in self.avail:
                self.avail[movie] = SortedList()
            self.avail[movie].add((price, shop))
    
    def search(self, movie: int) -> List[int]:
        if movie not in self.avail:
            return []
        # top-5 (price, shop) uthao, shop return karo
        return [shop for (price, shop) in self.avail[movie][:5]]
    
    def rent(self, shop: int, movie: int) -> None:
        p = self.price_map[(shop, movie)]
        self.avail[movie].remove((p, shop))
        self.rented.add((p, shop, movie))
    
    def drop(self, shop: int, movie: int) -> None:
        p = self.price_map[(shop, movie)]
        self.rented.remove((p, shop, movie))
        self.avail[movie].add((p, shop))
    
    def report(self) -> List[List[int]]:
        # top-5 rented movies
        return [[shop, movie] for (p, shop, movie) in self.rented[:5]]