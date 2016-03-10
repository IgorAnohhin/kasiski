__author__ = 'v-iganoh'


class Syt:

    def _devide(self, nums):
        print('divide')
        nums_devided = []
        mn = min(nums)
        nums.remove(mn)
        for n in nums:
            nums_devided.append(n % mn)
        nums_devided.append(mn)
        return nums_devided

    def compute(self, nums):
        print('compute %s' % nums)
        print('filter 0')
        nums = [n for n in nums if n != 0]
        print('result %s' % nums)

        if len(nums) == 1:
            print('syt %s' % nums[0])
            self.syt = nums[0]
        else:
            nums = self._devide(nums)
            print('residue %s' % nums)
            self.compute(nums)

        return self.syt