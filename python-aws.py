import boto3
import requests

# --- Config ---
AWS_REGION = "us-east-1"   # Budgets API is global, but region must be specified
ACCOUNT_ID = "942632789264"   # Replace with your AWS Account ID
BUDGET_NAME = "Monthly-AWS-Cost-Alert-INR"
ALERT_EMAIL = "sthontla.mail@gmail.com"           # Replace with your notification email
BUDGET_LIMIT_INR = 10             # Example: ₹500 monthly threshold

# --- Step 1: Convert INR to USD (AWS bills in USD) ---
def convert_inr_to_usd(amount_in_inr):
    try:
        response = requests.get("https://api.exchangerate.host/latest?base=USD&symbols=INR").json()
        usd_to_inr = response["rates"]["INR"]
        usd_amount = round(amount_in_inr / usd_to_inr, 2)
        print(f"Conversion Rate: 1 USD = {usd_to_inr:.2f} INR")
        print(f"Budget Limit: ₹{amount_in_inr} ≈ ${usd_amount} USD")
        return usd_amount
    except Exception as e:
        print("Currency conversion failed:", e)
        return amount_in_inr  # fallback

# --- Step 2: Create AWS Budget ---
def create_budget():
    client = boto3.client("budgets", region_name=AWS_REGION)

    budget_limit_usd = convert_inr_to_usd(BUDGET_LIMIT_INR)

    response = client.create_budget(
        AccountId=ACCOUNT_ID,
        Budget={
            "BudgetName": BUDGET_NAME,
            "BudgetLimit": {"Amount": str(budget_limit_usd), "Unit": "USD"},
            "TimeUnit": "MONTHLY",
            "BudgetType": "COST",
            "CostFilters": {},  # Empty = all AWS services/resources
            "TimePeriod": {
                "Start": "2026-01-01T00:00:00Z",
                "End": "2080-01-01T00:00:00Z"
            }
        },
        NotificationsWithSubscribers=[
            {
                "Notification": {
                    "NotificationType": "ACTUAL",
                    "ComparisonOperator": "GREATER_THAN",
                    "Threshold": 80.0,  # Trigger at 80% of budget
                    "ThresholdType": "PERCENTAGE"
                },
                "Subscribers": [{"SubscriptionType": "EMAIL", "Address": ALERT_EMAIL}]
            }
        ]
    )
    print("Budget created successfully:", response)

# --- Run ---
if __name__ == "__main__":
    create_budget()