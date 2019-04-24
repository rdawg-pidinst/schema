Metadata Schema for the Persistent Identification of Scientific Measuring Instruments
=====================================================================================

The following table presents the metadata schema for the persistent
identification of instruments mapped onto the `DataCite Metadata
Schema 4.2`_.  Note that the current version of the DataCite schema
has not been designed to describe instruments.  As a consequence, some
definitions in the DataCite schema need to be stretched.  For a few
relevant instrument properties there is even no suitable place in the
DataCite schema at all.

In this presentation, the DataCite schema is mostly taken as is,
assuming that no adaptations are made to accommodate instruments.
Nevertheless, there are some shortcomings of this approach, so some
amendments of the schema would facilitate its use for instruments and
should be negotiated with DataCite.


+-------+----------------------------+------------+-----+--------------------------+------------------------+
| ID    | Property                   | Obligation | Occ | Definition               | Allowed values,        |
|       |                            |            |     |                          | constraints,           |
|       |                            |            |     |                          | remarks                |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 1     | Identifier                 | M          | 1   | Unique string that       | DOI                    |
|       |                            |            |     | identifies the           |                        |
|       |                            |            |     | instrument instance      |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 1.1   | identifierType             | M          | 1   | Type of the identifier   | Controlled list of     |
|       |                            |            |     |                          | values:[#identtype]_   |
|       |                            |            |     |                          |   DOI                  |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 2     | Creator                    | M          | 1-n | The instrument's         |                        |
|       |                            |            |     | manufacturer(s) or       |                        |
|       |                            |            |     | developer. This may      |                        |
|       |                            |            |     | also be the owner for    |                        |
|       |                            |            |     | custom build             |                        |
|       |                            |            |     | instruments              |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 2.1   | creatorName                | M          | 1   | Full name of the         | Free text              |
|       |                            |            |     | manufacturer             |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 2.1.1 | nameType                   | R          | 0-1 | The type of name         | Controlled list of     |
|       |                            |            |     |                          | values:[#cr_nametype]_ |
|       |                            |            |     |                          |   Organizational       |
|       |                            |            |     |                          |   Personal             |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 2.2   | givenName                  | R          | 0-1 | First name of the        | Free text              |
|       |                            |            |     | manufacturer, if         |                        |
|       |                            |            |     | applicable               |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 2.3   | familyName                 | R          | 0-1 | Last name of the         | Free text              |
|       |                            |            |     | manufacturer, if         |                        |
|       |                            |            |     | applicable               |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 2.4   | nameIdentifier             | R          | 0-n | Unique identifier of the | Free text, format is   |
|       |                            |            |     | manufacturer             | dependent upon schema  |
|       |                            |            |     |                          |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 2.4.1 | nameIdentifierScheme       | R          | 1   | The name of the name     | Free text, mandatory   |
|       |                            |            |     | identifier schema        | if nameIdentifier is   |
|       |                            |            |     |                          | used. Examples: ROR,   |
|       |                            |            |     |                          | ISNI, ORCID            |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 2.4.2 | schemeURI                  | O          | 0-1 | The URI of the name      | Examples:              |
|       |                            |            |     | identifier schema        | http://www.isni.org,   |
|       |                            |            |     |                          | https://orcid.org      |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 2.5   | affiliation                | O          | 0-n | Organizational or        | Free text              |
|       |                            |            |     | institutional            | [#cr_affiliation]_     |
|       |                            |            |     | affiliation of the       |                        |
|       |                            |            |     | manufacturer             |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 3     | Title                      | M          | 1   | Name by which the        | Free text              |
|       |                            |            |     | instrument instance is   |                        |
|       |                            |            |     | known                    |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 3.1   | titleType                  | O          | 0-1 | The type of Title        | Controlled list of     |
|       |                            |            |     |                          | values:[#titletype]_   |
|       |                            |            |     |                          |   AlternativeTitle     |
|       |                            |            |     |                          |   Subtitle             |
|       |                            |            |     |                          |   TranslatedTitle      |
|       |                            |            |     |                          |   Other                |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 4     | Publisher                  | M          | 1   | The name of the entity   | Free text              |
|       |                            |            |     | that holds, archives,    | [#publisher]_          |
|       |                            |            |     | publishes, prints,       |                        |
|       |                            |            |     | distributes, releases,   |                        |
|       |                            |            |     | issues, or produces the  |                        |
|       |                            |            |     | resource                 |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 5     | PublicationYear            | M          | 1   | The year when the data   | YYYY [#pubyear]_       |
|       |                            |            |     | was made publicly        |                        |
|       |                            |            |     | available                |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 6     | Subject                    | R          | 0-n | Subject, keyword,        | Free text [#subject]_  |
|       |                            |            |     | classification code, or  |                        |
|       |                            |            |     | key phrase describing    |                        |
|       |                            |            |     | the instrument           |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 6.1   | subjectScheme              | O          | 0-1 | The name of the subject  | Free text              |
|       |                            |            |     | scheme or classification |                        |
|       |                            |            |     | code or authority if one |                        |
|       |                            |            |     | is used                  |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 6.2   | schemeURI                  | O          | 0-1 | The URI of the subject   |                        |
|       |                            |            |     | identifier scheme        |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 6.3   | valueURI                   | O          | 0-1 | The URI of the subject   |                        |
|       |                            |            |     | term                     |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 7     | Contributor                | M          | 1-n | Institution(s)           | [#contributor]_        |
|       |                            |            |     | responsible for the      |                        |
|       |                            |            |     | management of the        |                        |
|       |                            |            |     | instrument. This may     |                        |
|       |                            |            |     | include the legal        |                        |
|       |                            |            |     | owner, the operator,     |                        |
|       |                            |            |     | or an institute          |                        |
|       |                            |            |     | providing access to      |                        |
|       |                            |            |     | the instrument.          |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 7.1   | contributorType            | M          | 1   | The type of contributor  | Controlled list of     |
|       |                            |            |     |                          | values:                |
|       |                            |            |     |                          |   HostingInstitution   |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 7.2   | contributorName            | M          | 1   | Full name of the owner   | Free text              |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 7.2.1 | nameType                   | R          | 0-1 | The type of name         | Controlled list of     |
|       |                            |            |     |                          | values:[#cntrb_sub]_   |
|       |                            |            |     |                          |   Organizational       |
|       |                            |            |     |                          |   Personal             |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 7.3   | givenName                  | R          | 0-1 | First name of the        | Free text              |
|       |                            |            |     | owner, if                |                        |
|       |                            |            |     | applicable               |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 7.4   | familyName                 | R          | 0-1 | Last name of the         | Free text              |
|       |                            |            |     | owner, if                |                        |
|       |                            |            |     | applicable               |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 7.5   | nameIdentifier             | R          | 0-n | Unique identifier of the | Free text, format is   |
|       |                            |            |     | owner                    | dependent upon schema  |
|       |                            |            |     |                          |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 7.5.1 | nameIdentifierScheme       | R          | 1   | The name of the name     | Free text, mandatory   |
|       |                            |            |     | identifier schema        | if nameIdentifier is   |
|       |                            |            |     |                          | used. Examples: ROR,   |
|       |                            |            |     |                          | ISNI, ORCID            |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 7.5.2 | schemeURI                  | O          | 0-1 | The URI of the name      | Examples:              |
|       |                            |            |     | identifier schema        | http://www.isni.org,   |
|       |                            |            |     |                          | https://orcid.org      |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 7.6   | affiliation                | O          | 0-n | Organizational or        | Free text              |
|       |                            |            |     | institutional            | [#cntrb_sub]_          |
|       |                            |            |     | affiliation of the       |                        |
|       |                            |            |     | owner                    |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 8     | Date                       | R          | 0-n | Dates relevant to the    | ISO 8601 [#date]_      |
|       |                            |            |     | instrument               |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 8.1   | dateType                   | R          | 1   | The type of the date     | Controlled list of     |
|       |                            |            |     |                          | values, see DataCite   |
|       |                            |            |     |                          | schema                 |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 8.2   | dateInformation            | O          | 0-1 | Specific information     | Free text              |
|       |                            |            |     | about the date, if       |                        |
|       |                            |            |     | appropriate              |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 10    | ResourceType               | M          | 1   | A description of the     | Free text.  Suggested  |
|       |                            |            |     | resource                 | values:                |
|       |                            |            |     |                          |   Platform             |
|       |                            |            |     |                          |   Instrument           |
|       |                            |            |     |                          |   Sensor               |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 10.1  | resourceTypeGeneral        | M          | 1   | The general type of the  | Controlled list of     |
|       |                            |            |     | resource                 | values:[#restypegen]_  |
|       |                            |            |     |                          |   Other                |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 11    | AlternateIdentifier        | R          | 0-n | Identifiers other than   | Free text, should be   |
|       |                            |            |     | the DOI pertaining to    | unique identifiers     |
|       |                            |            |     | the same instrument      |                        |
|       |                            |            |     | instance.  This should   |                        |
|       |                            |            |     | be used if the           |                        |
|       |                            |            |     | instrument has a serial  |                        |
|       |                            |            |     | number.  Other possible  |                        |
|       |                            |            |     | uses include an owner's  |                        |
|       |                            |            |     | inventory number or an   |                        |
|       |                            |            |     | entry in some instrument |                        |
|       |                            |            |     | data base.               |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 11.1  | alternateIdentifierType    | R          | 1   | Type of the identifier   | Free text.  Mandatory  |
|       |                            |            |     |                          | if AlternateIdentifier |
|       |                            |            |     |                          | is used.  Suggested    |
|       |                            |            |     |                          | values include:        |
|       |                            |            |     |                          |   serialNumber         |
|       |                            |            |     |                          |   inventoryNumber      |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 12    | RelatedIdentifier          | R          | 0-n | Identifiers of related   | Free text, must be     |
|       |                            |            |     | resources                | globally unique        |
|       |                            |            |     |                          | identifiers.           |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 12.1  | relatedIdentifierType      | R          | 1   | Type of the identifier   | Controlled list of     |
|       |                            |            |     |                          | values, see DataCite   |
|       |                            |            |     |                          | schema                 |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 12.2  | relationType               | R          | 1   | Description of the       | Controlled list of     |
|       |                            |            |     | relationship             | values, see DataCite   |
|       |                            |            |     |                          | schema [#reltype]_     |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 12.3  | relatedMetaDataScheme      | O          | 0-1 | The name of the related  | Use only for           |
|       |                            |            |     | metadata scheme          | HasMetadata            |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 12.4  | schemeURI                  | O          | 0-1 | The URI of the related   | Use only for           |
|       |                            |            |     | metadata scheme          | HasMetadata            |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 12.5  | schemeType                 | O          | 0-1 | The type of the related  | Use only for           |
|       |                            |            |     | metadata scheme          | HasMetadata            |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 12.6  | resourceTypeGeneral        | O          | 0-1 | The general type of the  | Controlled list of     |
|       |                            |            |     | related resource         | values, see DataCite   |
|       |                            |            |     |                          | schema                 |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 17    | Description                | R          | 0-1 | Technical description    | Free text              |
|       |                            |            |     | of the device and its    |                        |
|       |                            |            |     | capabilities             |                        |
+-------+----------------------------+------------+-----+--------------------------+------------------------+
| 17.1  | descriptionType            | R          | 1   | The type of the          | Controlled list of     |
|       |                            |            |     | description              | values:[#desctype]_    |
|       |                            |            |     |                          |   Abstract             |
|       |                            |            |     |                          |   Methods              |
|       |                            |            |     |                          |   SeriesInformation    |
|       |                            |            |     |                          |   TableOfContents      |
|       |                            |            |     |                          |   TechnicalInfo        |
|       |                            |            |     |                          |   Other                |
+-------+----------------------------+------------+-----+--------------------------+------------------------+


Footnotes
---------

.. [#identtype] If registering the PID with DataCite, it will
   forcibly be a DOI.
.. [#cr_nametype] The manufacturer of an instrument will most likely
   be an organization.  In that case, `nameType` should be provided
   with a value of "Organizational".
.. [#cr_affiliation] If the manufacturer is an organization,
   `affiliation` will be redundant with `creatorName`.  It may be
   useful nevertheless to repeat that value in `affiliation` to
   facilitate organization searches.
.. [#titletype] None of the specific values for `titleType` in the
   DataCite schema really fits an instrument name. The value "Other"
   will need to be used here.
.. [#publisher] `Publisher` does not seem to fit at all for
   instruments.  But it is mandatory in the DataCite schema, so we can
   not skip it.  Need to negotiate with DataCite what to put here.
   Maybe the institution responsible to manage this DOI record and its
   metadata?
.. [#pubyear] Similar problem for `PublicationYear` as for
   `Publisher`.
.. [#subject] Use `Subject` for the classification of the type of the
   instrument.
.. [#contributor] `Contributor` with
   `contributorType=HostingInstitution` should be used for the owner
   of the instrument.  Other contributor types as permitted by the
   DataCite schema are of course possible, but are not considered in
   this presentation.  Note that `Contributor` is only recommended in
   the DataCite schema, but at least one owner (e.g. `Contributor`
   with `contributorType=HostingInstitution`) should be considered
   mandatory for instruments.
.. [#cntrb_sub] Same remarks as for the subproperties `nameType` and
   `affiliation` of `Creator` also applies to the corresponding
   subproperties of `Contributor`.
.. [#date] Use `Date` with `dateType=Available` to indicate when the
   instrument was in operation, either with a single date to indicate
   when this instrument instance started operation, or a date interval
   if this instrument instance ceased to be in operation.
.. [#restypegen] None of the specific values for `resourceTypeGeneral`
   in the DataCite schema fits an instrument. This leaves "Other" as
   the only option.
.. [#reltype] Use "HasPart" and "IsPartOf" in lieu of "HasComponent"
   and "IsComponentOf".
.. [#desctype] Not all of the listed values for `descriptionType`
   make sense for an instrument description.  "TechnicalInfo" should
   be used for a technical description.


Notes and Issues
----------------

In the following, we collect some issues with the mapping of the
instrument metadata schema onto DataCite as presented above, roughly
ordered by increasing importance, from least concern to critical:

+ There is no `LandingPage` property in the DataCite schema.
  Nevertheless, the URL of a landing page is registered with every
  DataCite DOI in the practice.  As long as there actually is a
  landing page that the instrument PID resolves to, it is considered
  mostly an esthetic question whether this is explicitely named in the
  schema or not.

+ There is no suitable place for `VariableMeasured` in the DataCite
  schema.  On the other hand, honestly speaking, the concepts for
  representing this information in our general schema have not been
  very advanced either.  Linking some external resource with
  `RelatedIdentifier` / `relationType=HasMetadata` using some
  externally defined ontology seem to be the most viable approach
  anyway.

+ It should be possible to tell from the PID and its metadata that
  this one pertains to an instrument and not any other kind of
  resource.  The only property in the DataCite schema suitable to hold
  this information is `ResourceType` and its subproperty
  `resourceTypeGeneral`.  `ResourceType` is free text which does not
  offer a reliable classification.  The only usuable value for
  `resourceTypeGeneral` is "Other".  It would be desirable to add
  "Instrument" to the controlled list of values for
  `resourceTypeGeneral`.

+ It is not obvious that the name of the instrument would be in
  `Title`.  This difficulty is even aggravated by the fact that there
  is no suitable specific value for `titleType` for this purpose.  It
  would be desirable to add "Name" to the controlled list of values
  for `titleType`.  This could also be useful for other resources then
  instruments, if they have a well known name.

+ It is not clear what to put into `Publisher` and `PublicationYear`
  for instruments.

+ The only suitable property to store a serial number is
  `AlternateIdentifier`.  It has been argued in the group that for
  this approach to be useful one would need to have a controlled list
  of values for `alternateIdentifierType` that includes an entry for
  "serialNumber", although there has not been a consensus on this.  It
  has also been argued that such a controlled list of values would be
  impractical for some other use cases.  This is still an unresolved
  issue also in the general schema.

+ As mentioned above, some of the definitions in the DataCite schema
  need to be significantly stretched in order to squeeze the relevant
  metadata for instruments in.  It is not obvious what piece of
  information should be put where.  It seems that some sort of a
  dedicated handbook on how to correctly create instrument metadata
  using this schema will be needed.  The existing general DataCite
  documentation will not be enough.

+ There is no suitable place to put the model name of the instrument,
  although this is considered a very important piece of information.
  
  It has been suggested to use `AlternateIdentifier`, but that does
  not fit: `AlternateIdentifier` is for alternate identifiers that
  pertain to the same individual instrument instance.  A model name
  identifies a series of instruments having the same or similar
  specifications, but not an individual instrument.


.. _DataCite Metadata Schema 4.2: https://schema.datacite.org/meta/kernel-4.2/
