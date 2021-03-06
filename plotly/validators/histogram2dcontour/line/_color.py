import _plotly_utils.basevalidators


class ColorValidator(_plotly_utils.basevalidators.ColorValidator):

    def __init__(
        self,
        plotly_name='color',
        parent_name='histogram2dcontour.line',
        **kwargs
    ):
        super(ColorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            anim=kwargs.pop('anim', True),
            edit_type=kwargs.pop('edit_type', 'style+colorbars'),
            role=kwargs.pop('role', 'style'),
            **kwargs
        )
