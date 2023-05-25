{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n",
      "1\n",
      "429981696\n"
     ]
    }
   ],
   "source": [
    "class Calculator:\n",
    "    '''\n",
    "    Do addition, subtraction, multiplication, divison,The exponent of a number, return reminder & floor division \n",
    "    '''\n",
    "    def addition(self, a, b):\n",
    "        return a + b\n",
    "    def subtraction(self, a, b):\n",
    "        return a - b\n",
    "    def multiplication(self, a, b):\n",
    "        return a * b\n",
    "    def division(self, a, b):\n",
    "        try:\n",
    "            return a / b\n",
    "        except ZeroDivisonError:\n",
    "            return 'It is impossible.'\n",
    "    def exponent(self, a, b):\n",
    "        return a ** b\n",
    "    def reminder(self, a, b):\n",
    "        return a % b\n",
    "    def floordivision(self, a, b):\n",
    "        return a // b\n",
    "\n",
    "my_calculator = Calculator()\n",
    "\n",
    "temp = my_calculator.addition(12,8)\n",
    "print(temp)\n",
    "temp = my_calculator.floordivision(12,8)\n",
    "print(temp)\n",
    "temp = my_calculator.exponent(12,8)\n",
    "print(temp)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
