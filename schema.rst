Metadata Schema for the Persistent Identification of Scientific Measuring Instruments
=====================================================================================

+-------+----------------------------+------------+-----+--------------------------+------------------------+
| ID    | Property                   | Obligation | Occ | Definition               | Allowed values,        |
|       |                            |            |     |                          | constraints,           |
|       |                            |            |     |                          | remarks                |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 1     | Identifier                 | M          | 1   | Unique string that       | PIDINST                |
|       |                            |            |     | identifies the           |                        |
|       |                            |            |     | instrument instance      |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 1.1   | identifierType             | M          | 1   | Type of the identifier   | Controlled list        |
|       |                            |            |     |                          | of values:             |
|       |                            |            |     |                          |   PIDINST              |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 2     | LandingPage                | M          | 1   | A landing page that      | URL                    |
|       |                            |            |     | the identifier           |                        |
|       |                            |            |     | resolves to              |                        |
|       |                            |            |     |                          |                        |
|       |                            |            |     |                          |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 3     | Name                       | M          | 1   | Name by which the        | Free text              |
|       |                            |            |     | instrument instance is   |                        |
|       |                            |            |     | known                    |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 4     | Owner                      | M          | 1-n | Institution(s)           |                        |
|       |                            |            |     | responsible for the      |                        |
|       |                            |            |     | management of the        |                        |
|       |                            |            |     | instrument. This may     |                        |
|       |                            |            |     | include the legal        |                        |
|       |                            |            |     | owner, the operator,     |                        |
|       |                            |            |     | or an institute          |                        |
|       |                            |            |     | providing access to      |                        |
|       |                            |            |     | the instrument.          |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 4.1   | ownerName                  | M          | 1   | Full name of the owner   | Free text              |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 4.2   | ownerContact               | O          | 0-1 | Contact address of the   | Electronic mail        |
|       |                            |            |     | owner                    | address                |
|       |                            |            |     |                          |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 4.3   | ownerIdentifier            | O          | 0-1 | Persistent identifier    | Free text, must be     |
|       |                            |            |     | used to identify the     | globally unique        |
|       |                            |            |     | owner                    | identifiers.           |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 4.3.1 | ownerIdentifierType        | O          | 1   | Type of the identifier   | Free text              |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 5     | Manufacturer               | M          | 1-n | The instrument's         |                        |
|       |                            |            |     | manufacturer(s) or       |                        |
|       |                            |            |     | developer. This may      |                        |
|       |                            |            |     | also be the owner for    |                        |
|       |                            |            |     | custom build             |                        |
|       |                            |            |     | instruments              |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 5.1   | manufacturerName           | M          | 1   | Full name of the         | Free text              |
|       |                            |            |     | manufacturer             |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 5.2   | manufacturerIdentifier     | O          | 0-1 | Persistent identifier    | Free text, must be     |
|       |                            |            |     | used to identify the     | globally unique        |
|       |                            |            |     | manufacturer             | identifiers.           |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 5.2.1 | manufacturerIdentifierType | O          | 1   | Type of the identifier   | Free text              |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 6     | Model                      | R          | 0-1 | Name of the model or     |                        |
|       |                            |            |     | type of device as        |                        |
|       |                            |            |     | attributed by the        |                        |
|       |                            |            |     | manufacturer             |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 6.1   | modelName                  | R          | 1   | Full name of the model   | Free text              |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 6.2   | modelIdentifier            | O          | 0-1 | Persistent identifier    | Free text, must be a   |
|       |                            |            |     | used to identify the     | globally unique        |
|       |                            |            |     | model                    | identifier.            |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 6.2.1 | modelIdentifierType        | O          | 1   | Type of the identifier   | Free text              |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 7     | Description                | R          | 0-1 | Technical description    | Free text              |
|       |                            |            |     | of the device and its    |                        |
|       |                            |            |     | capabilities             |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 8     | InstrumentType             | R          | 0-1 | Classification of the    | Free text              |
|       |                            |            |     | type of the instrument   |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 9     | MeasuredVariable           | R          | 0-n | The variable(s) that     | Free text              |
|       |                            |            |     | this instrument          |                        |
|       |                            |            |     | measures or observes     |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 10    | Date                       | R          | 0-n | Dates relevant to the    | ISO 8601               |
|       |                            |            |     | instrument               |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 10.1  | dateType                   | R          | 1   | The type of the date     | Controlled list        |
|       |                            |            |     |                          | of values:             |
|       |                            |            |     |                          |   Commissioned,        |
|       |                            |            |     |                          |   DeCommissioned,      |
|       |                            |            |     |                          |   ...                  |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 11    | RelatedIdentifier          | R          | 0-n | Identifiers of related   | Free text, must be     |
|       |                            |            |     | resources                | globally unique        |
|       |                            |            |     |                          | identifiers.           |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 11.1  | relatedIdentifierType      | R          | 1   | Type of the identifier   | Controlled list        |
|       |                            |            |     |                          | of values:             |
|       |                            |            |     |                          |   PIDINST, DOI,        |
|       |                            |            |     |                          |   Handle, URL,         |
|       |                            |            |     |                          |   URN, ...             |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 11.2  | relationType               | R          | 1   | Description of the       | Controlled list        |
|       |                            |            |     | relationship             | of values:             |
|       |                            |            |     |                          |   IsDescribedBy,       |
|       |                            |            |     |                          |   IsNewVersionOf,      |
|       |                            |            |     |                          |   IsPreviousVersionOf, |
|       |                            |            |     |                          |   HasComponent,        |
|       |                            |            |     |                          |   IsComponentOf,       |
|       |                            |            |     |                          |   References,          |
|       |                            |            |     |                          |   HasMetadata, ...     |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 12    | AlternateIdentifier        | R          | 0-n | Identifiers other than   | Free text, should be   |
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
| 12.1  | alternateIdentifierType    | R          | 1   | Type of the identifier   | Free text.  Mandatory  |
|       |                            |            |     |                          | if AlternateIdentifier |
|       |                            |            |     |                          | is used.  Suggested    |
|       |                            |            |     |                          | values include:        |
|       |                            |            |     |                          |   serialNumber,        |
|       |                            |            |     |                          |   inventoryNumber, ... |
+-------+----------------------------+------------+-----+--------------------------+------------------------+


Notes
-----

- A suitable name for the instrument PID system still needs to be
  found.  As a place holder, we use PIDINST here.


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
