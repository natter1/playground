import pyvista as pv


class BaseTheme:
    def __init__(self):
        # None -> rcParmas value not changed
        self._auto_close = None
        self._background = None
        self._camera = None
        self._window_size = None
        self._font = None
        self._cmap = None
        self._color = None
        self._nan_color = None
        self._edge_color = None
        self._outline_color = None
        self._floor_color = None
        self._colorbar_orientation = None
        self._colorbar_horizontal = None
        self._colorbar_vertical = None
        self._show_scalar_bar = None
        self._show_edges = None
        self._lighting = None
        self._interactive = None
        self._render_points_as_spheres = None
        self._use_panel = None
        self._transparent_background = None
        self._title = None
        self._axes = None
        self._multi_samples = None
        self._multi_rendering_splitting_position = None
        self._volume_mapper = None
        self._depth_peeling = None
        self._slide_style = None

    @property
    def auto_close(self):
        return self._auto_close

    @auto_close.setter
    def auto_close(self, value):
        self._auto_close = value

    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, value):
        self._background = value

    @property
    def camera(self):
        return self._camera

    @camera.setter
    def camera(self, value):
        self._camera = value

    @property
    def window_size(self):
        return self._window_size

    @window_size.setter
    def window_size(self, value):
        self._window_size = value

    @property
    def font(self):
        return self._font

    @font.setter
    def font(self, value):
        self._font = value

    @property
    def cmap(self):
        return self._cmap

    @cmap.setter
    def cmap(self, value):
        self._cmap = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def nan_color(self):
        return self._nan_color

    @nan_color.setter
    def nan_color(self, value):
        self._nan_color = value

    @property
    def edge_color(self):
        return self._edge_color

    @edge_color.setter
    def edge_color(self, value):
        self._edge_color = value

    @property
    def outline_color(self):
        return self._outline_color

    @outline_color.setter
    def outline_color(self, value):
        self._outline_color = value

    @property
    def floor_color(self):
        return self._floor_color

    @floor_color.setter
    def floor_color(self, value):
        self._floor_color = value

    @property
    def colorbar_orientation(self):
        return self._colorbar_orientation

    @colorbar_orientation.setter
    def colorbar_orientation(self, value):
        self._colorbar_orientation = value

    @property
    def colorbar_horizontal(self):
        return self._colorbar_horizontal

    @colorbar_horizontal.setter
    def colorbar_horizontal(self, value):
        self._colorbar_horizontal = value

    @property
    def colorbar_vertical(self):
        return self._colorbar_vertical

    @colorbar_vertical.setter
    def colorbar_vertical(self, value):
        self._colorbar_vertical = value

    @property
    def show_scalar_bar(self):
        return self._show_scalar_bar

    @show_scalar_bar.setter
    def show_scalar_bar(self, value):
        self._show_scalar_bar = value

    @property
    def show_edges(self):
        return self._show_edges

    @show_edges.setter
    def show_edges(self, value):
        self._show_edges = value

    @property
    def lighting(self):
        return self._lighting

    @lighting.setter
    def lighting(self, value):
        self._lighting = value

    @property
    def interactive(self):
        return self._interactive

    @interactive.setter
    def interactive(self, value):
        self._interactive = value

    @property
    def render_points_as_spheres(self):
        return self._render_points_as_spheres

    @render_points_as_spheres.setter
    def render_points_as_spheres(self, value):
        self._render_points_as_spheres = value

    @property
    def use_panel(self):
        return self._use_panel

    @use_panel.setter
    def use_panel(self, value):
        self._use_panel = value

    @property
    def transparent_background(self):
        return self._transparent_background

    @transparent_background.setter
    def transparent_background(self, value):
        self._transparent_background = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def axes(self):
        return self._axes

    @axes.setter
    def axes(self, value):
        self._axes = value

    @property
    def multi_samples(self):
        return self._multi_samples

    @multi_samples.setter
    def multi_samples(self, value):
        self._multi_samples = value

    @property
    def multi_rendering_splitting_position(self):
        return self._multi_rendering_splitting_position

    @multi_rendering_splitting_position.setter
    def multi_rendering_splitting_position(self, value):
        self._multi_rendering_splitting_position = value

    @property
    def volume_mapper(self):
        return self._volume_mapper

    @volume_mapper.setter
    def volume_mapper(self, value):
        self._volume_mapper = value

    @property
    def depth_peeling(self):
        return self._depth_peeling

    @depth_peeling.setter
    def depth_peeling(self, value):
        self._depth_peeling = value

    @property
    def slide_style(self):
        return self._slide_style

    @slide_style.setter
    def slide_style(self, value):
        self._slide_style = value

    def use(self):
        # set theme to rcParams
        pass

    def use_for(self, plot):
        # only use for given plot
        pass

    def copy_from(self, theme):
        pass

    def _generate_dict(self):
        # generate dict for use with pv.set_plot_theme()
        pass


class DefaultTheme(BaseTheme):
    def __init__(self):
        super().__init__()
        self.auto_close = True
        self.background = [0.3, 0.3, 0.3]
        self.camera = {
            'position': [1, 1, 1],
            'viewup': [0, 0, 1],
        }
        self.window_size = [1024, 768]
        self.font = {
            'family': 'arial',
            'size': 12,
            'title_size': None,
            'label_size': None,
            'color': [1, 1, 1],
            'fmt': None,
        }
        self.cmap = 'viridis'
        self.color = 'white'
        self.nan_color = 'darkgray'
        self.edge_color = 'black'
        self.outline_color = 'white'
        self.floor_color = 'gray'
        self.colorbar_orientation = 'horizontal'
        self.colorbar_horizontal = {
            'width': 0.6,
            'height': 0.08,
            'position_x': 0.35,
            'position_y': 0.05,
        }
        self.colorbar_vertical = {
            'width': 0.08,
            'height': 0.45,
            'position_x': 0.9,
            'position_y': 0.02,
        }
        self.show_scalar_bar = True
        self.show_edges = False
        self.lighting = True
        self.interactive = False
        self.render_points_as_spheres = False
        self.use_panel = False
        self.transparent_background = False
        self.title = 'PyVista'
        self.axes = {
            'x_color': 'tomato',
            'y_color': 'seagreen',
            'z_color': 'mediumblue',
            'box': False,
            'show': True,
        }
        self.multi_samples = 4
        self.multi_rendering_splitting_position = None  # todo: how to know whether None should be set or should be ignored?
        import os
        self.volume_mapper = 'fixed_point' if os.name == 'nt' else 'smart'
        self.depth_peeling = {
            'number_of_peels': 4,
            'occlusion_ratio': 0.0,
            'enabled': False,
        }
        self.slide_style = {
            'classic': {
                'slider_length': 0.02,
                'slider_width': 0.04,
                'slider_color': (0.5, 0.5, 0.5),
                'tube_width': 0.005,
                'tube_color': (1, 1, 1),
                'cap_opacity': 1,
                'cap_length': 0.01,
                'cap_width': 0.02,
            },
            'modern': {
                'slider_length': 0.02,
                'slider_width': 0.04,
                'slider_color': (0.43137255, 0.44313725, 0.45882353),
                'tube_width': 0.04,
                'tube_color': (0.69803922, 0.70196078, 0.70980392),
                'cap_opacity': 0,
                'cap_length': 0.01,
                'cap_width': 0.02,
            },
        }
    @property
    def cmap(self):
        return super().cmap
    @cmap.setter
    def cmap(self, value):
        # todo: consider if build-in themes should be read only
        pass

# paraview
# rcParams['background'] = PARAVIEW_BACKGROUND
# rcParams['cmap'] = 'coolwarm'
# rcParams['font']['family'] = 'arial'
# rcParams['font']['label_size'] = 16
# rcParams['font']['color'] = 'white'
# rcParams['show_edges'] = False
# rcParams['color'] = 'white'
# rcParams['outline_color'] = 'white'
# rcParams['edge_color'] = 'black'
# rcParams['axes']['x_color'] = 'tomato'
# rcParams['axes']['y_color'] = 'gold'
# rcParams['axes']['z_color'] = 'green'
#
# # document
# rcParams['background'] = 'white'
# rcParams['cmap'] = 'viridis'
# rcParams['font']['size'] = 18
# rcParams['font']['title_size'] = 18
# rcParams['font']['label_size'] = 18
# rcParams['font']['color'] = 'black'
# rcParams['show_edges'] = False
# rcParams['color'] = 'tan'
# rcParams['outline_color'] = 'black'
# rcParams['edge_color'] = 'black'
# rcParams['axes']['x_color'] = 'tomato'
# rcParams['axes']['y_color'] = 'seagreen'
# rcParams['axes']['z_color'] = 'blue'
#
# rcParams['background'] = 'black'
# rcParams['cmap'] = 'viridis'
# rcParams['font']['color'] = 'white'
# rcParams['show_edges'] = False
# rcParams['color'] = 'tan'
# rcParams['outline_color'] = 'white'
# rcParams['edge_color'] = 'white'
# rcParams['axes']['x_color'] = 'tomato'
# rcParams['axes']['y_color'] = 'seagreen'
# rcParams['axes']['z_color'] = 'blue'