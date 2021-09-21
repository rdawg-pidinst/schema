Metadata Schema for the Persistent Identification of Scientific Measuring Instruments
=====================================================================================

+-------+------------------------------+------------+-----+--------------------------+------------------------+
| ID    | Property                     | Obligation | Occ | Definition               | Allowed values,        |
|       |                              |            |     |                          | constraints,           |
|       |                              |            |     |                          | remarks                |
+-------+------------------------------+------------+-----+--------------------------+------------------------+
| 1     | Identifier                   | M          | 1   | Unique string that       |                        |
|       |                              |            |     | identifies the           |                        |
|       |                              |            |     | instrument instance      |                        |
+-------+------------------------------+------------+-----+--------------------------+------------------------+
| 1.1   | identifierType               | M          | 1   | Type of the identifier   | [#identtype]_          |
+-------+------------------------------+------------+-----+--------------------------+------------------------+
| 2     | SchemaVersion                | M          | 1   | Version number of the    | Fixed value            |
|       |                              |            |     | PIDINST schema used in   | [#schemaversion]_      |
|       |                              |            |     | this record              |                        |
+-------+------------------------------+------------+-----+--------------------------+------------------------+
| 3     | LandingPage                  | M          | 1   | A landing page that      | URL                    |
|       |                              |            |     | the identifier           |                        |
|       |                              |            |     | resolves to              |                        |
|       |                              |            |     |                          |                        |
|       |                              |            |     |                          |                        |
+-------+------------------------------+------------+-----+--------------------------+------------------------+
| 4     | Name                         | M          | 1   | Name by which the        | Free text              |
|       |                              |            |     | instrument instance is   |                        |
|       |                              |            |     | known                    |                        |
+-------+------------------------------+------------+-----+--------------------------+------------------------+
| 5     | Owner                        | M          | 1-n | Institution(s)           |                        |
|       |                              |            |     | responsible for the      |                        |
|       |                              |            |     | management of the        |                        |
|       |                              |            |     | instrument. This may     |                        |
|       |                              |            |     | include the legal        |                        |
|       |                              |            |     | owner, the operator,     |                        |
|       |                              |            |     | or an institute          |                        |
|       |                              |            |     | providing access to      |                        |
|       |                              |            |     | the instrument.          |                        |
+-------+------------------------------+------------+-----+--------------------------+------------------------+
| 5.1   | ownerName                    | M          | 1   | Full name of the owner   | Free text              |
+-------+------------------------------+------------+-----+--------------------------+------------------------+
| 5.2   | ownerContact                 | O          | 0-1 | Contact address of the   | Electronic mail        |
|       |                              |            |     | owner                    | address                |
|       |                              |            |     |                          |                        |
+-------+------------------------------+------------+-----+--------------------------+------------------------+
| 5.3   | ownerIdentifier              | O          | 0-1 | Identifier used to       | Free text, should be   |
|       |                              |            |     | identify the owner       | a globally unique      |
|       |                              |            |     |                          | identifier.            |
+-------+------------------------------+------------+-----+--------------------------+------------------------+
| 5.3.1 | ownerIdentifierType          | O          | 1   | Type of the identifier   | Free text              |
+-------+------------------------------+------------+-----+--------------------------+------------------------+
| 6     | Manufacturer                 | M          | 1-n | The instrument's         |                        |
|       |                              |            |     | manufacturer(s) or       |                        |
|       |                              |            |     | developer. This may      |                        |
|       |                              |            |     | also be the owner for    |                        |
|       |                              |            |     | custom build             |                        |
|       |                              |            |     | instruments              |                        |
+-------+------------------------------+------------+-----+--------------------------+------------------------+
| 6.1   | manufacturerName             | M          | 1   | Full name of the         | Free text              |
|       |                              |            |     | manufacturer             |                        |
+-------+------------------------------+------------+-----+--------------------------+------------------------+
| 6.2   | manufacturerIdentifier       | O          | 0-1 | Identifier used to       | Free text, should be   |
|       |                              |            |     | identify the             | a globally unique      |
|       |                              |            |     | manufacturer             | identifier.            |
+-------+------------------------------+------------+-----+--------------------------+------------------------+
| 6.2.1 | manufacturerIdentifierType   | O          | 1   | Type of the identifier   | Free text              |
+-------+------------------------------+------------+-----+--------------------------+------------------------+
| 7     | Model                        | R          | 0-1 | Name of the model or     |                        |
|       |                              |            |     | type of device as        |                        |
|       |                              |            |     | attributed by the        |                        |
|       |                              |            |     | manufacturer             |                        |
+-------+------------------------------+------------+-----+--------------------------+------------------------+
| 7.1   | modelName                    | R          | 1   | Full name of the model   | Free text              |
+-------+------------------------------+------------+-----+--------------------------+------------------------+
| 7.2   | modelIdentifier              | O          | 0-1 | Identifier used to       | Free text, should be   |
|       |                              |            |     | identify the model       | a globally unique      |
|       |                              |            |     |                          | identifier.            |
+-------+------------------------------+------------+-----+--------------------------+------------------------+
| 7.2.1 | modelIdentifierType          | O          | 1   | Type of the identifier   | Free text              |
+-------+------------------------------+------------+-----+--------------------------+------------------------+
| 8     | Description                  | R          | 0-1 | Technical description    | Free text              |
|       |                              |            |     | of the device and its    |                        |
|       |                              |            |     | capabilities             |                        |
+-------+------------------------------+------------+-----+--------------------------+------------------------+
| 9     | InstrumentType               | R          | 0-n | Classification of the    |                        |
|       |                              |            |     | type of the instrument   |                        |
+-------+------------------------------+------------+-----+--------------------------+------------------------+
| 9.1   | instrumentTypeName           | R          | 1   | Full name of the         | Free text              |
|       |                              |            |     | instrument type          |                        |
+-------+------------------------------+------------+-----+--------------------------+------------------------+
| 9.2   | instrumentTypeIdentifier     | O          | 0-1 | Identifier used to       | Free text, should be a |
|       |                              |            |     | identify the type of the | globally unique        |
|       |                              |            |     | instrument               | identifier             |
+-------+------------------------------+------------+-----+--------------------------+------------------------+
| 9.2.1 | instrumentTypeIdentifierType | O          | 1   | Type of the identifier   | Free text              |
+-------+------------------------------+------------+-----+--------------------------+------------------------+
| 10    | MeasuredVariable             | R          | 0-n | The variable(s) that     | Free text              |
|       |                              |            |     | this instrument          |                        |
|       |                              |            |     | measures or observes     |                        |
+-------+------------------------------+------------+-----+--------------------------+------------------------+
| 11    | Date                         | R          | 0-n | Dates relevant to the    | ISO 8601               |
|       |                              |            |     | instrument               |                        |
+-------+------------------------------+------------+-----+--------------------------+------------------------+
| 11.1  | dateType                     | R          | 1   | The type of the date     | Controlled list        |
|       |                              |            |     |                          | of values:             |
|       |                              |            |     |                          |   Commissioned,        |
|       |                              |            |     |                          |   DeCommissioned       |
+-------+------------------------------+------------+-----+--------------------------+------------------------+
| 12    | RelatedIdentifier            | R          | 0-n | Identifiers of related   | Free text, must be     |
|       |                              |            |     | resources                | globally unique        |
|       |                              |            |     |                          | identifiers.           |
+-------+------------------------------+------------+-----+--------------------------+------------------------+
| 12.1  | relatedIdentifierType        | R          | 1   | Type of the identifier   | Controlled list        |
|       |                              |            |     |                          | of values:             |
|       |                              |            |     |                          |   ARK, arXiv, bibcode, |
|       |                              |            |     |                          |   DOI, EAN13, EISSN,   |
|       |                              |            |     |                          |   Handle, IGSN, ISBN,  |
|       |                              |            |     |                          |   ISSN, ISTC, LISSN,   |
|       |                              |            |     |                          |   PMID, PURL, RAiD,    |
|       |                              |            |     |                          |   RRID, UPC, URL,      |
|       |                              |            |     |                          |   URN, w3id            |
+-------+------------------------------+------------+-----+--------------------------+------------------------+
| 12.2  | relationType                 | R          | 1   | Description of the       | Controlled list        |
|       |                              |            |     | relationship             | of values:             |
|       |                              |            |     |                          |   IsDescribedBy,       |
|       |                              |            |     |                          |   IsNewVersionOf,      |
|       |                              |            |     |                          |   IsPreviousVersionOf, |
|       |                              |            |     |                          |   HasComponent,        |
|       |                              |            |     |                          |   IsComponentOf,       |
|       |                              |            |     |                          |   References,          |
|       |                              |            |     |                          |   HasMetadata,         |
|       |                              |            |     |                          |   WasUsedIn,           |
|       |                              |            |     |                          |   IsIdenticalTo,       |
|       |                              |            |     |                          |   IsAttachedTo         |
+-------+------------------------------+------------+-----+--------------------------+------------------------+
| 13    | AlternateIdentifier          | R          | 0-n | Identifiers other than   | Free text, should be   |
|       |                              |            |     | the PIDINST pertaining   | unique identifiers     |
|       |                              |            |     | to the same instrument   |                        |
|       |                              |            |     | instance.  This should   |                        |
|       |                              |            |     | be used if the           |                        |
|       |                              |            |     | instrument has a serial  |                        |
|       |                              |            |     | number.  Other possible  |                        |
|       |                              |            |     | uses include an owner's  |                        |
|       |                              |            |     | inventory number or an   |                        |
|       |                              |            |     | entry in some instrument |                        |
|       |                              |            |     | data base.               |                        |
+-------+------------------------------+------------+-----+--------------------------+------------------------+
| 13.1  | alternateIdentifierType      | R          | 1   | Type of the identifier   | Controlled list of     |
|       |                              |            |     |                          | values:                |
|       |                              |            |     |                          |   SerialNumber,        |
|       |                              |            |     |                          |   InventoryNumber,     |
|       |                              |            |     |                          |   Other                |
+-------+------------------------------+------------+-----+--------------------------+------------------------+
| 13.2  | alternateIdentifierName      | O          | 0-1 | A supplementary name for | Free text              |
|       |                              |            |     | the identifier type.     |                        |
|       |                              |            |     | This is mostly useful if |                        |
|       |                              |            |     | alternateIdentifierType  |                        |
|       |                              |            |     | is Other.                |                        |
+-------+------------------------------+------------+-----+--------------------------+------------------------+


Notes
-----

.. [#identtype] The type of the identifier depends on the provider
   being used to register the instrument PID.  In the case of ePIC,
   the value of `identifierType` would be "Handle".

.. [#schemaversion] The value of `SchemaVersion` is defined to be
   equal to the version number for each release version of the schema.
