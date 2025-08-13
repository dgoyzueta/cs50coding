class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Object jar cannot be initialized with a negative number")
        self.capacity = capacity
        self.balance = 0

    def __str__(self):
        return "🍪" * self.balance

    def deposit(self, n):
        c = self.balance
        c = c + n
        if c > self.capacity:
            raise ValueError("Deposit of cookies exceeds the capacity jar")
        self.balance = self.balance + n

    def withdraw(self, n):
        c = self.balance
        c = c - n
        if c < 0:
            raise ValueError("There are not enough cookies to take from the jar")
        self.balance = self.balance - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self.balance


def main():
    jar = Jar(20)

    print("Capacity is", jar.capacity)

    deposit = input("Enter deposit: ").strip()
    jar.deposit(int(deposit))
    print("Balance", jar)

    withdraw = input("Enter withdrawal: ").strip()
    jar.withdraw(int(withdraw))
    print("Balance", jar)

    print("Size (balance) is", jar.size)

if __name__ == "__main__":
    main()
