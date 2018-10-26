Metadata Schema for the Persistent Identification of Scientific Measuring Instruments
=====================================================================================

+------+-------------------------+------------+-----+------------------------+------------------------+
| ID   | Property                | Obligation | Occ | Definition             | Allowed values,        |
|      |                         |            |     |                        | constraints,           |
|      |                         |            |     |                        | remarks                |
+------+-------------------------+------------+-----+------------------------+------------------------+
| 1    | Identifier              | M          | 1   | Unique string that     | PIDINST                |
|      |                         |            |     | identifies the         |                        |
|      |                         |            |     | instrument instance    |                        |
+------+-------------------------+------------+-----+------------------------+------------------------+
| 1.1  | identifierType          | M          | 1   | Type of the identifier | Controlled list        |
|      |                         |            |     |                        | of values:             |
|      |                         |            |     |                        |   PIDINST              |
+------+-------------------------+------------+-----+------------------------+------------------------+
| 2    | LandingPage             | M          | 1   | A landing page that    | URL                    |
|      |                         |            |     | the identifier         |                        |
|      |                         |            |     | resolves to            |                        |
|      |                         |            |     |                        |                        |
|      |                         |            |     |                        |                        |
+------+-------------------------+------------+-----+------------------------+------------------------+
| 3    | Name                    | M          | 1   | Name by which the      | Free text              |
|      |                         |            |     | instrument instance is |                        |
|      |                         |            |     | known                  |                        |
+------+-------------------------+------------+-----+------------------------+------------------------+
| 4    | Owner                   | M          | 1-n | Institution(s)         |                        |
|      |                         |            |     | responsible for the    |                        |
|      |                         |            |     | management of the      |                        |
|      |                         |            |     | instrument. This may   |                        |
|      |                         |            |     | include the legal      |                        |
|      |                         |            |     | owner, the operator,   |                        |
|      |                         |            |     | or an institute        |                        |
|      |                         |            |     | providing access to    |                        |
|      |                         |            |     | the instrument.        |                        |
+------+-------------------------+------------+-----+------------------------+------------------------+
| 4.1  | ownerName               | M          | 1   | Full name of the owner | Free text              |
+------+-------------------------+------------+-----+------------------------+------------------------+
| 5    | Manufacturer            | M          | 1-n | The instrument's       |                        |
|      |                         |            |     | manufacturer(s) or     |                        |
|      |                         |            |     | developer. This may    |                        |
|      |                         |            |     | also be the owner for  |                        |
|      |                         |            |     | custom build           |                        |
|      |                         |            |     | instruments            |                        |
+------+-------------------------+------------+-----+------------------------+------------------------+
| 5.1  | manufacturerName        | M          | 1   | Full name of the       | Free text              |
|      |                         |            |     | manufacturer           |                        |
+------+-------------------------+------------+-----+------------------------+------------------------+
| 6    | Description             | R          | 0-1 | Technical description  | Free text              |
|      |                         |            |     | of the device and its  |                        |
|      |                         |            |     | capabilities           |                        |
+------+-------------------------+------------+-----+------------------------+------------------------+
| 7    | InstrumentType          | R          | 0-1 | Classification of the  | Free text              |
|      |                         |            |     | type of the instrument |                        |
+------+-------------------------+------------+-----+------------------------+------------------------+
| 8    | VariableMeasured        | R          | 0-n | The variable(s) that   | Free text              |
|      |                         |            |     | this instrument        |                        |
|      |                         |            |     | measures or observes   |                        |
+------+-------------------------+------------+-----+------------------------+------------------------+
| 9    | Date                    | R          | 0-n | Dates relevant to the  | ISO 8601               |
|      |                         |            |     | instrument             |                        |
+------+-------------------------+------------+-----+------------------------+------------------------+
| 9.1  | dateType                | R          | 1   | The type of the date   | Controlled list        |
|      |                         |            |     |                        | of values:             |
|      |                         |            |     |                        |   Commissioned,        |
|      |                         |            |     |                        |   DeCommissioned,      |
|      |                         |            |     |                        |   ...                  |
+------+-------------------------+------------+-----+------------------------+------------------------+
| 10   | RelatedIdentifier       | R          | 0-n | Identifiers of related | Free text, must be     |
|      |                         |            |     | resources              | globally unique        |
|      |                         |            |     |                        | identifiers.           |
+------+-------------------------+------------+-----+------------------------+------------------------+
| 10.1 | relatedIdentifierType   | R          | 1   | Type of the identifier | Controlled list        |
|      |                         |            |     |                        | of values:             |
|      |                         |            |     |                        |   PIDINST, DOI,        |
|      |                         |            |     |                        |   Handle, URL,         |
|      |                         |            |     |                        |   URN, ...             |
+------+-------------------------+------------+-----+------------------------+------------------------+
| 10.2 | relationType            | R          | 1   | Description of the     | Controlled list        |
|      |                         |            |     | relationship           | of values:             |
|      |                         |            |     |                        |   IsDecribedBy,        |
|      |                         |            |     |                        |   IsNewVersionOf,      |
|      |                         |            |     |                        |   IsPreviousVersionOf, |
|      |                         |            |     |                        |   HasComponent,        |
|      |                         |            |     |                        |   IsComponentOf,       |
|      |                         |            |     |                        |   References,          |
|      |                         |            |     |                        |   HasMetadata, ...     |
+------+-------------------------+------------+-----+------------------------+------------------------+
| 11   | AlternateIdentifier     | O          | 0-n | Identifiers other than | Free text, should be   |
|      |                         |            |     | the PIDINST pertaining | unique identifiers     |
|      |                         |            |     | to the same instrument |                        |
|      |                         |            |     | instance               |                        |
+------+-------------------------+------------+-----+------------------------+------------------------+
| 11.1 | alternateIdentifierType | O          | 1   | Type of the identifier | Free text              |
+------+-------------------------+------------+-----+------------------------+------------------------+


Notes
-----

- A suitable name for the instrument PID system still needs to be
  found.  As a place holder, we use PIDINST here.
