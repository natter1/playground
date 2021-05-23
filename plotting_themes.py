from enum import Enum, auto
from typing import Literal, Optional

import pyvista as pv
from ansys.mapdl.core.post import PostProcessing
from pyvista.themes import DefaultTheme


# create singleton IGNORE and a type for TypeHinting
class Ignore(Enum):
    token = auto()


IGNORE = Ignore.token

def main():
    from pyvista import examples
    theme = DefaultTheme()
    theme.background = 'w'
    theme
    theme.font.size=40
    theme.font.color='red'
    pv.global_theme = theme
    dem = examples.download_crater_topo()
    dem.plot(cpos="xy")

    style = EmptyStyle()
    style.background = "blue"
    style.use_global()
    style.set_to(theme)

    dem.plot(cpos="xy")


class MAPDLTheme(DefaultTheme):
    def __init__(self):
        super().__init__()
        # settings from pymapdl/ansys/mapdl/core/misc.py _configure_pyvista()
        self.interactive = True
        self.cmap = "jet"
        self.font.family = "courier"
        self.title = "pyansys"


# not compatible with pyvista internal usage of Theme, therefore the name style
class EmptyStyle(DefaultTheme):
    def __init__(self):
        super().__init__()

        for name, _ in vars(self).items():
            setattr(self, name, IGNORE)

    def set_to(self, theme: DefaultTheme):
        if not isinstance(theme, DefaultTheme):
            raise TypeError('``theme`` must be a pyvista theme like '
                            '``pyvista.themes.DefaultTheme``')

        for name, value in vars(self).items():
            if getattr(self, name) is not IGNORE:
                setattr(theme, name, value)

    def use_global(self):
        for name, value in vars(self).items():
            if getattr(self, name) is not IGNORE:
                setattr(pv.global_theme, name, value)


# ---------------------------------------------------------------------------
# -------------------- rcParams set in different pymapdl as Style -----------
# ---------------------------------------------------------------------------

class GeneralPlotterStyle(EmptyStyle):
    def __init__(self):
        """
        Most (all?) plotting functions in pymapdl can address the parameters in general_plotter() via kwargs.
        """
        super().__init__()
        self.title = ''
        self.background = None
        self.window_size = None
        self.notebook = None
        # add_mesh kwargs:
        self.color = 'w'
        self.show_edges = None
        self.edge_color = None
        self.lighting = None
        self.cmap = None
        self.render_points_as_spheres = False
        self.smooth_shading = None

        # parameters not part of pyvista.DefaultTheme()
        self.cpos = None
        self.show_bounds = False
        self.show_axes = True
        self.off_screen = None
        self.savfig = None
        self.point_size = 5.0
        self.line_width = None
        self.opacity = 1.0
        self.flip_scalars = False
        self.n_colors = 256
        self.interpolate_before_map = True
        self.render_lines_as_tubes = False
        self.stitle = None  # todo: stitle is deprecated in pyvista -> scalar_bar_args

        # todo: up till now this is to format labels - not the same as pyvista!
        self.font.size = None
        self.font.family = None
        self.text_color = None

        # --------------------------------
        # --- inside general_plotter() ---
        # --------------------------------
        if notebook:
            off_screen = True


class APlotStyle(EmptyStyle):
    # Type Hints
    vtk: Optional[bool]
    quality: Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    show_area_numbering: bool
    show_line_numbering: bool
    color_areas: bool
    show_lines: bool
    stitle: Optional[str]

    def __init__(self):
        super().__init__()
        self.title = "MAPDL Area Plot"

        # parameters not part of pyvista.DefaultTheme()
        self.vtk = None  # todo: what does None mean?
        self.quality = 4
        self.show_area_numbering = False
        self.show_line_numbering = False
        self.color_areas = False
        self.show_lines = False
        self.stitle = None  # -> where to put instead?

        # ----------------------------------------------------------------------
        # --------------------------- current state ----------------------------
        # ----------------------------------------------------------------------

        # --------------------------
        # --- parameters aplot() ---
        # --------------------------
        kwargs={"..."}
        vtk = None  # -> vtk = self._use_vtk
        quality = 4
        show_area_numbering = False
        show_line_numbering = False
        color_areas = False
        show_lines = False
        kwargs  # -> ued for edge_color (mesh); given to general_plotter()

        # ----------------------
        # --- inside aplot() ---
        # ----------------------
        if vtk is None:
            vtk = self._use_vtk

        kwargs.setdefault('title', 'MAPDL Area Plot')
        kwargs.setdefault('stitle', None)  # todo: stitle is deprecated in pyvista -> scalar_bar_args
        kwargs.setdefault('line_width', 2)

        if show_lines:
            meshes.append({'mesh': lines,
                           'color': kwargs.get('edge_color', 'k')})


class EPlotStyle(EmptyStyle):
    show_node_numbering: bool
    vtk: Optional[bool]

    def __init__(self):
        super().__init__()
        self.title = 'MAPDL Element Plot'
        self.show_edges = True

        # parameters not part of pyvista.DefaultTheme()
        self.show_node_numbering = False
        self. vtk = None  # -> vtk = self._use_vtk

        # ----------------------------------------------------------------------
        # --------------------------- current state ----------------------------
        # ----------------------------------------------------------------------

        # --------------------------
        # --- parameters eplot() ---
        # --------------------------
        kwargs={"..."}
        show_node_numbering = False
        vtk = None
        kwargs  # -> ued for show_edges; given to general_plotter()

        # ----------------------
        # --- inside eplot() ---
        # ----------------------
        if vtk is None:
            vtk = self._use_vtk

        kwargs.setdefault('title', 'MAPDL Element Plot')
        kwargs.setdefault('show_edges', True)


class KPlotStyle(EmptyStyle):
    vtk: Optional[bool]
    show_keypoint_numbering: bool

    def __init__(self):
        super().__init__()
        self.title = 'MAPDL Keypoint Plot'

        # parameters not part of pyvista.DefaultTheme()
        self.vtk = None  # -> vtk = self._use_vtk
        self.show_keypoint_numbering = True

        # ----------------------------------------------------------------------
        # --------------------------- current state ----------------------------
        # ----------------------------------------------------------------------

        # --------------------------
        # --- parameters kplot() ---
        # --------------------------
        kwargs={"..."}
        vtk = None
        show_keypoint_numbering = True
        kwargs  # given to general_plotter()

        # ----------------------
        # --- inside kplot() ---
        # ----------------------
        if vtk is None:
            vtk = self._use_vtk
        kwargs.setdefault('title', 'MAPDL Keypoint Plot')


class LPLOTStyle(EmptyStyle):
    vtk: Optional[bool]
    show_line_numbering: bool
    show_keypoint_numbering: bool
    color_lines: bool

    def __init__(self):
        super().__init__()
        self.title = 'MAPDL Line Plot'

        # parameters not part of pyvista.DefaultTheme()
        self.vtk = None  # -> vtk = self._use_vtk
        self.show_line_numbering = True
        self.show_keypoint_numbering = False
        self.color_lines = False

        # --------------------------
        # --- parameters lplot() ---
        # --------------------------
        kwargs = {"..."}
        vtk = None
        show_line_numbering = True
        show_keypoint_numbering = False
        color_lines = False
        kwargs  # given to general_plotter()

        # ----------------------
        # --- inside lplot() ---
        # ----------------------
        if vtk is None:
            vtk = self._use_vtk

        kwargs.setdefault('title', 'MAPDL Line Plot')


class NPLOTStyle(EmptyStyle):
    # Type Hints
    vtk: Optional[bool]

    def __init__(self):
        super().__init__()
        self.title = 'MAPDL Node Plot'

        # parameters not part of pyvista.DefaultTheme()
        self.vtk = None  # -> vtk = self._use_vtk


        # ----------------------------------------------------------------------
        # --------------------------- current state ----------------------------
        # ----------------------------------------------------------------------

        # --------------------------
        # --- parameters nplot() ---
        # --------------------------
        kwargs = {"..."}
        vtk = None
        kwargs  # given to general_plotter()

        # ----------------------
        # --- inside nplot() ---
        # ----------------------
        if vtk is None:
            vtk = self._use_vtk

        kwargs.setdefault('title', 'MAPDL Node Plot')


class VPLOTStyle(EmptyStyle):
    # Type Hints
    vtk: Optional[bool]
    quality: Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    show_area_numbering: bool
    show_line_numbering: bool
    color_areas: bool
    show_lines: bool

    def __init__(self):
        super().__init__()
        # parameters not part of pyvista.DefaultTheme()
        self.vtk = None  # -> vtk = self._use_vtk
        self.quality = 4
        self.show_area_numbering = False
        self.show_line_numbering = False
        self.color_areas = False
        self.show_lines = True

        # ----------------------------------------------------------------------
        # --------------------------- current state ----------------------------
        # ----------------------------------------------------------------------

        # --------------------------
        # --- parameters vplot() ---
        # --------------------------
        kwargs = {"..."}
        vtk = None
        quality = 4
        show_area_numbering = False
        show_line_numbering = False
        color_areas = False
        show_lines = True
        kwargs  # given to aplot()

        # ----------------------
        # --- inside vplot() ---
        # ----------------------
        if vtk is None:
            vtk = self._use_vtk


# ----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------- PostProcessing -----------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# -------------------------
# ()
# -------------------------
# parameters:

# inside method:



kwargs = {}
# -------------------------
# plot_nodal_displacement()
# -------------------------
# parameters:
component='NORM'
show_node_numbering=False
kwargs  # -> self._plot_point_scalars()

# inside method:
kwargs.setdefault('stitle', '%s Displacement' % component)


# -------------------------
# plot_nodal_rotation()
# -------------------------
# parameters:
component  # no default value
show_node_numbering=False
kwargs  # -> self._plot_point_scalars()
# inside method:
kwargs.setdefault('stitle', '%s Rotation' % component)


# -------------------------
# plot_nodal_temperature()
# -------------------------
# parameters:
show_node_numbering=False
kwargs  # -> self._plot_point_scalars()
# inside method:
kwargs.setdefault('stitle', 'Nodal\nTemperature')


# -------------------------
# plot_nodal_pressure()
# -------------------------
# parameters:
show_node_numbering=False
kwargs  # -> self._plot_point_scalars()
# inside method:
kwargs.setdefault('stitle', 'Nodal\nPressure')


# --------------------
# plot_nodal_voltage()
# --------------------
# parameters:
show_node_numbering=False
kwargs  # -> self._plot_point_scalars()
# inside method:
kwargs.setdefault('stitle', 'Nodal\nVoltage')


# -----------------------------
# plot_nodal_component_stress()
# -----------------------------
# parameters:
component  # no default value
show_node_numbering=False
kwargs  # -> self._plot_point_scalars()
# inside method:
kwargs.setdefault('stitle', '%s Nodal\nStress' % component)


# -----------------------------
# plot_nodal_principal_stress()
# -----------------------------
# parameters:
component  # no default value
show_node_numbering=False
kwargs  # -> self._plot_point_scalars()
# inside method:
kwargs.setdefault('stitle', '%s Nodal\nPrincipal Stress' % component)


# -----------------------------
# plot_nodal_stress_intensity()
# -----------------------------
# parameters:
show_node_numbering=False
kwargs  # -> self._plot_point_scalars()
# inside method:
kwargs.setdefault('stitle', 'Nodal Stress\nIntensity')


# -------------------------
# ()
# -------------------------
# parameters:

# inside method:







from enum import Enum, auto
class NodalSolution(Enum):
    Displacement_X = auto()
    Displacement_Y = auto()
    Displacement_Z = auto()
    Displacement_NORM = auto()

    Rotation_X = auto()
    Rotation_Y = auto()
    Rotation_Z = auto()

    Temperature = auto()
    # ...


class NodalTheme(MAPDLTheme):
    def __init__(self):
        super().__init__()
        # todo: how to implement optional settings like stitle (in most cases plot() should take care of it)
        self.show_node_numbering = False


class _PostProcessing(PostProcessing):
    def __init__(self, mapdl):
        # todo: move to PostProcessing (allows function as self.nodal_displacement ...)
        super().__init__(mapdl)
        self._plot_dict = {  # scalar function, stitle, comp
            NodalSolution.Displacement_X: (self.nodal_displacement, 'X Displacement', 'X'),
            NodalSolution.Displacement_Y: (self.nodal_displacement, 'Y Displacement', 'Y'),
            NodalSolution.Displacement_Z: (self.nodal_displacement, 'Z Displacement', 'Z'),
            NodalSolution.Displacement_NORM: (self.nodal_displacement, 'NORM Displacement', 'NORM'),
            NodalSolution.Rotation_X: (self.nodal_rotation, 'X Rotation', 'X'),
            NodalSolution.Rotation_Y: (self.nodal_rotation, 'Y Rotation', 'y'),
            NodalSolution.Rotation_Z: (self.nodal_rotation, 'Z Rotation', 'Z'),
            NodalSolution.Temperature: (self.nodal_temperature, 'Nodal Temperature', None),
            # ...
        }

    def plot(self, solution: NodalSolution, show_node_numbering=False, **kwargs):
        func, _stitle, comp = self._plot_dict[solution]
        kwargs.setdefault('stitle', _stitle)
        if comp is not None:
            scalars = func(comp)
        else:
            scalars = func()

        return self._plot_point_scalars(scalars, show_node_numbering=show_node_numbering,
                                        **kwargs)




print(NodalSolution.Rotation_Y.name)


# ---------------------
# _plot_point_scalars()
# ---------------------
# parameters:
show_node_numbering=False
kwargs  # -> general_plotter()

# inside method:
meshes = [{'mesh': surf.copy(deep=False),  # deep=False for ipyvtk-simple
           'stitle': kwargs.pop('stitle', ''),
           'scalars': scalars}]
if show_node_numbering:
    labels = [{'points': surf.points, 'labels': surf['ansys_node_num']}]
kwargs.setdefault('title', 'MAPDL Displacement')  # todo: is this correct? title is not set in plot_nodal_...()


if __name__ == '__main__':
    main()
