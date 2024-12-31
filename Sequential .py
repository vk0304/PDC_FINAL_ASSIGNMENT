import time
import pandas as pd

class Transaction:
    """Class representing a blockchain transaction."""
    def __init__(self, sender, receiver, amount, signature):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.signature = signature

    def is_valid_signature(self):
        """Simulate digital signature validation (ECC/RSA)."""
        time.sleep(0.01)
        return True

class Validator:
    """Class responsible for validating transactions."""
    def __init__(self, transactions):
        self.transactions = transactions

    def validate_transaction(self, transaction):
        """Validate a single transaction."""
        if transaction.is_valid_signature():
            # Simulate additional checks like balance and timestamp
            time.sleep(0.01)
            return True
        return False

    def validate_all_sequential(self):
        """Validate all transactions sequentially."""
        return [self.validate_transaction(tx) for tx in self.transactions]

def load_transactions_from_csv(file_path):
    """Load transactions from a CSV file and return a list of Transaction objects."""
    df = pd.read_csv(file_path)
    transactions = []
    for _, row in df.iterrows():
        transactions.append(
            Transaction(
                sender=row['from_wallet'],
                receiver=row['to_wallet'],
                amount=row['amount'],
                signature=row['signature']
            )
        )
    return transactions

if __name__ == "__main__":
    # Load dataset
    dataset_path = "./dataset.csv"  
    print("Loading transactions from dataset...")
    transactions = load_transactions_from_csv(dataset_path)

    # Sequential validation
    print("Starting sequential validation...")
    validator = Validator(transactions)
    start_time = time.time()
    sequential_results = validator.validate_all_sequential()
    sequential_duration = time.time() - start_time

    print(f"Sequential validation completed in {sequential_duration:.2f} seconds.")
    print(f"Number of transactions validated: {len(sequential_results)}")
