from ._px import make_figure
import plotly.graph_objs as go

default_max_size = 20
default_symbol_seq = ["circle", "diamond", "square", "x", "cross"]
default_dash_seq = ["solid", "dot", "dash", "longdash", "dashdot", "longdashdot"]


def scatter(
    df,
    x=None,
    y=None,
    color=None,
    symbol=None,
    size=None,
    hover=None,
    text=None,
    color_map={},
    symbol_map={},
    color_sequence=None,
    symbol_sequence=default_symbol_seq,
    row=None,
    col=None,
    log_x=False,
    log_y=False,
    marginal_x=None,
    marginal_y=None,
    error_x=None,
    error_x_minus=None,
    error_y=None,
    error_y_minus=None,
    max_size=default_max_size,
    orders={},
):
    """Fetches rows from a Bigtable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by big_table.  Silly things may happen if
    other_silly_variable is not None.

    Args:
        big_table: An open Bigtable Table instance.
        keys: A sequence of strings representing the key of each table row
            to fetch.
        other_silly_variable: Another optional variable, that has a much
            longer name than the other args, and which does nothing.

    Returns:
        A dict mapping keys to the corresponding table row data
        fetched. Each row is represented as a tuple of strings. For
        example:

        {'Serak': ('Rigel VII', 'Preparer'),
         'Zim': ('Irk', 'Invader'),
         'Lrrr': ('Omicron Persei 8', 'Emperor')}

        If a key from the keys argument is missing from the dictionary,
        then that row was not found in the table.

    Raises:
        IOError: An error occurred accessing the bigtable.Table object.
    """
    return make_figure(
        args=locals(),
        constructor=go.Scatter,
        trace_patch=dict(mode="markers" + ("+text" if text else "")),
        grouped_mappings=["col", "row", "marker.color", "marker.symbol"],
        layout_patch=dict(barmode="overlay", violinmode="overlay"),  # for marginals
    )


def density_contour(
    df,
    x=None,
    y=None,
    color=None,
    color_map={},
    color_sequence=None,
    row=None,
    col=None,
    log_x=False,
    log_y=False,
    marginal_x=None,
    marginal_y=None,
    orders={},
):
    return make_figure(
        args=locals(),
        constructor=go.Histogram2dContour,
        trace_patch=dict(contours=dict(coloring="none")),
        grouped_mappings=["col", "row", "line.color"],
        layout_patch=dict(barmode="overlay", violinmode="overlay"),  # for marginals
    )


def line(
    df,
    x=None,
    y=None,
    split=None,
    color=None,
    dash=None,
    hover=None,
    text=None,
    color_map={},
    dash_map={},
    color_sequence=None,
    dash_sequence=default_dash_seq,
    row=None,
    col=None,
    log_x=False,
    log_y=False,
    error_x=None,
    error_x_minus=None,
    error_y=None,
    error_y_minus=None,
    orders={},
):
    return make_figure(
        args=locals(),
        constructor=go.Scatter,
        trace_patch=dict(mode="lines" + ("+markers+text" if text else "")),
        grouped_mappings=["col", "row", "line.color", "line.dash", "split"],
    )


def bar(
    df,
    x=None,
    y=None,
    color=None,
    color_map={},
    color_sequence=None,
    row=None,
    col=None,
    hover=None,
    text=None,
    orientation="v",
    normalization="",
    mode="group",
    log_x=False,
    log_y=False,
    error_x=None,
    error_x_minus=None,
    error_y=None,
    error_y_minus=None,
    orders={},
):
    return make_figure(
        args=locals(),
        constructor=go.Bar,
        trace_patch=dict(orientation=orientation, textposition="auto"),
        grouped_mappings=["col", "row", "marker.color"],
        layout_patch=dict(barnorm=normalization, barmode=mode),
    )


def histogram(
    df,
    x=None,
    y=None,
    color=None,
    color_map={},
    color_sequence=None,
    row=None,
    col=None,
    orientation="v",
    mode="stack",
    normalization=None,
    log_x=False,
    log_y=False,
    orders={},
):
    return make_figure(
        args=locals(),
        constructor=go.Histogram,
        trace_patch=dict(orientation=orientation, histnorm=normalization),
        grouped_mappings=["col", "row", "marker.color"],
        layout_patch=dict(barmode=mode),
    )


def violin(
    df,
    x=None,
    y=None,
    color=None,
    color_map={},
    color_sequence=None,
    orientation="v",
    mode="group",
    row=None,
    col=None,
    log_x=False,
    log_y=False,
    orders={},
):
    return make_figure(
        args=locals(),
        constructor=go.Violin,
        trace_patch=dict(orientation=orientation),
        grouped_mappings=["col", "row", "marker.color"],
        layout_patch=dict(violinmode=mode),
    )


def box(
    df,
    x=None,
    y=None,
    color=None,
    color_map={},
    color_sequence=None,
    orientation="v",
    mode="group",
    row=None,
    col=None,
    log_x=False,
    log_y=False,
    orders={},
):
    return make_figure(
        args=locals(),
        constructor=go.Box,
        trace_patch=dict(orientation=orientation),
        grouped_mappings=["col", "row", "marker.color"],
        layout_patch=dict(boxmode=mode),
    )


def scatter_3d(
    df,
    x=None,
    y=None,
    z=None,
    color=None,
    symbol=None,
    size=None,
    text=None,
    color_map={},
    symbol_map={},
    hover=None,
    color_sequence=None,
    symbol_sequence=default_symbol_seq,
    error_x=None,
    error_x_minus=None,
    error_y=None,
    error_y_minus=None,
    error_z=None,
    error_z_minus=None,
    max_size=default_max_size,
    orders={},
):
    return make_figure(
        args=locals(),
        constructor=go.Scatter3d,
        trace_patch=dict(mode="markers" + ("+text" if text else "")),
        grouped_mappings=["marker.color", "marker.symbol"],
    )


def line_3d(
    df,
    x=None,
    y=None,
    z=None,
    color=None,
    dash=None,
    text=None,
    color_map={},
    dash_map={},
    hover=None,
    color_sequence=None,
    dash_sequence=default_dash_seq,
    error_x=None,
    error_x_minus=None,
    error_y=None,
    error_y_minus=None,
    error_z=None,
    error_z_minus=None,
    orders={},
):
    return make_figure(
        args=locals(),
        constructor=go.Scatter3d,
        trace_patch=dict(mode="lines" + ("+markers+text" if text else "")),
        grouped_mappings=["line.color", "line.dash"],
    )


def scatter_ternary(
    df,
    a=None,
    b=None,
    c=None,
    color=None,
    symbol=None,
    size=None,
    text=None,
    color_map={},
    symbol_map={},
    hover=None,
    color_sequence=None,
    symbol_sequence=default_symbol_seq,
    max_size=default_max_size,
    orders={},
):
    return make_figure(
        args=locals(),
        constructor=go.Scatterternary,
        trace_patch=dict(mode="markers" + ("+text" if text else "")),
        grouped_mappings=["marker.color", "marker.symbol"],
    )


def line_ternary(
    df,
    a=None,
    b=None,
    c=None,
    color=None,
    dash=None,
    split=None,
    hover=None,
    text=None,
    color_map={},
    dash_map={},
    color_sequence=None,
    dash_sequence=default_dash_seq,
    orders={},
):
    return make_figure(
        args=locals(),
        constructor=go.Scatterternary,
        trace_patch=dict(mode="lines" + ("+markers+text" if text else "")),
        grouped_mappings=["marker.color", "line.dash", "split"],
    )


def scatter_polar(
    df,
    r,
    theta,
    color=None,
    symbol=None,
    size=None,
    hover=None,
    text=None,
    color_map={},
    symbol_map={},
    color_sequence=None,
    symbol_sequence=default_symbol_seq,
    direction="clockwise",
    startangle=90,
    max_size=default_max_size,
    orders={},
):
    return make_figure(
        args=locals(),
        constructor=go.Scatterpolar,
        trace_patch=dict(mode="markers" + ("+text" if text else "")),
        grouped_mappings=["marker.color", "marker.symbol"],
    )


def line_polar(
    df,
    r,
    theta,
    color=None,
    dash=None,
    hover=None,
    split=None,
    text=None,
    color_map={},
    dash_map={},
    color_sequence=None,
    dash_sequence=default_dash_seq,
    direction="clockwise",
    startangle=90,
    close_lines=False,
    orders={},
):
    return make_figure(
        args=locals(),
        constructor=go.Scatterpolar,
        trace_patch=dict(mode="lines" + ("+markers+text" if text else "")),
        grouped_mappings=["marker.color", "line.dash", "split"],
    )


def bar_polar(
    df,
    r=None,
    theta=None,
    color=None,
    hover=None,
    color_map={},
    color_sequence=None,
    normalization="",
    mode="relative",
    direction="clockwise",
    startangle=90,
    orders={},
):
    return make_figure(
        args=locals(),
        constructor=go.Barpolar,
        grouped_mappings=["marker.color"],
        layout_patch=dict(barnorm=normalization, barmode=mode),
    )


def choropleth(
    df,
    lat=None,
    lon=None,
    locations=None,
    color=None,
    color_sequence=None,
    hover=None,
    size=None,
    max_size=default_max_size,
    orders={},
):
    return make_figure(args=locals(), constructor=go.Choropleth)


def scatter_geo(
    df,
    lat=None,
    lon=None,
    locations=None,
    color=None,
    text=None,
    hover=None,
    color_map={},
    color_sequence=None,
    size=None,
    max_size=default_max_size,
    orders={},
):
    return make_figure(
        args=locals(),
        constructor=go.Scattergeo,
        trace_patch=dict(mode="markers" + ("+text" if text else "")),
        grouped_mappings=["marker.color"],
    )


def line_geo(
    df,
    lat=None,
    lon=None,
    locations=None,
    color=None,
    dash=None,
    text=None,
    hover=None,
    split=None,
    color_map={},
    color_sequence=None,
    dash_map={},
    dash_sequence=default_dash_seq,
    orders={},
):
    return make_figure(
        args=locals(),
        constructor=go.Scattergeo,
        trace_patch=dict(mode="lines" + ("+markers+text" if text else "")),
        grouped_mappings=["line.color", "line.dash", "split"],
    )


def scatter_mapbox(
    df,
    lat=None,
    lon=None,
    color=None,
    text=None,
    hover=None,
    color_map={},
    color_sequence=None,
    size=None,
    max_size=default_max_size,
    zoom=8,
    orders={},
):
    return make_figure(
        args=locals(),
        constructor=go.Scattermapbox,
        trace_patch=dict(mode="markers" + ("+text" if text else "")),
        grouped_mappings=["marker.color"],
    )


def line_mapbox(
    df,
    lat=None,
    lon=None,
    color=None,
    text=None,
    hover=None,
    split=None,
    color_map={},
    color_sequence=None,
    zoom=8,
    orders={},
):
    return make_figure(
        args=locals(),
        constructor=go.Scattermapbox,
        trace_patch=dict(mode="lines" + ("+markers+text" if text else "")),
        grouped_mappings=["line.color", "split"],
    )


def scatter_matrix(
    df,
    dimensions=None,
    color=None,
    symbol=None,
    color_map={},
    symbol_map={},
    color_sequence=None,
    symbol_sequence=default_symbol_seq,
    size=None,
    max_size=default_max_size,
    orders={},
):
    return make_figure(
        args=locals(),
        constructor=go.Splom,
        grouped_mappings=["marker.color", "marker.symbol"],
    )


def parallel_coordinates(df, dimensions=None, color=None, color_sequence=None):
    return make_figure(args=locals(), constructor=go.Parcoords)


def parallel_categories(df, dimensions=None, color=None, color_sequence=None):
    return make_figure(args=locals(), constructor=go.Parcats)
