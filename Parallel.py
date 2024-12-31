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
        time.sleep(0.01)  # Simulating signature verification time
        return True

def validate_transaction_data(row):
    """Validate a single transaction."""
    try:
        transaction = Transaction(
            sender=row['from_wallet'],
            receiver=row['to_wallet'],
            amount=row['amount'],
            signature=row['signature']
        )
        return transaction.is_valid_signature()
    except Exception as e:
        print(f"Error validating transaction: {e}")
        return False

def load_transactions_from_csv(file_path):
    """Load transactions from a CSV file and return a DataFrame."""
    return pd.read_csv(file_path)

def parallel_validation(transactions_df):
    """Validate all transactions sequentially."""
    results = []
    for _, row in transactions_df.iterrows():
        try:
            results.append(validate_transaction_data(row))
        except Exception as e:
            print(f"Error in validation: {e}")
            results.append(False)
    return results

if __name__ == "__main__":
    dataset_path = "./dataset.csv"  
    print("Loading transactions from dataset...")
    transactions_df = load_transactions_from_csv(dataset_path)

    # Parallel validation
    print("Starting parallel validation...")
    start_time = time.time()
    parallel_results = parallel_validation(transactions_df)
    parallel_duration = time.time() - start_time

    print(f"Parallel validation completed in {parallel_duration:.2f} seconds.")
    print(f"Number of transactions validated: {len(parallel_results)}")
    print(f"Valid Transactions: {sum(parallel_results)}")
