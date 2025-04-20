class Hanoi:
    def toh(self, N, from_rod, to_rod, aux_rod):
        if N == 1:
            print(f"move disk {N} from rod {from_rod} to rod {to_rod}")
            return 1

        count = self.toh(N - 1, from_rod, aux_rod, to_rod)

        print(f"move disk {N} from rod {from_rod} to rod {to_rod}")
        count += 1

        count += self.toh(N - 1, aux_rod, to_rod, from_rod)

        return count
