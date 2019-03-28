Examples
========

This directory collects examples of serializations of instrument
metedata using the PIDINST schema.

Note that as of the writing, the schema itself is still work in
progress and the platform to run the PIDINST infrastructure on has not
yet been decided.  Therefore, the exact format for those
serializations is not yet defined.  So the examples here should be
taken as just this, as examples to illustrate how things may look like
in the end.

Examples collected so far:

+ hzb-nanocluster.xml: NanoclusterTrap, an experimental station at
  HZB's electron storage ring BESSY II.

+ hzb-mx-14-1.xml, hzb-mx-14-1-pilatus.xml: Macromolecular
  Crystallography experimental station 14.1 at HZB's electron storage
  ring BESSY II.  This example describes the experimental station
  (hzb-mx-14-1.xml) itself and a separate record for one of it's major
  components, the Pilatus 6M detector (hzb-mx-14-1-pilatus.xml).  Both
  records are linked using the related identifier property with
  related identifier type `HasComponent` / `IsComponentOf`.
