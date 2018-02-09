# -*- coding: utf-8 -*-


"""
Module Legacy 

Content of the module
**********************

Summary:
========
.. autosummary::
     :toctree: _autosummary

    SimpleTesselatedTetraMechanicalMapping

    CenterPointTopologicalMapping

    FixedTranslationConstraint

    StopperConstraint

    ProjectionToTargetPlaneMapping

    SubsetTopologicalMapping

    Edge2QuadTopologicalMapping

    SlidingConstraint

    RegularGridSpringForceField

    CenterOfMassMulti2Mapping

    PythonMainScriptController

    BarycentricMapping

    ArticulatedSystemMapping

    Quad2TriangleTopologicalMapping

    IdentityMapping

    GearSpringForceField

    LCPForceFeedback

    CurveMapping

    Hexa2QuadTopologicalMapping

    FixedRotationConstraint

    CatmullRomSplineMapping

    JointSpringForceField

    SubsetMultiMapping

    SubsetMapping

    SPHFluidSurfaceMapping

    SkinningMapping

    StiffSpringForceField

    VectorSpringForceField

    Hexa2TetraTopologicalMapping

    RigidMapping

    SquareMapping

    CenterOfMassMultiMapping

    DevAngleCollisionMonitor

    DistanceMultiMapping

    CenterPointMechanicalMapping

    MeshSpringForceField

    AngularSpringForceField

    LineSetSkinningMapping

    BeamFEMForceField

    SimpleTesselatedHexaTopologicalMapping

    SquareDistanceMapping

    TubularMapping

    ProjectionToTargetLineMapping

    HexahedronCompositeFEMMapping

    ProjectionToLineMultiMapping

    Mesh2PointMechanicalMapping

    CompareTopology

    TOBBModel

    SpringForceField

    DevTensionMonitor

    ImplicitSurfaceMapping

    DistanceMapping

    DeformableOnRigidFrameMapping

    RigidRigidMapping

    TriangleBendingSprings

    QuadBendingSprings

    CenterOfMassMapping

    Mesh2PointTopologicalMapping

    SimpleTesselatedTetraTopologicalMapping

    BeamLinearMapping

    IdentityTopologicalMapping

    IdentityMultiMapping

    FrameSpringForceField

    SkeletalMotionConstraint

    Triangle2EdgeTopologicalMapping

    ProjectionToPlaneMultiMapping

    TCylinderModel

    PenalityContactForceField

    Tetra2TriangleTopologicalMapping

    UnilateralInteractionConstraint

    Distances

    RepulsiveSpringForceField

    ContactListener

    DistanceFromTargetMapping

    ExternalInterpolationMapping



Content:
========

.. automodule::

    SimpleTesselatedTetraMechanicalMapping

    CenterPointTopologicalMapping

    FixedTranslationConstraint

    StopperConstraint

    ProjectionToTargetPlaneMapping

    SubsetTopologicalMapping

    Edge2QuadTopologicalMapping

    SlidingConstraint

    RegularGridSpringForceField

    CenterOfMassMulti2Mapping

    PythonMainScriptController

    BarycentricMapping

    ArticulatedSystemMapping

    Quad2TriangleTopologicalMapping

    IdentityMapping

    GearSpringForceField

    LCPForceFeedback

    CurveMapping

    Hexa2QuadTopologicalMapping

    FixedRotationConstraint

    CatmullRomSplineMapping

    JointSpringForceField

    SubsetMultiMapping

    SubsetMapping

    SPHFluidSurfaceMapping

    SkinningMapping

    StiffSpringForceField

    VectorSpringForceField

    Hexa2TetraTopologicalMapping

    RigidMapping

    SquareMapping

    CenterOfMassMultiMapping

    DevAngleCollisionMonitor

    DistanceMultiMapping

    CenterPointMechanicalMapping

    MeshSpringForceField

    AngularSpringForceField

    LineSetSkinningMapping

    BeamFEMForceField

    SimpleTesselatedHexaTopologicalMapping

    SquareDistanceMapping

    TubularMapping

    ProjectionToTargetLineMapping

    HexahedronCompositeFEMMapping

    ProjectionToLineMultiMapping

    Mesh2PointMechanicalMapping

    CompareTopology

    TOBBModel

    SpringForceField

    DevTensionMonitor

    ImplicitSurfaceMapping

    DistanceMapping

    DeformableOnRigidFrameMapping

    RigidRigidMapping

    TriangleBendingSprings

    QuadBendingSprings

    CenterOfMassMapping

    Mesh2PointTopologicalMapping

    SimpleTesselatedTetraTopologicalMapping

    BeamLinearMapping

    IdentityTopologicalMapping

    IdentityMultiMapping

    FrameSpringForceField

    SkeletalMotionConstraint

    Triangle2EdgeTopologicalMapping

    ProjectionToPlaneMultiMapping

    TCylinderModel

    PenalityContactForceField

    Tetra2TriangleTopologicalMapping

    UnilateralInteractionConstraint

    Distances

    RepulsiveSpringForceField

    ContactListener

    DistanceFromTargetMapping

    ExternalInterpolationMapping


    
Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""  
__all__=['SimpleTesselatedTetraMechanicalMapping', 'CenterPointTopologicalMapping', 'FixedTranslationConstraint', 'StopperConstraint', 'ProjectionToTargetPlaneMapping', 'SubsetTopologicalMapping', 'Edge2QuadTopologicalMapping', 'SlidingConstraint', 'RegularGridSpringForceField', 'CenterOfMassMulti2Mapping', 'PythonMainScriptController', 'BarycentricMapping', 'ArticulatedSystemMapping', 'Quad2TriangleTopologicalMapping', 'IdentityMapping', 'GearSpringForceField', 'LCPForceFeedback', 'CurveMapping', 'Hexa2QuadTopologicalMapping', 'FixedRotationConstraint', 'CatmullRomSplineMapping', 'JointSpringForceField', 'SubsetMultiMapping', 'SubsetMapping', 'SPHFluidSurfaceMapping', 'SkinningMapping', 'StiffSpringForceField', 'VectorSpringForceField', 'Hexa2TetraTopologicalMapping', 'RigidMapping', 'SquareMapping', 'CenterOfMassMultiMapping', 'DevAngleCollisionMonitor', 'DistanceMultiMapping', 'CenterPointMechanicalMapping', 'MeshSpringForceField', 'AngularSpringForceField', 'LineSetSkinningMapping', 'BeamFEMForceField', 'SimpleTesselatedHexaTopologicalMapping', 'SquareDistanceMapping', 'TubularMapping', 'ProjectionToTargetLineMapping', 'HexahedronCompositeFEMMapping', 'ProjectionToLineMultiMapping', 'Mesh2PointMechanicalMapping', 'CompareTopology', 'TOBBModel', 'SpringForceField', 'DevTensionMonitor', 'ImplicitSurfaceMapping', 'DistanceMapping', 'DeformableOnRigidFrameMapping', 'RigidRigidMapping', 'TriangleBendingSprings', 'QuadBendingSprings', 'CenterOfMassMapping', 'Mesh2PointTopologicalMapping', 'SimpleTesselatedTetraTopologicalMapping', 'BeamLinearMapping', 'IdentityTopologicalMapping', 'IdentityMultiMapping', 'FrameSpringForceField', 'SkeletalMotionConstraint', 'Triangle2EdgeTopologicalMapping', 'ProjectionToPlaneMultiMapping', 'TCylinderModel', 'PenalityContactForceField', 'Tetra2TriangleTopologicalMapping', 'UnilateralInteractionConstraint', 'Distances', 'RepulsiveSpringForceField', 'ContactListener', 'DistanceFromTargetMapping', 'ExternalInterpolationMapping']
import SimpleTesselatedTetraMechanicalMapping
import CenterPointTopologicalMapping
import FixedTranslationConstraint
import StopperConstraint
import ProjectionToTargetPlaneMapping
import SubsetTopologicalMapping
import Edge2QuadTopologicalMapping
import SlidingConstraint
import RegularGridSpringForceField
import CenterOfMassMulti2Mapping
import PythonMainScriptController
import BarycentricMapping
import ArticulatedSystemMapping
import Quad2TriangleTopologicalMapping
import IdentityMapping
import GearSpringForceField
import LCPForceFeedback
import CurveMapping
import Hexa2QuadTopologicalMapping
import FixedRotationConstraint
import CatmullRomSplineMapping
import JointSpringForceField
import SubsetMultiMapping
import SubsetMapping
import SPHFluidSurfaceMapping
import SkinningMapping
import StiffSpringForceField
import VectorSpringForceField
import Hexa2TetraTopologicalMapping
import RigidMapping
import SquareMapping
import CenterOfMassMultiMapping
import DevAngleCollisionMonitor
import DistanceMultiMapping
import CenterPointMechanicalMapping
import MeshSpringForceField
import AngularSpringForceField
import LineSetSkinningMapping
import BeamFEMForceField
import SimpleTesselatedHexaTopologicalMapping
import SquareDistanceMapping
import TubularMapping
import ProjectionToTargetLineMapping
import HexahedronCompositeFEMMapping
import ProjectionToLineMultiMapping
import Mesh2PointMechanicalMapping
import CompareTopology
import TOBBModel
import SpringForceField
import DevTensionMonitor
import ImplicitSurfaceMapping
import DistanceMapping
import DeformableOnRigidFrameMapping
import RigidRigidMapping
import TriangleBendingSprings
import QuadBendingSprings
import CenterOfMassMapping
import Mesh2PointTopologicalMapping
import SimpleTesselatedTetraTopologicalMapping
import BeamLinearMapping
import IdentityTopologicalMapping
import IdentityMultiMapping
import FrameSpringForceField
import SkeletalMotionConstraint
import Triangle2EdgeTopologicalMapping
import ProjectionToPlaneMultiMapping
import TCylinderModel
import PenalityContactForceField
import Tetra2TriangleTopologicalMapping
import UnilateralInteractionConstraint
import Distances
import RepulsiveSpringForceField
import ContactListener
import DistanceFromTargetMapping
import ExternalInterpolationMapping
