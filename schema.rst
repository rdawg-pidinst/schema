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
| 12.3  | relatedIdentifierName        | O          | 0-1 | A name for the related   | Free text              |
|       |                              |            |     | resource, may be used to |                        |
|       |                              |            |     | give a hint on the       |                        |
|       |                              |            |     | content of that resource |                        |
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

Definition of terms in controlled lists of values
-------------------------------------------------

dateType
........

+----------------+---------------------------------------------------------+
| Value          | Definition                                              |
+----------------+---------------------------------------------------------+
| Commissioned   | The date when the instrument started to be in operation |
+----------------+---------------------------------------------------------+
| DeCommissioned | The date when the instrument ceased to be in operation  |
+----------------+---------------------------------------------------------+

relatedIdentifierType
.....................

+---------+-------------------------------------------------------------+
|  Value  | Definition                                                  |
+---------+-------------------------------------------------------------+
| ARK     | Archival Resource Key: a URI designed to support long-term  |
|         | access to information objects.                              |
+---------+-------------------------------------------------------------+
| arXiv   | arXiv identifier: arXiv.org is a repository of preprints    |
|         | of scientific papers in the fields of mathematics, physics, |
|         | astronomy, computer science, quantitative biology,          |
|         | statistics, and quantitative finance.                       |
+---------+-------------------------------------------------------------+
| bibcode | Astrophysics Data System bibliographic codes: a             |
|         | standardized 19-character identifier.                       |
+---------+-------------------------------------------------------------+
| DOI     | Digital Object Identifier: a character string used to       |
|         | uniquely identify an object.  A DOI name is divided into    |
|         | two parts, a prefix and a suffix, separated by a slash.     |
+---------+-------------------------------------------------------------+
| EAN13   | European Article Number, now renamed International Article  |
|         | Number, but retaining the original acronym, is a 13-digit   |
|         | barcoding standard that is a superset of the original       |
|         | 12-digit Universal Product Code (UPC) system.               |
+---------+-------------------------------------------------------------+
| EISSN   | Electronic International Standard Serial Number: ISSN used  |
|         | to identify periodicals in electronic form (eISSN or        |
|         | e-ISSN).                                                    |
+---------+-------------------------------------------------------------+
| Handle  | This refers specifically to an ID in the Handle system      |
|         | operated by the Corporation for National Research           |
|         | Initiatives (CNRI).                                         |
+---------+-------------------------------------------------------------+
| IGSN    | A persistent unique identifier for physical samples and     |
|         | specimens.  See https://www.igsn.org/                       |
+---------+-------------------------------------------------------------+
| ISBN    | International Standard Book Number: a unique numeric book   |
|         | identifier.                                                 |
+---------+-------------------------------------------------------------+
| ISSN    | International Standard Serial Number: a unique 8-digit      |
|         | number used to identify a print or electronic periodical    |
|         | publication.                                                |
+---------+-------------------------------------------------------------+
| ISTC    | International Standard Text Code: a unique number assigned  |
|         | to a textual work.  An ISTC consists of 16 numbers and/or   |
|         | letters.                                                    |
+---------+-------------------------------------------------------------+
| LISSN   | The linking ISSN or ISSN-L enables collocation or linking   |
|         | among different media versions of a continuing resource.    |
+---------+-------------------------------------------------------------+
| PMID    | PubMed identifier: a unique number assigned to each PubMed  |
|         | record.                                                     |
+---------+-------------------------------------------------------------+
| PURL    | Persistent Uniform Resource Locator.                        |
+---------+-------------------------------------------------------------+
| RAiD    | Research Activity Identifier, see https://www.raid.org.au/  |
+---------+-------------------------------------------------------------+
| RRID    | Research Resource Identifiers, see https://www.rrids.org/   |
+---------+-------------------------------------------------------------+
| UPC     | Universal Product Code is a barcode symbology used for      |
|         | tracking trade items in stores.                             |
+---------+-------------------------------------------------------------+
| URL     | Uniform Resource Locator, also known as web address.        |
+---------+-------------------------------------------------------------+
| URN     | Uniform Resource Name: a unique and persistent identifier   |
|         | of an electronic document.                                  |
+---------+-------------------------------------------------------------+
| w3id    | Permanent identifier for Web applications.  Mostly used to  |
|         | publish vocabularies and ontologies.                        |
+---------+-------------------------------------------------------------+

relationType
............

+---------------------+-------------------------------------------------------+
|  Value              | Definition                                            |
+---------------------+-------------------------------------------------------+
| IsDescribedBy       | The linked resource is a document describing the      |
|                     | instrument.                                           |
+---------------------+-------------------------------------------------------+
| IsNewVersionOf      | If an instrument is substantially modified, a new PID |
|                     | may be attributed to the new version.  In that case   |
|                     | the old and the new PID should be linked to each      |
|                     | other.  IsNewVersionOf should be used in the new PID  |
|                     | record to link the old instrument before the          |
|                     | modification.                                         |
+---------------------+-------------------------------------------------------+
| IsPreviousVersionOf | If an instrument is substantially modified, a new PID |
|                     | may be attributed to the new version.  In that case   |
|                     | the old and the new PID should be linked to each      |
|                     | other.  IsPreviousVersionOf should be used in the old |
|                     | PIDrecord to link the new instrument after the        |
|                     | modification.                                         |
+---------------------+-------------------------------------------------------+
| HasComponent        | In the case of a complex instrument, having multiple  |
|                     | components that may be considered as instruments in   |
|                     | their own right, with their own PIDs, these PIDs      |
|                     | should be linked.  HasComponent should be used in the |
|                     | PID record of the compound instrument to link the     |
|                     | components.                                           |
+---------------------+-------------------------------------------------------+
| IsComponentOf       | In the case of a complex instrument, having multiple  |
|                     | components that may be considered as instruments in   |
|                     | their own right, with their own PIDs, these PIDs      |
|                     | should be linked.  IsComponentOf should be used in    |
|                     | the PID records of the components to link the         |
|                     | compound instrument.                                  |
+---------------------+-------------------------------------------------------+
| References          | This may be used in the generic case, if no other     |
|                     | more specific relation type applies.                  |
+---------------------+-------------------------------------------------------+
| HasMetadata         | If there is additional metadata describing the        |
|                     | instrument, possibly using a community specific       |
|                     | metadata standard, that metadata record may be linked |
|                     | using HasMetadata.                                    |
+---------------------+-------------------------------------------------------+
| WasUsedIn           | If the instrument has been deployed in some research  |
|                     | activity, such as a cruise of a research vessel,      |
|                     | WasUsedIn may be used to link that activity.          |
+---------------------+-------------------------------------------------------+
| IsIdenticalTo       | If multiple PIDs have been attributed to a single     |
|                     | instrument (which should preferably be avoided in the |
|                     | first place), these PID records should be linked to   |
|                     | each other using IsIdenticalTo.                       |
+---------------------+-------------------------------------------------------+
| IsAttachedTo        | If the instrument is permanently attached to another  |
|                     | instrument, the PID records for both instruments      |
|                     | should link to each other using IsAttachedTo.         |
+---------------------+-------------------------------------------------------+

alternateIdentifierType
.......................

+-----------------+------------------------------------------------+
| Value           | Definition                                     |
+-----------------+------------------------------------------------+
| SerialNumber    | A serial number attributed by the manufacturer |
+-----------------+------------------------------------------------+
| InventoryNumber | An inventory number used by the owner          |
+-----------------+------------------------------------------------+
| Other           | Any other kind of identifier                   |
+-----------------+------------------------------------------------+

Notes
-----

.. [#identtype] The type of the identifier depends on the provider
   being used to register the instrument PID.  In the case of ePIC,
   the value of `identifierType` would be "Handle".

.. [#schemaversion] The value of `SchemaVersion` is defined to be
   equal to the version number for each release version of the schema.
