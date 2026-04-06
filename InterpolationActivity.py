#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sympy as sp
import numpy as np
import plotly.graph_objects as go

print("--- NEWTON'S DIVIDED DIFFERENCES METHOD ---")

# Data
t_data = [0, 5, 10]
C_data = [1.00, 0.60, 0.35]
t = sp.Symbol('t')

# TASK 1: Construct the polynomial
def newton_polynomial(x_vals, y_vals, var):
    n = len(x_vals)
    coef = np.zeros([n, n])
    coef[:,0] = y_vals
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x_vals[i+j] - x_vals[i])

    poly = coef[0, 0]
    for i in range(1, n):
        term = coef[0, i]
        for j in range(i):
            term *= (var - x_vals[j])
        poly += term
    return sp.expand(poly)

newton_expr = newton_polynomial(t_data, C_data, t)
print("\nTask 1: The exact Newton polynomial C(t) is:")
sp.pprint(newton_expr)

# TASK 2: Solve for t when C(t) = 0.50
roots = sp.solve(newton_expr - 0.50, t)
# Filter for the realistic positive root within our reaction timeframe
t_target = [float(r) for r in roots if r.is_real and float(r) > 0][0]
print(f"\nTask 2: The concentration reaches 0.50 mol/L at t = {t_target:.3f} min")

# TASK 3: Compare at t = 20 (Linear vs Exact)
m, b = np.polyfit(t_data, C_data, 1)
linear_pred = m * 20 + b
exact_pred = float(newton_expr.subs(t, 20))
print(f"\nTask 3: Prediction at t = 20 min:")
print(f"        Exact Interpolation = {exact_pred:.3f} mol/L")
print(f"        Linear Least Squares = {linear_pred:.3f} mol/L")

# --- Interactive Visualization with Plotly ---
eval_newton = sp.lambdify(t, newton_expr, 'numpy')
t_plot = np.linspace(0, 22, 100)
C_plot = eval_newton(t_plot)
linear_plot = m * t_plot + b

fig = go.Figure()
fig.add_trace(go.Scatter(x=t_plot, y=C_plot, mode='lines', name='Newton Polynomial C(t)', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=t_plot, y=linear_plot, mode='lines', name='Linear Fit (Least Squares)', line=dict(color='gray', dash='dash')))
fig.add_trace(go.Scatter(x=t_data, y=C_data, mode='markers', name='Reactor Data', marker=dict(color='red', size=10)))
fig.add_trace(go.Scatter(x=[t_target], y=[0.50], mode='markers', name=f'C = 0.50 (t={t_target:.2f})', marker=dict(color='green', symbol='x', size=12)))
fig.add_trace(go.Scatter(x=[20], y=[exact_pred], mode='markers', name='Newton Extrapolation (t=20)', marker=dict(color='blue', symbol='star', size=12)))

fig.update_layout(
    title='Reaction Rate (Newton Method vs Linear Fit)',
    xaxis_title='Time, t (min)',
    yaxis_title='Concentration, [A] (mol/L)',
    template='plotly_white',
    dragmode='pan' 
)
fig.show(config={'scrollZoom': True})


# In[2]:


import sympy as sp
import numpy as np
import plotly.graph_objects as go

print("--- LAGRANGE INTERPOLATION METHOD ---")

# Data
t_data = [0, 5, 10]
C_data = [1.00, 0.60, 0.35]
t = sp.Symbol('t')

# TASK 1: Construct the polynomial
def lagrange_polynomial(x_vals, y_vals, var):
    poly = 0
    n = len(x_vals)
    for i in range(n):
        term = y_vals[i]
        for j in range(n):
            if i != j:
                term *= (var - x_vals[j]) / (x_vals[i] - x_vals[j])
        poly += term
    return sp.expand(poly)

lagrange_expr = lagrange_polynomial(t_data, C_data, t)
print("\nTask 1: The exact Lagrange polynomial C(t) is:")
sp.pprint(lagrange_expr)

# TASK 2: Solve for t when C(t) = 0.50
roots = sp.solve(lagrange_expr - 0.50, t)
t_target = [float(r) for r in roots if r.is_real and float(r) > 0][0]
print(f"\nTask 2: The concentration reaches 0.50 mol/L at t = {t_target:.3f} min")

# TASK 3: Compare at t = 20 (Linear vs Exact)
m, b = np.polyfit(t_data, C_data, 1)
linear_pred = m * 20 + b
exact_pred = float(lagrange_expr.subs(t, 20))
print(f"\nTask 3: Prediction at t = 20 min:")
print(f"        Exact Interpolation = {exact_pred:.3f} mol/L")
print(f"        Linear Least Squares = {linear_pred:.3f} mol/L")

# --- Interactive Visualization with Plotly ---
eval_lagrange = sp.lambdify(t, lagrange_expr, 'numpy')
t_plot = np.linspace(0, 22, 100)
C_plot = eval_lagrange(t_plot)
linear_plot = m * t_plot + b

fig = go.Figure()
fig.add_trace(go.Scatter(x=t_plot, y=C_plot, mode='lines', name='Lagrange Polynomial C(t)', line=dict(color='purple')))
fig.add_trace(go.Scatter(x=t_plot, y=linear_plot, mode='lines', name='Linear Fit (Least Squares)', line=dict(color='gray', dash='dash')))
fig.add_trace(go.Scatter(x=t_data, y=C_data, mode='markers', name='Reactor Data', marker=dict(color='red', size=10)))
fig.add_trace(go.Scatter(x=[t_target], y=[0.50], mode='markers', name=f'C = 0.50 (t={t_target:.2f})', marker=dict(color='green', symbol='x', size=12)))
fig.add_trace(go.Scatter(x=[20], y=[exact_pred], mode='markers', name='Lagrange Extrapolation (t=20)', marker=dict(color='purple', symbol='star', size=12)))

fig.update_layout(
    title='Reaction Rate (Lagrange Method vs Linear Fit)',
    xaxis_title='Time, t (min)',
    yaxis_title='Concentration, [A] (mol/L)',
    template='plotly_white',
    dragmode='pan' 
)
fig.show(config={'scrollZoom': True})


# In[3]:


import sympy as sp
import numpy as np
import plotly.graph_objects as go

print("--- SPLINE INTERPOLATION METHOD (QUADRATIC) ---")

# Data
t_data = [0, 5, 10]
C_data = [1.00, 0.60, 0.35]
t = sp.Symbol('t')

# TASK 1: Construct the polynomial (Piecewise Spline)
spline_expr = sp.interpolating_spline(2, t, t_data, C_data)
print("\nTask 1: The exact Quadratic Spline Piecewise function C(t) is:")
sp.pprint(spline_expr)

# TASK 2: Solve for t when C(t) = 0.50
# Since Splines are piecewise, we solve numerically or evaluate the specific domain
# Concentration 0.50 falls between t=5 (C=0.6) and t=10 (C=0.35). 
# We pull the correct piece of the piecewise function for evaluation:
piecewise_funcs = spline_expr.args
for expr, condition in piecewise_funcs:
    if condition.subs(t, 7): # Check the domain that contains 5 < t < 10
        roots = sp.solve(expr - 0.50, t)
        t_target = [float(r) for r in roots if r.is_real and float(r) > 0][0]
        break
print(f"\nTask 2: The concentration reaches 0.50 mol/L at t = {t_target:.3f} min")

# TASK 3: Compare at t = 20 (Linear vs Exact)
m, b = np.polyfit(t_data, C_data, 1)
linear_pred = m * 20 + b
exact_pred = float(spline_expr.subs(t, 20))
print(f"\nTask 3: Prediction at t = 20 min:")
print(f"        Spline Extrapolation = {exact_pred:.3f} mol/L")
print(f"        Linear Least Squares = {linear_pred:.3f} mol/L")

# --- Interactive Visualization with Plotly ---
eval_spline = sp.lambdify(t, spline_expr, 'numpy')
t_plot = np.linspace(0, 22, 100)
C_plot = eval_spline(t_plot)
linear_plot = m * t_plot + b

fig = go.Figure()
fig.add_trace(go.Scatter(x=t_plot, y=C_plot, mode='lines', name='Quadratic Spline C(t)', line=dict(color='darkorange')))
fig.add_trace(go.Scatter(x=t_plot, y=linear_plot, mode='lines', name='Linear Fit (Least Squares)', line=dict(color='gray', dash='dash')))
fig.add_trace(go.Scatter(x=t_data, y=C_data, mode='markers', name='Reactor Data', marker=dict(color='red', size=10)))
fig.add_trace(go.Scatter(x=[t_target], y=[0.50], mode='markers', name=f'C = 0.50 (t={t_target:.2f})', marker=dict(color='green', symbol='x', size=12)))
fig.add_trace(go.Scatter(x=[20], y=[exact_pred], mode='markers', name='Spline Extrapolation (t=20)', marker=dict(color='darkorange', symbol='star', size=12)))

fig.update_layout(
    title='Reaction Rate (Spline Method vs Linear Fit)',
    xaxis_title='Time, t (min)',
    yaxis_title='Concentration, [A] (mol/L)',
    template='plotly_white',
    dragmode='pan' 
)
fig.show(config={'scrollZoom': True})


# In[ ]:




