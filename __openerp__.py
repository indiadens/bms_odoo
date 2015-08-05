{
	'name' : 'Crm Customization',
	'summary' : "Customer Relationship Management Module Customization",
	'description': """
		Crm Customization module for add new features for crm module
		   - add zoho crm functionality 
	""",
	'author' : 'ehAPI',
	'website' : 'www.ehapi.com',
	'category' : 'Customization',
	'version' : '1.0',
	'depends' : ['base','crm','mail'],
	'data' : [
			'crm_customization_view.xml',
			'view/menu.xml',
			'view/activities_view.xml',
			'view/clients_view.xml',
			],
	'installable' :True,
	'application' :True,
	'auto_install':False,
}