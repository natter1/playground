class Conta172:
    """
    Control object for element conta172.
    
    CONTA172 is used to represent contact
    and sliding between 2-D target surfaces (TARGE169) and a deformable surface, defined by this element. The element
    is applicable to 2-D structural and coupled-field contact analyses.
    It can be used for both pair-based contact and general contact.In the case of pair-based contact, the target surface is defined
    by the 2-D target element type, TARGE169.
    In the case of general contact, the target surface can be defined
    by CONTA172 elements (for deformable surfaces)
    or TARGE169 elements (for rigid bodies only). This element is located on the surfaces of 2-D solid elements with
                midside nodes (for example, PLANE183,
                    INTER193, SHELL209,
                    PLANE223, CPT213,
                    MATRIX50). The element has the same geometric characteristics as the solid
    element face with which it is connected (see Figure 172.1: CONTA172 Geometry). Contact occurs when the element surface
    penetrates an associated target surface.Coulomb friction, shear stress friction, user-defined friction
    with the USERFRIC subroutine, and user-defined
    contact interaction with the USERINTER subroutine
    are allowed. This element also allows separation of bonded contact
    to simulate interface delamination. See CONTA172 in the Mechanical APDL Theory Reference for more details about this element. Other surface-to-surface
    contact elements (CONTA171, CONTA173, CONTA174) are also available.Figure 172.1:  CONTA172 Geometry
    """
    def __init__(self):
        self._r1 = ""
        self._r2 = ""
        self._fkn = ""
        self._ftoln = ""
        self._icont = ""
        self._pinb = ""
        self._pmax = ""
        self._pmin = ""
        self._taumax = ""
        self._cnof = ""
        self._fkop = ""
        self._fkt = ""
        self._cohe = ""
        self._tcc = ""
        self._fhtg = ""
        self._sbct = ""
        self._rdvf = ""
        self._fwgt = ""
        self._ecc = ""
        self._fheg = ""
        self._fact = ""
        self._dc = ""
        self._slto = ""
        self._tnop = ""
        self._tols = ""
        self._ppcn = ""
        self._fpat = ""
        self._cor = ""
        self._strm = ""
        self._fdmn = ""
        self._fdmt = ""
        self._tbnd = ""
        self._wbid = ""
        self._pcc = ""
        self._psee = ""
        self._abpp = ""
        self._fpft = ""
        self._fpwt = ""
        self._dcc = ""
        self._dcon = ""
        self._abdc = ""

    @property
    def r1(self):
        """
        Target circle radius.
        """
        return self._r1

    @r1.setter
    def r1(self, value):
        self._r1 = value

    @property
    def r2(self):
        """
        Superelement thickness.
        """
        return self._r2

    @r2.setter
    def r2(self, value):
        self._r2 = value

    @property
    def fkn(self):
        """
        Normal penalty stiffness factor.
        """
        return self._fkn

    @fkn.setter
    def fkn(self, value):
        self._fkn = value

    @property
    def ftoln(self):
        """
        Penetration tolerance factor.
        """
        return self._ftoln

    @ftoln.setter
    def ftoln(self, value):
        self._ftoln = value

    @property
    def icont(self):
        """
        Initial contact closure.
        """
        return self._icont

    @icont.setter
    def icont(self, value):
        self._icont = value

    @property
    def pinb(self):
        """
        Pinball region.
        """
        return self._pinb

    @pinb.setter
    def pinb(self, value):
        self._pinb = value

    @property
    def pmax(self):
        """
        Upper limit of initial allowable penetration.
        """
        return self._pmax

    @pmax.setter
    def pmax(self, value):
        self._pmax = value

    @property
    def pmin(self):
        """
        Lower limit of initial allowable penetration.
        """
        return self._pmin

    @pmin.setter
    def pmin(self, value):
        self._pmin = value

    @property
    def taumax(self):
        """
        Maximum friction stress.
        """
        return self._taumax

    @taumax.setter
    def taumax(self, value):
        self._taumax = value

    @property
    def cnof(self):
        """
        Contact surface offset.
        """
        return self._cnof

    @cnof.setter
    def cnof(self, value):
        self._cnof = value

    @property
    def fkop(self):
        """
        Contact opening stiffness.
        """
        return self._fkop

    @fkop.setter
    def fkop(self, value):
        self._fkop = value

    @property
    def fkt(self):
        """
        Tangent penalty stiffness factor.
        """
        return self._fkt

    @fkt.setter
    def fkt(self, value):
        self._fkt = value

    @property
    def cohe(self):
        """
        Contact cohesion.
        """
        return self._cohe

    @cohe.setter
    def cohe(self, value):
        self._cohe = value

    @property
    def tcc(self):
        """
        Thermal contact conductance.
        """
        return self._tcc

    @tcc.setter
    def tcc(self, value):
        self._tcc = value

    @property
    def fhtg(self):
        """
        Frictional heating factor.
        """
        return self._fhtg

    @fhtg.setter
    def fhtg(self, value):
        self._fhtg = value

    @property
    def sbct(self):
        """
        Stefan-Boltzmann constant.
        """
        return self._sbct

    @sbct.setter
    def sbct(self, value):
        self._sbct = value

    @property
    def rdvf(self):
        """
        Radiation view factor.
        """
        return self._rdvf

    @rdvf.setter
    def rdvf(self, value):
        self._rdvf = value

    @property
    def fwgt(self):
        """
        Heat distribution weighing factor.
        """
        return self._fwgt

    @fwgt.setter
    def fwgt(self, value):
        self._fwgt = value

    @property
    def ecc(self):
        """
        Electric contact conductance.
        """
        return self._ecc

    @ecc.setter
    def ecc(self, value):
        self._ecc = value

    @property
    def fheg(self):
        """
        Joule dissipation weight factor.
        """
        return self._fheg

    @fheg.setter
    def fheg(self, value):
        self._fheg = value

    @property
    def fact(self):
        """
        Static/dynamic ratio.
        """
        return self._fact

    @fact.setter
    def fact(self, value):
        self._fact = value

    @property
    def dc(self):
        """
        Exponential decay coefficient.
        """
        return self._dc

    @dc.setter
    def dc(self, value):
        self._dc = value

    @property
    def slto(self):
        """
        Allowable elastic slip.
        """
        return self._slto

    @slto.setter
    def slto(self, value):
        self._slto = value

    @property
    def tnop(self):
        """
        Maximum allowable tensile contact pressure.
        """
        return self._tnop

    @tnop.setter
    def tnop(self, value):
        self._tnop = value

    @property
    def tols(self):
        """
        Target edge extension factor.
        """
        return self._tols

    @tols.setter
    def tols(self, value):
        self._tols = value

    @property
    def ppcn(self):
        """
        Pressure penetration criterion.
        """
        return self._ppcn

    @ppcn.setter
    def ppcn(self, value):
        self._ppcn = value

    @property
    def fpat(self):
        """
        Fluid penetration acting time.
        """
        return self._fpat

    @fpat.setter
    def fpat(self, value):
        self._fpat = value

    @property
    def cor(self):
        """
        Coefficient of restitution.
        """
        return self._cor

    @cor.setter
    def cor(self, value):
        self._cor = value

    @property
    def strm(self):
        """
        Load step number for ramping penetration.
        """
        return self._strm

    @strm.setter
    def strm(self, value):
        self._strm = value

    @property
    def fdmn(self):
        """
        Normal stabilization damping factor.
        """
        return self._fdmn

    @fdmn.setter
    def fdmn(self, value):
        self._fdmn = value

    @property
    def fdmt(self):
        """
        Tangential stabilization damping factor.
        """
        return self._fdmt

    @fdmt.setter
    def fdmt(self, value):
        self._fdmt = value

    @property
    def tbnd(self):
        """
        Critical bonding temperature.
        """
        return self._tbnd

    @tbnd.setter
    def tbnd(self, value):
        self._tbnd = value

    @property
    def wbid(self):
        """
        Internal contact pair ID (used by ANSYS Workbench).
        """
        return self._wbid

    @wbid.setter
    def wbid(self, value):
        self._wbid = value

    @property
    def pcc(self):
        """
        Pore fluid contact permeability coefficient.
        """
        return self._pcc

    @pcc.setter
    def pcc(self, value):
        self._pcc = value

    @property
    def psee(self):
        """
        Pore fluid seepage coefficient.
        """
        return self._psee

    @psee.setter
    def psee(self, value):
        self._psee = value

    @property
    def abpp(self):
        """
        Ambient pore pressure.
        """
        return self._abpp

    @abpp.setter
    def abpp(self, value):
        self._abpp = value

    @property
    def fpft(self):
        """
        Gap pore fluid flow participation factor.
        """
        return self._fpft

    @fpft.setter
    def fpft(self, value):
        self._fpft = value

    @property
    def fpwt(self):
        """
        Gap pore fluid flow distribution weighting factor.
        """
        return self._fpwt

    @fpwt.setter
    def fpwt(self, value):
        self._fpwt = value

    @property
    def dcc(self):
        """
        Contact diffusivity coefficient.
        """
        return self._dcc

    @dcc.setter
    def dcc(self, value):
        self._dcc = value

    @property
    def dcon(self):
        """
        Diffusive convection coefficient.
        """
        return self._dcon

    @dcon.setter
    def dcon(self, value):
        self._dcon = value

    @property
    def abdc(self):
        """
        Ambient concentration.
        """
        return self._abdc

    @abdc.setter
    def abdc(self, value):
        self._abdc = value

    def call_r(self):
        """
        Set all real constants by calling r and rmore.
        """
        pass  # todo
