import streamlit as st
from starter import COSTS, PROMISE, TIME_BLOCKS, ZONES

from pizza_delivery.main import best_promise


def _keep_promise_handles_apart() -> None:
    start, end = st.session_state["promise_range"]
    previous_start, previous_end = st.session_state["_previous_promise_range"]

    if end - start < 5:
        if start != previous_start:
            start = max(5, end - 5)
        else:
            end = min(90, start + 5)
        st.session_state["promise_range"] = (start, end)

    st.session_state["_previous_promise_range"] = st.session_state["promise_range"]


st.set_page_config(page_title="Rosa's Pizza Delivery")
st.markdown(
    """
    <style>
    .rosa-banner {
        position: relative;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1.5rem;
        overflow: hidden;
        margin: 0.25rem 0 1.5rem;
        padding: 1.7rem 2rem;
        border: 1px solid rgba(255, 226, 190, 0.22);
        border-radius: 1rem;
        color: #fff8ee;
        background:
            radial-gradient(ellipse at 90% 5%, rgba(255, 191, 111, 0.25), transparent 34%),
            linear-gradient(115deg, #681d1c 0%, #a83225 58%, #c34a2b 100%);
        box-shadow: 0 12px 28px rgba(104, 29, 28, 0.16);
    }
    .rosa-brand {
        display: flex;
        align-items: center;
        gap: 1rem;
        min-width: 0;
    }
    .rosa-mark {
        display: grid;
        flex: 0 0 3.6rem;
        width: 3.6rem;
        height: 3.6rem;
        place-items: center;
        border: 1px solid rgba(255, 248, 238, 0.4);
        border-radius: 50%;
        background: rgba(255, 248, 238, 0.12);
        font-size: 1.9rem;
    }
    .rosa-eyebrow {
        margin: 0 0 0.25rem;
        color: #ffd39a;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.15em;
        text-transform: uppercase;
    }
    .rosa-banner h1 {
        margin: 0;
        color: #fff8ee;
        font-size: clamp(1.55rem, 3vw, 2.25rem);
        font-weight: 750;
        letter-spacing: -0.035em;
        line-height: 1.1;
    }
    .rosa-tagline {
        margin: 0.45rem 0 0;
        color: rgba(255, 248, 238, 0.82);
        font-size: 0.95rem;
    }
    .rosa-banner-badge {
        flex: 0 0 auto;
        padding: 0.55rem 0.8rem;
        border: 1px solid rgba(255, 248, 238, 0.35);
        border-radius: 999px;
        color: #fff4e2;
        background: rgba(255, 248, 238, 0.1);
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }
    @media (max-width: 600px) {
        .rosa-banner { padding: 1.25rem; }
        .rosa-mark { flex-basis: 3rem; width: 3rem; height: 3rem; }
        .rosa-banner-badge { display: none; }
    }
    [data-testid="stMetricValue"] > div {
        font-size: clamp(0.8rem, 1.2vw, 1.15rem) !important;
        line-height: 1.2;
        white-space: nowrap;
    }
    [data-testid="stMetricLabel"] p {
        font-size: clamp(0.68rem, 0.85vw, 0.82rem);
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <header class="rosa-banner">
      <div class="rosa-brand">
        <div class="rosa-mark" aria-hidden="true">🍕</div>
        <div>
          <p class="rosa-eyebrow">Fresh from Rosa's kitchen</p>
          <h1>Rosa's Pizza Delivery</h1>
          <p class="rosa-tagline">Hot pizza. Happy customers. Smarter promises.</p>
        </div>
      </div>
      <div class="rosa-banner-badge">Delivery optimizer</div>
    </header>
    """,
    unsafe_allow_html=True,
)

st.header("Inputs")
zone_col, time_col = st.columns(2)

with zone_col:
    selected_zones = st.multiselect("Zones", options=ZONES)

with time_col:
    selected_time_blocks = st.multiselect("Time blocks", options=TIME_BLOCKS)

if "promise_range" not in st.session_state:
    st.session_state["promise_range"] = (max(5, PROMISE - 5), min(90, PROMISE))
if "_previous_promise_range" not in st.session_state:
    st.session_state["_previous_promise_range"] = st.session_state["promise_range"]

promise_start, promise_end = st.slider(
    "Promise range (minutes)",
    min_value=5,
    max_value=90,
    step=5,
    key="promise_range",
    on_change=_keep_promise_handles_apart,
)

margin_col, churn_col, refund_col = st.columns(3)
with margin_col:
    custom_margin = st.checkbox("Custom margin", key="custom_margin_enabled")
    if custom_margin:
        profit_margin = st.number_input(
            "Profit margin per order ($)",
            value=float(COSTS["margin"]),
            step=1.0,
            key="custom_margin",
        )
    else:
        profit_margin = st.slider(
            "Profit margin per order ($)",
            min_value=1,
            max_value=15,
            value=int(COSTS["margin"]),
            step=1,
            key="margin_slider",
        )

with churn_col:
    custom_churn = st.checkbox("Custom churn", key="custom_churn_enabled")
    if custom_churn:
        estimated_churn = st.number_input(
            "Estimated churn per late order",
            value=float(COSTS["churn_orders"]),
            step=0.1,
            format="%.1f",
            key="custom_churn",
        )
    else:
        estimated_churn = st.slider(
            "Estimated churn per late order",
            min_value=1.0,
            max_value=2.0,
            value=float(COSTS["churn_orders"]),
            step=0.1,
            key="churn_slider",
        )

with refund_col:
    custom_refund = st.checkbox("Custom refund", key="custom_refund_enabled")
    if custom_refund:
        refund_cost = st.number_input(
            "Refund cost per late order ($)",
            value=float(COSTS["refund"]),
            step=1.0,
            key="custom_refund",
        )
    else:
        refund_cost = st.slider(
            "Refund cost per late order ($)",
            min_value=1,
            max_value=15,
            value=int(COSTS["refund"]),
            step=1,
            key="refund_slider",
        )

if st.button("Calculate Recommendations", type="primary"):
    validation_errors = []
    if not selected_zones:
        validation_errors.append("Select at least one zone.")
    if not selected_time_blocks:
        validation_errors.append("Select at least one time block.")
    if promise_start > promise_end:
        validation_errors.append("Promise start must not be greater than promise end.")

    if validation_errors:
        for error in validation_errors:
            st.error(error)
    else:
        candidate_promises = range(promise_start, promise_end + 1, 5)
        selected_costs = {
            **COSTS,
            "margin": profit_margin,
            "churn_orders": estimated_churn,
            "refund": refund_cost,
        }
        all_results, best_results = best_promise(
            selected_zones,
            selected_time_blocks,
            candidate_promises,
            selected_costs,
        )
        st.session_state["recommendation_results"] = {
            "all_results": all_results,
            "best_results": best_results,
            "zones": list(selected_zones),
            "time_blocks": list(selected_time_blocks),
            "promise_start": promise_start,
            "promise_end": promise_end,
            "margin": profit_margin,
            "churn_orders": estimated_churn,
            "refund": refund_cost,
        }

results = st.session_state.get("recommendation_results")
if results:
    st.header("Recommendations")
    st.caption(
        f"Calculated for promises {results['promise_start']} to "
        f"{results['promise_end']} minutes, with margin "
        f"${results['margin']}, churn {results['churn_orders']:.1f}, "
        f"and refund ${results['refund']}."
    )

    for recommendation in results["best_results"]:
        st.subheader(
            f"{recommendation['zone']} | {recommendation['time_block']}"
        )
        metric_cols = st.columns(5)
        metric_cols[0].metric(
            "Recommended promise", f"{recommendation['promise_time']} min"
        )
        metric_cols[1].metric("Net profit", f"${recommendation['net_profit']:,.2f}")
        metric_cols[2].metric("Total orders", recommendation["total_orders"])
        metric_cols[3].metric("On-time orders", recommendation["on_time_orders"])
        metric_cols[4].metric("Late orders", recommendation["late_orders"])

        combination_results = [
            result
            for result in results["all_results"]
            if result["zone"] == recommendation["zone"]
            and result["time_block"] == recommendation["time_block"]
        ]
        table_rows = [
            {
                "Promise (min)": result["promise_time"],
                "Total orders": result["total_orders"],
                "On-time orders": result["on_time_orders"],
                "Late orders": result["late_orders"],
                "Profit": f"${result['profit']:,.2f}",
                "Late cost": f"${result['late_cost']:,.2f}",
                "Net profit": f"${result['net_profit']:,.2f}",
            }
            for result in combination_results
        ]
        with st.expander(
            f"Detailed results for {recommendation['zone']} | "
            f"{recommendation['time_block']}"
        ):
            st.table(table_rows)
