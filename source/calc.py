import pygame

class LongInt:
	def __init__(self, base: float, mantissa: int) -> None:
		self.base = base
		self.mantissa = mantissa
		self._rebase()

	def __str__(self) -> str:
		if self.mantissa <= 3:
			return f"{self.base * 10 ** self.mantissa:0.2f}"
		return f"{self.base:0.3f}e{self.mantissa}" 

	def _rebase(self) -> None:
		if self.base == 0:
			self.mantissa = 0
			return None

		while abs(self.base) >= 10:
			self.base /= 10
			self.mantissa += 1

		while abs(self.base) < 1:
			self.base *= 10
			self.mantissa -= 1

		return None

	def _copy(self) -> 'LongInt':
		return LongInt(self.base, self.mantissa)

	# ==================================
	# ADDITION METHODS (add, radd, iadd)
	# ==================================

	def __add__(self, _other) -> "LongInt":
		if isinstance(_other, int | float):
			_other = LongInt(_other, 0)

		if isinstance(_other, LongInt):
			other = _other._copy()

			long_int1 = self._copy()
		
			mantissa_difference = long_int1.mantissa - other.mantissa

			if mantissa_difference >= 7:
				return long_int1

			elif 0 <= mantissa_difference < 7:
				long_int1.base += other.base / (10 ** mantissa_difference)

			elif -6 <= mantissa_difference < 0:
				other.base += long_int1.base * (10 ** mantissa_difference)
				long_int1.base = other.base
				long_int1.mantissa = other.mantissa

			else:
				return other

			long_int1._rebase()
			return long_int1

		return NotImplemented

	def __radd__(self, _other) -> "LongInt":
		if isinstance(_other, int | float):
			other = LongInt(_other, 0)

			return self.__add__(other)

	def __iadd__(self, _other) -> "LongInt":
		if isinstance(_other, LongInt):
			other = _other._copy()

			mantissa_difference = self.mantissa - other.mantissa

			if mantissa_difference >= 7:
				return self

			elif 0 <= mantissa_difference < 7:
				self.base += other.base / (10 ** mantissa_difference)

			elif -6 <= mantissa_difference < 0:
				other.base += self.base * (10 ** mantissa_difference)
				self.base = other.base
				self.mantissa = other.mantissa

			else:
				return other

			self._rebase()
			return self

		return NotImplemented

	# =====================================
	# SUBTRACTION METHODS (sub, rsub, isub)
	# =====================================
	def __sub__(self, _other) -> "LongInt":
		if not isinstance(_other, LongInt):
			return NotImplemented

		other = LongInt(-_other.base, _other.mantissa)
		long_int1 = self._copy()

		return long_int1.__add__(other)

	def __rsub__(self, other) -> "LongInt":
		if not isinstance(_other, LongInt):
			return NotImplemented

		other = LongInt(_other.base, _other.mantissa)
		long_int1 = LongInt(-self.base, self.mantissa)

		return other.__add__(long_int1)

	def __isub__(self, _other) -> "LongInt":
		if not isinstance(_other, LongInt):
			return NotImplemented

		other = LongInt(-_other.base, _other.mantissa)

		return self.__add__(other)

	# ========================================
	# MULTIPLICATION METHODS (mul, rmul, imul)
	# ========================================
	def __mul__(self, other) -> "LongInt":
		if isinstance(other, int | float):
			long_int1 = self._copy()

			long_int1.base *= other

			long_int1._rebase()
			return long_int1

		elif isinstance(other, LongInt):
			long_int1 = self._copy()

			long_int1.base *= other.base
			long_int1.mantissa += other.mantissa

			long_int1._rebase()
			return long_int1

		return NotImplemented

	def __rmul__(self, other) -> "LongInt":
		return self.__mul__(other)

	def __imul__(self, other) -> "LongInt":
		if isinstance(other, int | float):
			self.base *= other
			self._rebase()
			return self

		elif isinstance(other, LongInt):
			self.base *= long_int2.base
			self.mantissa += long_int2.mantissa

			self._rebase()
			return self

		return NotImplemented

	# ==============================================
	# DIVISION METHODS (truediv, rtruediv, itruediv)
	# ==============================================
	def __truediv__(self, other) -> "LongInt":
		if isinstance(other, int | float):
			long_int1 = self._copy()

			long_int1.base /= other

			long_int1._rebase()
			return long_int1

		elif isinstance(other, LongInt):
			long_int1 = self._copy()

			long_int1.base /= other.base
			long_int1.mantissa -= other.mantissa

			long_int1._rebase()
			return long_int1

		return NotImplemented

	def __rtruediv__(self, other) -> "LongInt":
	    if isinstance(other, (int, float)):
	        return LongInt(other, 0) / self

	    return NotImplemented

	def __itruediv__(self, other) -> "LongInt":
		if isinstance(other, int | float):
			self.base /= other

			self._rebase()
			return self

		elif isinstance(other, LongInt):

			self.base /= other.base
			self.mantissa -= other.mantissa

			self._rebase()
			return self

		return NotImplemented

	# ==================================
	# EXPONENTIATION METHODS (pow, ipow)
	# ==================================
	def __pow__(self, other) -> "LongInt":
		if not isinstance(other, int | float):
			return NotImplemented

		long_int1 = self._copy()

		long_int1.base **= other
		long_int1.mantissa *= other

		long_int1._rebase()
		return long_int1

	def __ipow__(self, other) -> "LongInt":
		if not isinstance(other, int | float):
			return NotImplemented

		self.base **= other
		self.mantissa *= other

		self.rebase()
		return self

	# ===========================================
	# COMPARISON METHODS (eq, ne, lt, gt, le, ge)
	# ===========================================
	def __eq__(self, other):
		if not isinstance(other, LongInt):
			return NotImplemented

		return self.base == other.base and self.mantissa == other.mantissa

	def __ne__(self, other):
		if not isinstance(other, LongInt):
			return NotImplemented

		return self.base != other.base or self.mantissa != other.mantissa

	def __gt__(self, other):
		if not isinstance(other, LongInt):
			return NotImplemented

		self_sign = 1 if self.base >= 0 else -1
		other_sign = 1 if other.base >= 0 else -1

		if self_sign != other_sign:
			return self_sign > other_sign

		if self_sign == 1:
			if self.mantissa == other.mantissa:
				return self.base > other.base

			return self.mantissa > other.mantissa
		else:
			if self.mantissa == other.mantissa:
				return self.base < other.base

			return self.mantissa < other.mantissa

	def __lt__(self, other):
		if not isinstance(other, LongInt):
			return NotImplemented

		self_sign = 1 if self.base >= 0 else -1
		other_sign = 1 if other.base >= 0 else -1

		if self_sign != other_sign:
			return self_sign < other_sign

		if self_sign == 1:
			if self.mantissa == other.mantissa:
				return self.base < other.base

			return self.mantissa < other.mantissa
		else:
			if self.mantissa == other.mantissa:
				return self.base > other.base

			return self.mantissa < other.mantissa

	def __ge__(self, other):
		if not isinstance(other, LongInt):
			return NotImplemented

		if self.base == other.base and self.mantissa == other.mantissa:
			return True

		return self.__gt__(other)

	def __le__(self, other):
		if not isinstance(other, LongInt):
			return NotImplemented

		if self.base == other.base and self.mantissa == other.mantissa:
			return True

		return self.__lt__(other)

class UpgradeableParameter:
	def __init__(self, initial_value, value_function,
					   initial_cost, cost_function,
					   initial_multiplier, multiplier_function) -> None:
		self.value = initial_value
		self.cost = initial_cost
		self.multiplier = initial_multiplier
		self.value_function = value_function
		self.cost_function = cost_function
		self.multiplier_function = multiplier_function


	def purchase(self, currency) -> None:
		self.value = self.value_function(self.value)
		self.cost = self.cost_function(self.cost)
		self.multiplier = self.multiplier_function(self.multiplier)

def main():
	long_1 = LongInt(5.5, 300)
	long_2 = LongInt(3.3, 678)
	long_3 = LongInt(200, 3)
	long_4 = LongInt(1230, 58987)
	i = LongInt(0, 0)
	c = LongInt(5, 0)
	m = LongInt(1, 0)
	var = UpgradeableParameter(i, lambda i: i + 1, c, lambda i: i * 2, m, lambda i: i)

	x = LongInt(5, 0)
	print(var.value, var.cost, var.multiplier)
	if x >= var.cost:
		var.purchase(x)
		print(var.value, var.cost, var.multiplier)


	print(long_1 + long_2 + long_3 + long_4)
	print(long_1 * long_2 * long_3 * long_4)
	print(long_4 / (long_1 * long_2 * long_3))
	print(long_4 - long_3 - long_2 - long_1)
	print(long_4 == long_1)
	print(long_4 != long_1)
	print(long_4 > long_1)
	print(long_4 < long_1)

if __name__ == '__main__':
	main()
