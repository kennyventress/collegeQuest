# TITLE: title_code_dict.py
# DATE: July 25th, 2023
# PURPOSE: API requests that filter by major name have trouble accessing majors whose names have commas in them
#          (ex. "Biology, General"). To get around this, the dictionary below will match a major name to its
#          unique major code number. This way, the user can input any major name, and majors that contain the
#          user's input can be gathered from the API via the major code (ie. inexact searches are possible). 
#          Ex. the user can input  "Biology" and the API will return majors containing the word "Biology", 
#          so "Biology, General.", "Biochemistry, Biophysics and Molecular Biology.", etc. would be matching majors.
#          NOTE: Not all majors are here! There were crashes while trying to access API Data beyond page 36 or 37, out of
#                68 or so pages, so don't be alarmed.


title_code_dict = {
  "Natural Resources Conservation and Research.": "0301",
  "Area Studies.": "0501",
  "Ethnic, Cultural Minority, Gender, and Group Studies.": "0502",
  "Communication and Media Studies.": "0901",
  "Computer Science.": "1107",
  "Engineering, General.": "1401",
  "Linguistic, Comparative, and Related Language Studies and Services.": "1601",
  "East Asian Languages, Literatures, and Linguistics.": "1603",
  "Slavic, Baltic and Albanian Languages, Literatures, and Linguistics.": "1604",
  "Germanic Languages, Literatures, and Linguistics.": "1605",
  "Romance Languages, Literatures, and Linguistics.": "1609",
  "Classics and Classical Languages, Literatures, and Linguistics.": "1612",
  "English Language and Literature, General.": "2301",
  "Biology, General.": "2601",
  "Biochemistry, Biophysics and Molecular Biology.": "2602",
  "Neurobiology and Neurosciences.": "2615",
  "Mathematics.": "2701",
  "Medieval and Renaissance Studies.": "3013",
  "Science, Technology and Society.": "3015",
  "Cognitive Science.": "3025",
  "Multi/Interdisciplinary Studies, Other.": "3099",
  "Philosophy.": "3801",
  "Religion/Religious Studies.": "3802",
  "Chemistry.": "4005",
  "Geological and Earth Sciences/Geosciences.": "4006",
  "Physics.": "4008",
  "Psychology, General.": "4201",
  "Research and Experimental Psychology.": "4227",
  "Public Policy Analysis.": "4405",
  "Anthropology.": "4502",
  "Economics.": "4506",
  "International Relations and National Security Studies.": "4509",
  "Political Science and Government.": "4510",
  "Sociology.": "4511",
  "Dance.": "5003",
  "Drama/Theatre Arts and Stagecraft.": "5005",
  "Fine and Studio Arts.": "5007",
  "Music.": "5009",
  "History.": "5401",
  "Agriculture, General.": "0100",
  "Agricultural Business and Management.": "0101",
  "Computer and Information Sciences, General.": "1101",
  "Teaching Assistants/Aides.": "1315",
  "Industrial Production Technologies/Technicians.": "1506",
  "Human Development, Family Studies, and Related Services.": "1907",
  "Liberal Arts and Sciences, General Studies and Humanities.": "2401",
  "Biological and Physical Sciences.": "3001",
  "Health and Physical Education/Fitness.": "3105",
  "Criminal Justice and Corrections.": "4301",
  "Fire Protection.": "4302",
  "Public Administration and Social Service Professions, Other.": "4499",
  "Social Sciences, General.": "4501",
  "Precision Metal Working.": "4805",
  "Design and Applied Arts.": "5004",
  "Film/Video and Photographic Arts.": "5006",
  "Allied Health Diagnostic, Intervention, and Treatment Professions.": "5109",
  "Mental and Social Health Services and Allied Professions.": "5115",
  "Registered Nursing, Nursing Administration, Nursing Research and Clinical Nursing.": "5138",
  "Practical Nursing, Vocational Nursing and Nursing Assistants.": "5139",
  "Business/Commerce, General.": "5201",
  "Business Administration, Management and Operations.": "5202",
  "Accounting and Related Services.": "5203",
  "Business Operations Support and Assistant Services.": "5204",
  "Cosmetology and Related Personal Grooming Services.": "1204",
  "Journalism.": "0904",
  "Radio, Television, and Digital Communication.": "0907",
  "Public Relations, Advertising, and Applied Communication.": "0909",
  "Audiovisual Communications Technologies/Technicians.": "1002",
  "Graphic Communications.": "1003",
  "Computer Programming.": "1102",
  "Computer Software and Media Applications.": "1108",
  "Computer Systems Networking and Telecommunications.": "1109",
  "Computer/Information Technology Administration and Management.": "1110",
  "Culinary Arts and Related Services.": "1205",
  "Special Education and Teaching.": "1310",
  "Engineering Technology, General.": "1500",
  "Electromechanical Instrumentation and Maintenance Technologies/Technicians.": "1504",
  "Environmental Control Technologies/Technicians.": "1505",
  "Drafting/Design Engineering Technologies/Technicians.": "1513",
  "American Sign Language.": "1616",
  "Family and Consumer Sciences/Human Sciences, General.": "1901",
  "Foods, Nutrition, and Related Services.": "1905",
  "Apparel and Textiles.": "1909",
  "Non-Professional General Legal Studies (Undergraduate).": "2200",
  "Legal Support Services.": "2203",
  "Library and Archives Assisting.": "2503",
  "Human Services, General.": "4400",
  "Geography and Cartography.": "4507",
  "Building/Construction Finishing, Management, and Inspection.": "4604",
  "Electrical/Electronics Maintenance and Repair Technology.": "4701",
  "Heavy/Industrial Equipment Maintenance Technologies.": "4703",
  "Vehicle Maintenance and Repair Technologies.": "4706",
  "Visual and Performing Arts, General.": "5001",
  "Health Services/Allied Health/Health Sciences, General.": "5100",
  "Communication Disorders Sciences and Services.": "5102",
  "Allied Health and Medical Assisting Services.": "5108",
  "Health/Medical Preparatory Programs.": "5111",
  "Entrepreneurial and Small Business Operations.": "5207",
  "International Business.": "5211",
  "Real Estate.": "5215",
  "General Sales, Merchandising and Related Marketing Operations.": "5218",
  "Business, Management, Marketing, and Related Support Services, Other.": "5299",
  "Natural Resources Management and Policy.": "0302",
  "Information Science/Studies.": "1104",
  "Education, General.": "1301",
  "Curriculum and Instruction.": "1303",
  "Educational Administration and Supervision.": "1304",
  "Student Counseling and Personnel Services.": "1311",
  "Teacher Education and Professional Development, Specific Levels and Methods.": "1312",
  "Teacher Education and Professional Development, Specific Subject Areas.": "1313",
  "Rhetoric and Composition/Writing Studies.": "2313",
  "Theological and Ministerial Studies.": "3906",
  "Theology and Religious Vocations, Other.": "3999",
  "Clinical, Counseling and Applied Psychology.": "4228",
  "Arts, Entertainment,and Media Management.": "5010",
  "Health and Medical Administrative Services.": "5107",
  "Business/Managerial Economics.": "5206",
  "Finance and Financial Management Services.": "5208",
  "Human Resources Management and Services.": "5210",
  "Marketing.": "5214",
  "Agricultural Production Operations.": "0103",
  "Forestry.": "0305",
  "Energy Systems Technologies/Technicians.": "1517",
  "Science Technologies/Technicians, Other.": "4199",
  "Carpenters.": "4602",
  "Electrical and Power Transmission Installers.": "4603",
  "Woodworking.": "4807",
  "Dental Support Services and Allied Professions.": "5106",
  "Hospitality Administration/Management.": "5209",
  "Architectural Sciences and Technology.": "0409",
  "Education, Other.": "1399",
  "Mechanical Engineering Related Technologies/Technicians.": "1508",
  "Demography and Population Studies.": "4505",
  "Clinical/Medical Laboratory Science/Research and Allied Professions.": "5110",
  "Computer Systems Analysis.": "1105",
  "Data Entry/Microcomputer Applications.": "1106",
  "Computer and Information Sciences and Support Services, Other.": "1199",
  "Security Science and Technology.": "4304",
  "Leatherworking and Upholstery.": "4803",
  "Taxation.": "5216",
  "Medicine.": "5112",
  "Alternative and Complementary Medicine and Medical Systems.": "5133",
  "Electrical, Electronics and Communications Engineering.": "1410",
  "Engineering-Related Technologies.": "1511",
  "Physical Science Technologies/Technicians.": "4103",
  "Air Transportation.": "4901",
  "Ground Transportation.": "4902",
  "Public Health.": "5122",
  "Management Information Systems and Services.": "5212",
  "Applied Horticulture and Horticultural Business Services.": "0106",
  "Educational/Instructional Media Design.": "1305",
  "Middle/Near Eastern and Semitic Languages, Literatures, and Linguistics.": "1611",
  "Physical Sciences.": "4001",
  "Astronomy and Astrophysics.": "4002",
  "Marine Transportation.": "4903",
  "Specialized Sales, Merchandising and  Marketing Operations.": "5219",
  "Podiatric Medicine/Podiatry.": "5121",
  "Rehabilitation and Therapeutic Professions.": "5123",
  "Electrical Engineering Technologies/Technicians.": "1503",
  "Computer Engineering Technologies/Technicians.": "1512",
  "Engineering Technologies/Technicians, Other.": "1599",
  "Microbiological Sciences and Immunology.": "2605",
  "Archeology.": "4503",
  "Plumbing and Related Water Supply Services.": "4605",
  "Visual and Performing Arts, Other.": "5099",
  "Health Professions and Related Clinical Sciences, Other.": "5199",
  "Food Science and Technology.": "0110",
  "Veterinary/Animal Health Technologies/Technicians.": "0183",
  "Landscape Architecture.": "0406",
  "Southeast Asian and Australasian/Pacific Languages, Literatures, and Linguistics.": "1614",
  "Physiology, Pathology and Related Sciences.": "2609",
  "Nutrition Sciences.": "3019",
  "Construction Management.": "5220",
  "City/Urban, Community and Regional Planning.": "0403",
  "Bilingual, Multilingual, and Multicultural Education.": "1302",
  "Teaching English or French as a Second or Foreign Language.": "1314",
  "Aerospace, Aeronautical and Astronautical Engineering.": "1402",
  "Biomedical/Medical Engineering.": "1405",
  "Civil Engineering.": "1408",
  "Computer Engineering.": "1409",
  "Engineering Science.": "1413",
  "Environmental/Environmental Health Engineering.": "1414",
  "Mechanical Engineering.": "1419",
  "Manufacturing Engineering.": "1436",
  "Engineering, Other.": "1499",
  "Quality Control and Safety Technologies/Technicians.": "1507",
  "Construction Engineering Technologies.": "1510",
  "Housing and Human Environments.": "1906",
  "Zoology/Animal Biology.": "2607",
  "Biomathematics, Bioinformatics, and Computational Biology.": "2611",
  "Ecology, Evolution, Systematics, and Population Biology.": "2613",
  "Applied Mathematics.": "2703",
  "Statistics.": "2705",
  "Mathematics and Computer Science.": "3008",
  "Gerontology.": "3011",
  "International/Global Studies.": "3020",
  "Computational Science.": "3030",
  "Parks, Recreation and Leisure Studies.": "3101",
  "Public Administration.": "4404",
  "Social Work.": "4407",
  "Criminology.": "4504",
  "Urban Studies/Affairs.": "4512",
  "Social Sciences, Other.": "4599",
  "Pharmacy, Pharmaceutical Sciences, and Administration.": "5120",
  "Dietetics and Clinical Nutrition Services.": "5131",
  "Architectural History and Criticism.": "0408",
  "Industrial Engineering.": "1435",
  "Law.": "2201",
  "Legal Research and Advanced Professional Studies.": "2202",
  "Legal Professions and Studies, Other.": "2299",
  "Peace Studies and Conflict Resolution.": "3005",
  "Data Analytics.": "3071",
  "Medical Illustration and Informatics.": "5127",
  "Management Sciences and Quantitative Methods.": "5213",
  "Museology/Museum Studies.": "3014",
  "Systems Engineering.": "1427",
  "Botany/Plant Biology.": "2603",
  "Cell/Cellular Biology and Anatomical Sciences.": "2604",
  "Behavioral Sciences.": "3017",
  "Natural Sciences.": "3018",
  "Marine Sciences.": "3032",
  "Health-Related Knowledge and Skills.": "3401",
  "Philosophy and Religious Studies, Other.": "3899",
  "Bioethics/Medical Ethics.": "5132",
  "Architecture.": "0402",
  "Data Processing.": "1103",
  "Biotechnology.": "2612",
  "Agricultural Mechanization.": "0102",
  "Homeland Security, Law Enforcement, Firefighting and Related Protective Services, Other.": "4399",
  "Heating, Air Conditioning, Ventilation and Refrigeration Maintenance Technology/Technician (HAC, HACR, HVAC, HVACR).": "4702",
  "Somatic Bodywork and Related Therapeutic Services.": "5135",
  "Bible/Biblical Studies.": "3902",
  "Missions/Missionary Studies and Missiology.": "3903",
  "Religious Education.": "3904",
  "Pastoral Counseling and Specialized Ministries.": "3907",
  "Communication, Journalism, and Related Programs, Other.": "0999",
  "Construction Trades, General.": "4600",
  "International and Comparative Education.": "1307",
  "Chemical Engineering.": "1407",
  "Materials Engineering": "1418",
  "Engineering-Related Fields.": "1515",
  "Library Science and Administration.": "2501",
  "Biological and Biomedical Sciences, Other.": "2699",
  "Human Computer Interaction.": "3031",
  "Atmospheric Sciences and Meteorology.": "4004",
  "Psychology, Other.": "4299",
  "Foreign Languages, Literatures, and Linguistics, Other.": "1699",
  "Engineering Physics.": "1412",
  "Classical and Ancient Studies.": "3022",
  "Insurance.": "5217",
  "Plant Sciences.": "0111",
  "Agriculture, Agriculture Operations, and Related Sciences, Other.": "0199",
  "Parks, Recreation and Leisure Facilities Management.": "3103",
  "Health Aides/Attendants/Orderlies.": "5126",
  "Systems Science and Theory.": "3006",
  "Human Biology.": "3027",
  "Family and Consumer Sciences/Human Sciences, Other.": "1999",
  "English Language and Literature/Letters, Other.": "2399",
  "Leisure and Recreational Activities.": "3601",
  "Ophthalmic and Optometric Support Services and Allied Professions.": "5118",
  "Biology Technician/Biotechnology Laboratory Technician.": "4101",
  "Mathematics and Statistics, Other.": "2799",
  "Biopsychology.": "3010",
  "Historic Preservation and Conservation.": "3012",
  "Religious/Sacred Music.": "3905",
  "Basic Skills and Developmental/Remedial Education.": "3201",
  "Philosophy and Religious Studies, General.": "3800",
  "Optometry.": "5117",
  "Educational Assessment, Evaluation, and Research.": "1306",
  "Environmental Design.": "0404",
  "Real Estate Development.": "0410",
  "Architecture and Related Services, Other.": "0499",
  "Architectural Engineering.": "1404",
  "Petroleum Engineering.": "1425",
  "Operations Research.": "1437",
  "Electrical and Computer Engineering.": "1447",
  "Genetics.": "2608",
  "Pharmacology and Toxicology.": "2610",
  "Molecular Medicine.": "2614",
  "Intelligence, Command Control and Information Operations.": "2902",
  "Military Technologies and Applied Sciences, Other.": "2999",
  "Multi-/Interdisciplinary Studies, General.": "3000",
  "Dispute Resolution.": "3028",
  "Sustainability Studies.": "3033",
  "Materials Sciences.": "4010",
  "Dentistry.": "5104",
  "Advanced/Graduate Dentistry and Oral Sciences.": "5105",
  "Medical Clinical Sciences/Graduate Medical Studies.": "5114",
  "Dental Residency Programs.": "6001",
  "Physical Sciences, Other.": "4099",
  "Nursing.": "5116",
  "Agricultural and Domestic Animal Services.": "0105",
  "Architectural Engineering Technologies/Technicians.": "1501",
  "Construction Trades, Other.": "4699",
  "Homeland Security.": "4303",
  "Business/Corporate Communications.": "5205",
  "Interior Architecture.": "0405",
  "Crafts/Craft Design, Folk Art and Artisanry.": "5002",
  "Communications Technology/Technician.": "1001",
  "Mining and Petroleum Technologies/Technicians.": "1509",
  "Funeral Service and Mortuary Science.": "1203",
  "Agriculture/Veterinary Preparatory Programs.": "0113",
  "Mechanic and Repair Technologies/Technicians, Other.": "4799",
  "Social and Philosophical Foundations of Education.": "1309",
  "Biochemical Engineering.": "1443",
  "Community Organization and Advocacy.": "4402",
  "Outdoor Education.": "3106",
  "Religious Institution Administration and Law.": "3908",
  "Precision Systems Maintenance and Repair Technologies.": "4704",
  "Metallurgical Engineering.": "1420",
  "Mining and Mineral Engineering.": "1421",
  "Nuclear Engineering.": "1423",
  "Geological/Geophysical Engineering.": "1439",
  "Mechatronics, Robotics, and Automation Engineering.": "1442",
  "Biological/Biosystems Engineering.": "1445",
  "Data Science.": "3070",
  "Agricultural Public Services.": "0108",
  "Animal Sciences.": "0109",
  "Soil Sciences.": "0112",
  "Veterinary Medicine.": "0180",
  "Veterinary Biomedical and Clinical Sciences.": "0181",
  "Fishing and Fisheries Sciences and Management.": "0303",
  "Wildlife and Wildlands Science and Management.": "0306",
  "Energy Systems Engineering.": "1448",
  "Family and Consumer Sciences/Human Sciences Business Services.": "1902",
  "Applied Statistics.": "2706",
  "Nanotechnology.": "1516",
  "Mason/Masonry.": "4601",
  "Intercultural/Multicultural and Diversity Studies.": "3023",
  "Agricultural and Food Products Processing.": "0104",
  "Civil Engineering Technologies/Technicians.": "1502",
  "Military Systems and Maintenance Technology.": "2904",
  "Movement and Mind-Body Therapies and Education.": "5136",
  "Parks, Recreation, Leisure, and Fitness Studies, Other.": "3199",
  "Engineering Chemistry.": "1444",
  "Military Applied Sciences.": "2903",
  "Science Technologies/Technicians, General.": "4100",
  "Literature.": "2314",
  "Chiropractic.": "5101",
  "Cultural Studies/Critical Theory and Analysis.": "3026",
  "Sociology and Anthropology.": "4513",
  "Nuclear and Industrial Radiologic Technologies/Technicians.": "4102",
  "Transportation and Materials Moving, Other.": "4999",
  "Naval Architecture and Marine Engineering.": "1422",
  "Family and Consumer Economics and Related Studies.": "1904",
  "Ocean Engineering.": "1424",
  "Clinical Psychology.": "4202",
  "Publishing.": "0910",
  "Modern Greek Language and Literature.": "1606",
  "Agricultural Engineering.": "1403",
  "Surveying Engineering.": "1438",
  "Medical Residency Programs - General Certificates.": "6004",
  "Radiology Residency/Fellowship Programs.": "6126",
  "Construction Engineering.": "1433",
  "Osteopathic Medicine/Osteopathy.": "5119",
  "Mechanics and Repairers, General.": "4700",
  "Telecommunications Management.": "5221",
  "Personal Awareness and Self-Improvement.": "3701",
  "History and Political Science.": "3046",
  "Rural Sociology.": "4514",
  "Nuclear Engineering Technologies/Technicians.": "1514",
  "Personal and Culinary Services, Other.": "1299",
  "Engineering Mechanics.": "1411",
  "Textile Sciences and Engineering.": "1428",
  "Earth Systems Science.": "3038",
  "Library Science, Other.": "2599",
  "Accounting and Computer Science.": "3016",
  "International Agriculture.": "0107",
  "Veterinary Residency Programs.": "6003",
  "American Indian/Native American Languages, Literatures, and Linguistics.": "1610",
  "Noncommercial Vehicle Operation.": "3602",
  "South Asian Languages, Literatures, and Linguistics.": "1607",
  "Communications Technologies/Technicians and Support Services, Other.": "1099",
  "Air Force ROTC, Air Science and Operations.": "2801",
  "Alternative and Complementary Medical Support Services.": "5134",
  "Boilermaking/Boilermaker.": "4808",
  "Precision Production, Other.": "4899",
  "Citizenship Activities.": "3301",
  "Community Psychology.": "4204",
  "Celtic Languages, Literatures, and Linguistics.": "1613",
  "Natural Resources and Conservation, Other.": "0399",
  "Electromechanical Engineering.": "1441",
  "Second Language Learning.": "1617",
  "Energy and Biologically Based Therapies.": "5137",
  "Veterinary Administrative Services.": "0182",
  "Physics and Astronomy.": "4011",
  "Physiological Psychology/Psychobiology.": "4211",
  "Philosophy, Politics, and Economics.": "3051",
  "Army ROTC, Military Science and Operations.": "2803",
  "Paper Science and Engineering.": "1440",
  "Maritime Studies.": "3029",
  "Energy Systems Maintenance and Repair Technologies/Technicians.": "4707",
  "Geography and Environmental Studies.": "3044",
  "Iranian/Persian Languages, Literatures, and Linguistics.": "1608",
  "High School/Secondary Certificate Programs.": "5302",
  "Counseling Psychology.": "4206",
  "African Languages, Literatures, and Linguistics.": "1602",
  "Turkic, Uralic-Altaic, Caucasian, and Central Asian Languages, Literatures, and Linguistics.": "1615",
  "Polymer/Plastics Engineering.": "1432",
  "High School/Secondary Diploma Programs.": "5301",
  "Holocaust and Related Studies.": "3021",
  "Precision Production Trades, General.": "4800",
  "Digital Humanities and Textual Studies.": "3052",
  "Cultural Studies and Comparative Literature.": "3036",
  "Surgery Residency/Fellowship Programs.": "6127",
  "Work and Family Studies.": "1900",
  "Environmental Geosciences.": "3041",
  "Ceramic Sciences and Engineering.": "1406",
  "Security Policy and Strategy.": "2806",
  "Economics and Computer Science.": "3039",
  "Interpersonal and Social Skills.": "3501",
  "Thanatology.": "3053",
  "Linguistics and Computer Science.": "3048",
  "Mathematical Economics.": "3049",
  "Military Science and Operational Studies.": "2805",
  "Military Technology and Applied Sciences Management.": "2906",
  "Medical Residency Programs - Subspecialty Certificates.": "6005",
  "Forest Engineering.": "1434",
  "Creative Writing.": "2305",
  "Area, Ethnic, Cultural, and Gender Studies, Other.": "0599",
  "Community/Environmental/Socially-Engaged Art.": "5011",
  "History and Language/Literature.": "3045",
  "Casino Operations and Services.": "1206",
  "Anthrozoology.": "3034"
}