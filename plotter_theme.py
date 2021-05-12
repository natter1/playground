from enum import Enum, auto
from typing import Union, Literal

import pyvista as pv


# create singleton IGNORE and a type for TypeHinting
from pyvista import parse_font_family


class Ignore(Enum):
    token = auto()


IGNORE = Ignore.token

def main():
    from pyvista import examples
    theme = BaseTheme()
    theme.background = 'w'
    theme.set_font(size=40, color='red')
    theme.use()
    dem = examples.download_crater_topo()
    dem.plot(cpos="xy")

    DefaultTheme().use()
    dem.plot(cpos="xy")


class BaseTheme:
    def __init__(self):
        # IGNORE -> rcParmas value not changed
        self._jupyter_backend = IGNORE
        self._auto_close = IGNORE
        self._background = IGNORE
        self._full_screen = IGNORE
        self._camera = IGNORE
        self._notebook = IGNORE
        self._window_size = IGNORE
        self._font = IGNORE
        self._cmap = IGNORE
        self._color = IGNORE
        self._nan_color = IGNORE
        self._edge_color = IGNORE
        self._outline_color = IGNORE
        self._floor_color = IGNORE
        self._colorbar_orientation = IGNORE
        self._colorbar_horizontal = IGNORE
        self._colorbar_vertical = IGNORE
        self._show_scalar_bar = IGNORE
        self._show_edges = IGNORE
        self._lighting = IGNORE
        self._interactive = IGNORE
        self._render_points_as_spheres = IGNORE
        self._use_ipyvtk = IGNORE
        self._use_panel = IGNORE
        self._transparent_background = IGNORE
        self._title = IGNORE
        self._axes = IGNORE
        self._multi_samples = IGNORE
        self._multi_rendering_splitting_position = IGNORE
        self._volume_mapper = IGNORE
        self._smooth_shading = IGNORE
        self._depth_peeling = IGNORE
        self._silhouette = IGNORE
        self._slider_style = IGNORE

    @property
    def jupyter_backend(self):
        return self._jupyter_backend

    @jupyter_backend.setter
    def jupyter_backend(self, value):
        self._jupyter_backend = value

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
    def full_screen(self):
        return self._full_screen

    @full_screen.setter
    def full_screen(self, value):
        self._full_screen = value

    @property
    def camera(self):
        return self._camera

    @camera.setter
    def camera(self, value):
        self._camera = value

    @property
    def notebook(self):
        return self._notebook

    @notebook.setter
    def notebook(self, value):
        self._notebook = value

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
    def font(self, value: dict):
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
    def use_ipyvtk(self):
        return self._use_ipyvtk

    @use_ipyvtk.setter
    def use_ipyvtk(self, value):
        self._use_ipyvtk = value

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
    def smooth_shading(self):
        return self._smooth_shading

    @smooth_shading.setter
    def smooth_shading(self, value):
        self._smooth_shading = value

    @property
    def depth_peeling(self):
        return self._depth_peeling

    @depth_peeling.setter
    def depth_peeling(self, value):
        self._depth_peeling = value

    @property
    def silhouette(self):
        return self._silhouette

    @silhouette.setter
    def silhouette(self, value):
        self._silhouette = value

    @property
    def slider_style(self):
        return self._slider_style

    @slider_style.setter
    def slider_style(self, value):
        self._slider_style = value

    def use(self):
        # set theme to rcParams
        theme_dict = self._generate_dict()
        from pyvista import DEFAULT_THEME
        for k, v in DEFAULT_THEME.items():
            if theme_dict[k] is not IGNORE:
                pv.rcParams[k] = theme_dict[k]

    def use_for(self, plot):
        # only use for given plot
        pass

    def copy_from(self, theme):
        pass

    def _generate_dict(self):
        # generate dict for use with pv.set_plot_theme()
        return {
            "jupyter_backend": self.jupyter_backend,
            "auto_close": self.auto_close,
            "background": self.background,
            "full_screen": self.full_screen,
            "camera": self.camera,
            "notebook": self.notebook,
            "window_size": self.window_size,
            "font": self.font,
            "cmap": self.cmap,
            "color": self.color,
            "nan_color": self.nan_color,
            "edge_color": self.edge_color,
            "outline_color": self.outline_color,
            "floor_color": self.floor_color,
            "colorbar_orientation": self.colorbar_orientation,
            "colorbar_horizontal": self.colorbar_horizontal,
            "colorbar_vertical": self.colorbar_vertical,
            "show_scalar_bar": self.show_scalar_bar,
            "show_edges": self.show_edges,
            "lighting": self.lighting,
            "interactive": self.interactive,
            "render_points_as_spheres": self.render_points_as_spheres,
            "use_ipyvtk": self.use_ipyvtk,
            "use_panel": self.use_panel,
            "transparent_background": self.transparent_background,
            "title": self.title,
            "axes": self.axes,
            "multi_samples": self.multi_samples,
            "multi_rendering_splitting_position": self.multi_rendering_splitting_position,
            "volume_mapper": self.volume_mapper,
            "smooth_shading": self.smooth_shading,
            "depth_peeling": self.depth_peeling,
            "silhouette": self.silhouette,
            "slider_style": self.slider_style
        }


class DefaultTheme(BaseTheme):
    def __init__(self):
        super().__init__()
        self.jupyter_backend = 'ipyvtklink'
        self.auto_close = True
        self.background = [0.3, 0.3, 0.3]
        self.camera = {
            'position': [1, 1, 1],
            'viewup': [0, 0, 1],
        }
        self.notebook = None
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
        self.use_ipyvtk = False
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
        self.multi_rendering_splitting_position = None
        import os
        self.volume_mapper = 'fixed_point' if os.name == 'nt' else 'smart'
        self.smooth_shading = False
        self.depth_peeling = {
            'number_of_peels': 4,
            'occlusion_ratio': 0.0,
            'enabled': False,
        }
        self.silhouette = {
            'color': 'black',
            'line_width': 2,
            'opacity': 1.0,
            'feature_angle': False,
            'decimate': 0.9,
        }
        self.slider_style = {
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



if __name__ == '__main__':
    main()
