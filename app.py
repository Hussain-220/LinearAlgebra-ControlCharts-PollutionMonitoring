# 

import dash
from dash import html, dcc
import dash_bootstrap_components as dbc  # For styling and themes

# Initialize the Dash app with a Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO])  # Use a polished theme

# Explanations for each chart
chart_explanations = {
    "svd_pca_visualization.html": """
        The 3D PCA visualization reduces the high-dimensional pollution data into three components for easy interpretation.
        This chart helps identify patterns, clusters, and anomalies in the data by showing distributions in 3D space.
    """,
    "mahalanobis_distances.html": """
        Mahalanobis distance detects outliers by measuring how far a point is from the mean, considering correlations among variables.
        It is a powerful tool for identifying unusual patterns or anomalies in the dataset.
    """,
    "ewma_control_charts.html": """
        EWMA (Exponentially Weighted Moving Average) control charts smooth data over time to highlight subtle trends and detect deviations.
        These charts are commonly used for monitoring gradual process changes.
    """,
    "cusum_control_charts.html": """
        CUSUM (Cumulative Sum) control charts accumulate deviations from the target to detect gradual shifts in process behavior.
        They are highly sensitive to small changes in data trends.
    """,
    "shewhart_control_charts.html": """
        Shewhart control charts monitor individual data points to detect sudden changes or outliers in a process.
        These are ideal for identifying random or assignable variations in the data.
    """
}

# Define the layout of the app
app.layout = dbc.Container(
    [
        # Header
        html.Div([
            html.H1(
                "Pollution Data Monitoring Dashboard",
                style={
                    "textAlign": "center",
                    "marginTop": "20px",
                    "marginBottom": "40px",
                    "color": "#343a40",  # Dark gray
                }
            )
        ]),

        # Dropdown for selecting charts
        html.Div(
            [
                html.Label("Select a Chart to Display", style={"fontWeight": "bold", "fontSize": "18px"}),
                dcc.Dropdown(
                    id="chart-selector",
                    options=[
                        {"label": "3D PCA Visualization", "value": "svd_pca_visualization.html"},
                        {"label": "Mahalanobis Distances", "value": "mahalanobis_distances.html"},
                        {"label": "EWMA Control Charts", "value": "ewma_control_charts.html"},
                        {"label": "CUSUM Control Charts", "value": "cusum_control_charts.html"},
                        {"label": "Shewhart Control Charts", "value": "shewhart_control_charts.html"}
                    ],
                    value="svd_pca_visualization.html",  # Default value
                    placeholder="Select a chart",
                    style={"width": "70%", "margin": "auto", "marginBottom": "30px"},
                ),
            ]
        ),

        # Chart and explanation container
        html.Div(id="chart-container", style={"marginTop": "20px"})
    ],
    fluid=True,  # Make the layout fluid and responsive
)

# Callback to update the chart and explanation based on dropdown selection
@app.callback(
    dash.dependencies.Output("chart-container", "children"),
    [dash.dependencies.Input("chart-selector", "value")]
)
def update_chart(selected_chart):
    explanation = chart_explanations.get(selected_chart, "No explanation available for this chart.")
    
    return dbc.Row(
        [
            # Explanation Card
            dbc.Col(
                dbc.Card(
                    dbc.CardBody([
                        html.H4("Chart Explanation", className="card-title", style={"color": "#007BFF"}),  # Blue title
                        html.P(
                            explanation,
                            style={
                                "textAlign": "justify",
                                "fontSize": "16px",
                                "lineHeight": "1.8",
                                "marginBottom": "10px"
                            },
                            className="card-text"
                        )
                    ]),
                    style={"marginBottom": "20px", "boxShadow": "0px 4px 6px rgba(0, 0, 0, 0.1)"}
                ),
                width=12  # Full-width card
            ),

            # Chart IFrame
            dbc.Col(
                html.Div([
                    html.H4("Chart View", style={"textAlign": "center", "color": "#343a40"}),  # Dark gray title
                    html.Iframe(
                        srcDoc=open(selected_chart, "r").read(),
                        style={
                            "width": "100%",
                            "height": "600px",
                            "border": "2px solid #dee2e6",
                            "borderRadius": "8px",
                            "boxShadow": "0px 4px 6px rgba(0, 0, 0, 0.1)"
                        }
                    )
                ]),
                width=12  # Full-width chart
            )
        ],
        justify="center"  # Center-align everything
    )

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
