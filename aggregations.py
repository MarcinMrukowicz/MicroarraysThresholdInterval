from abc import ABC, abstractmethod
import numpy as np
from scipy.stats.mstats import gmean


class Aggregation(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def aggregate_numpy_arrays_representation(self, fuzzy_sets):
        """
        :param fuzzy_sets: a numpy array holding fuzzy sets represented directly as numpy arrays
        :return: a fuzzy set, a numpy array result of aggregation
        """
        pass

    def aggregate_interval_valued_fuzzy_sets(self, fuzzy_sets):
        """
        :param fuzzy_sets: a numpy array holding fuzzy sets as IntervalValuedFuzzySet class instances
        :return: a fuzzy set, result of aggregation
        """
        fuzzy_sets_as_numpy = np.array([f.numpy_representation for f in fuzzy_sets])
        return self.aggregate_numpy_arrays_representation(fuzzy_sets_as_numpy)

    @staticmethod
    def change_aggregation_to_name(agg):
        if isinstance(agg, A1Aggregation):
            return 'A1'
        if isinstance(agg, A2Aggregation):
            return 'A2'
        if isinstance(agg, A3Aggregation):
            return 'A3'
        if isinstance(agg, A4Aggregation):
            return 'A4'
        if isinstance(agg, A5Aggregation):
            return 'A5'
        if isinstance(agg, A6Aggregation):
            return 'A6'
        if isinstance(agg, A7Aggregation):
            return 'A7'
        if isinstance(agg, A8Aggregation):
            return 'A8'
        if isinstance(agg, A9Aggregation):
            return 'A9'
        if isinstance(agg, A10Aggregation):
            return 'A10'


# aggregations names comes from paper
class A1Aggregation(Aggregation):
    def __init__(self):
        super().__init__()

    def aggregate_numpy_arrays_representation(self, fuzzy_sets):
        return fuzzy_sets.sum(axis=0) / fuzzy_sets.shape[0]


class GMeanNumericallyImproved(Aggregation):
    def __init__(self, axis=0):
        super().__init__()
        self.axis = axis

    def aggregate_numpy_arrays_representation(self, fuzzy_sets):
        if len(fuzzy_sets.shape) > 1:
            raise RuntimeWarning('The implementation of this aggregation only allows'
                                 'one dimensional array')
        if 0 in fuzzy_sets:
            return 0.0
        if 0.0 in fuzzy_sets:
            return 0.0
        return gmean(fuzzy_sets, axis=self.axis)


class A2Aggregation(Aggregation):
    def __init__(self):
        super().__init__()

    def _f(self, sum, upper, lower, n):
        sum -= upper
        sum += lower
        return sum / n

    def aggregate_numpy_arrays_representation(self, fuzzy_sets):
        summed = fuzzy_sets.sum(axis=0)
        t = np.array([self._f(summed[1], f[1], f[0], fuzzy_sets.shape[0]) for f in fuzzy_sets])
        return np.array([summed[0] / fuzzy_sets.shape[0], np.max(t)])


class A3Aggregation(Aggregation):
    def __init__(self):
        super().__init__()

    def aggregate_numpy_arrays_representation(self, fuzzy_sets):
        summed = fuzzy_sets.sum(axis=0)
        # division by zero, here 0/0 = 0
        if summed[1] == 0:
            return np.array([summed[0] / fuzzy_sets.shape[0], 0])
        # standard way
        squared = np.square(fuzzy_sets[:, 1])
        return np.array([summed[0] / fuzzy_sets.shape[0], np.sum(squared, axis=0) / summed[1]])


class A4Aggregation(Aggregation):
    # parameter p should be integer >= 3
    def __init__(self, p=3):
        super().__init__()
        if p < 3:
            if p == 2:
                raise RuntimeWarning('Setting parameter p equal to 2 coincides to A3')
            raise RuntimeWarning('Parameter p should be integer >= 3')
        if p is float:
            raise RuntimeWarning('Parameter p should be integer')
        self.p = p

    def aggregate_numpy_arrays_representation(self, fuzzy_sets):
        summed = fuzzy_sets.sum(axis=0)
        # division by zero, here 0/0 = 0
        if summed[1] == 0:
            return np.array([summed[0] / fuzzy_sets.shape[0], 0])
        # standard way
        powered = np.power(fuzzy_sets[:, 1], self.p)
        powered_minus_one = np.power(fuzzy_sets[:, 1], self.p - 1)
        #print('powered', powered)
        return np.array([summed[0] / fuzzy_sets.shape[0], np.sum(powered, axis=0) / np.sum(powered_minus_one)])


class A5Aggregation(Aggregation):
    def __init__(self):
        super().__init__()

    def aggregate_numpy_arrays_representation(self, fuzzy_sets):
        lower = np.square(fuzzy_sets[:, 0])
        upper = np.float_power(fuzzy_sets[:, 1], 3)
        n = fuzzy_sets.shape[0]
        return np.array([np.sqrt(lower.sum(axis=0) / n), np.float_power(upper.sum(axis=0) / n, (1 / 3))])


class A6Aggregation(Aggregation):
    def __init__(self):
        super().__init__()

    def aggregate_numpy_arrays_representation(self, fuzzy_sets):
        lower = np.float_power(fuzzy_sets[:, 0], 3)
        upper = np.float_power(fuzzy_sets[:, 1], 4)
        n = fuzzy_sets.shape[0]
        return np.array(
            [np.float_power(lower.sum(axis=0) / n, (1 / 3)), np.float_power(upper.sum(axis=0) / n, (1 / 4))])


class A7Aggregation(Aggregation):
    def __init__(self):
        super().__init__()

    def _f(self, sum, upper, lower, n):
        sum -= lower
        sum += upper
        return sum / n

    def aggregate_numpy_arrays_representation(self, fuzzy_sets):
        summed = fuzzy_sets.sum(axis=0)
        t = np.array([self._f(summed[0], f[1], f[0], fuzzy_sets.shape[0]) for f in fuzzy_sets])
        return np.array([np.min(t), summed[1] / fuzzy_sets.shape[0]])


class A8Aggregation(Aggregation):
    def __init__(self):
        super().__init__()

    def aggregate_numpy_arrays_representation(self, fuzzy_sets):
        n = fuzzy_sets.shape[0]
        lower = GMeanNumericallyImproved(axis=0).aggregate_numpy_arrays_representation(fuzzy_sets[:, 0])
        upper_down = fuzzy_sets[:, 1].sum(axis=0)
        # division by zero, here 0/0 = 0
        if upper_down == 0:
            return np.array([lower, 0])
        upper_up = np.square(fuzzy_sets[:, 1]).sum(axis=0)
        return np.array([lower, upper_up / upper_down])


class A9Aggregation(Aggregation):
    def __init__(self):
        super().__init__()

    def aggregate_numpy_arrays_representation(self, fuzzy_sets):
        lower = np.square(fuzzy_sets[:, 0])
        n = fuzzy_sets.shape[0]
        upper_down = np.power(fuzzy_sets[:, 1], 2).sum(axis=0)
        # division by zero, here 0/0 = 0
        if upper_down == 0:
            return np.array([np.sqrt(lower.sum(axis=0) / n), 0])
        upper_up = np.power(fuzzy_sets[:, 1], 3).sum(axis=0)
        return np.array([np.sqrt(lower.sum(axis=0) / n), upper_up / upper_down])


class A10Aggregation(Aggregation):
    def __init__(self):
        super().__init__()

    def aggregate_numpy_arrays_representation(self, fuzzy_sets):
        lower = np.square(fuzzy_sets[:, 0])
        n = fuzzy_sets.shape[0]
        upper = np.square(fuzzy_sets[:, 1])
        return np.array([np.sqrt(lower.sum(axis=0) / n), np.sqrt(upper.sum(axis=0) / n)])

