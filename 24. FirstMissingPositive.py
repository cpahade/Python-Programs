class FMP:
    def firstMissingPositive(self, nums):
        nums.sort()
        smallest = 1
        for n in nums:
            if n == smallest:
                smallest += 1

        return smallest


def main():
    nums = [1,2,0]
    obj = FMP()
    print(obj.firstMissingPositive(nums))

main()