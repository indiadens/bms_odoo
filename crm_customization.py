from openerp.osv import fields, osv
from openerp import  tools, api
import datetime
from openerp.exceptions import except_orm, Warning, RedirectWarning

# from openerp import models, fields, api
class crm_custom_fields(osv.osv):
	_inherit = "crm.lead"
	_columns = {
		'lead_source' : fields.selection([('aus_day_email_prom','Australia Day Email Promotion'),
										('google_adwords','Google Adwords'),
										('direct_email','Direct Email'),
										('direct_call','Direct Call'),
										('fb','Facebook'),
										('search_engine','Search Engine'),
										('frnds_family','Friends/Family'),
										('referral','Referral'),
										('mara_website','MARA Website'),
										('gulf_news','Gulf News'),
										('whatsapp','Whatsapp'),
										('bms_website','BMS Website'),
										('email_compaign','Email Compaign'),
										('walkin','Walkin'),
										('advertisement','Advertisement'),
										('other','Other'),
										('blog','Blog'),
										('linkedin','Linkedin'),
										('news_paper','News Paper'),
										('twitter','Twitter'),
										('globe','Globe'),
										('existing_client','Existing Client'),
										('sms_marketing','SMS Marketing'),
										('fb_compaign','FB Compaign'),
										],'Lead Source', required=True),

		'email_sent' : fields.char('Email Sent'),
		'sales_consultant' : fields.many2one('res.users','Sale Consultant'),
		'booked_by' : fields.many2one('res.users','Booked By'),
		'organisation' : fields.selection([('bms','BMS'),
											('fbp','FBP')],'Organisation'),
		'handling_ofc' : fields.selection([('bms_adelaide','BMS Adelaide'),
											('fbp_dubai','FBP Dubai'),
			('fbp_bms','FBP Blue Stone Migration Services')],'Handling Office'),
		'lead_date' : fields.date('Lead Assignment Date'),
		'followup_date' : fields.date('Followup Date'),
		'followup_date_time':fields.selection([
											('12:00AM-12:30AM','12:00 AM - 12:30 AM'),
											('12:30AM-1:00AM','12:30 AM - 1:00 AM'),
											('1:00AM-1:30AM','1:00 AM - 1:30 AM'),
											('1:30AM-2:00AM','1:30 AM - 2:00 AM'),
											('2:00AM-2:30AM','2:00 AM - 2:30 AM'),
											('2:30AM-3:00AM','2:30 AM - 3:00 AM'),
											('3:00AM-3:30AM','3:00 AM - 3:30 AM'),
											('3:30AM-4:00AM','3:30 AM - 4:00 AM'),
											('4:00AM-4:30AM','4:00 AM - 4:30 AM'),
											('4:30AM-5:00AM','4:30 AM - 5:00 AM'),
											('5:00AM-5:30AM','5:00 AM - 5:30 AM'),
											('5:30AM-6:00AM','5:30 AM - 6:00 AM'),
											('6:00AM-6:30AM','6:00 AM - 6:30 AM'),
											('6:30AM-7:00AM','6:30 AM - 7:00 AM'),
											('7:00AM-7:30AM','7:00 AM - 7:30 AM'),
											('7:30AM-8:00AM','7:30 AM - 8:00 AM'),
											('8:00AM-8:30AM','8:00 AM - 8:30 AM'),
											('8:30AM-9:00AM','8:30 AM - 9:00 AM'),
											('9:00AM-9:30AM','9:00 AM - 9:30 AM'),
											('9:30AM-10:00AM','9:30 AM - 10:00 AM'),
											('10:00AM-10:30AM','10:00 AM - 10:30 AM'),
											('10:30AM-11:00AM','10:30 AM - 11:00 AM'),
											('11:00AM-11:30AM','11:00 AM - 11:30 AM'),
											('11:30AM-12:00PM','11:30 AM - 12:00 PM'),
											('12:00PM-12:30PM','12:00 PM - 12:30 PM'),
											('12:30PM-1:00PM','12:30 PM - 1:00 PM'),
											('1:00PM-1:30PM','1:00 PM - 1:30 PM'),
											('1:30PM-2:00PM','1:30 PM - 2:00 PM'),
											('2:00PM-2:30PM','2:00 PM - 2:30 PM'),
											('2:30PM-3:00PM','2:30 PM - 3:00 PM'),
											('3:00PM-3:30PM','3:00 PM - 3:30 PM'),
											('3:30PM-4:00PM','3:30 PM - 4:00 PM'),
											('4:00PM-4:30PM','4:00 PM - 4:30 PM'),
											('4:30PM-5:00PM','4:30 PM - 5:00 PM'),
											('5:00PM-5:30PM','5:00 PM - 5:30 PM'),
											('5:30PM-6:00PM','5:30 PM - 6:00 PM'),
											('6:00PM-6:30PM','6:00 PM - 6:30 PM'),
											('6:30PM-7:00PM','6:30 PM - 7:00 PM'),
											('7:00PM-7:30PM','7:00 PM - 7:30 PM'),
											('7:30PM-8:00PM','7:30 PM - 8:00 PM'),
											('8:00PM-8:30PM','8:00 PM - 8:30 PM'),
											('8:30PM-9:00PM','8:30 PM - 9:00 PM'),
											('9:00PM-9:30PM','9:00 PM - 9:30 PM'),
											('9:30PM-10:00PM','9:30 PM - 10:00 PM'),
											('10:00PM-10:30PM','10:00 PM - 10:30 PM'),
											('10:30PM-11:00PM','10:30 PM - 11:00 PM'),
											('11:00PM-11:30PM','11:00 PM - 11:30 PM'),
											], 'Time'),
		'appointment_date' : fields.date('Booked Appointment Date'),
		'appointment_date_time':fields.selection([
												('12:00AM-12:30AM','12:00 AM - 12:30 AM'),
												('12:30AM-1:00AM','12:30 AM - 1:00 AM'),
												('1:00AM-1:30AM','1:00 AM - 1:30 AM'),
												('1:30AM-2:00AM','1:30 AM - 2:00 AM'),
												('2:00AM-2:30AM','2:00 AM - 2:30 AM'),
												('2:30AM-3:00AM','2:30 AM - 3:00 AM'),
												('3:00AM-3:30AM','3:00 AM - 3:30 AM'),
												('3:30AM-4:00AM','3:30 AM - 4:00 AM'),
												('4:00AM-4:30AM','4:00 AM - 4:30 AM'),
												('4:30AM-5:00AM','4:30 AM - 5:00 AM'),
												('5:00AM-5:30AM','5:00 AM - 5:30 AM'),
												('5:30AM-6:00AM','5:30 AM - 6:00 AM'),
												('6:00AM-6:30AM','6:00 AM - 6:30 AM'),
												('6:30AM-7:00AM','6:30 AM - 7:00 AM'),
												('7:00AM-7:30AM','7:00 AM - 7:30 AM'),
												('5:00AM-5:30AM','5:00 AM - 5:30 AM'),
												('5:30AM-6:00AM','5:30 AM - 6:00 AM'),
												('6:00AM-6:30AM','6:00 AM - 6:30 AM'),
												('6:30AM-7:00AM','6:30 AM - 7:00 AM'),
												('7:00AM-7:30AM','7:00 AM - 7:30 AM'),
												('7:30AM-8:00AM','7:30 AM - 8:00 AM'),
												('8:00AM-8:30AM','8:00 AM - 8:30 AM'),
												('8:30AM-9:00AM','8:30 AM - 9:00 AM'),
												('9:00AM-9:30AM','9:00 AM - 9:30 AM'),
												('9:30AM-10:00AM','9:30 AM - 10:00 AM'),
												('10:00AM-10:30AM','10:00 AM - 10:30 AM'),
												('10:30AM-11:00AM','10:30 AM - 11:00 AM'),
												('11:00AM-11:30AM','11:00 AM - 11:30 AM'),
												('11:30AM-12:00PM','11:30 AM - 12:00 PM'),
												('12:00PM-12:30PM','12:00 PM - 12:30 PM'),
												('12:30PM-1:00PM','12:30 PM - 1:00 PM'),
												('1:00PM-1:30PM','1:00 PM - 1:30 PM'),
												('1:30PM-2:00PM','1:30 PM - 2:00 PM'),
												('2:00PM-2:30PM','2:00 PM - 2:30 PM'),
												('2:30PM-3:00PM','2:30 PM - 3:00 PM'),
												('3:00PM-3:30PM','3:00 PM - 3:30 PM'),
												('3:30PM-4:00PM','3:30 PM - 4:00 PM'),
												('4:00PM-4:30PM','4:00 PM - 4:30 PM'),
												('4:30PM-5:00PM','4:30 PM - 5:00 PM'),
												('5:00PM-5:30PM','5:00 PM - 5:30 PM'),
												('5:30PM-6:00PM','5:30 PM - 6:00 PM'),
												('6:00PM-6:30PM','6:00 PM - 6:30 PM'),
												('6:30PM-7:00PM','6:30 PM - 7:00 PM'),
												('7:00PM-7:30PM','7:00 PM - 7:30 PM'),
												('7:30PM-8:00PM','7:30 PM - 8:00 PM'),
												('8:00PM-8:30PM','8:00 PM - 8:30 PM'),
												('8:30PM-9:00PM','8:30 PM - 9:00 PM'),
												('9:00PM-9:30PM','9:00 PM - 9:30 PM'),
												('9:30PM-10:00PM','9:30 PM - 10:00 PM'),
												('10:00PM-10:30PM','10:00 PM - 10:30 PM'),
												('10:30PM-11:00PM','10:30 PM - 11:00 PM'),
												('11:00PM-11:30PM','11:00 PM - 11:30 PM'),
												], 'Time'),
		'contract_signed_date' : fields.date('Contract Signed Date'),
		'contact_name': fields.char('', size=64),
		'remarks_age':fields.integer('Remarks-Age'),
		'eng_ability' : fields.selection([('limited_below_4.5','Limited(below 4.5)'),
										('functional_4.5','Functional(4.5)'),
										('vocational_5','Vocational(5)'),
										('competent_6','Competent(6)'),
										('competent_plus_6.5','Competent Plus(6.5)'),
										('proficient_7','Proficient(7)'),
										('superior','Superior(8 and above)')],'Remarks-English Language Ability'),
		'work_exp' : fields.selection([('1','1 Year'),
									('2','2 Years'),
									('3','3 Years'),
									('4','4 Years'),
									('5','5 Years'),
									('6','6 Years'),
									('7','7 Years'),
									('8','8 Years'),
									('9','9 Years'),
									('10','10 and above Years')],'Remarks-Overseas Work Experience'),
		'educational_qualification' : fields.selection([('phd','PHD'),
														('master','Master'),
														('bachelor','Bachelor'),
														('diploma','Diploma'),
														('certificates','Certificates'),],'Remarks - Educational Qualification(s):'),
		'aus_employment' : fields.selection([('1-3','1 year-less than 3 years'),
											('3-5','3 years-less than 5 years'),
											('5-8','5 years-less than 8 years'),
											('8-10','8 years-but not less than 10 years')],'Remarks-Australian Employment'),

		'aus_study' : fields.selection([('none','None'),
										('tr_qua','Australian Degree, Diploma or Trade Qualification')],'Remarks - Australian Study:'),
		

		'other_factors' : fields.selection([('none','None'),
			('naati','NAATI'),
			('study_regional','Study & Live in Regional Area'),
			('partner_skills','Partner Skills'),
			('prof_year_cmpltd','Professional Year Completed in Australia'),
			],'Remarks - Other Factors:'),


		'state_sponsorship' : fields.selection([('none','None'),
			('sa','SA'),
			('vic','VIC'),
			('nsw','NSW'),
			('qld','QLD'),
			('act','ACT'),
			('wa','WA'),
			('nt','NT'),
			('tas','TAS'),
			],'Remarks - State Sponsorship:'),
		'visa_type' : fields.selection([('none','None'),
			('189','189'),
			('190_sn','190-SN'),
			('489','489-SN'),
			('489_br','489-BR'),
			],'Type of Visa - GSM:'),
		'relative_sponsor' : fields.selection([('child/stepchild','Child or Step Child'),
			('parent/stepparent','Parent or Step Parent'),
			('bro/stepbro/adoptivebro','Brother/Step Brother/Adoptive Brother'),
			('sis/stepsis/adoptivesis','Sister/Step Sister/Adoptive Sister'),
			('nephew/stepnephew/adoptivenephew','Nephew/Step Nephew/Adoptive Nephew'),
			('niece/stepniece/adoptiveniece','Niece/Step Niece/Adoptive Niece'),
			('uncle/adoptiveuncle','Uncle/Adoptive Uncle'),
			('aunt/adoptiveaunt','Aunt/Adoptive Aunt'),
			('1st_cousin','First Cousin'),
			],'Relative Sponsor:'),
		'points_age' : fields.selection([('none','None'),
			('13','13'),
			('25','25'),
			('15','15'),
			('0','0'),
			],'Points - Age:'),

		'points_eng_ability' : fields.selection([('none','None'),
			('0','0'),
			('10','10'),
			('20','20'),
			],'Points - English Language Ability:'),

		'points_overseas_exp' : fields.selection([('none','None'),
			('5','5'),
			('10','10'),
			('15','15'),
			],'Points - Overseas Work Experience?:'),

		'points_aus_emp' : fields.selection([('none','None'),
			('5','5'),
			('10','10'),
			('15','15'),
			('20','20'),
			],'Points - Australian Employment:'),

		'points_edu_qua' : fields.selection([('none','None'),
			('10','10'),
			('15','15'),
			('20','20'),
			],'Points - Educational Qualification(s):'),

		'points_aus_study' : fields.selection([('none','None'),
			('5','5'),
			],'Points - Australian Study:'),


		'points_oth_factors' : fields.selection([('none','None'),
			('5','5'),
			],'Points - Other Factors:'),

		'points_state_sponsorship' : fields.selection([('none','None'),
			('5','190'),
			('10','489'),
			],'Points - State Sponsorship:'),

		'total_points' : fields.integer('Total Points'),

		'relative_sponsor_state' : fields.selection([('none','None'),
			('sa','SA-Anywhere'),
			('vic','VIC-Anywhere'),
			('nsw','NSW-Check Postcode'),
			('qld','QLD-Check Postcode'),
			('act','ACT-Anywhere'),
			('wa','WA-Anywhere'),
			('nt','NT-Anywhere'),
			('tas','TAS-Anywhere'),
			],'Relative Sponsor - State'),

		#points tests for nz fields

		'skilled_employment' : fields.selection([
			('more_12mnths','Current skilled employment in New Zealand for 12 months or more'),
			('less_12mnths','Offer of skilled employment in New Zealand or current employment in New Zealand for less than 12 months'),
			],'Remarks - Skilled Employment:'),

		'employment_offer' : fields.selection([
			('future_growth_area_10','In an identified future growth area 10'),
			('absolute_skill_shortage_10','In an area of absolute skills shortage 10'),
			('outside_auckland_10','In a region outside Auckland 10'),
			('emp_offer_20','Partner employment or offer of employment 20'),
			],'Remarks - Employment or offer of employment:'),

		'relevant_work_exp' : fields.selection([
			('2','2 Years 10'),
			('4','4 Years 15'),
			('6','6 Years 20'),
			('9','9 Years 25'),
			('10','10 Years 30')],'Remarks - Relevant work experience'),

		'nz_work_exp' : fields.selection([
			('1','1 Year 5'),
			('2','2 Years 10'),
			('3','3 Years or more 15'),
			],'Remarks - NZ work experience:'),

		'work_exp_identified_future' : fields.selection([
			('2-5','2 to five years 10'),
			('<6','6 Years or more 15'),
			],'Remarks - Work experience in an identified future:'),

		'work_exp_area_skill_shortage' : fields.selection([
			('2-5','2 to five years 10'),
			('<6','6 Years or more 15'),
			],'Remarks - Work exp in an area of skill shortage:'),

		'recog_qualification' : fields.selection([
			('lvl_4to6','Level four to six on the NZQF (eg trade qualification, diploma) 40'),
			('lvl_7or8','Level seven or eight on the NZQF (eg bachelor degree, bachelor degree with Honours) 50'),
			('lvl_9or10','Level nine or ten on the NZQF (eg Masters degree, Doctorate) 60'),
			],'Remarks - Recognised qualifications:'),


		'qua_nz' : fields.selection([
			('lvl_4to6','Two years of full-time study in NZ completing a recognised bachelor degree (level seven on the NZQF) 10'),
			('lvl_7or8','Level seven or eight on the NZQF (eg bachelor degree, bachelor degree with Honours) 50'),
			('lvl_9or10','Level nine or ten on the NZQF (eg Masters degree, Doctorate) 60'),
			],'Remarks - Qualifications:'),

		'qualification' : fields.char('Qualification'),
		'work_exp_notes': fields.char('Work Experience Notes'),
		'english_notes': fields.char('English'),
		'state_sponsorship_notes': fields.char('State Sponsorship'),

		'qualification_notes': fields.char('Qualification Notes'),
		'work_experience': fields.char('Work Experience'),
		'other_factors_notes': fields.char('Other Factors'),


		#Visa Assesment details
		'anzsco_code': fields.char('ANZSCO Code'),
		'migrate_to' : fields.selection([('Australia','Australia'),('New Zealand','New Zealand')], 'Migrate To'),
		'anzsco_desc': fields.char('ANZSCO Description'),
		'assessing_auth' : fields.selection([
			("Architects Accreditation Council of Australia (AACA)","Architects Accreditation Council of Australia (AACA)"),
			("Australian Association of Social Workers (AASW)","Australian Association of Social Workers (AASW)"),
			("Australasian College of Physical Scientists and Engineers in Medicine (ACPSEM)","Australasian College of Physical Scientists and Engineers in Medicine (ACPSEM)"),
			("Australian Computer Society (ACS)","Australian Computer Society (ACS)"),
			("Australian Dental Council (ADC)","Australian Dental Council (ADC)"),
			("Australian Institute of Management (AIM)","Australian Institute of Management (AIM)"),
			("Australian Institute of Medical Scientists (AIMS)","Australian Institute of Medical Scientists (AIMS)"),
			("Australian Institute of Quantity Surveyors (AIQS)","Australian Institute of Quantity Surveyors (AIQS)"),
			("Australian Institute of Radiography (AIR)","Australian Institute of Radiography (AIR)"),
			("Australian Institute of Teaching and School Leadership (AITSL)","Australian Institute of Teaching and School Leadership (AITSL)"),
			("Australian Community Workers Association (ACWA)","Australian Community Workers Association (ACWA)"),
			("Australian Maritime Safety Authority (AMSA)","Australian Maritime Safety Authority (AMSA)"),
			("Australian Nursing and Midwifery Accreditation Council (ANMAC)","Australian Nursing and Midwifery Accreditation Council (ANMAC)"),
			("Australian and New Zealand Osteopathic Council (ANZOC)","Australian and New Zealand Osteopathic Council (ANZOC)"),
			("Australian and New Zealand Podiatry Accreditation Council (ANZPAC)","Australian and New Zealand Podiatry Accreditation Council (ANZPAC)"),
			("Australian and New Zealand Society of Nuclear Medicine (ANZSNM)","Australian and New Zealand Society of Nuclear Medicine (ANZSNM)"),
			("Australian Pharmacy Council (APharmC)","Australian Pharmacy Council (APharmC)"),
			("Australian Physiotherapy Council (APC)","Australian Physiotherapy Council (APC)"),
			("Australian Psychological Society (APS)","Australian Psychological Society (APS)"),
			("Australasian Veterinary Boards Council (AVBC)","Australasian Veterinary Boards Council (AVBC)"),
			("Certified Practising Accountants of Australia (CPAA)","Certified Practising Accountants of Australia (CPAA)"),
			("Chinese Medicine Board of Australia (CMBA)","Chinese Medicine Board of Australia (CMBA)"),
			("Council on Chiropractic Education Australasia (CCEA)","Council on Chiropractic Education Australasia (CCEA)"),
			("Civil Aviation Safety Authority (CASA)","Civil Aviation Safety Authority (CASA)"),
			("Dietitians Association of Australia (DAA)","Dietitians Association of Australia (DAA)"),
			("Engineers Australia (EA)","Engineers Australia (EA)"),
			("Institute of Chartered Accountants in Australia (ICAA)","Institute of Chartered Accountants in Australia (ICAA)"),
			("Medical Board of Australia (MBA)","Medical Board of Australia (MBA)"),
			("National Accreditation Authority for Translators and Interpreters (NAATI)","National Accreditation Authority for Translators and Interpreters (NAATI)"),
			("Occupational Therapy Council (OTC)","Occupational Therapy Council (OTC)"),
			("Optometry Council of Australia and New Zealand (OCANZ)","Optometry Council of Australia and New Zealand (OCANZ)"),
			("Institute of Public Accountants (IPA)","Institute of Public Accountants (IPA)"),
			("Speech Pathology Association of Australia (SPA)","Speech Pathology Association of Australia (SPA)"),
			("State Legal Admissions Authority","State Legal Admissions Authority"),
			("Surveying and Spatial Sciences Institute (SSSI)","Surveying and Spatial Sciences Institute (SSSI)"),
			("Trades Recognition Australia (TRA)","Trades Recognition Australia (TRA)"),
			("Vocational Education and Training Assessment Services (VETASSESS)","Vocational Education and Training Assessment Services (VETASSESS)"),


			], 'Assessing Authority'),
		

		# points test nz
		'rem_skill_emp':fields.selection([('skill_nz12','Current skilled employment in NewZealand for 12 months or more'),('skill_nz_less12','Offer of skilled employment in New Zealand or current employment in New Zealand for less than 12 months')],'Remarks - Skilled Employment'),
		
		'rem_emp_offer':fields.selection([('emp_offer_identified10','In an identified future growth area 10'),('emp_offer_absolute10','In an area of absolute skills shortage 10'),
			('emp_offer_region','In a region outside Auckland 10'),('emp_offer_partner','Partner employment or offer of employment 20')],'Remarks - Employment or offer of employment'),
		
		'rem_work_exp':fields.selection([('work_exp10','Two years 10'),('work_exp15','Four years 15'),('work_exp20','Six years 20'),('work_exp25','Eight years 25'),('work_exp30','Ten years 30')],'Remarks - Relevant work experience'),

		'rem_nz_exp':fields.selection([('nz_exp5','One year 5'),('nz_exp10','Two year 10'),('nz_15','Three years or more 15')],'Remarks - NZ work experience'),

		'rem_work_diff':fields.selection([('work_5to10','Two to 5 years 10'),('work_15','Six years or more 15')],'Remarks - Work experience in an identified future'),

		'rem_skill_sort':fields.selection([('skill_sort10','Tow to five years 10'),('skill_sort15','Six years or more 15')],'Remarks - Work exp in an area of skill shortage'),

		'rem_recog':fields.selection([('remark_rec_4to6','Level four to six on the NZQF (eg trade qualification, diploma) 40'),('remark_rec_7or8','Level seven or eight on the NZQF (eg bachelor degree, bachelor degree with Honours) 50'),
			('remark_rec_9or10','Level nine or ten on the NZQF (eg Masters degree, Doctorate) 60')],'Remarks - Recognised qualifications'),

		'rem_qual':fields.selection([('remark_qual2','Two years of full-time study in NZ completing a recognised bachelor degree (level seven on the NZQF) 10'),
			('remark_qual1','One year of full-time study in NZ completing a recognised post-graduate (levels eight, nine or ten on the NZQF)10'),
			('remark_qual15','Two years of full-time study in NZ completing a recognised post-graduate (level nine, or ten on the NZQF) 15')],'Remarks - Qualifications'),

		'rem_family':fields.selection([('rem_fam','Close family in New Zealand')],'Remarks - Family'),

		'rem_age':fields.selection([('age_20to29','20 to 29 (30)'),('age_30to39','30 to 39 (40)'),('age_40to44','40 to 44 (20)'),('age_45to49','45 to 49 (10)'),('age_50to55','50 to 55 (5)')],'Remarks- Age NZ'),

		'total_points_nz':fields.integer('Total points NZ'),

		'point_skill_emp':fields.selection([('point_skill50','60'),('point_skill60','50')],'Points - Skilled employment'),

		'point_emp_offer':fields.selection([('point_emp10','10'),('point_emp20','20')],'Points - Employment or offer of empolyment'),

		'pints_work_exp':fields.selection([('point_work10','10'),('point_work15','15'),('piont_work20','20'),('point_work25','25'),('point_work30','30')],'Points- Relevant Work experience'),

		'point_nz_exp':fields.selection([('point_nz5','5'),('point_nz10','10'),('point_nz15','15')],'Points - NZ work experience'),

		'point_exp_indentified':fields.selection([('pointexp_indentified10','10'),('pointexp_indentified15','15')],'Points - Work experience in an identified future'),

		'point_exp_skillsort':fields.selection([('point_skillsort10','10'),('point_skillsort20','20')],'Points - Work exp in an area of skill shortage'),

		'points_recog_qual':fields.selection([('rec_qaul40','40'),('rec_qaul50','50'),('rec_qaul60','60')],'Points - Recognised qualifications'),

		'points_qual':fields.selection([('points_qual10','10'),('points_qual15','15'),('points_qual20','20')],'Points - Qualifications'),

		'points_family':fields.selection([('points_family10','10')],'Points - Family'),

		'points_agenz':fields.selection([('points_agenz30','30'),('points_agenz25','25'),('points_agenz20','20'),('points_agenz10','10'),('points_agenz5','5')],'Points - Age NZ'),




		
	}
crm_custom_fields()

class client_bms(osv.osv):

	_inherit = 'res.partner'

	_columns = {

	'dob' : fields.date('Date of Birth'),
	'age' : fields.integer('Age (years)'),
	'gender' : fields.selection([('male','Male'),
		('female','Female')],'Gender'),
	'visa_type':fields.selection([('visa1','General Skilled Migration'),('visa2','Business Skilled Migration'),('visa3','Corporate Visas(Employer Sponsored)'),
		('visa4','Temporary Work Visa'),('visa5','Family Migration'),('visa6','Investor Visa'),('visa7','Partner (spouse) Visa'),('visa8','Parent Visa'),
		('visa9','Skilled Student Visa'),('visa10','Visitor Visa'),('visa11','Citizenship & Resident Return Visas'),('visa12','Migration Review Tribunel'),('visa13','Work Visa')],'Visa Type'),

	'nationality':fields.many2one('nation.bms','Nationality'),
	'resume':fields.boolean("Resume"),

	}


	@api.onchange('dob')
	def _onchange_dob(self):
		if self.dob:
			Format = '%Y-%m-%d'
			
			born = datetime.datetime.strptime(self.dob, Format)
			today = datetime.date.today()
			age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))

			if age < 0:
				raise except_orm('Value Error',"Age cann't be negative")
			else:
				self.age = age
			


client_bms()



class nationality_bms(osv.osv):
	_name = 'nation.bms'

	_columns={
		'name':fields.char("Your Nationality",size=30,required=True),
	}
nationality_bms()


