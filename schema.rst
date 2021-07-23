Metadata Schema for the Persistent Identification of Scientific Measuring Instruments
=====================================================================================

+-------+----------------------------+------------+-----+--------------------------+------------------------+
| ID    | Property                   | Obligation | Occ | Definition               | Allowed values,        |
|       |                            |            |     |                          | constraints,           |
|       |                            |            |     |                          | remarks                |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 1     | Identifier                 | M          | 1   | Unique string that       |                        |
|       |                            |            |     | identifies the           |                        |
|       |                            |            |     | instrument instance      |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 1.1   | identifierType             | M          | 1   | Type of the identifier   | [#identtype]_          |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 2     | SchemaVersion              | M          | 1   | Version number of the    | Fixed value according  |
|       |                            |            |     | PIDINST schema used in   | to the current version |
|       |                            |            |     | this record              | of the schema          |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 3     | LandingPage                | M          | 1   | A landing page that      | URL                    |
|       |                            |            |     | the identifier           |                        |
|       |                            |            |     | resolves to              |                        |
|       |                            |            |     |                          |                        |
|       |                            |            |     |                          |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 4     | Name                       | M          | 1   | Name by which the        | Free text              |
|       |                            |            |     | instrument instance is   |                        |
|       |                            |            |     | known                    |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 5     | Owner                      | M          | 1-n | Institution(s)           |                        |
|       |                            |            |     | responsible for the      |                        |
|       |                            |            |     | management of the        |                        |
|       |                            |            |     | instrument. This may     |                        |
|       |                            |            |     | include the legal        |                        |
|       |                            |            |     | owner, the operator,     |                        |
|       |                            |            |     | or an institute          |                        |
|       |                            |            |     | providing access to      |                        |
|       |                            |            |     | the instrument.          |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 5.1   | ownerName                  | M          | 1   | Full name of the owner   | Free text              |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 5.2   | ownerContact               | O          | 0-1 | Contact address of the   | Electronic mail        |
|       |                            |            |     | owner                    | address                |
|       |                            |            |     |                          |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 5.3   | ownerIdentifier            | O          | 0-1 | Persistent identifier    | Free text, must be     |
|       |                            |            |     | used to identify the     | globally unique        |
|       |                            |            |     | owner                    | identifiers.           |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 5.3.1 | ownerIdentifierType        | O          | 1   | Type of the identifier   | Free text              |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 6     | Manufacturer               | M          | 1-n | The instrument's         |                        |
|       |                            |            |     | manufacturer(s) or       |                        |
|       |                            |            |     | developer. This may      |                        |
|       |                            |            |     | also be the owner for    |                        |
|       |                            |            |     | custom build             |                        |
|       |                            |            |     | instruments              |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 6.1   | manufacturerName           | M          | 1   | Full name of the         | Free text              |
|       |                            |            |     | manufacturer             |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 6.2   | manufacturerIdentifier     | O          | 0-1 | Persistent identifier    | Free text, must be     |
|       |                            |            |     | used to identify the     | globally unique        |
|       |                            |            |     | manufacturer             | identifiers.           |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 6.2.1 | manufacturerIdentifierType | O          | 1   | Type of the identifier   | Free text              |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 7     | Model                      | R          | 0-1 | Name of the model or     |                        |
|       |                            |            |     | type of device as        |                        |
|       |                            |            |     | attributed by the        |                        |
|       |                            |            |     | manufacturer             |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 7.1   | modelName                  | R          | 1   | Full name of the model   | Free text              |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 7.2   | modelIdentifier            | O          | 0-1 | Persistent identifier    | Free text, must be a   |
|       |                            |            |     | used to identify the     | globally unique        |
|       |                            |            |     | model                    | identifier.            |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 7.2.1 | modelIdentifierType        | O          | 1   | Type of the identifier   | Free text              |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 8     | Description                | R          | 0-1 | Technical description    | Free text              |
|       |                            |            |     | of the device and its    |                        |
|       |                            |            |     | capabilities             |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 9     | InstrumentType             | R          | 0-1 | Classification of the    | Free text              |
|       |                            |            |     | type of the instrument   |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 10    | MeasuredVariable           | R          | 0-n | The variable(s) that     | Free text              |
|       |                            |            |     | this instrument          |                        |
|       |                            |            |     | measures or observes     |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 11    | Date                       | R          | 0-n | Dates relevant to the    | ISO 8601               |
|       |                            |            |     | instrument               |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 11.1  | dateType                   | R          | 1   | The type of the date     | Controlled list        |
|       |                            |            |     |                          | of values:             |
|       |                            |            |     |                          |   Commissioned,        |
|       |                            |            |     |                          |   DeCommissioned,      |
|       |                            |            |     |                          |   ...                  |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 12    | RelatedIdentifier          | R          | 0-n | Identifiers of related   | Free text, must be     |
|       |                            |            |     | resources                | globally unique        |
|       |                            |            |     |                          | identifiers.           |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 12.1  | relatedIdentifierType      | R          | 1   | Type of the identifier   | Controlled list        |
|       |                            |            |     |                          | of values:             |
|       |                            |            |     |                          |   ARK, arXiv, bibcode, |
|       |                            |            |     |                          |   DOI, EAN13, EISSN,   |
|       |                            |            |     |                          |   Handle, IGSN, ISBN,  |
|       |                            |            |     |                          |   ISSN, ISTC, LISSN,   |
|       |                            |            |     |                          |   PMID, PURL, RAiD,    |
|       |                            |            |     |                          |   RRID, UPC, URL,      |
|       |                            |            |     |                          |   URN, w3id            |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 12.2  | relationType               | R          | 1   | Description of the       | Controlled list        |
|       |                            |            |     | relationship             | of values:             |
|       |                            |            |     |                          |   IsDescribedBy,       |
|       |                            |            |     |                          |   IsNewVersionOf,      |
|       |                            |            |     |                          |   IsPreviousVersionOf, |
|       |                            |            |     |                          |   HasComponent,        |
|       |                            |            |     |                          |   IsComponentOf,       |
|       |                            |            |     |                          |   References,          |
|       |                            |            |     |                          |   HasMetadata, ...     |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 13    | AlternateIdentifier        | R          | 0-n | Identifiers other than   | Free text, should be   |
|       |                            |            |     | the PIDINST pertaining   | unique identifiers     |
|       |                            |            |     | to the same instrument   |                        |
|       |                            |            |     | instance.  This should   |                        |
|       |                            |            |     | be used if the           |                        |
|       |                            |            |     | instrument has a serial  |                        |
|       |                            |            |     | number.  Other possible  |                        |
|       |                            |            |     | uses include an owner's  |                        |
|       |                            |            |     | inventory number or an   |                        |
|       |                            |            |     | entry in some instrument |                        |
|       |                            |            |     | data base.               |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 13.1  | alternateIdentifierType    | R          | 1   | Type of the identifier   | Controlled list of     |
|       |                            |            |     |                          | values:                |
|       |                            |            |     |                          |   SerialNumber,        |
|       |                            |            |     |                          |   InventoryNumber,     |
|       |                            |            |     |                          |   Other                |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 13.2  | alternateIdentifierName    | O          | 0-1 | A supplementary name for | Free text              |
|       |                            |            |     | the identifier type.     |                        |
|       |                            |            |     | This is mostly useful if |                        |
|       |                            |            |     | alternateIdentifierType  |                        |
|       |                            |            |     | is Other.                |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+


Notes
-----

.. [#identtype] The type of the identifier depends on the provider
   being used to register the instrument PID.  In the case of ePIC,
   the value of `identifierType` would be "Handle".


Criteria for adding and classifying properties
----------------------------------------------

This section formulates criteria for adding properties to the schema
and for classifying them as mandatory, recommended, or optional.
These criteria should be taken as guidelines to consider in the
discussion, but not as strict rules.

Criteria for adding properties
..............................

A property should be included in the schema, if an application
requires to store some piece of information in the metadata that
cannot be represented appropriately in any other already existing
property.  Otherwise, the schema would become useless for that
application.

On the other hand, redundancy should be avoided.  Ideally, there
should be only one place in the schema for any given piece of
information.

Criteria for classifying the obligation of properties
.....................................................

A property should be classified as mandatory, if either

- an PIDINST does not make sense at all without that property, or if

- an application requires to find this piece of information in third
  party PIDINST metadata.

It should be taken into account that each mandatory property creates
an additional burden for metadata providers.  So this classification
should be used carefully.  If any application is not able to provide
meaningful values for the property, this should be taken as a strong
hint that the classification as mandatory is not appropriate.  On the
other hand, the application may fall back on “Standard values for
unknown information” (see Appendix 3 in the `DataCite 4.1 Metadata
Schema Documentation`_), so that applications may put into mandatory
attributes if this piece of information is not available.

A property that is not mandatory should be classified as recommended
if this piece of information is considered to be general useful in
third party PIDINST metadata for many applications.

Properties that are neither mandatory nor recommended are optional.


.. _DataCite 4.1 Metadata Schema Documentation: https://schema.datacite.org/meta/kernel-4.1/
