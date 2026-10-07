# Rosa Pizza Delivery Optimization App

## Commands

- `uv add <pkg>` to add dependencies.
- `uv run ...` to run commands.
- Never use `pip` or bare `python`.
- App: `uv run streamlit run app.py`

## Architecture

- `main.py` contains the existing recommendation logic for determining the best promised delivery time.
- `app.py` is the Streamlit UI.
- `app.py` collects all user inputs through Streamlit widgets, calls the recommendation logic from `main.py`, and displays the results.
- Keep `app.py` as a thin UI wrapper.
- Do not duplicate or reimplement the recommendation algorithm in `app.py`.
- Reuse the existing recommendation functions and logic in `main.py`.
- Do not create a second implementation of the recommendation logic.
- The existing behavior in `main.py` must be preserved.

## Multi-Selection Behavior

- The user may select multiple zones and multiple time blocks.
- Each zone + time-block combination must be optimized independently.
- Do NOT combine orders from different zones or time blocks into one optimization.
- For example, selecting 2 zones and 2 time blocks must produce 4 independent recommendations.
- The recommendation logic for this behavior must remain in `main.py`.
- Do not implement separate multi-selection optimization logic in `app.py`.

## Starter Package

Use the supplied `starter` package for:

- `ZONES`
- `TIME_BLOCKS`
- `COSTS`
- `PROMISE`
- `delivery_times`

Do not recreate, hardcode, modify, or replace these values.

Do not create a custom version of `delivery_times()`.

## Streamlit Inputs

### Zones

Multi-select using the supplied `ZONES`.

### Time Blocks

Multi-select using the supplied `TIME_BLOCKS`.

### Promised Delivery Time Range

Allow the user to set:

- Start: 5 to 85 minutes
- End: 10 to 90 minutes
- Interval: 5 minutes

### Profit Margin

Allow the user to set:

- Minimum: 1
- Maximum: 15
- Step: 1

### Estimated Churn

Allow the user to adjust estimated churn per late order:

- Minimum: 1
- Maximum: 2
- Step: 0.1

Use the supplied starter value as the default.

### Refund Cost

Allow the user to set:

- Minimum: 1
- Maximum: 15
- Step: 1

## Recommendation Logic

The existing recommendation logic in `main.py` must be used.

For each selected zone + time-block combination, the logic should evaluate every candidate promised delivery time.

For each promise:

1. Call `delivery_times(zone, time_block, promise)`.
2. Calculate total orders.
3. Count late orders where delivery time > promise.
4. Calculate on-time orders.
5. Calculate profit.
6. Calculate late-order costs.
7. Calculate net profit.
8. Select the promise with the highest net profit.

Do not change the existing recommendation methodology unless required to expose it to the Streamlit application.

## Results

After the user clicks the calculation button:

- Display the recommended promised delivery time for every selected zone + time-block combination.
- Display the corresponding net profit.
- Display on-time orders and late orders.
- Display the detailed results for all tested promises.
- Within each zone + time-block combination, order detailed results from highest to lowest net profit.

## Constraints

- Do not hardcode recommendation results.
- Do not hardcode the supplied starter data.
- Do not modify the starter package.
- Do not duplicate recommendation logic in `app.py`.
- Preserve the existing recommendation behavior in `main.py`.
- Make the smallest reasonable changes needed to expose the existing recommendation logic through Streamlit.
- Reuse existing code rather than duplicating logic.

## Dependencies

- Use `uv` for dependency management.
- Never use `pip` or bare `python`.
- Do not add unnecessary dependencies.
- Ask before adding any dependency that is not already required by the project.