import bisect
import itertools
import traceback
from bisect import bisect_left
from cmath import inf
from typing import List

from rest_framework.exceptions import APIException
from rest_framework import generics

from .json import Response
import bisect

class Minimum_difference(generics.ListCreateAPIView):

    def post(self, request):
        try:
            import json as j
            data = j.loads(request.body)
            datas = data['array']
            xrange = range
            nums = datas
            left, right = nums[:len(nums) // 2], nums[len(nums) // 2:]
            total1, total2 = sum(left), sum(right)
            result = float("inf")
            for k in xrange(len(left) + 1):
                sums = sorted(2 * sum(comb) - total1 for comb in itertools.combinations(left, k))
                for comb in itertools.combinations(right, len(left) - k):
                    diff = 2 * sum(comb) - total2
                    i = bisect.bisect_left(sums, -diff)
                    if i < len(sums):
                        result = min(result, abs(sums[i] + diff))
                    if i > 0:
                        result = min(result, abs(sums[i - 1] + diff))
            print(result, 'results')
            return Response(result, True)
        except:
            raise APIException(traceback.print_exc())