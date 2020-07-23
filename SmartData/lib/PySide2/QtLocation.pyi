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
PySide2.QtLocation, except for defaults which are replaced by "...".
"""

# Module PySide2.QtLocation
import PySide2
from PySide2.support.signature import typing
from PySide2.support.signature.mapping import (
    Virtual, Missing, Invalid, Default, Instance)

class Object(object): pass

import shiboken2 as Shiboken
Shiboken.Object = Object

import PySide2.QtCore
import PySide2.QtPositioning
import PySide2.QtLocation


class QGeoCodeReply(PySide2.QtCore.QObject):

    @typing.overload
    def __init__(self, error:PySide2.QtLocation.QGeoCodeReply.Error, errorString:str, parent:PySide2.QtCore.QObject=...): ...
    @typing.overload
    def __init__(self, parent:PySide2.QtCore.QObject=...): ...
    def abort(self): ...
    def addLocation(self, location:PySide2.QtPositioning.QGeoLocation): ...
    def error(self) -> PySide2.QtLocation.QGeoCodeReply.Error: ...
    def errorString(self) -> str: ...
    def isFinished(self) -> bool: ...
    def limit(self) -> int: ...
    def locations(self) -> typing.List: ...
    def offset(self) -> int: ...
    def setError(self, error:PySide2.QtLocation.QGeoCodeReply.Error, errorString:str): ...
    def setFinished(self, finished:bool): ...
    def setLimit(self, limit:int): ...
    def setLocations(self, locations:typing.List): ...
    def setOffset(self, offset:int): ...
    def setViewport(self, viewport:PySide2.QtPositioning.QGeoShape): ...
    def viewport(self) -> PySide2.QtPositioning.QGeoShape: ...


class QGeoCodingManager(PySide2.QtCore.QObject):

    @typing.overload
    def geocode(self, address:PySide2.QtPositioning.QGeoAddress, bounds:PySide2.QtPositioning.QGeoShape=...) -> PySide2.QtLocation.QGeoCodeReply: ...
    @typing.overload
    def geocode(self, searchString:str, limit:int=..., offset:int=..., bounds:PySide2.QtPositioning.QGeoShape=...) -> PySide2.QtLocation.QGeoCodeReply: ...
    def locale(self) -> PySide2.QtCore.QLocale: ...
    def managerName(self) -> str: ...
    def managerVersion(self) -> int: ...
    def reverseGeocode(self, coordinate:PySide2.QtPositioning.QGeoCoordinate, bounds:PySide2.QtPositioning.QGeoShape=...) -> PySide2.QtLocation.QGeoCodeReply: ...
    def setLocale(self, locale:PySide2.QtCore.QLocale): ...


class QGeoCodingManagerEngine(PySide2.QtCore.QObject):

    def __init__(self, parameters:typing.Dict, parent:PySide2.QtCore.QObject=...): ...
    @typing.overload
    def geocode(self, address:PySide2.QtPositioning.QGeoAddress, bounds:PySide2.QtPositioning.QGeoShape) -> PySide2.QtLocation.QGeoCodeReply: ...
    @typing.overload
    def geocode(self, address:str, limit:int, offset:int, bounds:PySide2.QtPositioning.QGeoShape) -> PySide2.QtLocation.QGeoCodeReply: ...
    def locale(self) -> PySide2.QtCore.QLocale: ...
    def managerName(self) -> str: ...
    def managerVersion(self) -> int: ...
    def reverseGeocode(self, coordinate:PySide2.QtPositioning.QGeoCoordinate, bounds:PySide2.QtPositioning.QGeoShape) -> PySide2.QtLocation.QGeoCodeReply: ...
    def setLocale(self, locale:PySide2.QtCore.QLocale): ...


class QGeoManeuver(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtLocation.QGeoManeuver): ...
    def __copy__(self): ...
    def direction(self) -> PySide2.QtLocation.QGeoManeuver.InstructionDirection: ...
    def distanceToNextInstruction(self) -> float: ...
    def extendedAttributes(self) -> typing.Dict: ...
    def instructionText(self) -> str: ...
    def isValid(self) -> bool: ...
    def position(self) -> PySide2.QtPositioning.QGeoCoordinate: ...
    def setDirection(self, direction:PySide2.QtLocation.QGeoManeuver.InstructionDirection): ...
    def setDistanceToNextInstruction(self, distance:float): ...
    def setExtendedAttributes(self, extendedAttributes:typing.Dict): ...
    def setInstructionText(self, instructionText:str): ...
    def setPosition(self, position:PySide2.QtPositioning.QGeoCoordinate): ...
    def setTimeToNextInstruction(self, secs:int): ...
    def setWaypoint(self, coordinate:PySide2.QtPositioning.QGeoCoordinate): ...
    def timeToNextInstruction(self) -> int: ...
    def waypoint(self) -> PySide2.QtPositioning.QGeoCoordinate: ...


class QGeoRoute(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtLocation.QGeoRoute): ...
    def __copy__(self): ...
    def bounds(self) -> PySide2.QtPositioning.QGeoRectangle: ...
    def distance(self) -> float: ...
    def extendedAttributes(self) -> typing.Dict: ...
    def firstRouteSegment(self) -> PySide2.QtLocation.QGeoRouteSegment: ...
    def path(self) -> typing.List: ...
    def request(self) -> PySide2.QtLocation.QGeoRouteRequest: ...
    def routeId(self) -> str: ...
    def setBounds(self, bounds:PySide2.QtPositioning.QGeoRectangle): ...
    def setDistance(self, distance:float): ...
    def setExtendedAttributes(self, extendedAttributes:typing.Dict): ...
    def setFirstRouteSegment(self, routeSegment:PySide2.QtLocation.QGeoRouteSegment): ...
    def setPath(self, path:typing.List): ...
    def setRequest(self, request:PySide2.QtLocation.QGeoRouteRequest): ...
    def setRouteId(self, id:str): ...
    def setTravelMode(self, mode:PySide2.QtLocation.QGeoRouteRequest.TravelMode): ...
    def setTravelTime(self, secs:int): ...
    def travelMode(self) -> PySide2.QtLocation.QGeoRouteRequest.TravelMode: ...
    def travelTime(self) -> int: ...


class QGeoRouteReply(PySide2.QtCore.QObject):

    @typing.overload
    def __init__(self, error:PySide2.QtLocation.QGeoRouteReply.Error, errorString:str, parent:PySide2.QtCore.QObject=...): ...
    @typing.overload
    def __init__(self, request:PySide2.QtLocation.QGeoRouteRequest, parent:PySide2.QtCore.QObject=...): ...
    def abort(self): ...
    def addRoutes(self, routes:typing.List): ...
    def error(self) -> PySide2.QtLocation.QGeoRouteReply.Error: ...
    def errorString(self) -> str: ...
    def isFinished(self) -> bool: ...
    def request(self) -> PySide2.QtLocation.QGeoRouteRequest: ...
    def routes(self) -> typing.List: ...
    def setError(self, error:PySide2.QtLocation.QGeoRouteReply.Error, errorString:str): ...
    def setFinished(self, finished:bool): ...
    def setRoutes(self, routes:typing.List): ...


class QGeoRouteRequest(Shiboken.Object):

    @typing.overload
    def __init__(self, origin:PySide2.QtPositioning.QGeoCoordinate, destination:PySide2.QtPositioning.QGeoCoordinate): ...
    @typing.overload
    def __init__(self, other:PySide2.QtLocation.QGeoRouteRequest): ...
    @typing.overload
    def __init__(self, waypoints:typing.List=...): ...
    def departureTime(self) -> PySide2.QtCore.QDateTime: ...
    def excludeAreas(self) -> typing.List: ...
    def extraParameters(self) -> typing.Dict: ...
    def featureTypes(self) -> typing.List: ...
    def featureWeight(self, featureType:PySide2.QtLocation.QGeoRouteRequest.FeatureType) -> PySide2.QtLocation.QGeoRouteRequest.FeatureWeight: ...
    def maneuverDetail(self) -> PySide2.QtLocation.QGeoRouteRequest.ManeuverDetail: ...
    def numberAlternativeRoutes(self) -> int: ...
    def routeOptimization(self) -> PySide2.QtLocation.QGeoRouteRequest.RouteOptimizations: ...
    def segmentDetail(self) -> PySide2.QtLocation.QGeoRouteRequest.SegmentDetail: ...
    def setDepartureTime(self, departureTime:PySide2.QtCore.QDateTime): ...
    def setExcludeAreas(self, areas:typing.List): ...
    def setExtraParameters(self, extraParameters:typing.Dict): ...
    def setFeatureWeight(self, featureType:PySide2.QtLocation.QGeoRouteRequest.FeatureType, featureWeight:PySide2.QtLocation.QGeoRouteRequest.FeatureWeight): ...
    def setManeuverDetail(self, maneuverDetail:PySide2.QtLocation.QGeoRouteRequest.ManeuverDetail): ...
    def setNumberAlternativeRoutes(self, alternatives:int): ...
    def setRouteOptimization(self, optimization:PySide2.QtLocation.QGeoRouteRequest.RouteOptimizations): ...
    def setSegmentDetail(self, segmentDetail:PySide2.QtLocation.QGeoRouteRequest.SegmentDetail): ...
    def setTravelModes(self, travelModes:PySide2.QtLocation.QGeoRouteRequest.TravelModes): ...
    def setWaypoints(self, waypoints:typing.List): ...
    def setWaypointsMetadata(self, waypointMetadata:typing.List): ...
    def travelModes(self) -> PySide2.QtLocation.QGeoRouteRequest.TravelModes: ...
    def waypoints(self) -> typing.List: ...
    def waypointsMetadata(self) -> typing.List: ...


class QGeoRouteSegment(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtLocation.QGeoRouteSegment): ...
    def __copy__(self): ...
    def distance(self) -> float: ...
    def isLegLastSegment(self) -> bool: ...
    def isValid(self) -> bool: ...
    def maneuver(self) -> PySide2.QtLocation.QGeoManeuver: ...
    def nextRouteSegment(self) -> PySide2.QtLocation.QGeoRouteSegment: ...
    def path(self) -> typing.List: ...
    def setDistance(self, distance:float): ...
    def setManeuver(self, maneuver:PySide2.QtLocation.QGeoManeuver): ...
    def setNextRouteSegment(self, routeSegment:PySide2.QtLocation.QGeoRouteSegment): ...
    def setPath(self, path:typing.List): ...
    def setTravelTime(self, secs:int): ...
    def travelTime(self) -> int: ...


class QGeoRoutingManager(PySide2.QtCore.QObject):

    def calculateRoute(self, request:PySide2.QtLocation.QGeoRouteRequest) -> PySide2.QtLocation.QGeoRouteReply: ...
    def locale(self) -> PySide2.QtCore.QLocale: ...
    def managerName(self) -> str: ...
    def managerVersion(self) -> int: ...
    def measurementSystem(self) -> PySide2.QtCore.QLocale.MeasurementSystem: ...
    def setLocale(self, locale:PySide2.QtCore.QLocale): ...
    def setMeasurementSystem(self, system:PySide2.QtCore.QLocale.MeasurementSystem): ...
    def supportedFeatureTypes(self) -> PySide2.QtLocation.QGeoRouteRequest.FeatureTypes: ...
    def supportedFeatureWeights(self) -> PySide2.QtLocation.QGeoRouteRequest.FeatureWeights: ...
    def supportedManeuverDetails(self) -> PySide2.QtLocation.QGeoRouteRequest.ManeuverDetails: ...
    def supportedRouteOptimizations(self) -> PySide2.QtLocation.QGeoRouteRequest.RouteOptimizations: ...
    def supportedSegmentDetails(self) -> PySide2.QtLocation.QGeoRouteRequest.SegmentDetails: ...
    def supportedTravelModes(self) -> PySide2.QtLocation.QGeoRouteRequest.TravelModes: ...
    def updateRoute(self, route:PySide2.QtLocation.QGeoRoute, position:PySide2.QtPositioning.QGeoCoordinate) -> PySide2.QtLocation.QGeoRouteReply: ...


class QGeoRoutingManagerEngine(PySide2.QtCore.QObject):

    def __init__(self, parameters:typing.Dict, parent:PySide2.QtCore.QObject=...): ...
    def calculateRoute(self, request:PySide2.QtLocation.QGeoRouteRequest) -> PySide2.QtLocation.QGeoRouteReply: ...
    def locale(self) -> PySide2.QtCore.QLocale: ...
    def managerName(self) -> str: ...
    def managerVersion(self) -> int: ...
    def measurementSystem(self) -> PySide2.QtCore.QLocale.MeasurementSystem: ...
    def setLocale(self, locale:PySide2.QtCore.QLocale): ...
    def setMeasurementSystem(self, system:PySide2.QtCore.QLocale.MeasurementSystem): ...
    def setSupportedFeatureTypes(self, featureTypes:PySide2.QtLocation.QGeoRouteRequest.FeatureTypes): ...
    def setSupportedFeatureWeights(self, featureWeights:PySide2.QtLocation.QGeoRouteRequest.FeatureWeights): ...
    def setSupportedManeuverDetails(self, maneuverDetails:PySide2.QtLocation.QGeoRouteRequest.ManeuverDetails): ...
    def setSupportedRouteOptimizations(self, optimizations:PySide2.QtLocation.QGeoRouteRequest.RouteOptimizations): ...
    def setSupportedSegmentDetails(self, segmentDetails:PySide2.QtLocation.QGeoRouteRequest.SegmentDetails): ...
    def setSupportedTravelModes(self, travelModes:PySide2.QtLocation.QGeoRouteRequest.TravelModes): ...
    def supportedFeatureTypes(self) -> PySide2.QtLocation.QGeoRouteRequest.FeatureTypes: ...
    def supportedFeatureWeights(self) -> PySide2.QtLocation.QGeoRouteRequest.FeatureWeights: ...
    def supportedManeuverDetails(self) -> PySide2.QtLocation.QGeoRouteRequest.ManeuverDetails: ...
    def supportedRouteOptimizations(self) -> PySide2.QtLocation.QGeoRouteRequest.RouteOptimizations: ...
    def supportedSegmentDetails(self) -> PySide2.QtLocation.QGeoRouteRequest.SegmentDetails: ...
    def supportedTravelModes(self) -> PySide2.QtLocation.QGeoRouteRequest.TravelModes: ...
    def updateRoute(self, route:PySide2.QtLocation.QGeoRoute, position:PySide2.QtPositioning.QGeoCoordinate) -> PySide2.QtLocation.QGeoRouteReply: ...


class QGeoServiceProvider(PySide2.QtCore.QObject):

    def __init__(self, providerName:str, parameters:typing.Dict=..., allowExperimental:bool=...): ...
    @staticmethod
    def availableServiceProviders() -> typing.List: ...
    def error(self) -> PySide2.QtLocation.QGeoServiceProvider.Error: ...
    def errorString(self) -> str: ...
    def geocodingError(self) -> PySide2.QtLocation.QGeoServiceProvider.Error: ...
    def geocodingErrorString(self) -> str: ...
    def geocodingFeatures(self) -> PySide2.QtLocation.QGeoServiceProvider.GeocodingFeatures: ...
    def geocodingManager(self) -> PySide2.QtLocation.QGeoCodingManager: ...
    def mappingError(self) -> PySide2.QtLocation.QGeoServiceProvider.Error: ...
    def mappingErrorString(self) -> str: ...
    def mappingFeatures(self) -> PySide2.QtLocation.QGeoServiceProvider.MappingFeatures: ...
    def navigationError(self) -> PySide2.QtLocation.QGeoServiceProvider.Error: ...
    def navigationErrorString(self) -> str: ...
    def navigationFeatures(self) -> PySide2.QtLocation.QGeoServiceProvider.NavigationFeatures: ...
    def placeManager(self) -> PySide2.QtLocation.QPlaceManager: ...
    def placesError(self) -> PySide2.QtLocation.QGeoServiceProvider.Error: ...
    def placesErrorString(self) -> str: ...
    def placesFeatures(self) -> PySide2.QtLocation.QGeoServiceProvider.PlacesFeatures: ...
    def routingError(self) -> PySide2.QtLocation.QGeoServiceProvider.Error: ...
    def routingErrorString(self) -> str: ...
    def routingFeatures(self) -> PySide2.QtLocation.QGeoServiceProvider.RoutingFeatures: ...
    def routingManager(self) -> PySide2.QtLocation.QGeoRoutingManager: ...
    def setAllowExperimental(self, allow:bool): ...
    def setLocale(self, locale:PySide2.QtCore.QLocale): ...
    def setParameters(self, parameters:typing.Dict): ...


class QGeoServiceProviderFactory(Shiboken.Object):

    def __init__(self): ...
    def createGeocodingManagerEngine(self, parameters:typing.Dict, error:PySide2.QtLocation.QGeoServiceProvider.Error, errorString:str) -> PySide2.QtLocation.QGeoCodingManagerEngine: ...
    def createPlaceManagerEngine(self, parameters:typing.Dict, error:PySide2.QtLocation.QGeoServiceProvider.Error, errorString:str) -> PySide2.QtLocation.QPlaceManagerEngine: ...
    def createRoutingManagerEngine(self, parameters:typing.Dict, error:PySide2.QtLocation.QGeoServiceProvider.Error, errorString:str) -> PySide2.QtLocation.QGeoRoutingManagerEngine: ...


class QGeoServiceProviderFactoryV2(PySide2.QtLocation.QGeoServiceProviderFactory):

    def __init__(self): ...


class QPlace(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtLocation.QPlace): ...
    def __copy__(self): ...
    def appendContactDetail(self, contactType:str, detail:PySide2.QtLocation.QPlaceContactDetail): ...
    def attribution(self) -> str: ...
    def categories(self) -> typing.List: ...
    def contactDetails(self, contactType:str) -> typing.List: ...
    def contactTypes(self) -> typing.List: ...
    def content(self, type:PySide2.QtLocation.QPlaceContent.Type) -> typing.Dict: ...
    def detailsFetched(self) -> bool: ...
    def extendedAttribute(self, attributeType:str) -> PySide2.QtLocation.QPlaceAttribute: ...
    def extendedAttributeTypes(self) -> typing.List: ...
    def icon(self) -> PySide2.QtLocation.QPlaceIcon: ...
    def insertContent(self, type:PySide2.QtLocation.QPlaceContent.Type, content:typing.Dict): ...
    def isEmpty(self) -> bool: ...
    def location(self) -> PySide2.QtPositioning.QGeoLocation: ...
    def name(self) -> str: ...
    def placeId(self) -> str: ...
    def primaryEmail(self) -> str: ...
    def primaryFax(self) -> str: ...
    def primaryPhone(self) -> str: ...
    def primaryWebsite(self) -> PySide2.QtCore.QUrl: ...
    def ratings(self) -> PySide2.QtLocation.QPlaceRatings: ...
    def removeContactDetails(self, contactType:str): ...
    def removeExtendedAttribute(self, attributeType:str): ...
    def setAttribution(self, attribution:str): ...
    def setCategories(self, categories:typing.List): ...
    def setCategory(self, category:PySide2.QtLocation.QPlaceCategory): ...
    def setContactDetails(self, contactType:str, details:typing.List): ...
    def setContent(self, type:PySide2.QtLocation.QPlaceContent.Type, content:typing.Dict): ...
    def setDetailsFetched(self, fetched:bool): ...
    def setExtendedAttribute(self, attributeType:str, attribute:PySide2.QtLocation.QPlaceAttribute): ...
    def setIcon(self, icon:PySide2.QtLocation.QPlaceIcon): ...
    def setLocation(self, location:PySide2.QtPositioning.QGeoLocation): ...
    def setName(self, name:str): ...
    def setPlaceId(self, identifier:str): ...
    def setRatings(self, ratings:PySide2.QtLocation.QPlaceRatings): ...
    def setSupplier(self, supplier:PySide2.QtLocation.QPlaceSupplier): ...
    def setTotalContentCount(self, type:PySide2.QtLocation.QPlaceContent.Type, total:int): ...
    def supplier(self) -> PySide2.QtLocation.QPlaceSupplier: ...
    def totalContentCount(self, type:PySide2.QtLocation.QPlaceContent.Type) -> int: ...


class QPlaceAttribute(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtLocation.QPlaceAttribute): ...
    def __copy__(self): ...
    def isEmpty(self) -> bool: ...
    def label(self) -> str: ...
    def setLabel(self, label:str): ...
    def setText(self, text:str): ...
    def text(self) -> str: ...


class QPlaceCategory(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtLocation.QPlaceCategory): ...
    def __copy__(self): ...
    def categoryId(self) -> str: ...
    def icon(self) -> PySide2.QtLocation.QPlaceIcon: ...
    def isEmpty(self) -> bool: ...
    def name(self) -> str: ...
    def setCategoryId(self, identifier:str): ...
    def setIcon(self, icon:PySide2.QtLocation.QPlaceIcon): ...
    def setName(self, name:str): ...


class QPlaceContactDetail(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtLocation.QPlaceContactDetail): ...
    def __copy__(self): ...
    def clear(self): ...
    def label(self) -> str: ...
    def setLabel(self, label:str): ...
    def setValue(self, value:str): ...
    def value(self) -> str: ...


class QPlaceContent(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtLocation.QPlaceContent): ...
    def __copy__(self): ...
    def attribution(self) -> str: ...
    def setAttribution(self, attribution:str): ...
    def setSupplier(self, supplier:PySide2.QtLocation.QPlaceSupplier): ...
    def setUser(self, user:PySide2.QtLocation.QPlaceUser): ...
    def supplier(self) -> PySide2.QtLocation.QPlaceSupplier: ...
    def type(self) -> PySide2.QtLocation.QPlaceContent.Type: ...
    def user(self) -> PySide2.QtLocation.QPlaceUser: ...


class QPlaceContentReply(PySide2.QtLocation.QPlaceReply):

    def __init__(self, parent:PySide2.QtCore.QObject=...): ...
    def content(self) -> typing.Dict: ...
    def nextPageRequest(self) -> PySide2.QtLocation.QPlaceContentRequest: ...
    def previousPageRequest(self) -> PySide2.QtLocation.QPlaceContentRequest: ...
    def request(self) -> PySide2.QtLocation.QPlaceContentRequest: ...
    def setContent(self, content:typing.Dict): ...
    def setNextPageRequest(self, next:PySide2.QtLocation.QPlaceContentRequest): ...
    def setPreviousPageRequest(self, previous:PySide2.QtLocation.QPlaceContentRequest): ...
    def setRequest(self, request:PySide2.QtLocation.QPlaceContentRequest): ...
    def setTotalCount(self, total:int): ...
    def totalCount(self) -> int: ...
    def type(self) -> PySide2.QtLocation.QPlaceReply.Type: ...


class QPlaceContentRequest(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtLocation.QPlaceContentRequest): ...
    def __copy__(self): ...
    def clear(self): ...
    def contentContext(self) -> typing.Any: ...
    def contentType(self) -> PySide2.QtLocation.QPlaceContent.Type: ...
    def limit(self) -> int: ...
    def placeId(self) -> str: ...
    def setContentContext(self, context:typing.Any): ...
    def setContentType(self, type:PySide2.QtLocation.QPlaceContent.Type): ...
    def setLimit(self, limit:int): ...
    def setPlaceId(self, identifier:str): ...


class QPlaceDetailsReply(PySide2.QtLocation.QPlaceReply):

    def __init__(self, parent:PySide2.QtCore.QObject=...): ...
    def place(self) -> PySide2.QtLocation.QPlace: ...
    def setPlace(self, place:PySide2.QtLocation.QPlace): ...
    def type(self) -> PySide2.QtLocation.QPlaceReply.Type: ...


class QPlaceEditorial(PySide2.QtLocation.QPlaceContent):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtLocation.QPlaceContent): ...
    def language(self) -> str: ...
    def setLanguage(self, data:str): ...
    def setText(self, text:str): ...
    def setTitle(self, data:str): ...
    def text(self) -> str: ...
    def title(self) -> str: ...


class QPlaceIcon(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtLocation.QPlaceIcon): ...
    def __copy__(self): ...
    def isEmpty(self) -> bool: ...
    def manager(self) -> PySide2.QtLocation.QPlaceManager: ...
    def parameters(self) -> typing.Dict: ...
    def setManager(self, manager:PySide2.QtLocation.QPlaceManager): ...
    def setParameters(self, parameters:typing.Dict): ...
    def url(self, size:PySide2.QtCore.QSize=...) -> PySide2.QtCore.QUrl: ...


class QPlaceIdReply(PySide2.QtLocation.QPlaceReply):

    def __init__(self, operationType:PySide2.QtLocation.QPlaceIdReply.OperationType, parent:PySide2.QtCore.QObject=...): ...
    def id(self) -> str: ...
    def operationType(self) -> PySide2.QtLocation.QPlaceIdReply.OperationType: ...
    def setId(self, identifier:str): ...
    def type(self) -> PySide2.QtLocation.QPlaceReply.Type: ...


class QPlaceImage(PySide2.QtLocation.QPlaceContent):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtLocation.QPlaceContent): ...
    def imageId(self) -> str: ...
    def mimeType(self) -> str: ...
    def setImageId(self, identifier:str): ...
    def setMimeType(self, data:str): ...
    def setUrl(self, url:PySide2.QtCore.QUrl): ...
    def url(self) -> PySide2.QtCore.QUrl: ...


class QPlaceManager(PySide2.QtCore.QObject):

    def category(self, categoryId:str) -> PySide2.QtLocation.QPlaceCategory: ...
    def childCategories(self, parentId:str=...) -> typing.List: ...
    def childCategoryIds(self, parentId:str=...) -> typing.List: ...
    def compatiblePlace(self, place:PySide2.QtLocation.QPlace) -> PySide2.QtLocation.QPlace: ...
    def getPlaceContent(self, request:PySide2.QtLocation.QPlaceContentRequest) -> PySide2.QtLocation.QPlaceContentReply: ...
    def getPlaceDetails(self, placeId:str) -> PySide2.QtLocation.QPlaceDetailsReply: ...
    def initializeCategories(self) -> PySide2.QtLocation.QPlaceReply: ...
    def locales(self) -> typing.List: ...
    def managerName(self) -> str: ...
    def managerVersion(self) -> int: ...
    def matchingPlaces(self, request:PySide2.QtLocation.QPlaceMatchRequest) -> PySide2.QtLocation.QPlaceMatchReply: ...
    def parentCategoryId(self, categoryId:str) -> str: ...
    def removeCategory(self, categoryId:str) -> PySide2.QtLocation.QPlaceIdReply: ...
    def removePlace(self, placeId:str) -> PySide2.QtLocation.QPlaceIdReply: ...
    def saveCategory(self, category:PySide2.QtLocation.QPlaceCategory, parentId:str=...) -> PySide2.QtLocation.QPlaceIdReply: ...
    def savePlace(self, place:PySide2.QtLocation.QPlace) -> PySide2.QtLocation.QPlaceIdReply: ...
    def search(self, query:PySide2.QtLocation.QPlaceSearchRequest) -> PySide2.QtLocation.QPlaceSearchReply: ...
    def searchSuggestions(self, request:PySide2.QtLocation.QPlaceSearchRequest) -> PySide2.QtLocation.QPlaceSearchSuggestionReply: ...
    def setLocale(self, locale:PySide2.QtCore.QLocale): ...
    def setLocales(self, locale:typing.List): ...


class QPlaceManagerEngine(PySide2.QtCore.QObject):

    def __init__(self, parameters:typing.Dict, parent:PySide2.QtCore.QObject=...): ...
    def category(self, categoryId:str) -> PySide2.QtLocation.QPlaceCategory: ...
    def childCategories(self, parentId:str) -> typing.List: ...
    def childCategoryIds(self, categoryId:str) -> typing.List: ...
    def compatiblePlace(self, original:PySide2.QtLocation.QPlace) -> PySide2.QtLocation.QPlace: ...
    def constructIconUrl(self, icon:PySide2.QtLocation.QPlaceIcon, size:PySide2.QtCore.QSize) -> PySide2.QtCore.QUrl: ...
    def getPlaceContent(self, request:PySide2.QtLocation.QPlaceContentRequest) -> PySide2.QtLocation.QPlaceContentReply: ...
    def getPlaceDetails(self, placeId:str) -> PySide2.QtLocation.QPlaceDetailsReply: ...
    def initializeCategories(self) -> PySide2.QtLocation.QPlaceReply: ...
    def locales(self) -> typing.List: ...
    def manager(self) -> PySide2.QtLocation.QPlaceManager: ...
    def managerName(self) -> str: ...
    def managerVersion(self) -> int: ...
    def matchingPlaces(self, request:PySide2.QtLocation.QPlaceMatchRequest) -> PySide2.QtLocation.QPlaceMatchReply: ...
    def parentCategoryId(self, categoryId:str) -> str: ...
    def removeCategory(self, categoryId:str) -> PySide2.QtLocation.QPlaceIdReply: ...
    def removePlace(self, placeId:str) -> PySide2.QtLocation.QPlaceIdReply: ...
    def saveCategory(self, category:PySide2.QtLocation.QPlaceCategory, parentId:str) -> PySide2.QtLocation.QPlaceIdReply: ...
    def savePlace(self, place:PySide2.QtLocation.QPlace) -> PySide2.QtLocation.QPlaceIdReply: ...
    def search(self, request:PySide2.QtLocation.QPlaceSearchRequest) -> PySide2.QtLocation.QPlaceSearchReply: ...
    def searchSuggestions(self, request:PySide2.QtLocation.QPlaceSearchRequest) -> PySide2.QtLocation.QPlaceSearchSuggestionReply: ...
    def setLocales(self, locales:typing.List): ...


class QPlaceMatchReply(PySide2.QtLocation.QPlaceReply):

    def __init__(self, parent:PySide2.QtCore.QObject=...): ...
    def places(self) -> typing.List: ...
    def request(self) -> PySide2.QtLocation.QPlaceMatchRequest: ...
    def setPlaces(self, results:typing.List): ...
    def setRequest(self, request:PySide2.QtLocation.QPlaceMatchRequest): ...
    def type(self) -> PySide2.QtLocation.QPlaceReply.Type: ...


class QPlaceMatchRequest(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtLocation.QPlaceMatchRequest): ...
    def __copy__(self): ...
    def clear(self): ...
    def parameters(self) -> typing.Dict: ...
    def places(self) -> typing.List: ...
    def setParameters(self, parameters:typing.Dict): ...
    def setPlaces(self, places:typing.List): ...
    def setResults(self, results:typing.List): ...


class QPlaceProposedSearchResult(PySide2.QtLocation.QPlaceSearchResult):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtLocation.QPlaceSearchResult): ...
    def searchRequest(self) -> PySide2.QtLocation.QPlaceSearchRequest: ...
    def setSearchRequest(self, request:PySide2.QtLocation.QPlaceSearchRequest): ...


class QPlaceRatings(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtLocation.QPlaceRatings): ...
    def __copy__(self): ...
    def average(self) -> float: ...
    def count(self) -> int: ...
    def isEmpty(self) -> bool: ...
    def maximum(self) -> float: ...
    def setAverage(self, average:float): ...
    def setCount(self, count:int): ...
    def setMaximum(self, max:float): ...


class QPlaceReply(PySide2.QtCore.QObject):

    def __init__(self, parent:PySide2.QtCore.QObject=...): ...
    def abort(self): ...
    def error(self) -> PySide2.QtLocation.QPlaceReply.Error: ...
    def errorString(self) -> str: ...
    def isFinished(self) -> bool: ...
    def setError(self, error:PySide2.QtLocation.QPlaceReply.Error, errorString:str): ...
    def setFinished(self, finished:bool): ...
    def type(self) -> PySide2.QtLocation.QPlaceReply.Type: ...


class QPlaceResult(PySide2.QtLocation.QPlaceSearchResult):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtLocation.QPlaceSearchResult): ...
    def distance(self) -> float: ...
    def isSponsored(self) -> bool: ...
    def place(self) -> PySide2.QtLocation.QPlace: ...
    def setDistance(self, distance:float): ...
    def setPlace(self, place:PySide2.QtLocation.QPlace): ...
    def setSponsored(self, sponsored:bool): ...


class QPlaceReview(PySide2.QtLocation.QPlaceContent):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtLocation.QPlaceContent): ...
    def dateTime(self) -> PySide2.QtCore.QDateTime: ...
    def language(self) -> str: ...
    def rating(self) -> float: ...
    def reviewId(self) -> str: ...
    def setDateTime(self, dt:PySide2.QtCore.QDateTime): ...
    def setLanguage(self, data:str): ...
    def setRating(self, data:float): ...
    def setReviewId(self, identifier:str): ...
    def setText(self, text:str): ...
    def setTitle(self, data:str): ...
    def text(self) -> str: ...
    def title(self) -> str: ...


class QPlaceSearchReply(PySide2.QtLocation.QPlaceReply):

    def __init__(self, parent:PySide2.QtCore.QObject=...): ...
    def nextPageRequest(self) -> PySide2.QtLocation.QPlaceSearchRequest: ...
    def previousPageRequest(self) -> PySide2.QtLocation.QPlaceSearchRequest: ...
    def request(self) -> PySide2.QtLocation.QPlaceSearchRequest: ...
    def results(self) -> typing.List: ...
    def setNextPageRequest(self, next:PySide2.QtLocation.QPlaceSearchRequest): ...
    def setPreviousPageRequest(self, previous:PySide2.QtLocation.QPlaceSearchRequest): ...
    def setRequest(self, request:PySide2.QtLocation.QPlaceSearchRequest): ...
    def setResults(self, results:typing.List): ...
    def type(self) -> PySide2.QtLocation.QPlaceReply.Type: ...


class QPlaceSearchRequest(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtLocation.QPlaceSearchRequest): ...
    def categories(self) -> typing.List: ...
    def clear(self): ...
    def limit(self) -> int: ...
    def recommendationId(self) -> str: ...
    def relevanceHint(self) -> PySide2.QtLocation.QPlaceSearchRequest.RelevanceHint: ...
    def searchArea(self) -> PySide2.QtPositioning.QGeoShape: ...
    def searchContext(self) -> typing.Any: ...
    def searchTerm(self) -> str: ...
    def setCategories(self, categories:typing.List): ...
    def setCategory(self, category:PySide2.QtLocation.QPlaceCategory): ...
    def setLimit(self, limit:int): ...
    def setRecommendationId(self, recommendationId:str): ...
    def setRelevanceHint(self, hint:PySide2.QtLocation.QPlaceSearchRequest.RelevanceHint): ...
    def setSearchArea(self, area:PySide2.QtPositioning.QGeoShape): ...
    def setSearchContext(self, context:typing.Any): ...
    def setSearchTerm(self, term:str): ...


class QPlaceSearchResult(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtLocation.QPlaceSearchResult): ...
    def icon(self) -> PySide2.QtLocation.QPlaceIcon: ...
    def setIcon(self, icon:PySide2.QtLocation.QPlaceIcon): ...
    def setTitle(self, title:str): ...
    def title(self) -> str: ...
    def type(self) -> PySide2.QtLocation.QPlaceSearchResult.SearchResultType: ...


class QPlaceSearchSuggestionReply(PySide2.QtLocation.QPlaceReply):

    def __init__(self, parent:PySide2.QtCore.QObject=...): ...
    def setSuggestions(self, suggestions:typing.List): ...
    def suggestions(self) -> typing.List: ...
    def type(self) -> PySide2.QtLocation.QPlaceReply.Type: ...


class QPlaceSupplier(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtLocation.QPlaceSupplier): ...
    def __copy__(self): ...
    def icon(self) -> PySide2.QtLocation.QPlaceIcon: ...
    def isEmpty(self) -> bool: ...
    def name(self) -> str: ...
    def setIcon(self, icon:PySide2.QtLocation.QPlaceIcon): ...
    def setName(self, data:str): ...
    def setSupplierId(self, identifier:str): ...
    def setUrl(self, data:PySide2.QtCore.QUrl): ...
    def supplierId(self) -> str: ...
    def url(self) -> PySide2.QtCore.QUrl: ...


class QPlaceUser(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtLocation.QPlaceUser): ...
    def __copy__(self): ...
    def name(self) -> str: ...
    def setName(self, name:str): ...
    def setUserId(self, identifier:str): ...
    def userId(self) -> str: ...

# eof
