"""
Becker's Barley Trellis Plot
----------------------------
The example demonstrates the trellis charts created by Richard Becker, William Cleveland and others in the 1990s. Using the visualization technique below they identified an anomoly in a widely used agriculatural dataset, which they termed ["The Morris Mistake."](https://www.albany.edu/acc/courses/acc522fall2007/lecturenotes/trellis.usermanual.pdf). It became their favored way of showcasing the power of this pioneering plot.
"""
# category: case studies
import altair as alt
from vega_datasets import data

source = data.barley()

alt.Chart(source, title="The Morris Mistake").mark_point().encode(
    alt.X(
        'yield:Q',
        scale=alt.Scale(zero=False),
        axis=alt.Axis(grid=False, title="Barley Yield (bushels/acre)")
    ),
    alt.Y(
        'variety:N',
        sort=alt.EncodingSortField(field='yield:Q', op='sum', order='descending'),
        scale=alt.Scale(rangeStep=20),
        axis=alt.Axis(title="", grid=True)
    ),
    color=alt.Color('year:N', legend=alt.Legend(title="Year")),
    row=alt.Row(
        'site:N',
        title="",
        sort=alt.EncodingSortField(field='yield:Q', op='sum', order='descending'),
    )
).configure_view(stroke="transparent")