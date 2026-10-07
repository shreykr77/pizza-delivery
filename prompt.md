Read and follow these files before making any changes:

1. `CLAUDE.md`
2. `.github/skills/notebook-to-streamlit/SKILL.md`
3. `main.py`
4. The supplied `starter` package

Your task is to create `app.py` for the Rosa's Pizza Delivery optimization assignment.

## Core requirement

`main.py` already contains the recommendation/optimization logic.

Use the existing logic from `main.py`. Do NOT create a second recommendation algorithm in `app.py`.

`app.py` must be a thin Streamlit UI layer that:

1. Collects inputs from the user.
2. Passes those inputs to the existing logic in `main.py`.
3. Displays the recommendations and detailed results.

## Important constraints

* Do NOT use Pandas.
* Do NOT modify the supplied `starter` package.
* Do NOT recreate or hardcode:

  * `ZONES`
  * `TIME_BLOCKS`
  * `COSTS`
  * `PROMISE`
  * `delivery_times`
* Import and reuse the supplied values/functions.
* Do not hardcode recommendation results.
* Do not duplicate the optimization logic from `main.py`.
* Preserve the existing recommendation methodology.
* Make the smallest reasonable change to `main.py` only if necessary to expose its existing results cleanly to `app.py`.
* Use `uv` for running/testing. Do not use `pip` or bare `python`.

## Streamlit UI

Create a clear and simple Streamlit interface.

### Zone selection

Use a multi-select widget populated from the supplied `ZONES`.

The user must be able to select multiple zones.

### Time-block selection

Use a multi-select widget populated from the supplied `TIME_BLOCKS`.

The user must be able to select multiple time blocks.

### Promise range

Provide:

* Promise start: 5–85 minutes
* Promise end: 10–90 minutes
* Step: 5 minutes

The candidate promises passed to the recommendation logic should be:

`range(promise_start, promise_end + 1, 5)`

Validate that the start is not greater than the end.

### Profit margin

Provide a selector from:

* Minimum: 1
* Maximum: 15
* Step: 1

### Estimated churn

Provide a selector from:

* Minimum: 1
* Maximum: 2
* Step: 0.1

Use the supplied starter value as the default where appropriate.

### Refund cost

Provide a selector from:

* Minimum: 1
* Maximum: 15
* Step: 1

### Calculate button

Include a clear button such as:

`Calculate Recommendations`

The recommendation calculation should happen when this button is
clicked.

## Multi-selection behavior

This is important.

Every zone + time-block combination must be optimized independently.

For example, if the user selects:

Zones:

* Central
* Far West

Time blocks:

* Lunch
* Fri/Sat eve

the app must produce four independent recommendations:

* Central + Lunch
* Central + Fri/Sat eve
* Far West + Lunch
* Far West + Fri/Sat eve

Do NOT combine all selected orders into one optimization.

This behavior must come from the existing logic in `main.py`, not from
a duplicate implementation in `app.py`.

## Results

After calculation, display a recommendation summary for every
selected zone + time-block combination.

For each combination show:

* Zone
* Time block
* Recommended promise
* Net profit
* Total orders
* On-time orders
* Late orders

Also provide the detailed results for every candidate promise that
was tested.

Within each zone + time-block combination, detailed results must be
sorted from highest to lowest net profit.

Do not mix the optimization results of different combinations.

Do not use Pandas to display the results. Use normal Python data
structures and Streamlit components.

## Streamlit state

Follow the state-management instructions in
`.github/skills/notebook-to-streamlit/SKILL.md`.

In particular:

* Store calculated results in `st.session_state`.
* Do not make results disappear when another widget causes a rerun.
* Render stored results outside the Calculate button block.
* Do not unnecessarily recalculate on every widget interaction.

## Validation

Handle sensible invalid input cases, including:

* No zone selected.
* No time block selected.
* Promise start greater than promise end.

Show a clear Streamlit message instead of failing with an exception.

## Visual structure

Keep the UI simple and professional.

Suggested structure:

* Page title
* Short description
* Input section
* Calculate button
* Recommendation summary
* Detailed results by zone + time block

Do not add unnecessary charts, dependencies, or features.

## Testing

After creating `app.py`:

1. Check that imports work.
2. Run the app using:

`uv run streamlit run app.py`

3. Verify that the app can:

   * select multiple zones
   * select multiple time blocks
   * change promise range
   * change margin
   * change churn
   * change refund cost
   * calculate recommendations
   * display independent recommendations for every zone/time-block combination
   * display detailed results
4. Verify that changing another widget after calculation does not
   unexpectedly erase the displayed results.

Do not rewrite `main.py` unnecessarily. If you discover that a small
change is required to expose the existing results to Streamlit,
explain that change and keep it minimal.

At the end, tell me:

* which files you created or modified
* what you changed
* how to run the app locally
* whether `main.py` required any changes
* any issues that still need my attention
