# Rosa's Pizza Delivery Optimizer

Explore the live app: [Rosa's Pizza Delivery Optimizer](https://pizza-delivery-n8azg2abjcl2ejo9hphhqr.streamlit.app/)

View the original notebook: [Rosa's Pizza Delivery Optimization on Google Colab](https://colab.research.google.com/drive/1czSOgRJfbrdW-l3ZdaaXMXT8U_oSEIzp?usp=sharing)

## About

Rosa's Pizza Delivery Optimizer is an interactive Streamlit app for exploring delivery-time promises and their impact on order volume and profit. Choose one or more delivery zones and time blocks, then compare promise times independently for every selected zone/time-block combination.

The app uses the project's existing recommendation logic and the supplied Rosa's delivery simulator. For each candidate promise, it estimates on-time and late orders, order profit, late-order costs, and net profit, then highlights the most profitable promise for each combination.

## Using the app

1. Select one or more zones and time blocks.
2. Choose a promise range from 5 to 90 minutes. Both endpoints move in 5-minute increments, and must remain at least 5 minutes apart.
3. Set profit margin per order, estimated churn per late order, and refund cost per late order. Use the custom input option to enter values outside the standard slider ranges.
4. Select **Calculate Recommendations**.
5. Review the recommended promise and key order/profit metrics. Expand a combination's details to compare every tested promise, sorted by net profit.

Each zone and time-block combination is optimized separately; orders from different combinations are not combined.

## Run locally

Install [uv](https://docs.astral.sh/uv/) if needed, then run from the project directory:

```powershell
uv sync
uv run streamlit run app.py
```