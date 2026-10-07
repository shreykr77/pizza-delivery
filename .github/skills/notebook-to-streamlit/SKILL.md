---
name: code-to-streamlit
description: Use when adding a Streamlit front end to an existing Python application whose recommendation or computation logic already exists in main.py. Covers reusing existing logic, mapping Python inputs to Streamlit widgets, independent multi-selection optimization, and rerun-safe Streamlit state. Not for creating the core computation from scratch or duplicating the existing logic.
-----------------------------------------------

# Code-to-Streamlit Conversion

## Purpose

Add a Streamlit front end to the existing Rosa's Pizza Delivery application.

The existing recommendation logic is already implemented in `main.py`. Reuse that logic rather than creating a second implementation in `app.py`.

`app.py` should be a thin Streamlit UI layer that collects user inputs, calls the existing logic from `main.py`, and displays the results.

---

## Step 1 — Inspect the existing code

Before making changes:

* Read `main.py` completely.
* Identify the existing recommendation/optimization function.
* Understand its inputs, outputs, and current behavior.
* Identify how it uses the supplied `starter` package.
* Do not replace the existing recommendation methodology.
* Do not create a new recommendation algorithm in `app.py`.

The supplied `starter` package provides:

* `ZONES`
* `TIME_BLOCKS`
* `COSTS`
* `PROMISE`
* `delivery_times`

Do not recreate, hardcode, modify, or replace these values/functions.

---

## Step 2 — Reuse the existing recommendation logic

The optimization logic must remain in `main.py`.

`app.py` must call the existing recommendation function(s) from `main.py`.

Do not duplicate calculations or optimization logic in `app.py`.

If `main.py` needs a small change to expose results to Streamlit, make the smallest reasonable change while preserving its existing behavior.

The recommendation must be calculated independently for every selected zone + time-block combination.

For example:

* 2 selected zones
* 2 selected time blocks

must produce **4 independent recommendations**.

Do not combine orders across zones or time blocks into a single optimization.

---

## Step 3 — Map the existing inputs to Streamlit

Create Streamlit widgets corresponding to the application's existing inputs.

| Existing input                 | Streamlit interface                           |
| ------------------------------ | --------------------------------------------- |
| Zone                           | `st.multiselect` using supplied `ZONES`       |
| Time block                     | `st.multiselect` using supplied `TIME_BLOCKS` |
| Promise start                  | selector from 5 to 85, step 5                 |
| Promise end                    | selector from 10 to 90, step 5                 |
| Profit margin                  | selector from 1 to 15, step 1                 |
| Estimated churn per late order | selector from 1 to 2, step 0.1                |
| Refund cost per late order     | selector from 1 to 15, step 1                 |
| Calculate                      | `st.button`                                   |

Use the values from the supplied `starter` package as defaults where appropriate.

Do not hardcode the starter data itself.

---

## Step 4 — Candidate promise range

The application must generate candidate promises from the selected start and end values using 5-minute increments.

Valid promise values are between 5 and 90 minutes.

For example:

```python
range(promise_start, promise_end + 1, 5)
```

Validate that:

* the start is at least 5
* the end is at most 90
* the start is not greater than the end
* candidate promises use 5-minute increments

The optimization must evaluate every candidate promise in the selected range.

---

## Step 5 — Recommendation calculation

For each selected zone + time-block combination, evaluate every candidate promise.

For each candidate promise:

1. Call:
   `delivery_times(zone, time_block, promise)`
2. Calculate total orders.
3. Count late orders where:
   `delivery_time > promise`
4. Calculate on-time orders.
5. Calculate customer profit using the selected profit margin.
6. Calculate late-order costs using the selected churn and refund
   costs.
7. Calculate net profit.
8. Select the promise with the highest net profit.

The existing calculation methodology in `main.py` is authoritative.
Do not implement a different formula in `app.py`.

---

## Step 6 — Results

After the user clicks the Calculate button, display:

### Recommendation summary

For every selected zone + time-block combination, show:

* Zone
* Time block
* Recommended promised delivery time
* Net profit
* Total orders
* On-time orders
* Late orders

Each combination must be shown independently.

### Detailed results

Also allow the user to review the results for every candidate promise tested.

Within each zone + time-block combination:

* show all tested promises
* show the relevant order/profit metrics
* sort results from highest to lowest net profit

Do not mix detailed results from different zone + time-block combinations into one optimization table.

Use standard Python data structures and Streamlit components for displaying results.

---

## Step 7 — Streamlit state discipline

Streamlit reruns the entire script whenever a widget changes.

The calculation result should not disappear simply because the user interacts with another widget after calculating.

Use `st.session_state` for results that need to persist across reruns.

Recommended behavior:

* Widget changes collect input values.
* Clicking Calculate performs the recommendation calculation.
* Store the calculated results in `st.session_state`.
* Render the stored results outside the button block.
* Do not recalculate unnecessarily on every widget interaction.

For example, the structure should conceptually be:

```python
if st.button("Calculate"):
    st.session_state["results"] = calculate_using_main(...)

if "results" in st.session_state:
    display_results(st.session_state["results"])
```

Do not put all result rendering exclusively inside the `if st.button(...)` block.

---

## Step 8 — Keep app.py thin

`app.py` should primarily contain:

* Streamlit page configuration
* input widgets
* input validation
* calls to functions from `main.py`
* session-state handling
* result presentation

Do not put the recommendation algorithm in `app.py`.

Do not create a second version of `best_promise()` in `app.py`.

Do not hardcode recommendation results.

---

## Step 9 — Dependencies

Use the existing project dependencies and the supplied `starter` package.

Do not add unnecessary dependencies.

Use `uv` for dependency management.

Do not use `pip` or bare `python` commands.

If a new dependency is genuinely required, ask before adding it.

---

## Step 10 — Preserve existing functionality

Do not modify the supplied starter package.

Do not change the underlying recommendation methodology merely to make the Streamlit UI easier to implement.

If `main.py` already works, preserve its existing behavior.

Any changes to `main.py` should be minimal and only made when needed to expose its existing logic cleanly to `app.py`.

---

## Done when

* [ ] `main.py` remains the source of recommendation/optimization logic.
* [ ] `app.py` is a thin Streamlit UI layer.
* [ ] The supplied `starter` package is reused.
* [ ] `ZONES`, `TIME_BLOCKS`, `COSTS`, `PROMISE`, and `delivery_times` are not recreated or modified.
* [ ] Multiple zones can be selected.
* [ ] Multiple time blocks can be selected.
* [ ] Each zone + time-block combination is optimized independently.
* [ ] Promise start/end can be selected from 5 to 90 minutes.
* [ ] Promise candidates use 5-minute increments.
* [ ] Profit margin can be adjusted from 1 to 15.
* [ ] Churn cost can be adjusted from 1 to 2 in 0.1 increments.
* [ ] Refund cost can be adjusted from 1 to 15.
* [ ] A Calculate button triggers the recommendation.
* [ ] Recommended promises are displayed for every selected zone + time-block combination.
* [ ] Detailed results for all tested promises are available.
* [ ] Detailed results are sorted by net profit within each zone + time-block combination.
* [ ] Results persist after Streamlit reruns.
* [ ] The application runs locally with: `uv run streamlit run app.py`
* [ ] The application does not duplicate the recommendation logic.
