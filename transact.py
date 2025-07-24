class Transaction:
    def __init__(self, transction_type, amount):
        self.type= transaction_type
        self.amount=amount
        self.next=None
class TransactionHistory:
    def __init__(self):
        self.head=None
    def add_transaction(self, transaction_Type, amount):
        nn=Transaction(transaction_type,amount)
        if not self.head:
            self.head=nn
        else:
            current= self.head
            while current.next:
                current=current.next
            current.next=nn
        print("f{transaction_type of Rs.{amount} recorded...")
    def show_histry(self):
        if not self.head:
            print("No Transaction found...")
            return
        print("/n Transaction History")
        current=self.head
        count=1
        while current:
            print(f"{count}, {current.type}-Rs{current.amount}")
            current=current.next
            count+=1   
history=TransactionHistory()
while True:
    print("/n------ATM Transaction Menu-----")
    print("1.Deposit")
    print("2.WithDraw")
    print("3.History")
    print("4.Exit")
    choice=input("Enter your choice:")
    if choice=='1':
        amount=float(input("Enter Amount to Deposit:"))
        history.add_transaction("Deposit",amount)
    elif choice=='2':
        amount=float(input("Enter amount to withdraw:"))
        history.add_transaction("Withdraw",amount)
    elif choice=='3':
        history.show_history()
    elif choice=='4':
        print("End of Transaction ... EXit")
        break
    else:
        print("choose 1/2/3/4...only")
