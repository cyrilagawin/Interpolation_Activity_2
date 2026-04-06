# Engineering Numerical Methods: Polynomial Interpolation

This repository contains Python solutions for applying numerical interpolation methods to real-world engineering problems. The scripts calculate exact polynomials and generate interactive visualizations for analyzing data across multiple engineering disciplines.

## 🚀 Features

* **Exact Polynomial Generation:** Uses `SymPy` to mathematically solve and construct exact equations for interpolation.
* **Interactive Visualizations:** Uses `Plotly` to render interactive graphs. You can left-click and drag to pan, use your scroll wheel to zoom in/out, and hover over curves to see precise data points.
* **Multiple Interpolation Methods:** * Newton's Divided Differences
    * Lagrange Interpolation
    * Spline Interpolation (Quadratic & Cubic)
* **Comparative Analysis:** Compares exact polynomial extrapolation against linear Least Squares fitting.

## 🛠️ Problems Covered

1.  **Civil Engineering (Bridge Deflection):** Interpolating the vertical deflection of a bridge beam supported at both ends using a quadratic polynomial.
2.  **Electrical Engineering (Signal Processing):** Reconstructing a digital-to-analog converter (DAC) voltage signal over time, including an analysis of Runge's Phenomenon for high-degree polynomials.
3.  **Chemical Engineering (Reaction Rates):** Modeling reactant concentration in a batch reactor over time, finding the roots of the equation, and comparing polynomial extrapolation to linear curve fitting.

## 📦 Prerequisites and Installation

To run the code in this repository, you will need Python installed along with the following libraries:

* `numpy`
* `sympy`
* `plotly`

You can install all required dependencies at once using pip:

```bash
pip install numpy sympy plotly


<img width="1497" height="818" alt="newton" src="https://github.com/user-attachments/assets/efe4d90f-a2d3-4485-8ca2-49517ceda4f5" />

<img width="1486" height="818" alt="lagrange" src="https://github.com/user-attachments/assets/fad8258e-a7f5-4f6a-9b17-0cb29e23755e" />
<img width="1486" height="818" alt="spline" src="https://github.com/user-attachments/assets/98bb5ce6-45e9-4f34-8004-bf8c995fdb63" />

