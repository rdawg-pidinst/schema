Supporting Material
===================

This directory contains supporting material for the PIDINST schema.
This includes:

+ pidinst-schema-1_0.xsd: a XML Schema Definition file.

+ examples: examples of serializations of instrument metedata using
  the PIDINST schema.  Examples collected so far:

  - hzb-nanocluster.xml: NanoclusterTrap, an experimental station at
    HZB's electron storage ring BESSY II.

  - hzb-mx-14-1.xml, hzb-mx-14-1-pilatus.xml: Macromolecular
    Crystallography experimental station 14.1 at HZB's electron
    storage ring BESSY II.  This example describes the experimental
    station (hzb-mx-14-1.xml) itself and a separate record for one of
    it's major components, the Pilatus 6M detector
    (hzb-mx-14-1-pilatus.xml).  Both records are linked using the
    related identifier property with related identifier type
    `HasComponent` / `IsComponentOf`.

Note that the PIDINST schema by itself only defines the properties to
represent instrument descriptions and the semantics of these
properties.  It is technology agnostic and not limited to one
particular serialization format.  The XML examples are just that:
examples that illustrate how the schema could be implemented
using XML.  The XML Schema Definition file is not authoritative.
