class FizzBuzz():
    def __init__(self, min_number:int, max_numnber:int):
        self.min_number = min_number
        self.max_numnber = max_numnber
        self.fizz = "Fizz"
        self.buzz = "Buzz"
    def FizzBuzz(self):
        display_str = ""
        temp_str = ""
        for i in range(self.min_number, self.max_numnber):
            temp_str = ""
            print_num = True
            if i % 3 == 0:
                temp_str += f"{self.fizz}"
                print_num = False
            if i % 5 == 0:
                temp_str += f"{self.buzz}"
                print_num = False
            if print_num:
                display_str += f"{i:>8}"
            else:
                display_str += f"{temp_str:>8}"
            if i % 10 == 0:
                display_str += "\n"
            else:
                display_str += ", "
        print(display_str)
if __name__ == "__main__":
    fizz_buzz = FizzBuzz(1, 100)
    fizz_buzz.FizzBuzz()