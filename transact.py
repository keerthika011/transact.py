{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "65e81cfe-2d6d-45ea-af0f-fe20ecaaa7a6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "/n------ATM Transaction Menu-----\n",
      "1.Deposit\n",
      "2.WithDraw\n",
      "3.History\n",
      "4.Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice: 1\n",
      "Enter Amount to Deposit: 100\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'transaction_type' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[7], line 40\u001b[0m\n\u001b[0;32m     38\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m choice\u001b[38;5;241m==\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m1\u001b[39m\u001b[38;5;124m'\u001b[39m:\n\u001b[0;32m     39\u001b[0m     amount\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mfloat\u001b[39m(\u001b[38;5;28minput\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mEnter Amount to Deposit:\u001b[39m\u001b[38;5;124m\"\u001b[39m))\n\u001b[1;32m---> 40\u001b[0m     history\u001b[38;5;241m.\u001b[39madd_transaction(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mDeposit\u001b[39m\u001b[38;5;124m\"\u001b[39m,amount)\n\u001b[0;32m     41\u001b[0m \u001b[38;5;28;01melif\u001b[39;00m choice\u001b[38;5;241m==\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m2\u001b[39m\u001b[38;5;124m'\u001b[39m:\n\u001b[0;32m     42\u001b[0m     amount\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mfloat\u001b[39m(\u001b[38;5;28minput\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mEnter amount to withdraw:\u001b[39m\u001b[38;5;124m\"\u001b[39m))\n",
      "Cell \u001b[1;32mIn[7], line 10\u001b[0m, in \u001b[0;36mTransactionHistory.add_transaction\u001b[1;34m(self, transaction_Type, amount)\u001b[0m\n\u001b[0;32m      9\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21madd_transaction\u001b[39m(\u001b[38;5;28mself\u001b[39m, transaction_Type, amount):\n\u001b[1;32m---> 10\u001b[0m     nn\u001b[38;5;241m=\u001b[39mTransaction(transaction_type,amount)\n\u001b[0;32m     11\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhead:\n\u001b[0;32m     12\u001b[0m         \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhead\u001b[38;5;241m=\u001b[39mnn\n",
      "\u001b[1;31mNameError\u001b[0m: name 'transaction_type' is not defined"
     ]
    }
   ],
   "source": [
    "class Transaction:\n",
    "    def __init__(self, transction_type, amount):\n",
    "        self.type= transaction_type\n",
    "        self.amount=amount\n",
    "        self.next=None\n",
    "class TransactionHistory:\n",
    "    def __init__(self):\n",
    "        self.head=None\n",
    "    def add_transaction(self, transaction_Type, amount):\n",
    "        nn=Transaction(transaction_type,amount)\n",
    "        if not self.head:\n",
    "            self.head=nn\n",
    "        else:\n",
    "            current= self.head\n",
    "            while current.next:\n",
    "                current=current.next\n",
    "            current.next=nn\n",
    "        print(\"f{transaction_type of Rs.{amount} recorded...\")\n",
    "    def show_histry(self):\n",
    "        if not self.head:\n",
    "            print(\"No Transaction found...\")\n",
    "            return\n",
    "        print(\"/n Transaction History\")\n",
    "        current=self.head\n",
    "        count=1\n",
    "        while current:\n",
    "            print(f\"{count}, {current.type}-Rs{current.amount}\")\n",
    "            current=current.next\n",
    "            count+=1   \n",
    "history=TransactionHistory()\n",
    "while True:\n",
    "    print(\"/n------ATM Transaction Menu-----\")\n",
    "    print(\"1.Deposit\")\n",
    "    print(\"2.WithDraw\")\n",
    "    print(\"3.History\")\n",
    "    print(\"4.Exit\")\n",
    "    choice=input(\"Enter your choice:\")\n",
    "    if choice=='1':\n",
    "        amount=float(input(\"Enter Amount to Deposit:\"))\n",
    "        history.add_transaction(\"Deposit\",amount)\n",
    "    elif choice=='2':\n",
    "        amount=float(input(\"Enter amount to withdraw:\"))\n",
    "        history.add_transaction(\"Withdraw\",amount)\n",
    "    elif choice=='3':\n",
    "        history.show_history()\n",
    "    elif choice=='4':\n",
    "        print(\"End of Transaction ... EXit\")\n",
    "        break\n",
    "    else:\n",
    "        print(\"choose 1/2/3/4...only\")\n",
    "        \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0f70b27d-29ed-4222-b35d-71f7d268ad51",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
