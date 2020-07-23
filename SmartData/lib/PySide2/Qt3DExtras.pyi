# This Python file uses the following encoding: utf-8
#############################################################################
##
## Copyright (C) 2019 The Qt Company Ltd.
## Contact: https://www.qt.io/licensing/
##
## This file is part of Qt for Python.
##
## $QT_BEGIN_LICENSE:LGPL$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https://www.qt.io/terms-conditions. For further
## information use the contact form at https://www.qt.io/contact-us.
##
## GNU Lesser General Public License Usage
## Alternatively, this file may be used under the terms of the GNU Lesser
## General Public License version 3 as published by the Free Software
## Foundation and appearing in the file LICENSE.LGPL3 included in the
## packaging of this file. Please review the following information to
## ensure the GNU Lesser General Public License version 3 requirements
## will be met: https://www.gnu.org/licenses/lgpl-3.0.html.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 2.0 or (at your option) the GNU General
## Public license version 3 or any later version approved by the KDE Free
## Qt Foundation. The licenses are as published by the Free Software
## Foundation and appearing in the file LICENSE.GPL2 and LICENSE.GPL3
## included in the packaging of this file. Please review the following
## information to ensure the GNU General Public License requirements will
## be met: https://www.gnu.org/licenses/gpl-2.0.html and
## https://www.gnu.org/licenses/gpl-3.0.html.
##
## $QT_END_LICENSE$
##
#############################################################################

"""
This file contains the exact signatures for all functions in module
PySide2.Qt3DExtras, except for defaults which are replaced by "...".
"""

# Module PySide2.Qt3DExtras
import PySide2
from PySide2.support.signature import typing
from PySide2.support.signature.mapping import (
    Virtual, Missing, Invalid, Default, Instance)

class Object(object): pass

import shiboken2 as Shiboken
Shiboken.Object = Object

import PySide2.QtCore
import PySide2.QtGui
import PySide2.Qt3DCore
import PySide2.Qt3DRender
import PySide2.Qt3DExtras


class Qt3DExtras(Shiboken.Object):


    class QAbstractCameraController(PySide2.Qt3DCore.Qt3DCore.QEntity):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def acceleration(self) -> float: ...
        def camera(self) -> PySide2.Qt3DRender.Qt3DRender.QCamera: ...
        def deceleration(self) -> float: ...
        def linearSpeed(self) -> float: ...
        def lookSpeed(self) -> float: ...
        def setAcceleration(self, acceleration:float): ...
        def setCamera(self, camera:PySide2.Qt3DRender.Qt3DRender.QCamera): ...
        def setDeceleration(self, deceleration:float): ...
        def setLinearSpeed(self, linearSpeed:float): ...
        def setLookSpeed(self, lookSpeed:float): ...

        class InputState(Shiboken.Object):

            @typing.overload
            def __init__(self): ...
            @typing.overload
            def __init__(self, InputState:PySide2.Qt3DExtras.Qt3DExtras.QAbstractCameraController.InputState): ...
            def __copy__(self): ...

    class QAbstractSpriteSheet(PySide2.Qt3DCore.Qt3DCore.QNode):

        def currentIndex(self) -> int: ...
        def setCurrentIndex(self, currentIndex:int): ...
        def setTexture(self, texture:PySide2.Qt3DRender.Qt3DRender.QAbstractTexture): ...
        def texture(self) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture: ...
        def textureTransform(self) -> PySide2.QtGui.QMatrix3x3: ...

    class QConeGeometry(PySide2.Qt3DRender.Qt3DRender.QGeometry):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def bottomRadius(self) -> float: ...
        def hasBottomEndcap(self) -> bool: ...
        def hasTopEndcap(self) -> bool: ...
        def indexAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def length(self) -> float: ...
        def normalAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def positionAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def rings(self) -> int: ...
        def setBottomRadius(self, bottomRadius:float): ...
        def setHasBottomEndcap(self, hasBottomEndcap:bool): ...
        def setHasTopEndcap(self, hasTopEndcap:bool): ...
        def setLength(self, length:float): ...
        def setRings(self, rings:int): ...
        def setSlices(self, slices:int): ...
        def setTopRadius(self, topRadius:float): ...
        def slices(self) -> int: ...
        def texCoordAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def topRadius(self) -> float: ...
        def updateIndices(self): ...
        def updateVertices(self): ...

    class QConeMesh(PySide2.Qt3DRender.Qt3DRender.QGeometryRenderer):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def bottomRadius(self) -> float: ...
        def hasBottomEndcap(self) -> bool: ...
        def hasTopEndcap(self) -> bool: ...
        def length(self) -> float: ...
        def rings(self) -> int: ...
        def setBottomRadius(self, bottomRadius:float): ...
        def setFirstInstance(self, firstInstance:int): ...
        def setGeometry(self, geometry:PySide2.Qt3DRender.Qt3DRender.QGeometry): ...
        def setHasBottomEndcap(self, hasBottomEndcap:bool): ...
        def setHasTopEndcap(self, hasTopEndcap:bool): ...
        def setIndexOffset(self, indexOffset:int): ...
        def setInstanceCount(self, instanceCount:int): ...
        def setLength(self, length:float): ...
        def setPrimitiveRestartEnabled(self, enabled:bool): ...
        def setPrimitiveType(self, primitiveType:PySide2.Qt3DRender.Qt3DRender.QGeometryRenderer.PrimitiveType): ...
        def setRestartIndexValue(self, index:int): ...
        def setRings(self, rings:int): ...
        def setSlices(self, slices:int): ...
        def setTopRadius(self, topRadius:float): ...
        def setVertexCount(self, vertexCount:int): ...
        def slices(self) -> int: ...
        def topRadius(self) -> float: ...

    class QCuboidGeometry(PySide2.Qt3DRender.Qt3DRender.QGeometry):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def indexAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def normalAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def positionAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def setXExtent(self, xExtent:float): ...
        def setXYMeshResolution(self, resolution:PySide2.QtCore.QSize): ...
        def setXZMeshResolution(self, resolution:PySide2.QtCore.QSize): ...
        def setYExtent(self, yExtent:float): ...
        def setYZMeshResolution(self, resolution:PySide2.QtCore.QSize): ...
        def setZExtent(self, zExtent:float): ...
        def tangentAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def texCoordAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def updateIndices(self): ...
        def updateVertices(self): ...
        def xExtent(self) -> float: ...
        def xyMeshResolution(self) -> PySide2.QtCore.QSize: ...
        def xzMeshResolution(self) -> PySide2.QtCore.QSize: ...
        def yExtent(self) -> float: ...
        def yzMeshResolution(self) -> PySide2.QtCore.QSize: ...
        def zExtent(self) -> float: ...

    class QCuboidMesh(PySide2.Qt3DRender.Qt3DRender.QGeometryRenderer):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def setFirstInstance(self, firstInstance:int): ...
        def setGeometry(self, geometry:PySide2.Qt3DRender.Qt3DRender.QGeometry): ...
        def setIndexOffset(self, indexOffset:int): ...
        def setInstanceCount(self, instanceCount:int): ...
        def setPrimitiveRestartEnabled(self, enabled:bool): ...
        def setPrimitiveType(self, primitiveType:PySide2.Qt3DRender.Qt3DRender.QGeometryRenderer.PrimitiveType): ...
        def setRestartIndexValue(self, index:int): ...
        def setVertexCount(self, vertexCount:int): ...
        def setXExtent(self, xExtent:float): ...
        def setXYMeshResolution(self, resolution:PySide2.QtCore.QSize): ...
        def setXZMeshResolution(self, resolution:PySide2.QtCore.QSize): ...
        def setYExtent(self, yExtent:float): ...
        def setYZMeshResolution(self, resolution:PySide2.QtCore.QSize): ...
        def setZExtent(self, zExtent:float): ...
        def xExtent(self) -> float: ...
        def xyMeshResolution(self) -> PySide2.QtCore.QSize: ...
        def xzMeshResolution(self) -> PySide2.QtCore.QSize: ...
        def yExtent(self) -> float: ...
        def yzMeshResolution(self) -> PySide2.QtCore.QSize: ...
        def zExtent(self) -> float: ...

    class QCylinderGeometry(PySide2.Qt3DRender.Qt3DRender.QGeometry):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def indexAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def length(self) -> float: ...
        def normalAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def positionAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def radius(self) -> float: ...
        def rings(self) -> int: ...
        def setLength(self, length:float): ...
        def setRadius(self, radius:float): ...
        def setRings(self, rings:int): ...
        def setSlices(self, slices:int): ...
        def slices(self) -> int: ...
        def texCoordAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def updateIndices(self): ...
        def updateVertices(self): ...

    class QCylinderMesh(PySide2.Qt3DRender.Qt3DRender.QGeometryRenderer):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def length(self) -> float: ...
        def radius(self) -> float: ...
        def rings(self) -> int: ...
        def setFirstInstance(self, firstInstance:int): ...
        def setGeometry(self, geometry:PySide2.Qt3DRender.Qt3DRender.QGeometry): ...
        def setIndexOffset(self, indexOffset:int): ...
        def setInstanceCount(self, instanceCount:int): ...
        def setLength(self, length:float): ...
        def setPrimitiveRestartEnabled(self, enabled:bool): ...
        def setPrimitiveType(self, primitiveType:PySide2.Qt3DRender.Qt3DRender.QGeometryRenderer.PrimitiveType): ...
        def setRadius(self, radius:float): ...
        def setRestartIndexValue(self, index:int): ...
        def setRings(self, rings:int): ...
        def setSlices(self, slices:int): ...
        def setVertexCount(self, vertexCount:int): ...
        def slices(self) -> int: ...

    class QDiffuseMapMaterial(PySide2.Qt3DRender.Qt3DRender.QMaterial):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def ambient(self) -> PySide2.QtGui.QColor: ...
        def diffuse(self) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture: ...
        def setAmbient(self, color:PySide2.QtGui.QColor): ...
        def setDiffuse(self, diffuse:PySide2.Qt3DRender.Qt3DRender.QAbstractTexture): ...
        def setShininess(self, shininess:float): ...
        def setSpecular(self, specular:PySide2.QtGui.QColor): ...
        def setTextureScale(self, textureScale:float): ...
        def shininess(self) -> float: ...
        def specular(self) -> PySide2.QtGui.QColor: ...
        def textureScale(self) -> float: ...

    class QDiffuseSpecularMapMaterial(PySide2.Qt3DRender.Qt3DRender.QMaterial):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def ambient(self) -> PySide2.QtGui.QColor: ...
        def diffuse(self) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture: ...
        def setAmbient(self, ambient:PySide2.QtGui.QColor): ...
        def setDiffuse(self, diffuse:PySide2.Qt3DRender.Qt3DRender.QAbstractTexture): ...
        def setShininess(self, shininess:float): ...
        def setSpecular(self, specular:PySide2.Qt3DRender.Qt3DRender.QAbstractTexture): ...
        def setTextureScale(self, textureScale:float): ...
        def shininess(self) -> float: ...
        def specular(self) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture: ...
        def textureScale(self) -> float: ...

    class QDiffuseSpecularMaterial(PySide2.Qt3DRender.Qt3DRender.QMaterial):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def ambient(self) -> PySide2.QtGui.QColor: ...
        def diffuse(self) -> typing.Any: ...
        def isAlphaBlendingEnabled(self) -> bool: ...
        def normal(self) -> typing.Any: ...
        def setAlphaBlendingEnabled(self, enabled:bool): ...
        def setAmbient(self, ambient:PySide2.QtGui.QColor): ...
        def setDiffuse(self, diffuse:typing.Any): ...
        def setNormal(self, normal:typing.Any): ...
        def setShininess(self, shininess:float): ...
        def setSpecular(self, specular:typing.Any): ...
        def setTextureScale(self, textureScale:float): ...
        def shininess(self) -> float: ...
        def specular(self) -> typing.Any: ...
        def textureScale(self) -> float: ...

    class QExtrudedTextGeometry(PySide2.Qt3DRender.Qt3DRender.QGeometry):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def extrusionLength(self) -> float: ...
        def font(self) -> PySide2.QtGui.QFont: ...
        def indexAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def normalAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def positionAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def setDepth(self, extrusionLength:float): ...
        def setFont(self, font:PySide2.QtGui.QFont): ...
        def setText(self, text:str): ...
        def text(self) -> str: ...

    class QExtrudedTextMesh(PySide2.Qt3DRender.Qt3DRender.QGeometryRenderer):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def depth(self) -> float: ...
        def font(self) -> PySide2.QtGui.QFont: ...
        def setDepth(self, depth:float): ...
        def setFont(self, font:PySide2.QtGui.QFont): ...
        def setText(self, text:str): ...
        def text(self) -> str: ...

    class QFirstPersonCameraController(PySide2.Qt3DExtras.Qt3DExtras.QAbstractCameraController):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...

    class QForwardRenderer(PySide2.Qt3DRender.Qt3DRender.QTechniqueFilter):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def camera(self) -> PySide2.Qt3DCore.Qt3DCore.QEntity: ...
        def clearColor(self) -> PySide2.QtGui.QColor: ...
        def externalRenderTargetSize(self) -> PySide2.QtCore.QSize: ...
        def gamma(self) -> float: ...
        def isFrustumCullingEnabled(self) -> bool: ...
        def setCamera(self, camera:PySide2.Qt3DCore.Qt3DCore.QEntity): ...
        def setClearColor(self, clearColor:PySide2.QtGui.QColor): ...
        def setExternalRenderTargetSize(self, size:PySide2.QtCore.QSize): ...
        def setFrustumCullingEnabled(self, enabled:bool): ...
        def setGamma(self, gamma:float): ...
        def setSurface(self, surface:PySide2.QtCore.QObject): ...
        def setViewportRect(self, viewportRect:PySide2.QtCore.QRectF): ...
        def surface(self) -> PySide2.QtCore.QObject: ...
        def viewportRect(self) -> PySide2.QtCore.QRectF: ...

    class QGoochMaterial(PySide2.Qt3DRender.Qt3DRender.QMaterial):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def alpha(self) -> float: ...
        def beta(self) -> float: ...
        def cool(self) -> PySide2.QtGui.QColor: ...
        def diffuse(self) -> PySide2.QtGui.QColor: ...
        def setAlpha(self, alpha:float): ...
        def setBeta(self, beta:float): ...
        def setCool(self, cool:PySide2.QtGui.QColor): ...
        def setDiffuse(self, diffuse:PySide2.QtGui.QColor): ...
        def setShininess(self, shininess:float): ...
        def setSpecular(self, specular:PySide2.QtGui.QColor): ...
        def setWarm(self, warm:PySide2.QtGui.QColor): ...
        def shininess(self) -> float: ...
        def specular(self) -> PySide2.QtGui.QColor: ...
        def warm(self) -> PySide2.QtGui.QColor: ...

    class QMetalRoughMaterial(PySide2.Qt3DRender.Qt3DRender.QMaterial):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def ambientOcclusion(self) -> typing.Any: ...
        def baseColor(self) -> typing.Any: ...
        def metalness(self) -> typing.Any: ...
        def normal(self) -> typing.Any: ...
        def roughness(self) -> typing.Any: ...
        def setAmbientOcclusion(self, ambientOcclusion:typing.Any): ...
        def setBaseColor(self, baseColor:typing.Any): ...
        def setMetalness(self, metalness:typing.Any): ...
        def setNormal(self, normal:typing.Any): ...
        def setRoughness(self, roughness:typing.Any): ...
        def setTextureScale(self, textureScale:float): ...
        def textureScale(self) -> float: ...

    class QMorphPhongMaterial(PySide2.Qt3DRender.Qt3DRender.QMaterial):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def ambient(self) -> PySide2.QtGui.QColor: ...
        def diffuse(self) -> PySide2.QtGui.QColor: ...
        def interpolator(self) -> float: ...
        def setAmbient(self, ambient:PySide2.QtGui.QColor): ...
        def setDiffuse(self, diffuse:PySide2.QtGui.QColor): ...
        def setInterpolator(self, interpolator:float): ...
        def setShininess(self, shininess:float): ...
        def setSpecular(self, specular:PySide2.QtGui.QColor): ...
        def shininess(self) -> float: ...
        def specular(self) -> PySide2.QtGui.QColor: ...

    class QNormalDiffuseMapMaterial(PySide2.Qt3DRender.Qt3DRender.QMaterial):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def ambient(self) -> PySide2.QtGui.QColor: ...
        def diffuse(self) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture: ...
        def normal(self) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture: ...
        def setAmbient(self, ambient:PySide2.QtGui.QColor): ...
        def setDiffuse(self, diffuse:PySide2.Qt3DRender.Qt3DRender.QAbstractTexture): ...
        def setNormal(self, normal:PySide2.Qt3DRender.Qt3DRender.QAbstractTexture): ...
        def setShininess(self, shininess:float): ...
        def setSpecular(self, specular:PySide2.QtGui.QColor): ...
        def setTextureScale(self, textureScale:float): ...
        def shininess(self) -> float: ...
        def specular(self) -> PySide2.QtGui.QColor: ...
        def textureScale(self) -> float: ...

    class QNormalDiffuseSpecularMapMaterial(PySide2.Qt3DRender.Qt3DRender.QMaterial):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def ambient(self) -> PySide2.QtGui.QColor: ...
        def diffuse(self) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture: ...
        def normal(self) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture: ...
        def setAmbient(self, ambient:PySide2.QtGui.QColor): ...
        def setDiffuse(self, diffuse:PySide2.Qt3DRender.Qt3DRender.QAbstractTexture): ...
        def setNormal(self, normal:PySide2.Qt3DRender.Qt3DRender.QAbstractTexture): ...
        def setShininess(self, shininess:float): ...
        def setSpecular(self, specular:PySide2.Qt3DRender.Qt3DRender.QAbstractTexture): ...
        def setTextureScale(self, textureScale:float): ...
        def shininess(self) -> float: ...
        def specular(self) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture: ...
        def textureScale(self) -> float: ...

    class QOrbitCameraController(PySide2.Qt3DExtras.Qt3DExtras.QAbstractCameraController):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def setZoomInLimit(self, zoomInLimit:float): ...
        def zoomInLimit(self) -> float: ...

    class QPerVertexColorMaterial(PySide2.Qt3DRender.Qt3DRender.QMaterial):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...

    class QPhongAlphaMaterial(PySide2.Qt3DRender.Qt3DRender.QMaterial):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def alpha(self) -> float: ...
        def ambient(self) -> PySide2.QtGui.QColor: ...
        def blendFunctionArg(self) -> PySide2.Qt3DRender.Qt3DRender.QBlendEquation.BlendFunction: ...
        def destinationAlphaArg(self) -> PySide2.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending: ...
        def destinationRgbArg(self) -> PySide2.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending: ...
        def diffuse(self) -> PySide2.QtGui.QColor: ...
        def setAlpha(self, alpha:float): ...
        def setAmbient(self, ambient:PySide2.QtGui.QColor): ...
        def setBlendFunctionArg(self, blendFunctionArg:PySide2.Qt3DRender.Qt3DRender.QBlendEquation.BlendFunction): ...
        def setDestinationAlphaArg(self, destinationAlphaArg:PySide2.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending): ...
        def setDestinationRgbArg(self, destinationRgbArg:PySide2.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending): ...
        def setDiffuse(self, diffuse:PySide2.QtGui.QColor): ...
        def setShininess(self, shininess:float): ...
        def setSourceAlphaArg(self, sourceAlphaArg:PySide2.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending): ...
        def setSourceRgbArg(self, sourceRgbArg:PySide2.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending): ...
        def setSpecular(self, specular:PySide2.QtGui.QColor): ...
        def shininess(self) -> float: ...
        def sourceAlphaArg(self) -> PySide2.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending: ...
        def sourceRgbArg(self) -> PySide2.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending: ...
        def specular(self) -> PySide2.QtGui.QColor: ...

    class QPhongMaterial(PySide2.Qt3DRender.Qt3DRender.QMaterial):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def ambient(self) -> PySide2.QtGui.QColor: ...
        def diffuse(self) -> PySide2.QtGui.QColor: ...
        def setAmbient(self, ambient:PySide2.QtGui.QColor): ...
        def setDiffuse(self, diffuse:PySide2.QtGui.QColor): ...
        def setShininess(self, shininess:float): ...
        def setSpecular(self, specular:PySide2.QtGui.QColor): ...
        def shininess(self) -> float: ...
        def specular(self) -> PySide2.QtGui.QColor: ...

    class QPlaneGeometry(PySide2.Qt3DRender.Qt3DRender.QGeometry):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def height(self) -> float: ...
        def indexAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def mirrored(self) -> bool: ...
        def normalAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def positionAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def resolution(self) -> PySide2.QtCore.QSize: ...
        def setHeight(self, height:float): ...
        def setMirrored(self, mirrored:bool): ...
        def setResolution(self, resolution:PySide2.QtCore.QSize): ...
        def setWidth(self, width:float): ...
        def tangentAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def texCoordAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def updateIndices(self): ...
        def updateVertices(self): ...
        def width(self) -> float: ...

    class QPlaneMesh(PySide2.Qt3DRender.Qt3DRender.QGeometryRenderer):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def height(self) -> float: ...
        def meshResolution(self) -> PySide2.QtCore.QSize: ...
        def mirrored(self) -> bool: ...
        def setFirstInstance(self, firstInstance:int): ...
        def setGeometry(self, geometry:PySide2.Qt3DRender.Qt3DRender.QGeometry): ...
        def setHeight(self, height:float): ...
        def setIndexOffset(self, indexOffset:int): ...
        def setInstanceCount(self, instanceCount:int): ...
        def setMeshResolution(self, resolution:PySide2.QtCore.QSize): ...
        def setMirrored(self, mirrored:bool): ...
        def setPrimitiveRestartEnabled(self, enabled:bool): ...
        def setPrimitiveType(self, primitiveType:PySide2.Qt3DRender.Qt3DRender.QGeometryRenderer.PrimitiveType): ...
        def setRestartIndexValue(self, index:int): ...
        def setVertexCount(self, vertexCount:int): ...
        def setWidth(self, width:float): ...
        def width(self) -> float: ...

    class QSkyboxEntity(PySide2.Qt3DCore.Qt3DCore.QEntity):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def baseName(self) -> str: ...
        def extension(self) -> str: ...
        def isGammaCorrectEnabled(self) -> bool: ...
        def setBaseName(self, path:str): ...
        def setExtension(self, extension:str): ...
        def setGammaCorrectEnabled(self, enabled:bool): ...

    class QSphereGeometry(PySide2.Qt3DRender.Qt3DRender.QGeometry):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def generateTangents(self) -> bool: ...
        def indexAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def normalAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def positionAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def radius(self) -> float: ...
        def rings(self) -> int: ...
        def setGenerateTangents(self, gen:bool): ...
        def setRadius(self, radius:float): ...
        def setRings(self, rings:int): ...
        def setSlices(self, slices:int): ...
        def slices(self) -> int: ...
        def tangentAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def texCoordAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def updateIndices(self): ...
        def updateVertices(self): ...

    class QSphereMesh(PySide2.Qt3DRender.Qt3DRender.QGeometryRenderer):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def generateTangents(self) -> bool: ...
        def radius(self) -> float: ...
        def rings(self) -> int: ...
        def setFirstInstance(self, firstInstance:int): ...
        def setGenerateTangents(self, gen:bool): ...
        def setGeometry(self, geometry:PySide2.Qt3DRender.Qt3DRender.QGeometry): ...
        def setIndexOffset(self, indexOffset:int): ...
        def setPrimitiveRestartEnabled(self, enabled:bool): ...
        def setPrimitiveType(self, primitiveType:PySide2.Qt3DRender.Qt3DRender.QGeometryRenderer.PrimitiveType): ...
        def setRadius(self, radius:float): ...
        def setRestartIndexValue(self, index:int): ...
        def setRings(self, rings:int): ...
        def setSlices(self, slices:int): ...
        def setVertexCount(self, vertexCount:int): ...
        def slices(self) -> int: ...

    class QSpriteGrid(PySide2.Qt3DExtras.Qt3DExtras.QAbstractSpriteSheet):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def columns(self) -> int: ...
        def rows(self) -> int: ...
        def setColumns(self, columns:int): ...
        def setRows(self, rows:int): ...

    class QSpriteSheet(PySide2.Qt3DExtras.Qt3DExtras.QAbstractSpriteSheet):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        @typing.overload
        def addSprite(self, sprite:PySide2.Qt3DExtras.Qt3DExtras.QSpriteSheetItem): ...
        @typing.overload
        def addSprite(self, x:int, y:int, width:int, height:int) -> PySide2.Qt3DExtras.Qt3DExtras.QSpriteSheetItem: ...
        def removeSprite(self, sprite:PySide2.Qt3DExtras.Qt3DExtras.QSpriteSheetItem): ...
        def setSprites(self, sprites:typing.List): ...
        def sprites(self) -> typing.List: ...

    class QSpriteSheetItem(PySide2.Qt3DCore.Qt3DCore.QNode):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def height(self) -> int: ...
        def setHeight(self, height:int): ...
        def setWidth(self, width:int): ...
        def setX(self, x:int): ...
        def setY(self, y:int): ...
        def width(self) -> int: ...
        def x(self) -> int: ...
        def y(self) -> int: ...

    class QText2DEntity(PySide2.Qt3DCore.Qt3DCore.QEntity):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def color(self) -> PySide2.QtGui.QColor: ...
        def font(self) -> PySide2.QtGui.QFont: ...
        def height(self) -> float: ...
        def setColor(self, color:PySide2.QtGui.QColor): ...
        def setFont(self, font:PySide2.QtGui.QFont): ...
        def setHeight(self, height:float): ...
        def setText(self, text:str): ...
        def setWidth(self, width:float): ...
        def text(self) -> str: ...
        def width(self) -> float: ...

    class QTextureMaterial(PySide2.Qt3DRender.Qt3DRender.QMaterial):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def isAlphaBlendingEnabled(self) -> bool: ...
        def setAlphaBlendingEnabled(self, enabled:bool): ...
        def setTexture(self, texture:PySide2.Qt3DRender.Qt3DRender.QAbstractTexture): ...
        def setTextureOffset(self, textureOffset:PySide2.QtGui.QVector2D): ...
        def setTextureTransform(self, matrix:PySide2.QtGui.QMatrix3x3): ...
        def texture(self) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture: ...
        def textureOffset(self) -> PySide2.QtGui.QVector2D: ...
        def textureTransform(self) -> PySide2.QtGui.QMatrix3x3: ...

    class QTorusGeometry(PySide2.Qt3DRender.Qt3DRender.QGeometry):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def indexAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def minorRadius(self) -> float: ...
        def normalAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def positionAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def radius(self) -> float: ...
        def rings(self) -> int: ...
        def setMinorRadius(self, minorRadius:float): ...
        def setRadius(self, radius:float): ...
        def setRings(self, rings:int): ...
        def setSlices(self, slices:int): ...
        def slices(self) -> int: ...
        def texCoordAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def updateIndices(self): ...
        def updateVertices(self): ...

    class QTorusMesh(PySide2.Qt3DRender.Qt3DRender.QGeometryRenderer):

        def __init__(self, parent:PySide2.Qt3DCore.Qt3DCore.QNode=...): ...
        def minorRadius(self) -> float: ...
        def radius(self) -> float: ...
        def rings(self) -> int: ...
        def setFirstInstance(self, firstInstance:int): ...
        def setGeometry(self, geometry:PySide2.Qt3DRender.Qt3DRender.QGeometry): ...
        def setIndexOffset(self, indexOffset:int): ...
        def setInstanceCount(self, instanceCount:int): ...
        def setMinorRadius(self, minorRadius:float): ...
        def setPrimitiveRestartEnabled(self, enabled:bool): ...
        def setPrimitiveType(self, primitiveType:PySide2.Qt3DRender.Qt3DRender.QGeometryRenderer.PrimitiveType): ...
        def setRadius(self, radius:float): ...
        def setRestartIndexValue(self, index:int): ...
        def setRings(self, rings:int): ...
        def setSlices(self, slices:int): ...
        def setVertexCount(self, vertexCount:int): ...
        def slices(self) -> int: ...

    class Qt3DWindow(PySide2.QtGui.QWindow):

        def __init__(self, screen:PySide2.QtGui.QScreen=...): ...
        def activeFrameGraph(self) -> PySide2.Qt3DRender.Qt3DRender.QFrameGraphNode: ...
        def camera(self) -> PySide2.Qt3DRender.Qt3DRender.QCamera: ...
        def defaultFrameGraph(self) -> PySide2.Qt3DExtras.Qt3DExtras.QForwardRenderer: ...
        def event(self, e:PySide2.QtCore.QEvent) -> bool: ...
        @typing.overload
        def registerAspect(self, aspect:PySide2.Qt3DCore.Qt3DCore.QAbstractAspect): ...
        @typing.overload
        def registerAspect(self, name:str): ...
        def renderSettings(self) -> PySide2.Qt3DRender.Qt3DRender.QRenderSettings: ...
        def resizeEvent(self, arg__1:PySide2.QtGui.QResizeEvent): ...
        def setActiveFrameGraph(self, activeFrameGraph:PySide2.Qt3DRender.Qt3DRender.QFrameGraphNode): ...
        def setRootEntity(self, root:PySide2.Qt3DCore.Qt3DCore.QEntity): ...
        def showEvent(self, e:PySide2.QtGui.QShowEvent): ...

# eof
