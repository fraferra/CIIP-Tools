#List of constants used for the models 
COORDINATOR = (
    ('yes', 'yes'),
    ('no','no'),
)
LISTED = (
    ('yes', 'yes'),
    ('no','no'),
    )
UNIVERSITY_ENDORSEMENT = (
    ('Strongly recommended','Strongly recommended'),
    ('Recommended','Recommended'),
    ('Not recommended', 'Not recommended'),
)
MANAGER_ENDORSEMENT = (
    ('---','---'),
    ('1-Highly recommended','1-Highly recommended'),
    ('2-Recommended','2-Recommended'),
    ('2.5','2.5'),
    ('3-Not recommended', '3-Not recommended'),
)
MASTER_UNDER = (
    ('---','---'),
    ('Undergraduate','Undergraduate'),
    ('Master','Master'),
    ('PhD', 'PhD')
)
UNIVERSITY_ROLE = (
       ('Tutor', 'Tutor'),
       ('Mentor','Mentor'),
       ('University Professor', 'University Professor'),
       ('Employeer', 'Employeer'),
)
STATUS_UPDATES = (
    ('In consideration', 'In consideration'),
    ('First Interview Scheduled','First Interview Scheduled'),
    ('First Interview Passed', 'First Interview Passed'),
    ('Interview with Manager Scheduled', 'Interview with Manager Scheduled'),
    ('On Hold', 'On Hold'),
    ('Withdrawn', 'Withdrawn'),
    ('Accepted', 'Accepted'),
    ('Declined', 'Declined'),
)

INTERVIEW_RESPONSE = (
    ('Accept', 'Accept'),
    ('Decline', 'Decline'),
    ('Request reschedule', 'Request reschedule'),
)

YEAR_OF_GRADUATION = (
    ('2014','2014'),
    ('2015','2015'),
    ('2016','2016'),
    ('2017','2017'),
)

PASSPORT = (
    ('Yes', 'Yes'),
    ('No','No'),
)

PROJECTS=(
   ('IT or Networking Academy', 'IT or Networking Academy'),
   ('Marketing or IT', 'Marketing or IT'),
   ('Sales or Marketing', 'Sales or Marketing'),
   ('Technology radar','Technology radar'),
   ('Security / Bret Hartman', 'Security / Bret Hartman'),
   ('Openstack / Big Data / Natural Language Processing /Research', 'Openstack / Big Data / Natural Language Processing /Research'),
   ('Corporate Technology Group or IT', 'Corporate Technology Group or IT'),
   ('Dave Ward Group or ENG','Dave Ward Group or ENG'),
   ('CTAO', 'CTAO'),
   ('Research','Research'),
   ('Machine Learning / Security', 'Machine Learning / Security'),
   ('SDN / Engineering','SDN / Engineering'),
   ('Openstack / Engineering','Openstack / Engineering'),
   ('IT','IT'),
   ('CSTG','CSTG'),
   ('GIS / IT','GIS / IT'),
   ('Collaboration / IT','Collaboration / IT'),
   ('Security / Engineering','Security / Engineering'),
   ('Marketing','Marketing'),
   ('Sales','Sales'),
   ('Engineering','Engineering'),
   ('Cloud / Engineering','Cloud / Engineering'),
   ('CIIP Tools / Engineering','CIIP Tools / Engineering'),
   ('CSMTG / Engineering','CSMTG / Engineering'),
   ('ONE PK / Engineering', 'ONE PK / Engineering'),
   ('CSMTG or Data Center/UCS Manager','CSMTG or Data Center/UCS Manager'),
   ('IT / Marketing or Services / TAC','IT / Marketing or Services / TAC'),
   ('Collaboration or IT', 'Collaboration or IT'),
   ('User Experience or Collaboration','User Experience or Collaboration'),
   ('App layer / Android - IT or Collaboration','App layer / Android - IT or Collaboration'),
   ('App layer- CSMTG / IT / SPVSS / CTG', 'App layer- CSMTG / IT / SPVSS / CTG'),
   ('IT or Test Engineering','IT or Test Engineering'),
   ('Research Journal Editor / Marketing','Research Journal Editor / Marketing'),


)

GENDER = (
    ('male', 'male'),
    ('female','female'),
)

SKILL_LEVEL = (
    ('Advanced','Advanced'),
    ('Intermediate','Intermediate'),
    ('Beginner','Beginner'),
    ('None','None'),
)

UNIVERSITY_CHOICES = (
    ('UCL', 'UCL'),
    ('Kent', 'Kent'),
    ('EPFL', 'EPFL'),
    ('Keio','Keio'),
    ('ZJU', 'ZJU'),
    ('BMSTU','BMSTU'),
    ('CTU', 'CTU'),
    ('Tsinghua', 'Tsinghua'),
    ('UNSW', 'UNSW'),
    ('IIT Roorkee', 'IIT Roorkee'),
    ('IIT Gandhinagar', 'IIT Gandhinagar'),
)

COUNTRIES = (
    ('AD', 'Andorra'),
    ('AE', 'United Arab Emirates'),
    ('AF', 'Afghanistan'),
    ('AG', 'Antigua & Barbuda'),
    ('AI', 'Anguilla'),
    ('AL', 'Albania'),
    ('AM', 'Armenia'),
    ('AN', 'Netherlands Antilles'),
    ('AO', 'Angola'),
    ('AQ', 'Antarctica'),
    ('AR', 'Argentina'),
    ('AS', 'American Samoa'),
    ('AT', 'Austria'),
    ('AU', 'Australia'),
    ('AW', 'Aruba'),
    ('AZ', 'Azerbaijan'),
    ('BA', 'Bosnia and Herzegovina'),
    ('BB', 'Barbados'),
    ('BD', 'Bangladesh'),
    ('BE', 'Belgium'),
    ('BF', 'Burkina Faso'),
    ('BG', 'Bulgaria'),
    ('BH', 'Bahrain'),
    ('BI', 'Burundi'),
    ('BJ', 'Benin'),
    ('BM', 'Bermuda'),
    ('BN', 'Brunei Darussalam'),
    ('BO', 'Bolivia'),
    ('BR', 'Brazil'),
    ('BS', 'Bahama'),
    ('BT', 'Bhutan'),
    ('BV', 'Bouvet Island'),
    ('BW', 'Botswana'),
    ('BY', 'Belarus'),
    ('BZ', 'Belize'),
    ('CA', 'Canada'),
    ('CC', 'Cocos (Keeling) Islands'),
    ('CF', 'Central African Republic'),
    ('CG', 'Congo'),
    ('CH', 'Switzerland'),
    ('CI', 'Ivory Coast'),
    ('CK', 'Cook Iislands'),
    ('CL', 'Chile'),
    ('CM', 'Cameroon'),
    ('CN', 'China'),
    ('CO', 'Colombia'),
    ('CR', 'Costa Rica'),
    ('CU', 'Cuba'),
    ('CV', 'Cape Verde'),
    ('CX', 'Christmas Island'),
    ('CY', 'Cyprus'),
    ('CZ', 'Czech Republic'),
    ('DE', 'Germany'),
    ('DJ', 'Djibouti'),
    ('DK', 'Denmark'),
    ('DM', 'Dominica'),
    ('DO', 'Dominican Republic'),
    ('DZ', 'Algeria'),
    ('EC', 'Ecuador'),
    ('EE', 'Estonia'),
    ('EG', 'Egypt'),
    ('EH', 'Western Sahara'),
    ('ER', 'Eritrea'),
    ('ES', 'Spain'),
    ('ET', 'Ethiopia'),
    ('FI', 'Finland'),
    ('FJ', 'Fiji'),
    ('FK', 'Falkland Islands (Malvinas)'),
    ('FM', 'Micronesia'),
    ('FO', 'Faroe Islands'),
    ('FR', 'France'),
    ('FX', 'France, Metropolitan'),
    ('GA', 'Gabon'),
    ('GB', 'United Kingdom (Great Britain)'),
    ('GD', 'Grenada'),
    ('GE', 'Georgia'),
    ('GF', 'French Guiana'),
    ('GH', 'Ghana'),
    ('GI', 'Gibraltar'),
    ('GL', 'Greenland'),
    ('GM', 'Gambia'),
    ('GN', 'Guinea'),
    ('GP', 'Guadeloupe'),
    ('GQ', 'Equatorial Guinea'),
    ('GR', 'Greece'),
    ('GS', 'South Georgia and the South Sandwich Islands'),
    ('GT', 'Guatemala'),
    ('GU', 'Guam'),
    ('GW', 'Guinea-Bissau'),
    ('GY', 'Guyana'),
    ('HK', 'Hong Kong'),
    ('HM', 'Heard & McDonald Islands'),
    ('HN', 'Honduras'),
    ('HR', 'Croatia'),
    ('HT', 'Haiti'),
    ('HU', 'Hungary'),
    ('ID', 'Indonesia'),
    ('IE', 'Ireland'),
    ('IL', 'Israel'),
    ('IN', 'India'),
    ('IO', 'British Indian Ocean Territory'),
    ('IQ', 'Iraq'),
    ('IR', 'Islamic Republic of Iran'),
    ('IS', 'Iceland'),
    ('IT', 'Italy'),
    ('JM', 'Jamaica'),
    ('JO', 'Jordan'),
    ('JP', 'Japan'),
    ('KE', 'Kenya'),
    ('KG', 'Kyrgyzstan'),
    ('KH', 'Cambodia'),
    ('KI', 'Kiribati'),
    ('KM', 'Comoros'),
    ('KN', 'St. Kitts and Nevis'),
    ('KP', 'Korea, Democratic People\'s Republic of'),
    ('KR', 'Korea, Republic of'),
    ('KW', 'Kuwait'),
    ('KY', 'Cayman Islands'),
    ('KZ', 'Kazakhstan'),
    ('KS', 'Kosova'),
    ('LA', 'Lao People\'s Democratic Republic'),
    ('LB', 'Lebanon'),
    ('LC', 'Saint Lucia'),
    ('LI', 'Liechtenstein'),
    ('LK', 'Sri Lanka'),
    ('LR', 'Liberia'),
    ('LS', 'Lesotho'),
    ('LT', 'Lithuania'),
    ('LU', 'Luxembourg'),
    ('LV', 'Latvia'),
    ('LY', 'Libyan Arab Jamahiriya'),
    ('MA', 'Morocco'),
    ('MC', 'Monaco'),
    ('MD', 'Moldova, Republic of'),
    ('MG', 'Madagascar'),
    ('MH', 'Marshall Islands'),
    ('ML', 'Mali'),
    ('MN', 'Mongolia'),
    ('MM', 'Myanmar'),
    ('MO', 'Macau'),
    ('MP', 'Northern Mariana Islands'),
    ('MQ', 'Martinique'),
    ('MR', 'Mauritania'),
    ('MS', 'Monserrat'),
    ('MT', 'Malta'),
    ('MU', 'Mauritius'),
    ('MV', 'Maldives'),
    ('MW', 'Malawi'),
    ('MX', 'Mexico'),
    ('MY', 'Malaysia'),
    ('MZ', 'Mozambique'),
    ('NA', 'Namibia'),
    ('NC', 'New Caledonia'),
    ('NE', 'Niger'),
    ('NF', 'Norfolk Island'),
    ('NG', 'Nigeria'),
    ('NI', 'Nicaragua'),
    ('NL', 'Netherlands'),
    ('NO', 'Norway'),
    ('NP', 'Nepal'),
    ('NR', 'Nauru'),
    ('NU', 'Niue'),
    ('NZ', 'New Zealand'),
    ('OM', 'Oman'),
    ('PA', 'Panama'),
    ('PE', 'Peru'),
    ('PF', 'French Polynesia'),
    ('PG', 'Papua New Guinea'),
    ('PH', 'Philippines'),
    ('PK', 'Pakistan'),
    ('PL', 'Poland'),
    ('PM', 'St. Pierre & Miquelon'),
    ('PN', 'Pitcairn'),
    ('PR', 'Puerto Rico'),
    ('PT', 'Portugal'),
    ('PW', 'Palau'),
    ('PY', 'Paraguay'),
    ('QA', 'Qatar'),
    ('RE', 'Reunion'),
    ('RO', 'Romania'),
    ('RU', 'Russian Federation'),
    ('RW', 'Rwanda'),
    ('SA', 'Saudi Arabia'),
    ('SB', 'Solomon Islands'),
    ('SC', 'Seychelles'),
    ('SD', 'Sudan'),
    ('SE', 'Sweden'),
    ('SG', 'Singapore'),
    ('SH', 'St. Helena'),
    ('SI', 'Slovenia'),
    ('SJ', 'Svalbard & Jan Mayen Islands'),
    ('SK', 'Slovakia'),
    ('SL', 'Sierra Leone'),
    ('SM', 'San Marino'),
    ('SN', 'Senegal'),
    ('SO', 'Somalia'),
    ('SR', 'Suriname'),
    ('ST', 'Sao Tome & Principe'),
    ('SV', 'El Salvador'),
    ('SY', 'Syrian Arab Republic'),
    ('SZ', 'Swaziland'),
    ('TC', 'Turks & Caicos Islands'),
    ('TD', 'Chad'),
    ('TF', 'French Southern Territories'),
    ('TG', 'Togo'),
    ('TH', 'Thailand'),
    ('TJ', 'Tajikistan'),
    ('TK', 'Tokelau'),
    ('TM', 'Turkmenistan'),
    ('TN', 'Tunisia'),
    ('TO', 'Tonga'),
    ('TP', 'East Timor'),
    ('TR', 'Turkey'),
    ('TT', 'Trinidad & Tobago'),
    ('TV', 'Tuvalu'),
    ('TW', 'Taiwan, Province of China'),
    ('TZ', 'Tanzania, United Republic of'),
    ('UA', 'Ukraine'),
    ('UG', 'Uganda'),
    ('UM', 'United States Minor Outlying Islands'),
    ('US', 'United States of America'),
    ('UY', 'Uruguay'),
    ('UZ', 'Uzbekistan'),
    ('VA', 'Vatican City State (Holy See)'),
    ('VC', 'St. Vincent & the Grenadines'),
    ('VE', 'Venezuela'),
    ('VG', 'British Virgin Islands'),
    ('VI', 'United States Virgin Islands'),
    ('VN', 'Viet Nam'),
    ('VU', 'Vanuatu'),
    ('WF', 'Wallis & Futuna Islands'),
    ('WS', 'Samoa'),
    ('YE', 'Yemen'),
    ('YT', 'Mayotte'),
    ('YU', 'Yugoslavia'),
    ('ZA', 'South Africa'),
    ('ZM', 'Zambia'),
    ('ZR', 'Zaire'),
    ('ZW', 'Zimbabwe'),
    ('ZZ', 'Unknown or unspecified country'),
)  



